from django.urls import path
import views

urlpatterns = [
    path('', views.main, name='main'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
] 