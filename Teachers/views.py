from django.shortcuts import render
from django.http import Http404
from Teachers.models import Teacher, Subject
from Teachers.serializers import TeacherSerializer, SubjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics



#*function based view


# @api_view(['GET', 'POST'])
# def teacherView(request):
#     if request.method == 'GET':
#         teacher = Teacher.objects.all()
#         serializer = TeacherSerializer(teacher, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == "POST":
#         serializer = TeacherSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def teacherDetailsView(request, pk):
#     try:
#         teachers = Teacher.objects.get(pk = pk)
#     except Teacher.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TeacherSerializer(teachers)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         serializer = TeacherSerializer(teachers, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         teachers.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

#* Class based view


# class Teachers(APIView):
#     def get(self, request):
#         teachers = Teacher.objects.all()
#         serializer = TeacherSerializer(teachers, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = TeacherSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TeachersDetail(APIView):
#     def get_object(self , pk):
#         try:
#             return Teacher.objects.get(pk = pk)
#         except Teacher.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         teacher = self.get_object(pk)
#         serializer = TeacherSerializer(teacher)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         teacher = self.get_object(pk)
#         serializer = TeacherSerializer(teacher, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         teacher = self.get_object(pk)
#         teacher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
#* Nested serializers
class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    
class TeacherDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'pk'

class SubjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'pk'

    


