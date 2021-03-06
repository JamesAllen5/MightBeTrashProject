from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    Pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping_name = models.TextField()
    
    def __str__(self):
        return f"{self.topping_name[:50]}..."

class Comment(models.Model):
    Pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    comment_entry = models.TextField()

    def __str__(self):
        return f"{self.comment_entry[:50]}..."