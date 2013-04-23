from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from cause.models import CausePage


def home(request):
    most_recent = CausePage.objects.filter(status=2).order_by('-publish_date')[:10]
    return render_to_response('index.html',
                              {"most_recent":most_recent},
                              context_instance=RequestContext(request))


def cause(request, pageslug):
    causedata = get_object_or_404(CausePage, slug=pageslug)
    return render_to_response('cause/cause.html',
                              {'causedata':causedata},
                              context_instance=RequestContext(request))