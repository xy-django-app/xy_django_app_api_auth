from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
import time
from django.db import models
from datetime import datetime

# Create your models here.
class ApiAuthCredentialAbstract(models.Model):
    
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(verbose_name=_(u"名称"), max_length=255, null=True, blank=True)
    app_key = models.UUIDField(verbose_name=_(u"app_key"), default=uuid.uuid4, editable=True, unique=True, blank=True, null=True)
    app_secret = models.UUIDField(verbose_name=_(u"app_secret"), default=uuid.uuid4, editable=True, unique=True, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _(u"授权用户凭证")
        verbose_name_plural = _(u"授权用户凭证")
        app_label = "xy_django_app_api_auth"

    def __str__(self):
        return str(self.id) + ". " + str(self.name) + " (" + str(self.app_key) + ")"


class ApiAuthCredential(ApiAuthCredentialAbstract):
    versions = models.ManyToManyField("xy_django_app_information.Version", verbose_name=_(u"所属版本"), related_name='%(app_label)s_%(class)s_versions', blank=True)

class ApiAuthCredentialCacheAbstract(models.Model):
    
    id = models.BigAutoField(primary_key=True)

    url = models.TextField(verbose_name=_(u"名称"), null=True, blank=True)
    time_stamp = models.DateTimeField(verbose_name=_(u"timestamp"), null=True, blank=True)
    nonce = models.TextField(verbose_name=_(u"nonce标识码"), null=True, blank=True)
    sign = models.TextField(verbose_name=_(u"sign标识码"), null=True, blank=True)

    @property
    def over_time_default(self):
        '''超时时间'''
        return 60

    @property
    def time_stamp_validate(self):
        if self.time_stamp == None:
            return False
        return time.mktime(self.time_stamp.timetuple())-time.mktime(datetime.now().timetuple()) <= self.over_time_default
    
    class Meta:
        abstract = True
        verbose_name = _(u"授权用户凭证缓存")
        verbose_name_plural = _(u"授权用户凭证缓存")
        app_label = "xy_django_app_api_auth"

    def __str__(self):
        return str(self.id) + ". " + str(self.url)


class ApiAuthCredentialCache(ApiAuthCredentialCacheAbstract):
    credential = models.ForeignKey("xy_django_app_api_auth.ApiAuthCredential", verbose_name=_(u"凭证"), related_name='%(app_label)s_%(class)s_credential', on_delete=models.SET_NULL, null=True, blank=True)
    