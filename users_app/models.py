from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'  # Set the table name to 'users'

    def __str__(self):
        return self.name