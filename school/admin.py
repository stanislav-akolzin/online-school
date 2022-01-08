from django.contrib import admin
from .import models


admin.site.register(models.TrainingCourse)
admin.site.register(models.UsersCourses)
admin.site.register(models.FileMaterial)
admin.site.register(models.TextMaterial)
admin.site.register(models.LinkMaterial)