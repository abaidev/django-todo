from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<ID: {self.id} - {self.task}>"