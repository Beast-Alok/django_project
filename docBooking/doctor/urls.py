from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.register,name="index"),
    path('login/',views.login_page,name="login_page"),
    path('appoint/',views.appoint,name="appoint"),
    path('docPage/',views.doctor_page,name="doctor_page"),
]
