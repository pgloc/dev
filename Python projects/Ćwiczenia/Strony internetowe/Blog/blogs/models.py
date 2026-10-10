from django.db import models

class BlogPost(models.Model):
    """Posty dodawane do bloga przez użytkownika."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return self.title