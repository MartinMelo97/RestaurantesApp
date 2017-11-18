from django.conf.urls import url
from .views import RestaurantsListView, RestaurantsDetailView, RestaurantCreateView, RestaurantEditView, RestaurantDeleteView

urlpatterns = [
    url(r'^$', RestaurantsListView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9]+)/$', RestaurantsDetailView.as_view(), name='detail'),
    url(r'^new/$', RestaurantCreateView.as_view(), name="new"),
    url(r'^edit/(?P<pk>[0-9]+)/$', RestaurantEditView.as_view(), name="edit"),
    url(r'^delete/(?P<pk>[0-9]+)/$', RestaurantDeleteView.as_view(), name="delete")
]