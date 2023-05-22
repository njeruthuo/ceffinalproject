from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Blog
from .forms import BlogForm


def index(request):
    return render(request, 'blog/index.html')


def gallery_view(request):
    return render(request, 'blog/gallery.html')


def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blog-list.html', context)


def my_blogs(request):
    # blogs written by the author himself will be displayed here
    user = request.user
    my_blogs = Blog.objects.filter(author=user)
    return render(request, 'blog/blog_list2.html', {
        'my_blogs': my_blogs
    })


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog/coming-soon.html', context)


def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog')
        else:
            messages.error(request, 'Error creating the blog post.')
    return render(request, 'blog/blog_create.html', {'form': form})


def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog-detail', pk=blog.pk)
        else:
            messages.error(request, 'Error updating the blog post.')
    return render(request, 'blog/blog_update.html', {'form': form})


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog')
    return render(request, 'blog/blog_delete.html', {'blog': blog})
