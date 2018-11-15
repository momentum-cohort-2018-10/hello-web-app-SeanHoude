from django.contrib import admin

# Register your models here.
from collection.models import ClimbingShoe


class ClimbingShoeAdmin(admin.ModelAdmin):
    model = ClimbingShoe
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ClimbingShoe, ClimbingShoeAdmin)