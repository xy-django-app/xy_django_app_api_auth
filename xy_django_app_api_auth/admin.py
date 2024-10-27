#-*- coding: UTF-8 -*-

from django.contrib import admin
from .models import *
# Register your models here.

class ApiAuthCredentialAdmin(admin.ModelAdmin):
    pass

admin.site.register(ApiAuthCredential, ApiAuthCredentialAdmin)

class ApiAuthCredentialCacheAdmin(admin.ModelAdmin):
    pass

admin.site.register(ApiAuthCredentialCache, ApiAuthCredentialCacheAdmin)
