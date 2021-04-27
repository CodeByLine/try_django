from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Article
from django.urls import reverse
from .forms import BlogForm, ArticleForm

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


from django.views import generic
from django.views.generic import ( 
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    # path for class-based views: 
        # <app_name>/<model_name>_list.html
)


class ArticleListView(generic.ListView):
    queryset = Article.objects.all()
    model = Article
    template_name = "blog/article_list.html"

class ArticleCreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm 
    #Above line is needed to address the errors here:
    #ImproperlyConfigured at /blog/article_create/ 
    # Using ModelFormMixin (base class of ArticleCreateView) without the 'fields' attribute is prohibited.
    template_name = "blog/article_create.html"
    # success_url = "blog/article_list.html"


    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    

## For the following to work: 
## 1. import 
## 2. change pk to id (Article, not Blog)


# class ArticleDetailView(DetailView):
#     template_name = "blog/article_detail.html"
#     queryset = Article.objects.all() ## queryset limits the choices available for the DetailView

#     def get_object(self):
#         id_=self.kwargs.get("id") ## overwrite default id label
#         return get_object_or_404(Article,id=id_)


class ArticleConfirmDeleteVew(generic.DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"


# Below: Base View Class = View
# from django.views import View
# class ArticleView(View):
    # template_name = 'name.html'
#     def get(self, request, *args, **kwargs):
#         return render(rquest, self.template_name, {})

#     def post(self, request, *args, **kwargs):
#         return render(rquest, 'about.html', {})