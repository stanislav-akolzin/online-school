from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class TrainingCourse(models.Model):
    '''Courses of online school'''
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name

    def get_mark(self):
        mark = Grade.objects.filter(course=self).aggregate(Avg('mark'))['mark__avg']
        if mark is None:
            return 0
        else:
            return mark


class UsersCourses(models.Model):
    '''Courses chosen by each user'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'users\' courses'

    def __str__(self) -> str:
        return self.user.username + '  -  ' + self.training_course.name


class FileMaterial(models.Model):
    '''File materials for courses'''
    title = models.CharField(max_length=250)
    content = models.FileField(upload_to='content/')
    description = models.TextField()
    training_course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE, related_name='files')

    class Meta:
        verbose_name_plural = 'file materials'

    def __str__(self):
        return self.title


class TextMaterial(models.Model):
    '''Text materials for courses'''
    title = models.CharField(max_length=250)
    content = models.TextField()
    description = models.TextField()
    training_course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE, related_name='texts')

    class Meta:
        verbose_name_plural = 'text materials'

    def __str__(self):
        return self.title


class LinkMaterial(models.Model):
    '''Web-links for educational materials for courses'''
    title = models.CharField(max_length=250)
    content = models.URLField(max_length=500)
    description = models.TextField()
    training_course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE, related_name='links')

    class Meta:
        verbose_name_plural = 'Web-links'

    def __str__(self):
        return self.title


class Grade(models.Model):
    '''Users marks for course'''
    course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(validators=[
                                    MinValueValidator(1),
                                    MaxValueValidator(5)
                                    ])

    class Meta:
        verbose_name_plural = 'grades'

    def __str__(self):
        return str(self.mark)