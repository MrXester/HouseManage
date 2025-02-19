from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import CreditCardForm,PlannedEventForm,TransactionSerieForm,TransactionForm
import os
from .models import CreditCard, PlannedEvent, TransactionSerie, Transaction
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.template import RequestContext
from django.http import Http404
#Create


class SetUserMixin(LoginRequiredMixin):
    user_field = 'user_field'

    def form_valid(self, form):
        setattr(form.instance, self.user_field, self.request.user)
        return super().form_valid(form)



class CreditCardCreateView(SetUserMixin,CreateView):
    model = CreditCard
    form_class = CreditCardForm
    template_name = os.path.join("forms","credit_forms.html")
    success_url = reverse_lazy("home")  # Redirect after success


class EventPlanningCreateView(SetUserMixin,CreateView):
    model = PlannedEvent
    form_class = PlannedEventForm
    template_name = os.path.join("forms","eventPlan_forms.html")
    success_url = reverse_lazy("home")  # Redirect after success




class TransactionCreateView(SetUserMixin,CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = os.path.join("forms","transaction_forms.html")
    success_url = reverse_lazy("home")  # Redirect after success


#Update


class UserOwnedUpdateView(LoginRequiredMixin, UpdateView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model,pk=self.kwargs['pk'])
        
        if obj.user_field != self.request.user:
            raise PermissionDenied()
        return obj

    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if 'edit' not in self.request.GET:  # Keep form locked unless editing
            for field in form.fields:
                form.fields[field].widget.attrs['disabled'] = True
        return form


    def get_success_url(self):
        return reverse_lazy(self.success_url)





class CreditCardUpdateView(UserOwnedUpdateView):
    model = CreditCard
    form_class = CreditCardForm
    template_name = os.path.join("forms","credit_forms.html")
    success_url = "home"  # Redirect after success


class EventPlanningUpdateView(UserOwnedUpdateView):
    model = PlannedEvent
    form_class = PlannedEventForm
    template_name = os.path.join("forms","eventPlan_forms.html")
    success_url = "home"  # Redirect after success




class TransactionUpdateView(UserOwnedUpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = os.path.join("forms","transaction_forms.html")
    success_url = "home"  # Redirect after success





def set_serie_inactive(request, pk):
    obj = get_object_or_404(TransactionSerie,pk=pk)
    success_url = reverse_lazy("home") 
    
    if obj.user_field != request.user:  # Ensure only the owner can modify it
        raise PermissionDenied()

    obj.active = False
    obj.save()
    return redirect(success_url)





def set_reference_paid(request, pk):
    obj = get_object_or_404(Transaction,pk=pk)
    success_url = reverse_lazy("home") 
    
    if obj.user_field != request.user:
        raise PermissionDenied()

    obj.paid = True
    obj.save()
    return redirect(success_url)






def page_not_found(request, exception):
    response = render(request,'general/page-404.html')
    response.status_code = 404
    return response


def page_forbiden(request, exception):
    response = render(request,'general/page-403.html')
    response.status_code = 403
    return response


def page_error(request):
    response = render(request,'general/page-500.html')
    response.status_code = 500
    return response






def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")