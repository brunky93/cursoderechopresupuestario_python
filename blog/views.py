from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import domain
from django.shortcuts import redirect

  
def inicio(request):
    return render(request, 'blog/inicio.html', {}) 

def material(request):
    return render(request, 'blog/material.html', {})   

def videos(request):
    return render(request, 'blog/videos.html', {})   

def contacto(request):
    return render(request, 'blog/contacto.html', {})   

def vinculacion(request):
    return render(request, 'blog/libro0.html', {})

def caja(request):
    return render(request, 'blog/libro1.html', {})

def pagos(request):
    return render(request, 'blog/libro2.html', {})

def presupuesto(request):
    return render(request, 'blog/libro3.html', {})

"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})"""

"""
def post_edit(request, pk):
    post = get_object_or_404(domain, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    """