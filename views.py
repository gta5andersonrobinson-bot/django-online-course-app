from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Submission, Choice

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Create a new submission instance
        submission = Submission.objects.create(enrollment_id=1) # Hardcoded enrollment for the lab
        
        # Capture the selected choices from the form
        for key, value in request.POST.items():
            if key.startswith('question_'):
                choice_id = value
                choice = Choice.objects.get(pk=choice_id)
                submission.choices.add(choice)
        
        submission.save()
        # Redirect to the results page
        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)
    
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Calculate the exam score
    correct_answers = submission.choices.filter(is_correct=True).count()
    total_questions = course.question_set.count()
    
    score = 0
    if total_questions > 0:
        score = (correct_answers / total_questions) * 100
        
    # Check if they passed (70% or higher)
    passed = score >= 70.0
    
    context = {
        'course': course,
        'submission': submission,
        'score': score,
        'passed': passed
    }
    return render(request, 'onlinecourse/exam_result.html', context)