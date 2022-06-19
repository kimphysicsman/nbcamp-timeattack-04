from django.contrib import admin
from .models import User, UserType, UserLog

# Register your models here.
admin.site.register(User)
admin.site.register(UserType)
admin.site.register(UserLog)