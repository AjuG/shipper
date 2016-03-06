from django.conf.urls import url

from jobs import views


urlpatterns = [
    url(r'^list/$', views.job_list),
    url(r'^pending/$', views.pending_job_list),
    url(r'^active/$', views.active_job_list),
    url(r'^complete/$', views.complete_job_list),
    url(r'^detail/(?P<uid>[0-9]+)/$', views.job_detail),
    url(r'^(?P<job_uid>[0-9]+)/get_porter/(?P<search_radius>[0-9]+)/$', views.get_available_porter),
]
