from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm
from .models import Post,Comment



# def index(request):
# 	return render(request,'polls/index.html')


def post_list(request):
	posts = Post.objects.order_by('created_date')
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'polls/post_list.html',{'posts':posts})

@login_required
def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	value = Comment.objects.filter(post=post,user=request.user).exists()
	if value == True:
		error = True
		return render(request,'polls/post_detail.html',{'post':post,'error':error})

	# import ipdb; ipdb.set_trace()
   # user = get_object_or_404(User)
	
	# import ipdb; ipdb.set_trace()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user = request.user
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'polls/post_detail.html', {'post':post,'form': form})

	


def signup(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('post_list')
	else:
		form = UserCreationForm()
	return render(request, 'polls/signup.html', {'form': form})


@login_required
def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	value = Comment.objects.filter(post=post,user=request.user).exists()
	if value == True:
		error = "You can't Comment Again"
		return render(request,'polls/post_detail.html',{'post':post,'error':error})

	# import ipdb; ipdb.set_trace()
   # user = get_object_or_404(User)
	
	# import ipdb; ipdb.set_trace()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user = request.user
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'polls/post_detail.html', {'form': form})

  


