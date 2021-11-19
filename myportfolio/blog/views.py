from django.db.models import fields
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from blog.models import Post, Comment


class PostList(ListView):
    
    def get(self, request):
        postList = Post.objects.all()
        ctx = {'post_list':postList}
        return render(request, template_name='post_list.html',context=ctx)

class PostDetail(DetailView):

    def get(self, request, pk):
        x = Post.objects.get(id=pk)
        comments = Comment.objects.filter(id=x).order_by('-updated_at')
        ctx = {'post':x, 'comments': comments}
        return render(request, template_name='post_detail.html', context=ctx)

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')