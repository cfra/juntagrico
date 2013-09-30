from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
from django.contrib.auth.views import login, logout
from django.views.generic import RedirectView



urlpatterns = patterns('',
	url('^$', 'static_ortoloco.views.home'),
	url('^aktuelles', 'static_ortoloco.views.home'),
	url('^idee', 'static_ortoloco.views.about'),
	url('^portrait', 'static_ortoloco.views.portrait'),
	url('^hintergrund', 'static_ortoloco.views.background'),
	url('^abo', 'static_ortoloco.views.abo'),
	url('^faq', 'static_ortoloco.views.faq'),
	url('^mitmachen', 'static_ortoloco.views.join'),
	url('^galerie', RedirectView.as_view(url='/photologue/gallery/page/1/')),
	url('^medien', 'static_ortoloco.views.media'),
    url('^kontakt', 'static_ortoloco.views.contact'),

    #url('^myortoloco/', 'my_ortoloco.views.myortoloco_home'),
    url('^my/home', 'my_ortoloco.views.my_home'),
    url('^my/passwort', 'my_ortoloco.views.my_change_password'),
    url('^my/jobs(?P<job_id>.*?)/', 'my_ortoloco.views.my_job'),
    url('^my/teams/(?P<bereich_id>.*?)/', 'my_ortoloco.views.my_team'),
    url('^my/profil', 'my_ortoloco.views.my_profile'),


    (r'^accounts/login/$',  login),
    (r'^logout/$', 'my_ortoloco.views.logout_view'),

    (r'^photologue/', include('photologue.urls')),

    url('^depots/', 'my_ortoloco.views.all_depots'),
    url('^depotliste/(?P<name_or_id>.*?)/', 'my_ortoloco.views.depot_list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^tinymce/', include('tinymce.urls')),
    url(r'^medias/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
	url(r'^downloads/(?P<param>.*)$', RedirectView.as_view(url='/medias/downloads/%(param)s')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),

)
