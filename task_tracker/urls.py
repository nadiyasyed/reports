from django.conf.urls import patterns, include, url
from django.conf import settings
from  account import views
from django.views.generic import TemplateView

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    

    url(r'^$',views.LoginView.as_view()),
    # HIgh Chart For Rainfall
    # url(r'^high/$',views.HighView.as_view()),
    url(r'^pdf/$',views.PdfView.as_view(template_name="mytemplate.html")),

    # url(r'^pdf/$',views.generate_pdf),
    url(r'^view-in-pdf/$', views.view_in_pdf, name='view_in_pdf'),
    url(r'^view-in-html/$', views.view_in_html, name='view_in_html'),

    # # url(r'^admin/', include(admin.site.urls)),
    # url(r'^account/', include('account.urls')),
    # url(r'^project/', include('project.urls')),
    # url(r'^task/', include('task.urls')),
)