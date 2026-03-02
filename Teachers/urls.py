from django.urls import path
from . import views

urlpatterns = [
    
    #* function based 
    # path('', views.teacherView),
    # path('teacher/<int:pk>', views.teacherDetailsView),

    #* Class based 
    # path('', views.Teachers.as_view()),
    # path('teacher/<int:pk>', views.TeachersDetail.as_view()),

    path('teacherV/', views.TeacherView.as_view()),
    path('subjectV/', views.SubjectView.as_view()),

    path('teacherV/<int:pk>/', views.TeacherDetailsView.as_view()),
    path('subjectV/<int:pk>/', views.SubjectDetailsView.as_view()),
]
