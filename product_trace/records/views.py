from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Records

# Create your views here.


class RecordsList(LoginRequiredMixin, ListView):
    model = Records
    template_name = "records/list.html"

    def get_queryset(self):
        uid = self.request.GET.get('uid', None)
        if not uid:
            return self.model.objects.order_by('-updated_time')[:10]
        return self.model.objects.filter(uid=uid)


class RecordsCreate(LoginRequiredMixin, CreateView):
    model = Records
    fields = ['uid', 'url']
    template_name = "records/create.html"
    success_url = '/records/list'


class RecordsUpdate(LoginRequiredMixin, UpdateView):
    model = Records
    fields = ['uid', 'url']
    template_name = "records/update.html"
    success_url = '/records/list'


class RecordsDelete(LoginRequiredMixin, DeleteView):
    model = Records
    template_name = "records/delete.html"
    success_url = '/records/list'


class RecordsDetail(LoginRequiredMixin, DetailView):
    model = Records
    template_name = "records/detail.html"
    success_url = '/records/list'

