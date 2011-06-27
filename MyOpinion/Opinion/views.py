
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.http import HttpResponse,HttpResponseRedirect
from models import Opinion, Comment


@csrf_exempt
def Opinion_detail(request, id, showComments=False):
	
	blog = Opinion.objects.get(pk=id)
	print blog.id,blog.author, blog.title, blog.body
	if showComments:
		comments = Comment.objects.filter(post__pk=id)
	if request.method == 'POST':
		comment = Comment(post=blog)
		form = CommentForm(request.POST,instance=comment)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:
		form = CommentForm()
	t = loader.get_template('blog/detail.html')
	c = Context({'blog':blog, 'comments':comments,'form':form.as_p()})
	return HttpResponse(t.render(c))

@csrf_exempt
def Opinion_avgRating(request,id)
	count=0
	blog = Opinion.objects.get(pk=id)
	if blog.like :
		count=count+1
        else:
 		continue
	t = loader.get_template('blog/avgRating.html')
	c = Context({'blog':blog, 'count':count,'form':form.as_p()})
	return HttpResponse(t.render(c))
def Opinion_editcomment(request, id):
	comment = Comment.objects.get(pk=id)
	if request.method == 'POST':
		form = CommentForm(request.POST,instance=comment)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Opinion/detail/'+str(comment.post.id)+'/True')
	else:
		form = CommentForm(instance=comment)
	t = loader.get_template('Opinion/detail.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c)
def home(request)
    t = loader.get_template('Opinion/home.html')
    c = Context(dict())
    return HttpResponse(t.render(c))


def search(request,term)
    opinion_list = Opinion.object.filter(title__icontains=term)
    t = loader.get_template('Opinion/search.html')
    c = Context({'opinion_list':opinion_list , 'term':term })
    for opinion in opinion_list 
        print Opinion.title
    return HttpResponse(t.render(c))
