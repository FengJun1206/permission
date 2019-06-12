from django.contrib import admin
from app import models

admin.site.register(models.UserProfile)
admin.site.register(models.Role)
admin.site.register(models.Menus)
admin.site.register(models.UserDetail)


