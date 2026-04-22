from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('logout/', views.logout_view, name='logout'),
]
