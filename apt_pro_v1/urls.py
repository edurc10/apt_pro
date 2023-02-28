from django.urls import path
<<<<<<< HEAD
import views

urlpatterns = [
    path('', views.main, name='main'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
] 
=======
from . import views

urlpatterns = [
    path('', views.main, name='main'),
]
>>>>>>> 8d38eb917f6d53e1c41b931c8eabc1c9e483d6b9
