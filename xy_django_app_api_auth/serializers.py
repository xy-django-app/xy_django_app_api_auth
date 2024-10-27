#-*- coding: UTF-8 -*-


from .models import *
from rest_framework import viewsets
from xy_admin_model_serializer.Admin_ModelSerializer import *

# Serializers define the API representation.
class ApiAuthCredentialSerializer(Admin_ModelSerializer):

    default_value = ""
    class Meta:
        model = ApiAuthCredential
        fields = '__all__'

# ViewSets define the view behavior.
class ApiAuthCredentialViewSet(viewsets.ModelViewSet):
    queryset = ApiAuthCredential.objects.all()
    serializer_class = ApiAuthCredentialSerializer


# Serializers define the API representation.
class ApiAuthCredentialCacheSerializer(Admin_ModelSerializer):

    default_value = ""
    
    class Meta:
        model = ApiAuthCredentialCache
        fields = "__all__"


# ViewSets define the view behavior.
class ApiAuthCredentialCacheViewSet(viewsets.ModelViewSet):
    queryset = ApiAuthCredentialCache.objects.all()
    serializer_class = ApiAuthCredentialCacheSerializer

