from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # used
    path('blog-list/', views.blog_list, name='blog'),  # used
    path('my-blogs/', views.my_blogs, name='my-blogs'),
    path('create/', views.create_blog, name='create-blog'),
    path('<int:pk>/detail', views.blog_detail, name='blog-detail'),
    path('update/<int:pk>/', views.update_blog, name='update-blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete-blog'),

    path('gallery/', views.gallery_view, name='gallery'),
    path('gallery/<int:pk>/', views.gallery_view, name='photo-view'),
    path('events/', views.gallery_view, name='events'),
    path('event/<int:pk>/', views.gallery_view, name='event-view'),
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
