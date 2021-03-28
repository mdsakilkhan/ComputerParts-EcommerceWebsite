from django.shortcuts import render

# Create your views here.
context = {'ourName': 'Team S', 'websiteTitle': 'Computer Parts'}

def home(request):
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html', context)

# purchase history or card verify
def parts(request):
    return render(request, 'parts.html', context)

# contect seller / customer service / return
def contact(request):
    return render(request, 'contact.html', context) 