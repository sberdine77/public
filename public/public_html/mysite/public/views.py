from django.shortcuts import render
from django.views.generic import TemplateView

class home(TemplateView):
	template_name = 'public/index.html'

def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['content'] = [
        { 'title': 'XXXXXX'},
        { 'title': 'Files'},
        { 'title': 'Social'},
    ]
    return context

class files(TemplateView):
	template_name = 'public/files.html'

class social(TemplateView):
	template_name = 'public/social.html'
