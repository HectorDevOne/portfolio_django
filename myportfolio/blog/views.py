from django.shortcuts import render
from django.views import View

class BlogIndex(View):
    
    def get(self, request):
        return render(request, template_name='blog_index.html')
