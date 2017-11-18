from django.conf.urls import url
from django.views.generic.base import TemplateView


class ProfileView(TemplateView):
    template_name = "profile.html"


urlpatterns = [
    url(r'^profile/$', ProfileView.as_view(), name="list"),
]