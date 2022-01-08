from .import models, serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.exceptions import APIException


class TrainingCourseList(generics.ListAPIView):
    '''Class for all courses of online school'''
    permission_classes = [AllowAny]
    queryset = models.TrainingCourse.objects.all()
    serializer_class = serializers.TrainingCourseSerializer


class MyCourses(generics.ListAPIView):
    '''Class of courses of a particular user'''
    auhtentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TrainingCourseSerializer

    def get_queryset(self):
        return models.TrainingCourse.objects.filter(userscourses__user_id=self.request.user.id)


class Materials(generics.ListAPIView):
    '''Class of materials for courses'''
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GetMaterialsSerializer

    def get_queryset(self):
        return models.TrainingCourse.objects.filter(userscourses__user_id=self.request.user.id)


class PassedCourses(APIException):
    status_code = HTTP_403_FORBIDDEN
    default_detail = 'You haven\'t taken this course yet, so you can\'t mark it.'


class MultipleGrade(APIException):
    status_code = HTTP_403_FORBIDDEN
    default_detail = 'You\'ve already marked this course.'


class Grade(generics.CreateAPIView):
    '''Class for making grades'''
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GradeSerializer
    
    def perform_create(self, serializer):
        if len(models.UsersCourses.objects.filter(user=self.request.user, training_course_id=self.request.data['course'])) >= 1:
            if (len(models.Grade.objects.filter(user=self.request.user, course_id=self.request.data['course']))) == 0:
                return serializer.save()
            else:
                raise MultipleGrade
        else:
            raise PassedCourses