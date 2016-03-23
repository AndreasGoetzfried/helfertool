from django.conf.urls import url

from . import views

app_name = 'badges'
urlpatterns = [
    #
    # settings
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/settings/$',
        views.settings,
        name='settings'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/settings/advanced',
        views.settings_advanced,
        name='settings_advanced'),

    #
    # permission
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/permission/'
        '(?P<permission_pk>[0-9]+)/$',
        views.edit_permission,
        name='edit_permission'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/permission/add/',
        views.edit_permission,
        name='new_permission'),

    #
    # role
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/role/'
        '(?P<role_pk>[0-9]+)/$',
        views.edit_role,
        name='edit_role'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/role/add/',
        views.edit_role,
        name='new_role'),

    #
    # design
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/design/'
        '(?P<design_pk>[0-9]+)/$',
        views.edit_design,
        name='edit_design'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/design/add/',
        views.edit_design,
        name='new_design'),

    #
    # badge generation
    #

    # overview page
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/$',
        views.index,
        name='index'),

    # warnings
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/warnings/'
        '(?P<job_pk>[0-9]+)$',
        views.warnings,
        name='warnings'),

    # generate for job
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/generate/'
        '(?P<job_pk>[0-9]+)/$',
        views.generate,
        name='generate_for_job'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/generate/'
        '(?P<job_pk>[0-9]+)/all/$',
        views.generate,
        {'generate_all': True},
        name='generate_all_for_job'),

    # generate for all jobs
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/generate/$',
        views.generate,
        name='generate'),

    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/generate/all/$',
        views.generate,
        {'generate_all': True},
        name='generate_all'),

    #
    # register badges
    #
    url(r'^(?P<event_url_name>[a-zA-Z0-9]+)/badges/register/',
        views.register,
        name='register'),
]