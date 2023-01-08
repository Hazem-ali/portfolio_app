from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='./images')
    email = models.EmailField(max_length=254)


    def __str__(self) -> str:
        return self.name

class ContactData(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=300)
    linkedin = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"Contact Data for {self.member.name}"

    class Meta:
        verbose_name_plural = 'Contact Data'
    


class About(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    brief_message = models.CharField( max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return f"About {self.member.name}"


class Service(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self) -> str:
        return f"Service offered by {self.member.name}"

# in future => rating and feedback(reviews)
