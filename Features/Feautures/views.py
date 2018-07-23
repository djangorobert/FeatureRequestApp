# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import FeatureRequest
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
#Front End view that connects with Knockoutjs

class FeatureRequestCreate(CreateView):
    model = FeatureRequest
    fields = '__all__'
    success_url = '/features/'

class FeatureRequestUpdate(UpdateView):
    model = FeatureRequest
    fields = '__all__'
    template_name_suffix = '_update_form'

class FeatureRequestList(ListView):
    model = FeatureRequest

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    def get_context_data(self, **kwargs):
        context = super(FeatureRequestDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class FeatureRequestDelete(DeleteView):
    model = FeatureRequest
    success_url = '/features/'