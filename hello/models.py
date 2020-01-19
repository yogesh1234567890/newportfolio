from django.db import models


class Contact(models.Model):
    class Meta:
        db_table = "tbl_contacts"
        verbose_name_plural = "Contact"
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Photos(models.Model):
    class Meta:
        db_table = "tbl_photo"
        verbose_name_plural = "Photos"

    logo_image = models.ImageField(upload_to="images", null=True)
    first_image = models.ImageField(upload_to="images", null=True)
    second_image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.logo_image


class login(models.Model):
    class Meta:
        db_table = "tbl_login"
        verbose_name_plural = "login"
    username = models.CharField(max_length=50)
    password =models.CharField(max_length=32)

    def __str__(self):
        return self.username


