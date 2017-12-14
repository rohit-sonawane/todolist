from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', # ADD THIS URL
                               namespace='rest_framework')), 
    url(r'^todolists/$', CreateView.as_view(), name="create"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
   
    #url(r'^get-token/', obtain_auth_token), # Add this line
}

urlpatterns = format_suffix_patterns(urlpatterns)