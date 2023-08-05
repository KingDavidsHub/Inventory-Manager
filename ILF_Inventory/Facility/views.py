from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm, InventoryItemForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FacilityItem
from ILF_Inventory.settings import LOW_QUANTITY
from django.contrib import messages
from django.db.models import Q

class Index(TemplateView):
    template_name = 'facility/index.html'


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = FacilityItem.objects.filter(user=self.request.user.id).order_by('id')

        return render(request, 'facility/dashboard.html', {'items': items})





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
            return redirect('business_index')
        return render(request, 'IT/signup.html', {"form": form})


class AddItem(LoginRequiredMixin, CreateView):
    model = FacilityItem
    form_class = InventoryItemForm
    template_name = 'facility/item_form.html'
    success_url = reverse_lazy('facility_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['projects'] = Project.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EditItem(LoginRequiredMixin, UpdateView):
    model = FacilityItem
    form_class = InventoryItemForm
    template_name = 'facility/item_form.html'
    success_url = reverse_lazy('facility_dashboard')


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = FacilityItem
    template_name = 'facility/delete_item.html'
    success_url = reverse_lazy('facility_dashboard')
    context_object_name = 'item'


class SearchInventory(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            items = FacilityItem.objects.filter(
                Q(name__icontains=query) |
                Q(owner__icontains=query) 
 
            )
        else:
            items = FacilityItem.objects.none()
        return render(request, 'facility/search.html', {'items': items, 'query': query})
    


    


