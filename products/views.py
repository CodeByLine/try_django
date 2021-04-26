from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.urls import reverse
from .forms import ProductForm, RawProductForm

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id) 
    if request.method == "POST":
        obj.delete()
        return redirect('../../' )
    context = {
        "object" : obj
    }
    return render(request, "products/product_confirm_delete.html", context )

def PracticeDataView(request, id):
    initial_data = {
        'title' : "Official Title"
        }

    # obj = Product.objects.get(id=1) 
    obj = get_object_or_404(Product, id=id) 
    # obj = Product.objects.get(id=1) #needed for changing objects
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    

    # form = ProductForm(request.POST or None,    
    #     initial=inital_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'products/product_create.html', context)

def product_create_view(request):
    my_form = RawProductForm() # () empty because-no prior data 
    if request.method == "POST":
        my_form = RawProductForm(request.POST) 
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    cxt = {
        'form' : my_form
    }

    return render(request, "products/product_create.html", cxt)
# verions 1
# def product_create_view(request):
#     form = ProductForm() #this clears the form
#     # form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     cxt = {
#         'form' : form
#     }

#     return render(request, "products/product_create.html", cxt)

def product_detail_view(request, id):

    object=Product.objects.get(id=id)
    # cxt = {
    #     'title': object.title,
    #     'description' : object.description,
    # }
    cxt = {
        'object' : object
    }
    return render(request, "products/product_detail.html", cxt)