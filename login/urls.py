from django.urls import path,include
from . import views 

urlpatterns =  [
    path('',views.indexView,name="home"),
    path('thought/',views.thoughtFeed,name="thought"),
    path('aboutus/',views.aboutView,name="about"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',views.loginView,name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',views.logoutView,name="logout"), 
   


   
    # path('disableCamera/', views.disableCamera, name='disableCamera'),
]