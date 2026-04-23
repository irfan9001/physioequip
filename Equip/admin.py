from django.contrib import admin
from .models import Category, Product, ProductImage, HeroSlide, SupportPage, FAQ, ContactPage, ContactQuery

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created_at']
    list_filter = ['category', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']

@admin.register(SupportPage)
class SupportPageAdmin(admin.ModelAdmin):
    pass

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order']
    list_editable = ['order']

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactQuery)
class ContactQueryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'phone', 'subject', 'message', 'created_at']

    def has_add_permission(self, request):
        return False
