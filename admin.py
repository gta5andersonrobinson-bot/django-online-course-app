from django.contrib import admin

# Importing the 7 required classes (models) from your app
from .models import Course, Lesson, Instructor, Enrollment, Question, Choice, Submission

# 1. Implement ChoiceInline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4  # Provides 4 empty choice fields by default

# 2. Implement QuestionInline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# 3. Implement QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    # This embeds the choices directly inside the Question admin page
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson', 'grade')

# 4. Implement LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    # This embeds the questions directly inside the Lesson admin page
    inlines = [QuestionInline]
    list_display = ('title', 'course')

# Registering the remaining models so they show up on the admin site
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Submission)

# Registering Lesson and Question with their custom admin configurations
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)