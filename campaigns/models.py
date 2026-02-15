import uuid
from django.db import models

class Campaign(models.Model):

    PLATFORM_CHOICES = [
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('LinkedIn', 'LinkedIn'),
    ]

    STATUS_CHOICES = [
        ('draft', 'draft'),
        ('scheduled', 'scheduled'),
        ('published', 'published'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255)

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    budget = models.DecimalField(max_digits=12, decimal_places=2)

    start_date = models.DateField()
    end_date = models.DateField()

    # Optional fields
    caption = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
