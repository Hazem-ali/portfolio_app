from django.db import models
from accounts.models import User
# Create your models here.



class ContactData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=50)
    facebook = models.CharField(max_length=300)
    linkedin = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"Contact Data for {self.user.full_name}"

    class Meta:
        verbose_name_plural = 'Contact Data'
    


class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    brief_message = models.CharField( max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return f"About {self.user.full_name}"


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self) -> str:
        return f"Service offered by {self.user.full_name}"

# in future => rating and feedback(reviews)
