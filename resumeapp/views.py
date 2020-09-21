from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy,reverse
# Create your views here.

# def home(request):
#     return render(request,'resumeapp/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'resumeapp/home.html'
    ordering = ['-post_date']
    def get_context_data(self, *args, **kwargs):
        cat_name = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context['catname'] = cat_name
        return context


def LikeView(request,pk):
    post =get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'resumeapp/article.html'
    def get_context_data(self, *args, **kwargs):
        cat_name = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['catname'] = cat_name
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'resumeapp/add_post.html'
    # fields = "__all__"
class AddCategory(CreateView):
    model = Category
    template_name = 'resumeapp/add_category.html'
    fields = "__all__"

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'resumeapp/update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'resumeapp/delete_post.html'
    success_url = reverse_lazy('home')


def category_view(request,cats):
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'resumeapp/category.html',{'cats':cats.title().replace('-',' '),'category_post':category_post})
