from django.db import models

class Contact(models.Model):
    class Meta:
        db_table="tbl_contacts"
        verbose_name_plural="Contact"
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name
    

