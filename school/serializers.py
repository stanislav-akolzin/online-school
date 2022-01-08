'''School app serializers'''
from rest_framework import serializers
from .import models


class TrainingCourseSerializer(serializers.ModelSerializer):
    '''Serializer for training course model'''

    mark = serializers.DecimalField(4, source='get_mark',  decimal_places=2)
    class Meta:
        model = models.TrainingCourse
        fields = ['name', 'description', 'mark']


class FileSerializer(serializers.ModelSerializer):
    '''Serializer for file materials'''
    class Meta:
        model = models.FileMaterial
        fields = ['title', 'description', 'content']


class TextSerializer(serializers.ModelSerializer):
    '''Serializer for text materials'''
    class Meta:
        model = models.TextMaterial
        fields = ['title', 'description', 'content']


class URLSerializer(serializers.ModelSerializer):
    '''Serializer for web-links for educational materials'''
    class Meta:
        model = models.LinkMaterial
        fields = ['title', 'description', 'content']

    
class GetMaterialsSerializer(serializers.ModelSerializer):
    '''Serializer for getting educational materials grouped by training courses'''
    files = FileSerializer(many=True)
    texts = TextSerializer(many=True)
    links = URLSerializer(many=True)

    class Meta:
        model = models.TrainingCourse
        fields = ['name', 'files', 'texts', 'links']


class GradeSerializer(serializers.ModelSerializer):
    '''Serializer for grades'''
    class Meta:
        model = models.Grade
        fields = ['course', 'user', 'mark']