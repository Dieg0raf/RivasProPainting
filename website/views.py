from django.shortcuts import render, HttpResponse

# Create your views here.

posts = [
    {
        'title': 'How to use behr 2024 color of the the year on your littletonHome',
        'date_posted': 'August 27, 2017',
        'content': 'First post content'
    },
    {
        'title': 'blog post 2',
        'date_posted': 'August 28, 2017',
        'content': 'second post content'
    }
]

def home(request):
    return render(request, 'website/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

def ourwork(request):
    return render(request, 'website/our_work.html', {'title': 'Our-Work','background': 'background-image-2.jpg'})

def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})
