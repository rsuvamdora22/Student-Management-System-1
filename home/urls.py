from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('details/', views.details, name='data'),
    path('student/<int:pk>/', views.student_detail, name='detail'),
    path('search/', views.search, name='search'),
    path('remove_student/<int:pk>/', views.remove_student, name='remove_student'),
    path('history/', views.history, name='history'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),  
    path('student/<int:pk>/edit/', views.edit_student, name='edit_student'),
]
