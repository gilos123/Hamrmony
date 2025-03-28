from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=500, verbose_name="שם")
    email = models.EmailField(max_length=150, verbose_name="אימייל")
    message = models.TextField(verbose_name="הודעה")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="תאריך יצירה")

    def __str__(self):
        return f"{self.name} - {self.email}"
