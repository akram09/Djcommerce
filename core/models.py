from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
CLOTHES_CATEGORIES = (
    ("S" , "Shirt"),
    ("SW", "Sport Wear"),
    ('O', 'Outwear'),
)
LABELS = (
    ('P','primary'),
    ('S', 'secondary'),
    ('D','danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True , null=True)
    label = models.CharField(choices = LABELS , max_length=1)
    category = models.CharField(choices = CLOTHES_CATEGORIES, max_length=2)
    slug = models.SlugField()
    description  = models.TextField(default= "Lorem Ipsum ")
    def __str__(self):
        return self.title

    def get_product_url(self):
        return reverse("core:item", kwargs= {
            'slug':self.slug
        })
    def get_add_to_cart(self):
        return reverse("core:add_to_cart", kwargs= {
            'slug':self.slug
        })
    def get_remove_from_cart(self):
        return reverse("core:remove_from_cart", kwargs= {
            'slug':self.slug
        })



class OrderItem(models.Model):
    item = models.ForeignKey(Item , on_delete =models.CASCADE)
    quantity  = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE , blank= True , null = True)
    ordered = models.BooleanField(default = False)
    def __str__(self):
        return "Item named {} with quantity {}".format(self.item.title , self.quantity)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    ordered = models.BooleanField(default =False)
    items = models.ManyToManyField(OrderItem)
    start_date  = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField(blank = True , null = True)
    def __str__(self):
        return "Order of the user {}  has {} items".format(self.user, self.items.count())
