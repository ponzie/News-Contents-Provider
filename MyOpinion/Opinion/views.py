def blog_editcomment(request, id):
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
