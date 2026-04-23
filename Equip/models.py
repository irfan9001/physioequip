from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    specifications = models.TextField(help_text="Format as a list or table in HTML if needed, or just plain text")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"

class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero_slides/')
    link_text = models.CharField(max_length=100, default='View Catalog', blank=True)
    link_url = models.CharField(max_length=200, default='/products/', blank=True)
    order = models.IntegerField(default=0, help_text="Sort order for slides (lower numbers appear first)")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-id']
class SupportPage(models.Model):
    warranty_policy = models.TextField(blank=True, help_text="HTML or plain text for Warranty Policy")
    shipping_info = models.TextField(blank=True, help_text="HTML or plain text for Shipping Info")
    terms_conditions = models.TextField(blank=True, help_text="HTML or plain text for Terms & Conditions")

    class Meta:
        verbose_name = "Support Page Content"
        verbose_name_plural = "Support Page Content"

    def __str__(self):
        return "Support Page Content"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question

class ContactPage(models.Model):
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    whatsapp_number = models.CharField(max_length=50, blank=True, help_text="Format: +919328090749")
    working_hours = models.TextField(blank=True)

    class Meta:
        verbose_name = "Contact Page Content"
        verbose_name_plural = "Contact Page Content"

    def __str__(self):
        return "Contact Page Content"

class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Query"
        verbose_name_plural = "Contact Queries"

    def __str__(self):
        return f"{self.name} - {self.subject}"
