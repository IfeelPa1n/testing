from django.shortcuts import render, redirect
from django.views.generic import View  # Correct import
from django.http import HttpResponse, JsonResponse
from .models import Student, Teacher
from django.contrib import messages
from django.http import JsonResponse

# Debugging import
print("Import successful: django.views.generic.View")

class WelcomeView(View):
    template_name = "welcome_page.html"  # Correct attribute name

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)  # Correct attribute usage

#End of WelcomeView


#Student
class VerifyStud(View):
    template = "verificationStudent.html"

    def get(self, request):
        context = {}
        return render(request, self.template, context)

    def post(self, request):
        id = request.POST.get('id')
        action = request.POST.get('action')

        if action == 'login':
            if Student.objects.filter(id=id).exists():
                return redirect('SchedEvent:StudentMainPage', id=id)  # Pass id in the URL
            else:
                messages.error(request, 'Invalid ID or non-existing')
        elif action == 'create':
            if Student.objects.filter(id=id).exists():
                messages.error(request, 'ID already exists. Please choose a different ID.')
            else:
                # Create a new Student object
                Student.objects.create(id=id)
                return redirect('SchedEvent:StudentMainPage', id=id)  # Pass id in the URL

        return render(request, self.template)
#End of Student

#Teacher
class VerifyTeach(View):
    template = "verificationTeacher.html"

    def get(self, request):
        context = {}
        return render(request, self.template, context)

    def post(self, request):
        id = request.POST.get('id')
        action = request.POST.get('action')

        if action == 'login':
            if Teacher.objects.filter(id=id).exists():
                return redirect('SchedEvent:TeacherMainPage', id=id)  # Redirect with id parameter
            else:
                messages.error(request, 'Invalid ID or non-existing')
        elif action == 'create':
            if Teacher.objects.filter(id=id).exists():
                messages.error(request, 'ID already exists. Please choose a different ID.')
            else:
                # Create a new Teacher object
                Teacher.objects.create(id=id)
                return redirect('SchedEvent:TeacherMainPage', id=id)  # Redirect with id parameter

        return render(request, self.template)
#End of Teacher