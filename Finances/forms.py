from django import forms
from .models import CreditCard, PlannedEvent, TransactionSerie, Transaction,Month
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ObjectDoesNotExist

class CardModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name



class TransactionSerieForm(forms.ModelForm):   
    nextDateExpected = forms.DateField(
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = TransactionSerie
        fields = ['nextDateExpected', 'businessDay', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Series Name'}),
        }


class CreditCardForm(TransactionSerieForm):   
    class Meta(TransactionSerieForm.Meta):
        model = CreditCard
        fields = TransactionSerieForm.Meta.fields + ['juro']


class PlannedEventForm(TransactionSerieForm):
    class Meta(TransactionSerieForm.Meta):
        model = PlannedEvent
        fields = TransactionSerieForm.Meta.fields + ['isFixedDate', 'cycle', 'isFixedValue', 'expectValue']






class TransactionForm(forms.ModelForm):
    dateEffect = forms.DateField(
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    toCreditCard = CardModelChoiceField(
        queryset=CreditCard.objects.all(),
        required=False,
        empty_label="Selecione um Cartão de Crédito"
    )


    
    def save(self, commit=True):
        instance = super().save(commit=False)
        try:
            month = Month.objects.get(month=instance.dateEffect.month,year=instance.dateEffect.year)
        except ObjectDoesNotExist as e:
            month = Month.objects.create(month=instance.dateEffect.month,year=instance.dateEffect.year)
        instance.monthReference = month # Example calculation
        if commit:
            instance.save()
        return instance


    class Meta:
        model = Transaction
        fields = ['name','description','isDebt', 'value',
        "dateEffect","paid","directDebt","mb_reference",
        "mb_entity","IBAN","toCreditCard","paymentDescription"]
    
