from django.contrib import admin
from django.db import models



# Create your models here.
class Opinion(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
	created=models.DateField(auto_now_add=True)
	author=models.CharField(max_length=50)
	like=models.BooleanField()
	def __unicode__(self):
		return self.title


class OpinionAdmin(admin.ModelAdmin):
	list_display = ('title','created','updated','like')
	list_filter = ('created',)
	search_fields = ('title','body')
	inlines = [CommentInline]
	def __unicode__(self):
		return self.list_display 

	
admin.site.register(Opinion, OpinionAdmin)

	
