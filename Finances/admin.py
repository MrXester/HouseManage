from django.contrib import admin
from .models import House,AccountEntry,Tag,Month



class HouseAdmin(admin.ModelAdmin):
    list_display= ("Name",)


class AccountEntryAdmin(admin.ModelAdmin):
    list_display= ("monthRef","activeHouse","value")


class TagAdmin(admin.ModelAdmin):
    list_display= ("isDebt","name","color")



class MonthAdmin(admin.ModelAdmin):
    list_display= ("month","year")



admin.site.register(House,HouseAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(AccountEntry,AccountEntryAdmin)
admin.site.register(Month,MonthAdmin)