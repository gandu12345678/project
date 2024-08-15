
from django.urls import path
from django.urls import include
from .views import Index
from .views import SignUpView,Dashboard
from django.contrib.auth import views as auth_views
from . import views
# urlpatterns = 
#     path('',Index.as_view(),name='index'),
#     path('signup/',SignUpView.as_view(),name="signup"),
#     path('login/',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
#     path('logout/',auth_views.LogoutView.as_view(template_name="logout.html"),name="logout"),
# ]
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('signup/',SignUpView.as_view(),name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path('logout/',views.logout_user,name="logout"),
]


# for api

# from .views import *
# from rest_framework.routers import DefaultRouter,SimpleRouter


# router = SimpleRouter()

# router.register(r"categories",CategoryViewSet)
# router.register(r"products",ProductViewSet)
 
# urlpatterns=[]+router.urls 