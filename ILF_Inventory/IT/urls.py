from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem, SearchInventory, StoreDashboard, AddStoreItem, EditStoreItem, DeleteStoreItem
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='it_index'),
    path('dashboard/', Dashboard.as_view(), name='it_dashboard'),
    path('store/', StoreDashboard.as_view(), name='it_store'),
    path('add-item/', AddItem.as_view(), name='it_add-item'),
    path('add-store-items/', AddStoreItem.as_view(), name='it_add-store-items'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='it_edit-item'),
    path('edit-store-item/<int:pk>', EditStoreItem.as_view(), name='it_edit-store-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='it_delete-item'),
    path('delete-store-item/<int:pk>', DeleteStoreItem.as_view(), name='it_delete-store-item'),
    path('search/',SearchInventory.as_view(), name ='it_search-item'),
    path('signup/', SignUpView.as_view(), name='it_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='IT/login.html'), name='it_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='IT/logout.html'), name='it_logout'),
]