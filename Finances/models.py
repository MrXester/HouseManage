from django.db import models
from colorfield.fields import ColorField

cycleTypes = {
    "S": "Semanal",
    "BiS": "BiSemanal",
    "M": "mensal",
    "Tri": "Trimestral",
    "SeM": "Semestral",
    "A": "Anual",
}

transactionConstraint = {
    "A": "Any Day",
    "BW": "Business Day before weekend",
    "WB": "Business Day after weekend",
}


#=========== Registers =========#
class House(models.Model):
    Name = models.CharField(max_length=25)


class Month(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()



class AccountEntry(models.Model):
    monthRef = models.ForeignKey(Month, on_delete=models.SET_NULL, null=True)
    activeHouse = models.ForeignKey(House, on_delete=models.SET_NULL, null=True)
    value = models.FloatField()




#============== Series ==============#
class TransactionSerie(models.Model):
    active = models.BooleanField(default=True) #if the series is active
    dateExpect = models.IntegerField() #days from the beginning of the cycle
    businessDay = models.CharField(max_length=3, choices=transactionConstraint.items()) #if the transaction occurs only in business days
    name = models.CharField(max_length=200)


class CreditCard(models.Model):
    series = models.OneToOneField(TransactionSerie, on_delete=models.SET_NULL, null=True)
    juro = models.FloatField()


class PlannedEvent(models.Model):
    series = models.OneToOneField(TransactionSerie, on_delete=models.SET_NULL, null=True)
    isFixedDate = models.BooleanField(default=True)
    cycle = models.CharField(max_length=4, choices=cycleTypes.items()) #cycle of occurence of the event
    isFixedValue = models.BooleanField(default=True)
    expectValue = models.FloatField()



#=========== Transaction =========#
class Tag(models.Model):
    isDebt = models.BooleanField(default=True)
    name = models.CharField(max_length=25)
    color = ColorField(default='#FF0000')



class PaymentReference(models.Model):
    paid = models.BooleanField(default=False)
    directDebt = models.BooleanField(default=False)
    mb_reference = models.CharField(max_length=20)
    mb_entity = models.CharField(max_length=20)
    IBAN = models.CharField(max_length=36)
    description = models.CharField(max_length=350)


class Transaction(models.Model):
    creditCard = models.ForeignKey(CreditCard, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(PlannedEvent, null=True, on_delete=models.SET_NULL)
    monthRef = models.ForeignKey(Month, on_delete=models.SET_NULL, null=True)

    isDebt = models.BooleanField(default=True)
    value = models.FloatField()
    dateRegister = models.DateField()
    dateEffect = models.DateField()
    personal = models.BooleanField(default=False)
    paymentReference = models.OneToOneField(PaymentReference, on_delete=models.SET_NULL, null=True)









