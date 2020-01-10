from django.contrib import admin
from hello.models import Contact,Photos
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def contact(obj):
        return obj

    list_display=['name','email','subject','message']


@admin.register(Photos)
class PhotoAdmin(admin.ModelAdmin):
    def photo(obj):
        return obj
    
    list_display=['logo_image','first_image','second_image']

