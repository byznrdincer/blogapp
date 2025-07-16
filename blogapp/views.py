from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comments
from .forms import PostForm,CommentsForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    posts=Post.objects.all()
    return render (request,'blog/home.html',{'posts':posts})

def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    comments=post.comments.all()
    if request.method=="POST":
        comment_form=CommentsForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            return redirect('post_detail',id=post.id)
    else:
        comment_form=CommentsForm()
    return render(request,'blog/post_detail.html',{'post':post,'comments':comments,'comment_form':comment_form})
    
def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=="POST":
       form=PostForm(request.POST,instance=post)
       if form.is_valid():
           form.save()
           return redirect('post_detail',id=post.id)
    else:
        form=PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})

def post_delete(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('home')
    
    
@login_required
def profile_view(request):
    profile = request.user.userprofile  # Giriş yapan kullanıcının profilini al

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Profil kaydedildikten sonra aynı sayfaya yönlendir
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'blog/profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


