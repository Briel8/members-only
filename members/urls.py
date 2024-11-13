from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('', views.index, name='index'),        # Home
    path('detail/<int:post_id>/', views.detail, name='detail'), # post details
    path('add/', views.add_post, name='add_post'),  # Make a post
    path('signup/', views.signup, name='signup'),      # New Member
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.logout_member, name='logout_member'), # Logout Logged in User
    #path('edit/', views.edit_post, name='edit_post'),
]