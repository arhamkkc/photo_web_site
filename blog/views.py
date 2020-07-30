from django.shortcuts import render,redirect
from blog.forms import PhotoForm,ContactForm
from blog.models import Photo,Category,Contact
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
# home page func
def home(request):
    cat = Category.objects.all()
    photo = Photo.objects.all().order_by('-pub_date')
    context = {'photo':photo,'cat':cat}
    return render(request,'blog/home.html',context)



def cat_detail(request,id):
    cat = Category.objects.get(id=id)
    photo = Photo.objects.filter(category= id).order_by('-pub_date')
    return render(request,'blog/cat_detail.html',{'photo':photo,'cat':cat})

def contact(request):
    register = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            register = True 
            return redirect('contact')
        else:
            messages.error(request,'Please fill all the detail correctly')
            return redirect('contact')


    else:
        form = ContactForm()

    return render(request,'blog/contact.html',{'form':form,'register':register})


def about(request):
    return render(request,'blog/about.html')


def gallery(request):
    cat = Category.objects.all()
    return render(request,'blog/gallery.html',{"cat":cat})
















# def basic(request):
#     form = PhotoForm()
#     if request.method == "POST":
#         form = PhotoForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             return HttpResponse('kakdma')
#     else:
#         form = PhotoForm()

#     return render(request,'blog/basic.html',{'form':form})


    
