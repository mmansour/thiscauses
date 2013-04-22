from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from django.core import serializers
from cause.models import CausePage
from mezzanine.utils.views import paginate
from mezzanine.blog.models import BlogPost, BlogCategory


def home(request):
    return render_to_response('index.html',
                            {},
                             context_instance=RequestContext(request))


def cause(request, pageslug):
    causedata = get_object_or_404(CausePage, slug=pageslug)
    return render_to_response('cause/cause.html',
                            {'causedata':causedata},
                             context_instance=RequestContext(request))