from django.contrib import admin
from django.core.mail import send_mail
from hello.models import Contact,Photos,login
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        send_mail(obj.subject, obj.message,['yogeshbhattarai073@gmail.com'],obj.email)
        return super().save_model(request, obj, form, change)
   
    # def contact(obj):
    #     return obj

    list_display=['name','email','subject','message']


@admin.register(Photos)
class PhotoAdmin(admin.ModelAdmin):
    def photo(obj):
        return obj
    
    list_display=['logo_image','first_image','second_image']



@admin.register(login)
class PhotoAdmin(admin.ModelAdmin):
    def log(obj):
        return obj
    
    list_display=['username','password']


