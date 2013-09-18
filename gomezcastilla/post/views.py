from gomezcastilla.post.models import Post, Category
from django.shortcuts import render_to_response
from django.template.defaultfilters import slugify
from django.template import RequestContext

def loop(request):
	posts = Post.objects.order_by('-creation_date')
	return render_to_response('index.html',{'posts':posts}, context_instance=RequestContext(request))

def single(request,idpost):
	single = Post.objects.get(slug=idpost)
	return render_to_response('single.html',{'single':single}, context_instance=RequestContext(request))

