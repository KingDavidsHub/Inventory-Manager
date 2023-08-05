from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem, SearchInventory
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='facility_index'),
    path('dashboard/', Dashboard.as_view(), name='facility_dashboard'),
    path('add-item/', AddItem.as_view(), name='facility_add-item'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='facility_edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='facility_delete-item'),
    path('search/',SearchInventory.as_view(), name ='facility_search-item'),
    path('signup/', SignUpView.as_view(), name='facility_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='facility/login.html'), name='facility_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='facility/logout.html'), name='facility_logout'),
]