from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import *
from . import *
from .forms import AddPostForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your views here.

def index(request):
    posts = Blog.objects.all()
    categories = Category.objects.all()
    active = -1
    return render(request, 'blog/index.html', {'title': 'Главная страница', 'posts': posts, 'categories': categories, 'active': active})

class HomeView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['categories'] = Category.objects.all()
        context['acitve'] = -1
        return context

def category_view(request, slug):
    categories = Category.objects.all()
    posts = Blog.objects.filter(category__slug = slug)
    active = slug
    return render(request, 'blog/index.html', {'title': f'Главная страница {Category.objects.get(slug = slug).name}', 'posts': posts, 'categories': categories, 'active': active}) 
 
class CategoryView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Страница категорий {Category.objects.get(slug = self.kwargs['slug']).name}"
        context['categories'] = Category.objects.all()
        context['acitve'] = self.kwargs['slug']
        return context

    def get_qeuryset(self, *args, **kwargs):
        return Blog.objects.filter(category__slug = self.kwargs['slug'])



def detail_post(request, pk):
    post = Blog.objects.get(pk=pk)
    return render(request, 'blog/post.html', {'title': post.title, 'post': post })

class DetailView(DetailView):
    model = Blog
    template_name = 'blog/post.html'
    context_object_name = 'post'


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm() 
    return render(request, 'blog/add_post.html', {'form': form, 'title': 'Добавление поста'})    

class AddPost(CreateView):
    model = Blog
    fields = '__all__'
    from_class = AddPostForm
    template_name = 'blog/add_post.html'
    context_object_name = 'form'

    success_ulr = reverse_lazy('home')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

'''
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_ulr = reverse_lazy('home')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация пользователя"
        return context
'''