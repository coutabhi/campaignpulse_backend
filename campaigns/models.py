import uuid
from django.db import models

class Campaign(models.Model):

    PLATFORM_CHOICES = [
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('LinkedIn', 'LinkedIn'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Paused', 'Paused'),
        ('Completed', 'Completed'),
        ('Draft', 'Draft'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255)

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)

    budget = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')

    start_date = models.DateField()
    end_date = models.DateField()

    # Optional content fields
    caption = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
