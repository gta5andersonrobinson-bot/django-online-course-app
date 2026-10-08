from django.urls import path
from . import views

# Add these inside your existing urlpatterns list:
urlpatterns = [
    # ... your other paths might be up here ...
    
    # Route for submitting the exam
    path('<int:course_id>/submit/', views.submit, name='submit'),
    
    # Route for showing the exam result
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]