from django.views import View
from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from .models import Comment, Film, Comment2
from django.utils import timezone

from django.views.decorators.http import require_http_methods

from .forms import Comment2Form

from django.template.context_processors import csrf

from django.core.exceptions import ObjectDoesNotExist

def index(request):
	context = {'films': Film.objects.all()}
	return render(request, 'movies/index.html', context)

class EArticleView(View):
    template_name = 'movies/film2.html'
    comment_form = Comment2Form
 
    def get(self, request, *args, **kwargs):
        film = get_object_or_404(Film, id=self.kwargs['film_id'])
        context = {}
        context.update(csrf(request))
        user = "y"
        context['film'] = film
        context['comments'] = film.comment2_set.all().order_by('path')

        context['form'] = self.comment_form
 
        return render_to_response(template_name=self.template_name, context=context)
 
@require_http_methods(["POST"])
def add_comment(request, film_id):
 
    form = Comment2Form(request.POST)
    film = get_object_or_404(Film, id=film_id)
 
    if form.is_valid():
        comment = Comment2()
        comment.path = []
        comment.film_id = film
        comment.author = form.cleaned_data['author']
        comment.content = form.cleaned_data['comment_area']
        comment.save()
 
        try:
            comment.path.extend(Comment2.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)
 
        comment.save()
 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))