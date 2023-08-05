from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm, InventoryItemForm, InventoryStoreForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ITItem, ITStore
from ILF_Inventory.settings import LOW_QUANTITY
from django.contrib import messages
from django.db.models import Q

class Index(TemplateView):
    template_name = 'IT/index.html'


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = ITItem.objects.filter(user=self.request.user.id).order_by('id')

        return render(request, 'IT/dashboard.html', {'items': items})


class StoreDashboard(LoginRequiredMixin, View):
	def get(self, request):
		items = ITStore.objects.filter(user=self.request.user.id).order_by('id')

		low_inventory = ITStore.objects.filter(
			user=self.request.user.id,
			amount_left__lte=LOW_QUANTITY
		)

		if low_inventory.count() > 0:
			if low_inventory.count() > 1:
				messages.error(request, f'{low_inventory.count()} items have low inventory')
			else:
				messages.error(request, f'{low_inventory.count()} item has low inventory')

		low_inventory_ids = ITStore.objects.filter(
			user=self.request.user.id,
			amount_left__lte=LOW_QUANTITY
		).values_list('id', flat=True)

		return render(request, 'IT/store.html', {'items': items, 'low_inventory_ids': low_inventory_ids})


class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'IT/signup.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('it_index')
        return render(request, 'IT/signup.html', {"form": form})


class AddItem(LoginRequiredMixin, CreateView):
    model = ITItem
    form_class = InventoryItemForm
    template_name = 'IT/item_form.html'
    success_url = reverse_lazy('it_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['projects'] = Project.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EditItem(LoginRequiredMixin, UpdateView):
    model = ITItem
    form_class = InventoryItemForm
    template_name = 'IT/item_form.html'
    success_url = reverse_lazy('it_dashboard')


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = ITItem
    template_name = 'IT/delete_item.html'
    success_url = reverse_lazy('it_dashboard')
    context_object_name = 'item'


class SearchInventory(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            items = ITItem.objects.filter(
                Q(staff_name__icontains=query) |
                Q(devices__icontains=query) |
                Q(model__icontains=query) |
                Q(supplier__icontains=query) 
            )
        else:
            items = ITItem.objects.none()
        return render(request, 'IT/search.html', {'items': items, 'query': query})
    

class AddStoreItem(LoginRequiredMixin, CreateView):
    model = ITStore
    form_class = InventoryStoreForm
    template_name = 'IT/item_form.html'
    success_url = reverse_lazy('it_store')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['projects'] = Project.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EditStoreItem(LoginRequiredMixin, UpdateView):
    model = ITStore
    form_class = InventoryStoreForm
    template_name = 'IT/store_item_form.html'
    success_url = reverse_lazy('it_store')

class DeleteStoreItem(LoginRequiredMixin, DeleteView):
    model = ITStore
    template_name = 'IT/store_delete_item.html'
    success_url = reverse_lazy('it_store')
    context_object_name = 'item'
