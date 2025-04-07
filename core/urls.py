from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .api_docs import APIDocsView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html', next_page='home'), name='logout'),
    path('question/new/', views.question_create, name='question_create'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('api-docs/', APIDocsView.as_view(), name='api-docs'),
]
