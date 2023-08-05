from django.shortcuts import render, redirect
from django.urls import reverse_lazy;
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SafetyItem, SafetyStore
from .forms import InventoryItemForm, InventoryStoreForm
from ILF_Inventory.settings import LOW_QUANTITY
from django.contrib import messages
from django.db.models import Q

# Create your views here.
class Index(TemplateView):
    template_name = 'safety/index.html'


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = SafetyItem.objects.filter(user=self.request.user.id).order_by('id')

        return render(request, 'safety/dashboard.html', {'items': items})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'safety/signup.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )

            login(request, user)
            return redirect ('safety_index')
        return render(request, 'safety/signup.html', {"form": form})
    
class StoreDashboard(LoginRequiredMixin, View):
	def get(self, request):
		items = SafetyStore.objects.filter(user=self.request.user.id).order_by('id')

		low_inventory = SafetyStore.objects.filter(
			user=self.request.user.id,
			left__lte=LOW_QUANTITY
		)

		if low_inventory.count() > 0:
			if low_inventory.count() > 1:
				messages.error(request, f'{low_inventory.count()} items have low inventory')
			else:
				messages.error(request, f'{low_inventory.count()} item has low inventory')

		low_inventory_ids = SafetyStore.objects.filter(
			user=self.request.user.id,
			left__lte=LOW_QUANTITY
		).values_list('id', flat=True)

		return render(request, 'safety/store.html', {'items': items, 'low_inventory_ids': low_inventory_ids})

class AddItem(LoginRequiredMixin, CreateView):
    model = SafetyItem
    form_class = InventoryItemForm
    template_name = 'safety/item_form.html'
    success_url = reverse_lazy('safety_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EditItem(LoginRequiredMixin, UpdateView):
    model = SafetyItem
    form_class = InventoryItemForm
    template_name = 'safety/item_form.html'
    success_url = reverse_lazy('safety_dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = SafetyItem
    template_name = 'safety/delete_item.html'
    success_url = reverse_lazy('safety_dashboard')
    context_object_name = 'item'


class AddStoreItem(LoginRequiredMixin, CreateView):
    model = SafetyStore
    form_class = InventoryStoreForm
    template_name = 'safety/item_form.html'
    success_url = reverse_lazy('safety_store')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['projects'] = Project.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditStoreItem(LoginRequiredMixin, UpdateView):
    model = SafetyStore
    form_class = InventoryStoreForm
    template_name = 'safety/store_item_form.html'
    success_url = reverse_lazy('safety_store')

class DeleteStoreItem(LoginRequiredMixin, DeleteView):
    model = SafetyStore
    template_name = 'safety/store_delete_item.html'
    success_url = reverse_lazy('safety_store')
    context_object_name = 'item'


class SearchInventory(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            items = SafetyItem.objects.filter(
                Q(staff_name__icontains=query) |
                Q(item_name__icontains=query) 
            )
        else:
            items = SafetyItem.objects.none()
        return render(request, 'safety/search.html', {'items': items, 'query': query})