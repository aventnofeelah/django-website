from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainRender, name='main_path'), #main page url
    path('login/', views.loginRender, name='login_path'),
    path('registration/', views.registRender, name='reigistration_path'),
    path('logout/', views.logoutView, name='logout_path'),
    path('users/', views.usersRender, name='users_path'),
    path('users/<int:user_id>/', views.profileRender, name='profile_path'),
    path('<int:user_id>/add-portfolio', views.addportfolioRender, name='addportfolio_path'),
    
]
