from django.conf.urls import url

from jobs import views


urlpatterns = [
    url(r'^list/$', views.job_list),
    url(r'^pending/$', views.pending_job_list),
    url(r'^active/$', views.active_job_list),
    url(r'^complete/$', views.complete_job_list),
    url(r'^job/(?P<pk>[0-9]+)/$', views.job_detail),
]
