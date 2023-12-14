from django.contrib import admin
from .models import Colis
# Register your models here.

class adminList(admin.ModelAdmin):
    list_display = ('LieuDepart', 'LieuLivraison', 'DateLivraison', 'DescriptionColis', 'StatutColis')


admin.site.register(Colis, adminList)