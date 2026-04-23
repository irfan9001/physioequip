from django.shortcuts import render, get_object_or_404
from .models import Category, Product, HeroSlide
from urllib.parse import quote
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Phone number for WhatsApp inquiries
WHATSAPP_NUMBER = "+919328090749"

def home(request):
    hero_slides = HeroSlide.objects.filter(is_active=True)
    categories = Category.objects.all()[:4] # Show up to 4 categories on home
    featured_products = Product.objects.all().order_by('-created_at')[:6] # Latest 6 products
    return render(request, 'Equip/home.html', {
        'hero_slides': hero_slides,
        'categories': categories,
        'featured_products': featured_products
    })

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'Equip/product_list.html', {
        'categories': categories,
        'products': products,
        'current_category': None
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)
    return render(request, 'Equip/product_list.html', {
        'current_category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # Pre-fill WhatsApp message
    message = f"Hello, I am interested in your product: {product.name}. Could you provide more details?"
    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER.replace('+', '').replace(' ', '')}?text={quote(message)}"
    
    return render(request, 'Equip/product_detail.html', {
        'product': product,
        'whatsapp_url': whatsapp_url
    })

def support_page(request):
    from .models import SupportPage, FAQ
    support_content = SupportPage.objects.first()
    faqs = FAQ.objects.all()
    return render(request, 'Equip/support.html', {
        'support_content': support_content,
        'faqs': faqs
    })

def contact_page(request):
    from .models import ContactPage
    from .forms import ContactForm
    from django.contrib import messages
    from django.shortcuts import redirect

    contact_content = ContactPage.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully. We will get back to you soon!')
            return redirect('contact_page')
        else:
            messages.error(request, 'There was an error in your submission. Please check the form below.')
    else:
        form = ContactForm()

    return render(request, 'Equip/contact.html', {
        'contact_content': contact_content,
        'form': form
    })

# REMOVE THIS AFTER FIRST USE FOR SECURITY
def create_admin(request):
    User = get_user_model()
    user = User.objects.filter(username='admin').first()
    if user:
        user.set_password('admin123')
        user.save()
        return HttpResponse('Admin password reset')
    else:
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse('Admin created')