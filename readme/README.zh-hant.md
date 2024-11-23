<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_django_app_api_auth/readme/README.zh-hant.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_api_auth

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## 說明

介面授權模型.

## 程式碼庫

| [Github](https://github.com/xy-django-app/xy_django_app_api_auth.git)         | [Gitee](https://gitee.com/xy-opensource/xy_django_app_api_auth.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_django_app_api_auth.git)          |
| ----------- | -------------|---------------------------------------|


## 安裝

```bash
# bash
pip install xy_django_app_api_auth
```

## 使用



##### 1. 直接引入

- ###### 1. 設定全域配置

在Django專案中的settings.py檔案中加入如下配置
例如: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

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

- ###### 2. 運行專案

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证接口授权管理系统
```

##### 2. 自訂

- ###### 1. 建立ApiAuth模組

> 操作 [範例工程](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp ApiAuth
# ApiAuth 模块创建在 source/Runner/Admin/ApiAuth 
```

- ###### 2. 設定全域配置

在Django專案中的settings.py檔案中加入如下配置
例如: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

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

- ###### 3. 在[ApiAuth](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth)模組的[models.py](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth/models.py)檔中加入如下程式碼

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

- ###### 4. 在[ApiAuth](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth)模組的[admin.py](../samples/xy_web_server_demo/source/Runner/Admin/ApiAuth/admin.py)檔中加入如下程式碼

```python
# admin.py

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

- ###### 5. 運行專案

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证接口授权管理系统
```

##### 運轉 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 下列倉庫

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------|

## 許可證
xy_django_app_api_auth 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![pay-total](./pay-total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```