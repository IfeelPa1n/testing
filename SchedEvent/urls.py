from django.urls import path
from . import views

print("Import successful: .views")

app_name = 'SchedEvent'

urlpatterns = [
    path("", views.WelcomeView.as_view(), name="welcomepage"),
    path("StudentVerify/", views.VerifyStud.as_view(), name="StudentVerificationStop"),
    path("TeacherVerify/", views.VerifyTeach.as_view(), name="TeacherVerificationStop"),
]