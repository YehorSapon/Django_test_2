from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home_page(TemplateView):
    template_name = "shop/index.html"

class Blog(TemplateView):
    template_name = "shop/blog.html"

def about(request):
    return render(request,
                  "shop/about.html")

def contact(request):
    return render(request,
                  "shop/contact.html")

def services(request):
    return render(request,
                  "shop/services.html")

def thankyou(request):
    return render(request,
                  "shop/thankyou.html")
