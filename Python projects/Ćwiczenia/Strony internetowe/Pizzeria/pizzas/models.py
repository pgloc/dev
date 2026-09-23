from django.db import models

class Pizza(models.Model):
    """Model reprezentujący pizzę."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return self.text

class Topping(models.Model):
    """Model reprezentujący dodatki do pizzy."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return f"{self.text[:50]}"