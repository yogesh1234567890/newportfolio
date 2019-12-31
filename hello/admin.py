from django.contrib import admin
from hello.models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def contact(obj):
        return obj

    list_display=['name','email','subject','message']