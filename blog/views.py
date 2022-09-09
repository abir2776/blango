from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

#published_at__lte=timezone.now()
# Create your views here.
def index(request):
  posts = Post.objects.filter.all()
  return render(request, "blog/index.html", {"posts": posts})

