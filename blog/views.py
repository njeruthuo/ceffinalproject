from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Blog, Gallery, Event, Message
from .forms import BlogForm


def index(request):
    return render(request, 'blog/index.html')


@login_required(login_url='login')
def gallery_view(request):
    photos = Gallery.objects.all()
    return render(request, 'blog/gallery.html', {
        'photos': photos,
    })


@login_required(login_url='login')
def photo_view(request, pk):
    photo = get_object_or_404(Gallery, pk=pk)
    return render(request, 'photo.html', {
        'photo': photo
    })


@login_required(login_url='login')
def events(request):
    events = Event.objects.all()
    return render(request, 'blog/event.html', {
        'events': events,
    })


@login_required(login_url='login')
def event_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event.html', {
        'event': event
    })


@login_required(login_url='login')
def blog_list(request):
    blogs = Blog.objects.all()
    # popular_blogs = Blog.objects.order_by(
    #     '-views')[:5]

    context = {
        'blogs': blogs,
        # 'popular_blogs': popular_blogs,
    }
    return render(request, 'blog/blog-list.html', context)


@login_required(login_url='login')
def my_blogs(request):
    # blogs written by self himself will be displayed here
    user = request.user
    my_blogs = Blog.objects.filter(author=user)
    return render(request, 'blog/blog_list2.html', {
        'my_blogs': my_blogs
    })


@login_required(login_url='login')
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    messages = blog.message_set.all().order_by('-created_at')

    if request.method == 'POST':

        content = Message.objects.create(
            user=request.user,
            blog=blog,
            message=request.POST.get('comment')
        )
        content.save()
        return redirect('blog-detail', pk=pk)

    context = {
        'blog': blog,
        'messages': messages,
    }
    return render(request, 'blog/blog-detail.html', context)


@login_required(login_url='login')
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
    return render(request, 'blog/blog-create.html', {'form': form})


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog')
    return render(request, 'blog/blog_delete.html', {'blog': blog})
