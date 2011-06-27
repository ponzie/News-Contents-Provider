from django.contrib import admin
from django.db import models



# Create your models here.!!!!
class Opinion(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
	created=models.DateField(auto_now_add=True)
	author=models.CharField(max_length=50)
	like=models.BooleanField()
	def __unicode__(self):
		return self.title



class CommentInline(admin.TabularInline):
	model = Comment	
class Comment(models.Model):
	body=  models.TextField()
        author=models.CharField(max_length=60)
	created    = models.DateTimeField(auto_now=True)
    	updated    = models.DateTimeField(auto_now=True)
	link= models.ForeignKey(Opinion)
	def __unicode__(self):
		return str(self.post)+","+self.author
	def body_first_70(self):
		return self.body[:70]


class OpinionAdmin(admin.ModelAdmin):
	list_display = ('title','created','updated','like')
	list_filter = ('created',)
	search_fields = ('title','body')
	inlines = [CommentInline]
	def __unicode__(self):
		return self.list_display 

class CommentAdmin(admin.ModelAdmin):
	list_display=('link','author','created','updated')
	list_display = ('body_first_70',)
	list_filter = ('created','author')

admin.site.register(Opinion, OpinionAdmin)
admin.site.register(Comment,CommentAdmin)


	
