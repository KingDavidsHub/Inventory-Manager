from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem, DeleteStoreItem, StoreDashboard, SearchInventory, AddStoreItem, EditStoreItem
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', Index.as_view(), name='business_index'),
    path('dashboard/', Dashboard.as_view(), name='business_dashboard'),
    path('store/', StoreDashboard.as_view(), name='business_store'),
    path('add-item/', AddItem.as_view(),name='business_add-item'),
    path('add-store-items/', AddStoreItem.as_view(), name='business_add-store-items'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='business_edit-item'),
    path('edit-store-item/<int:pk>', EditStoreItem.as_view(), name='business_edit-store-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='business_delete-item'),
    path('delete-store-item/<int:pk>', DeleteStoreItem.as_view(), name='business_delete-store-item'),
    path('search/',SearchInventory.as_view(), name ='business_search-item'),
    path('signup/', SignUpView.as_view(), name = 'business_signup'),
    path('login/', auth_views.LoginView.as_view(template_name= 'business/login.html'), name='business_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='business/logout.html'), name='business_logout'), 
]
