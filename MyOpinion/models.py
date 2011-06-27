from django.db import models
from django.contrib import admin

# Create your models here.

class Comment(models.Model):
	body=  models.TextField()
        author=models.CharField(max_length=60)
	created    = models.DateTimeField(auto_now=True)
    	updated    = models.DateTimeField(auto_now=True)
	link= models.ForeignKey(Opinion)
	def __unicode__(self):
		return str(self.post)+","+self.author
	def body_first_70(self):
		return self.body[:60]

class CommentInline(admin.TabularInline):
	model = Comment

class CommentAdmin(admin.ModelAdmin):
	list_display=('link','author','created','updated')
	list_display = ('body_first_70',)
	list_filter = ('created','author')

admin.site.register(Comment,CommentAdmin)
