from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename = 'employee')



urlpatterns = [
    # function based 
    path('students/', views.studentsView),
    path('students/<int:pk>', views.studentsDetailView),

    # class based 
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>', views.EmployeeDetail.as_view()),

    path('', include(router.urls)),
    
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

]
