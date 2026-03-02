from rest_framework import serializers
from .models import Teacher, Subject



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

        
class TeacherSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many= True, read_only =True)
    class Meta:
        model = Teacher
        fields = "__all__"