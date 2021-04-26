from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.urls import reverse
from .forms import BlogForm

def blog_list_view(request):
    queryset = Blog.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "blog/blog_list.html", context)

def blog_confirm_delete_view(request, id):
    obj = get_object_or_404(Blog, id=id) 
    if request.method == "POST":
        obj.delete()
        return redirect('../../' )
    context = {
        "object" : obj
    }
    return render(request, "blog/blog_confirm_delete.html", context )

def PracticeDataView(request, id):
    initial_data = {
        'title' : "Official Blog Title"
        }

    obj = get_object_or_404(Blog, id=id) 
    
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'blog/blog_create.html', context)

def blog_create_view(request):
    my_form = RawBlogForm() # () empty because-no prior data 
    if request.method == "POST":
        b_form = RawBlogForm(request.POST) 
        if b_form.is_valid():
            Blog.objects.create(**b_form.cleaned_data)
        else:
            print(b_form.errors)
    cxt = {
        'form' : b_form
    }

    return render(request, "blog/blog_create.html", cxt)

def blog_detail_view(request, id):

    object=Blog.objects.get(id=id)
    
    cxt = {
        'object' : object
    }
    return render(request, "blog/blog_detail.html", cxt)