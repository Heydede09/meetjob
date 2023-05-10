from django.contrib import admin

# Register your models here.

from .models import Goods

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name','price','create_date') #自訂顯示欄位


admin.site.register(Goods,GoodsAdmin)
