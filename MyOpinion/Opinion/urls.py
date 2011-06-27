from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'Opinion.views.home'),
	url(r'^(detail|info)/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'Opinion.views.Opinion_detail'),
	url(r'^search/(.)+$','Opinion.views.search'),
	url(r'^editcomment/(?P<id>\d+)/$','Opinion.views.Opinion_editcomment'),
	url(r'^rating/(?P<id>\d+)/$','Opinion.views.Opinion_avgRating'),
	)
