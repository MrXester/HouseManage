from django.contrib import admin
from .models import House,HouseMember,AccountEntry,Tag,Month,CreditCard, PlannedEvent, TransactionSerie, Transaction



class HouseAdmin(admin.ModelAdmin):
    list_display= ("Name",)


class AccountEntryAdmin(admin.ModelAdmin):
    list_display= ("monthRef","activeHouse","value")


class TagAdmin(admin.ModelAdmin):
    list_display= ("isDebt","name","color")



class MonthAdmin(admin.ModelAdmin):
    list_display= ("month","year")



admin.site.register(HouseMember)
admin.site.register(House,HouseAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(AccountEntry,AccountEntryAdmin)
admin.site.register(Month,MonthAdmin)
admin.site.register(CreditCard)
admin.site.register(PlannedEvent)
admin.site.register(TransactionSerie)
admin.site.register(Transaction)