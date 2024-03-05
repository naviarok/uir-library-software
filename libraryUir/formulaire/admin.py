from django.contrib import admin
from .models import Formulaire
# Register your models here.

class FormulaireAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Code', 'Items', 'Date')

admin.site.register(Formulaire, FormulaireAdmin)