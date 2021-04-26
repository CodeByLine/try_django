from django.db import models

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField()
    featured    = models.BooleanField(default=False)  # null=True, default=True

    #blank: how the field is rendered
    #null: how the database handles the info

    def get_absolute_url(self):  #with app_name in urls.py
        return reverse("products:product_detail", kwargs={"id": self.id})
        # return f"/products/{self.id}/" 
        # {{instance.id}}
        # <a href='/products/{{instance.id}}'>