from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # login, logout
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),

    # admin interface
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/new/$', views.edit_event, name='new_event'),

    # internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # registration
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/$', views.form, name='form'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/registered/(?P<helper_id>[a-z0-9\-]+)/$',
        views.registered, name='registered'),

    # manage event
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/manage/$', views.admin, name='manage_event'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/edit/$', views.edit_event, name='edit_event'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/delete/$', views.delete_event, name='delete_event'),

    # jobs
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/jobs/$', views.jobs_and_shifts, name='jobs_and_shifts'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/jobs/new/$', views.edit_job, name='new_job'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/jobs/(?P<job_pk>[0-9]+)/edit/$', views.edit_job, name='edit_job'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/jobs/(?P<job_pk>[0-9]+)/delete/$', views.delete_job, name='delete_job'),

    # shifts
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/jobs/(?P<job_pk>[0-9]+)/shift/(?P<shift_pk>[0-9]+)$', views.edit_shift, name='edit_shift'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/jobs/(?P<job_pk>[0-9]+)/shift/(?P<shift_pk>[0-9]+)/delete/$', views.delete_shift, name='delete_shift'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/jobs/(?P<job_pk>[0-9]+)/shift/new$', views.edit_shift, name='new_shift'),

    # helpers
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/helpers/$', views.helpers, name='helpers'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/helpers/job/(?P<job_pk>[0-9]+)$', views.helpers, name='jobhelpers'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/helpers/(?P<helper_pk>[0-9a-f\-]+)$', views.edit_helper, name='edit_helper'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/helpers/(?P<helper_pk>[0-9a-f\-]+)/delete/(?P<job_pk>[0-9]+)$', views.delete_helper, name='delete_helper'),

    # excel
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/excel/all$', views.excel, name='excel'),
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/excel/(?P<job_pk>[0-9]+)$', views.excel, name='jobexcel'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
