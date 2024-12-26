from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import *
from bson import ObjectId
from .forms import *
# Create your views here.
def home(request):
    context = {
        "template_product":product_form()

    }

    if request.method == "POST":
        create_product=product_form(request.POST)

        if create_product.is_valid():
            create_product.save()

            return redirect('/my_app/table/')

            
    return render(request,'index.html',context)


def table(request):
    read_data = product.objects.all()
    
    return render(request,'table.html',{"created_data": read_data})

def front(request):
    return render(request,'front.html')


def delete_product(request,id):
    selected_data = product.objects.get(id = id)

    selected_data.delete()

    return redirect('/my_app/table/')

def update_product(request,id):
    select_user = product.objects.get(id = id)

    context = {
        'up':product_form(instance=select_user)
    }

    if request.method == "POST":
        create_product=product_form(request.POST,instance=select_user)

        if create_product.is_valid():
            create_product.save()

            return redirect('/my_app/table/')

        
     
    return render(request,'update.html',context)

   



