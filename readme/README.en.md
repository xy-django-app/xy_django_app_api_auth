<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_app_api_auth/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_api_auth

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

Interface authorization model.

## Source Code Repositories

| [Github](https://github.com/xy-django-app/xy_django_app_api_auth.git)         | [Gitee](https://gitee.com/xy-opensource/xy_django_app_api_auth.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_django_app_api_auth.git)          |
| ----------- | -------------|---------------------------------------|
 

## Installation

```bash
# bash
pip install xy_django_app_api_auth
```

## How to use


##### 1. Direct import

- ###### 1. Setting global configuration

Add the following configuration to the settings.py file in the Django project.  
For example:[settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_information",
    "xy_django_app_api_auth",
    "Demo",
    "Resource",
    "Media",
]

```

- ###### 2. Run the project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证接口授权管理系统
```

##### 2. Custom

- ###### 1. Create the ApiAuth module

> Operation [Sample Project](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp ApiAuth
# ApiAuth 模块创建在 source/Runner/Admin/ApiAuth 
```

- ###### 2. Setting global configuration

Add the following configuration to the settings.py file in the Django project.  
For example: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Demo",
    "Resource",
    "Media",
    "ApiAuth",
]

```

- ###### 3. Add the following code to the [models.py](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth/models.py) of the  [ApiAuth](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth) module

```python
# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from xy_django_app_api_auth.abstracts import *


class MApiAuthCredential(MAApiAuthCredential):
    versions = models.ManyToManyField(
        "xy_django_app_information.MVersion",
        verbose_name=_("所属版本"),
        related_name="%(app_label)s_%(class)s_versions",
        blank=True,
    )

    class Meta:
        verbose_name = _("授权用户凭证")
        verbose_name_plural = _("授权用户凭证")
        app_label = "ApiAuth"


class MApiAuthCredentialCache(MAApiAuthCredentialCache):
    credential = models.ForeignKey(
        "ApiAuth.MApiAuthCredential",
        verbose_name=_("凭证"),
        related_name="%(app_label)s_%(class)s_credential",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("授权用户凭证缓存")
        verbose_name_plural = _("授权用户凭证缓存")
        app_label = "ApiAuth"

```

- ###### 4. Add the following code to the [admin.py](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth/admin.py) of the [ApiAuth](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth) module

```python
# admin.py
# -*- coding: UTF-8 -*-


from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(MApiAuthCredential)
class AApiAuthCredential(admin.ModelAdmin):
    pass


@admin.register(MApiAuthCredentialCache)
class AApiAuthCredentialCache(admin.ModelAdmin):
    pass

```

- ###### 5. Run the project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证接口授权管理系统
```

##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------|  


## License
xy_django_app_api_auth is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![pay-total](./pay-total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```