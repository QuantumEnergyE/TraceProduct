from django.conf.urls import url

from .views import RecordsList, RecordsCreate, RecordsUpdate, RecordsDelete, RecordsDetail

urlpatterns = [
    url('list', RecordsList.as_view()),
    url('create', RecordsCreate.as_view()),
    url('update/(?P<pk>[0-9]+)', RecordsUpdate.as_view()),
    url('delete/(?P<pk>[0-9]+)', RecordsDelete.as_view()),
    url('detail/(?P<pk>[0-9]+)', RecordsDetail.as_view()),
]