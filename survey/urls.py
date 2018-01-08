"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from survey_app.views import LogisticView,survey_detailView, we_offerView, IndexView, ReportsView
from home import views
from home.views import IndexView, ReportsView, LogisticView, we_offerView, survey_detailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^organization/$', views.organization, name='organization'),
    url(r'^logistic/',LogisticView.as_view(), name='logistic'),
    url(r'^human/$', views.human_res, name='human_res'),
    url(r'^reports/$', ReportsView.as_view(), name='reports'),
    url(r'^major_works/$', views.major_works, name='major_works'),
    # url(r'/home/ajax/$', views.process_ajax, name='major_works'),
    url(r'^upworking_works/$', views.upworking_works, name='upworking_works'),
    url(r'^ongoing_works/$', views.ongoing_works, name='ongoing_works'),
    # # url(r'^we_offer/$', views.we_offer, name='we_offer'),
    url(r'^we_offer/$',we_offerView.as_view(), name='we_offer'),
    # # url(r'^detail/$', views.survey_detail, name='survey_detail'),
    url(r'^detail/$',survey_detailView.as_view(), name='survey_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)