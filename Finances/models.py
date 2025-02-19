from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User



cycleTypes = {
    "S": "Semanal",
    "BiS": "Bisemanal",
    "M": "Mensal",
    "Tri": "Trimestral",
    "SeM": "Semestral",
    "A": "Anual",
}

transactionConstraint = {
    "A": "Qualquer Dia",
    "BW": "Dia útil ANTERIOR",
    "WB": "Dia útil POSTERIOR",
}





#=========== Registers =========#
class House(models.Model):
    Name = models.CharField(max_length=25)


class HouseMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    houses = models.ManyToManyField(House)


class Month(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()



class AccountEntry(models.Model):
    monthRef = models.ForeignKey(Month, on_delete=models.SET_NULL, null=True)
    activeHouse = models.ForeignKey(House, on_delete=models.SET_NULL, null=True)
    value = models.FloatField()




#=========== Transaction =========#
class Tag(models.Model):
    isDebt = models.BooleanField(default=True)
    name = models.CharField(max_length=25)
    color = ColorField(default='#FF0000')





#============== Series ==============#
class TransactionSerie(models.Model):
    user_field = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True) #if the series is active
    nextDateExpected = models.DateField()
    businessDay = models.CharField(max_length=3, choices=transactionConstraint.items()) #if the transaction occurs only in business days
    name = models.CharField(max_length=25, unique=True)


class CreditCard(TransactionSerie):
    juro = models.FloatField()


class PlannedEvent(TransactionSerie):
    isFixedDate = models.BooleanField(default=True)
    cycle = models.CharField(max_length=4, choices=cycleTypes.items()) #cycle of occurence of the event
    isFixedValue = models.BooleanField(default=True)
    expectValue = models.FloatField()
    tags = models.ManyToManyField(Tag)








class Transaction(models.Model):
    #relations
    user_field = models.ForeignKey(User, on_delete=models.CASCADE)
    fromCreditCard = models.ForeignKey(CreditCard, related_name="fromCC",null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(PlannedEvent, null=True, on_delete=models.SET_NULL)
    monthReference = models.ForeignKey(Month, on_delete=models.CASCADE)

    #properties
    isDebt = models.BooleanField(default=True)
    value = models.FloatField()
    dateRegister = models.DateField(auto_now_add=True)
    dateEffect = models.DateField()
    tags = models.ManyToManyField(Tag)
    paid = models.BooleanField(default=False,blank=True)
    
    #Payment Reference
    directDebt = models.BooleanField(default=False,blank=True)
    mb_reference = models.CharField(max_length=20,blank=True)
    mb_entity = models.CharField(max_length=20,blank=True)
    IBAN = models.CharField(max_length=36,blank=True)
    paymentDescription = models.CharField(max_length=300)
    toCreditCard = models.ForeignKey(CreditCard, null=True, on_delete=models.SET_NULL)
    
    #identifiers
    name = models.CharField(max_length=35, unique=True)
    description = models.TextField()

