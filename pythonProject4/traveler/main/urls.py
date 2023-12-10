from django.urls import path, re_path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup

urlpatterns = [
    path('',views.index, name ='home'),
    path('about',views.about, name='about'),
    path('add_attraction',views.add_attraction, name='add_attraction'),
    path('tours',views.tours, name='tours'),
    path('cooperation',views.cooperation, name='cooperation'),
    path('<int:pk>',views.AttractionDetailView.as_view(), name='attraction-detail'),
    path('add_comment/<int:attraction_id>',views.add_comment, name='add_comment'),
    path('unpublish_comment/<int:comment_id>/', views.unpublish_comment, name='unpublish_comment'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),
]