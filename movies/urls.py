from django.conf.urls import url

from . import views

app_name = 'movies'

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^(?P<film_id>[0-9]+)/$', views.EArticleView.as_view(), name='film2'),
    url(r'^comment2/(?P<film_id>[0-9]+)/$', views.add_comment, name='add_comment2'),
]