"""Features URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Feautures import views
from Feautures.models import FeatureRequest
#for the api, the routers there like urls but for the API.
from rest_framework import routers, viewsets
from Feautures.serializers import FeatureRequestSerializer

#API Djanog Rest Framework Viewset its like a View but for an api
#API View
class FeatureRequestViewSet(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer

router = routers.DefaultRouter()
router.register(r'featuresapi', FeatureRequestViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('features', views.FeatureRequestList.as_view(), name='feature_list'),
	url('new', views.FeatureRequestCreate.as_view(), name='feature_form'),
    url(r'^(?P<pk>\d+)\$', views.FeatureRequestDetailView.as_view(), name='featurerequest_detail'),
	url('r\^edit/(?P<pk>\d+)/edit/\$', views.FeatureRequestUpdate.as_view(), name='feature_update_form'),
    
    url('r\^delete/(?P<pk>\d+)/edit/\$', views.FeatureRequestDelete.as_view(), name='featurerequest_confirm_delete'),
    
]
