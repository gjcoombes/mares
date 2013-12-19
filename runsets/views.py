#! /usr/bin/env python2
# urls.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader

from runsets.models import RunSet, redis_connection
from runsets.forms import RunSetForm

def index(request):
    return HttpResponse("Welcome to the runsets index page")     


def find_stem(request, stem=None):
    """
    What runsets contain this stem?
    """
    r = RunSet('test', 'manta', 'running')
    r.add('monkeys')
    if r.is_member(stem):
        ctx = {'runsets': [r]}
    else:
        ctx = {}
    template = loader.get_template('runsets/find_stem.html')
    context = RequestContext(request, ctx)  
    s = "You have found the find page using stem: {}".format(stem)
    return HttpResponse(template.render(context))  

def find(request, group='all', machine='all', phase='all'):
    """
    Find all the runs in a runset or runsuperset
    """
    form = RunSetForm({'group': group, 'machine': machine, 'phase': phase})
    r = redis_connection()
    keys_pattern = ":".join([group, machine, phase]).replace('all', '*')
    keys = r.keys(keys_pattern)
    runsets = []
    for k in keys:
        runsets.append(RunSet(r_conn=r, key=k))

    return render(request, 'runsets/find.html', {
            'group'  : group,
            'machine': machine,
            'phase'  : phase,
            'runsets': runsets,
            'form'   : form,
        })

def find_form(request):
    """
    Present form for query
    """
    if request.method == 'POST':
        form = RunSetForm(request.POST)
        if form.is_valid():    
            g = form.cleaned_data['group']
            m = form.cleaned_data['machine']
            p = form.cleaned_data['phase']
        return redirect('runsets:find', group=g, machine=m, phase=p)    
    else:
        form = RunSetForm()
    return render(request, 'runsets/find.html', {'form': form})        