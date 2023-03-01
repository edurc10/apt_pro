from django.urls import path
from . import views

urlpatterns = [
# -------------------------------------------------------------------------------------------------
# real project start
# -------------------------------------------------------------------------------------------------
    path('', views.main, name='main'),
    path('apt2me', views.apt2me, name='apt2me'),
    path('id/<int:aptid>', views.Aptdata, name='aptid'),
    # path('testdatas/', views.getTestDatas, name='testdatas'),
    # path('testdata/<int:price>', views.getTestData, name='testdata'),
    path('postMember/', views.postMember, name='postMember'),
    

















# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# real project end
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
    # path('', views.post_list, name='main'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
] 