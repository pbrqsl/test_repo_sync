from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import ListView

def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    print(page_number)
    print(posts)
    posts = paginator.page(page_number)
    return render(request, 
                  'blog/post/list.html', 
                  {'posts': posts})

class PostList(ListView):
    queryset = Post.published.all()
    #model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name='blog/post/list.html'

def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No post found")
    post = get_object_or_404(Post,  
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    return render(request, 
                  'blog/post/detail.html', 
                  {'post': post})

