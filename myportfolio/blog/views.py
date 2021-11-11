from django.shortcuts import render
from django.views.generic import ListView

class PostList(ListView):
    
    def get(self, request):
        return render(request, template_name='post_list.html')
