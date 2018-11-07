from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from .models import Blog
from .forms import BlogForm
from django.contrib import messages

def index(request):
	posts=Blog.objects.all()
	return render(request,"index.html",{"posts":posts})

def create(request):
	form=BlogForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/')

	context={
		"title":'Post Create',
		"form":form,
	}
	return render(request,'create.html',context)

def detail(request,id):
	posts = Blog.objects.get(id=id)
	print(posts)
	context={
		"posts":posts
	}
	return render(request,"detail.html",context)

def update(request,id):
	instance = get_object_or_404(Blog, id=id)
	form =BlogForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('/')
	context={
		"title":"Post Upadte",
		"form":form
	}
	return render(request,"create.html",context)

def delete(request,id):
	obj=get_object_or_404(Blog,id=id)
	if request.method == 'POST':
		obj.delete()
		messages.success(request, "Your Post Deleted")
		return redirect('/')
	context={
		"obj":obj,
	}
	return render(request,"delete.html",context)