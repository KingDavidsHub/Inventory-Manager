from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem, DeleteStoreItem, StoreDashboard, SearchInventory, AddStoreItem, EditStoreItem
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', Index.as_view(), name='safety_index'),
    path('dashboard/', Dashboard.as_view(), name='safety_dashboard'),
    path('store/', StoreDashboard.as_view(), name='safety_store'),
    path('add-item/', AddItem.as_view(),name='safety_add-item'),
    path('add-store-items/', AddStoreItem.as_view(), name='safety_add-store-items'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='safety_edit-item'),
    path('edit-store-item/<int:pk>', EditStoreItem.as_view(), name='safety_edit-store-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='safety_delete-item'),
    path('delete-store-item/<int:pk>', DeleteStoreItem.as_view(), name='safety_delete-store-item'),
    path('search/',SearchInventory.as_view(), name ='safety_search-item'),
    path('signup/', SignUpView.as_view(), name = 'safety_signup'),
    path('login/', auth_views.LoginView.as_view(template_name= 'safety/login.html'), name='safety_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='safety/logout.html'), name='safety_logout'), 
]
