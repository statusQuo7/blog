from django.shortcuts import redirect, render
from django.http import  HttpResponse, request
from .models import Category, Post
from .forms import FeedbackForm, CommentForm, PostForm
from .bot import send_feedback
from .utils import feedback_message
from django.db.models import Q
from django.views.generic import ListView, TemplateView, FormView, DetailView

class PostListView(ListView):
    model = Post
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super(PostListView,self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        category_id = self.request.GET.get("category", None)
        if category_id:
            return Post.objects.filter(category_id=category_id)
        return Post.objects.all()



def drop(request):
    category_id = request.GET.get("category", None)
    categories = Category.objects.all()
    if category_id:
        posts = Post.objects.filter(category_id=category_id)
        return render(request, "index.html", {"index": "active", "posts":posts, "categories":categories}) 
    posts = Post.objects.all()
    return render(request, "index.html", {"index": "active", "posts":posts, "categories":categories})

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self,**kwargs):
        context = super(AboutView,self).get_context_data(**kwargs)
        context['about'] = "active"
        return context

def about(request):
    return render(request, "about.html", {"about": "active"})

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = FeedbackForm

    def get_context_data(self,**kwargs):
        context = super(ContactFormView,self).get_context_data(**kwargs)
        context['contact'] = "active"
        return context




def contact(request):
    feedback_form = FeedbackForm(request.POST or None)
    if request.method == "POST":
        text = feedback_message.format(**feedback_form.data)
        send_feedback(text)
    
    return render(request, "contact.html", {"contact": "active", "feedback_form": feedback_form})

class PostDetailView(DetailView):
    template_name = 'post.html'
    model = Post

    def get_context_data(self,**kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = CommentForm()
        return context

def post(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm()
    categories = Category.objects.all()
    return render(request, "post.html", {"post": post, "categories": categories, "comment_form": comment_form})

class CommentFormView(FormView):
    template_name = 'post.html'
    success_url = "/"
    form_class = CommentForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect("blog:post",pk=instance.post.pk)
        

    # def get_context_data(self,**kwargs):
    #     context = super(CommentFormView,self).get_context_data(**kwargs)
    #     context['contact'] = "active"
    #     return context

def comment_create(request):
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save()
        return redirect("blog:post",pk=instance.post.pk)
    return redirect("blog:drop",)

def search(request):
    param = request.GET.get("search", None)
    categories = Category.objects.all()
    if param:
        posts = Post.objects.filter(
            Q(title__icontains=param)|Q(author__icontains=param)
        )
        return render(request, "index.html", {"index": "active", "posts":posts, "categories":categories}) 
    posts = Post.objects.all()
    return render(request, "index.html", {"index": "active", "posts":posts, "categories":categories})

class SearchListView(ListView):
    model = Post
    template_name = "index.html"

    def get(self, request, args, *kwargs):
        param = request.GET.get("search", None)
        posts = Post.objects.all()       
        if param:
            posts = posts.filter(
                Q(title__icontains=param)|Q(author__icontains=param)
        )
            self.posts = posts       
            # return render(request, "index.html", {"index": "active", "posts":posts, "categories":categories})         
        return self.render_to_response(self.get_context_data(object_list=self.posts))
        # return render(request, "index.html", {"index": "active", "posts":posts, "categories":categories})

def create_post(request):
    form = PostForm(request.POST, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        instance = form.save()
        return redirect("blog:post",pk=instance.pk)
    return render(request, "createpost.html", {"form": form})
