from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home.as_view(), name = 'home'),
	url(r'^files/$', views.files.as_view(), name = 'files'),
	url(r'^social/$', views.social.as_view(), name = 'social'),

]