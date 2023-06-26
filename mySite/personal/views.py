from django.shortcuts import render
from mySite.personal.models import BlogPost

def create_blog_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        signature = request.POST.get('Cameron', 'Welcome')
        date = timezone.now()

        blog_post = BlogPost(title=title, body=body, signature=signature, date=date)
        blog_post.save()
        return redirect('blog:detail', pk=blog_post.pk)
    return render(request, 'create_blog_post.html')

def about(request):
    return render(request, 'personal/about.html')

def projects(request):
    return render(request, 'personal/projects.html')

def index(request):
    return render(request, 'personal/index.html')