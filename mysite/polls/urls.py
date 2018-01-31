from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # ex: /polls/5/
    url(r'^index/(?P<question_id>[\w-]+)/$', views.detail, name="detail"),
    # ex: /polls/5/results/
    url(r'^index/(?P<question_id>[\w-]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^index/(?P<question_id>[\w-]+)/vote/$', views.vote, name='vote'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)