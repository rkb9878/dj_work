from django.contrib import admin
from blog import models
# Register your models here.


admin.site.register([models.Blog,models.Author,models.Entry])

