from django.contrib import admin
from blogs.models import AutherRegistration, BlogModel
# Register your models here.
admin.site.register(AutherRegistration)
admin.site.register(BlogModel)