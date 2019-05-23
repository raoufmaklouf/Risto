from django.contrib import admin
from .models import Reserve


class PostModelAdmin(admin.ModelAdmin):
    list_display=['name','time','Guests']
    list_filter=['date'] 
    search_fields=['date','name'] 
    class Meta:
        model=Reserve 

admin.site.register(Reserve,PostModelAdmin)