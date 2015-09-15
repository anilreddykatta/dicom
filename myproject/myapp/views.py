# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            print(newdoc)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.search'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form, 'header': 'header.html'},
        context_instance=RequestContext(request)
    )


def search(request):
    if request.GET.get('filename'):
        documents = Document.objects.filter(docfile__icontains = request.GET.get('filename'))
        return render_to_response('searchresults.html',
                                  {'documents':documents, 'header':'header.html'},
                                  context_instance=RequestContext(request)
                                  )
    else:
        return render_to_response('searchresults.html',
                                  {'documents':Document.objects.all(), 'header':'header.html'},
                                  context_instance=RequestContext(request)
                                  )
    

def view(request):
    print(request.GET.get('file'))
    if request.GET.get('file'):
        return render_to_response('dicomviewer.html',
                                  {'document': request.GET.get('file'), 'header':'header.html'},
                                  context_instance=RequestContext(request)
                                  )