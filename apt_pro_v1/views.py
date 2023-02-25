from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'apt_pro_v1/main.html', {})