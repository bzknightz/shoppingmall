from django.db import models
from django.urls.base import reverse
import uuid

# Create your models here.


class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.TextField()
    img = models.ImageField(upload_to="uploads/%Y/%m/%d")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_show", kwargs={"pk": self.pk})
