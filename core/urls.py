"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from add_teacher.views import sign
from add_student.views import signs
from feed_data.views import data


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homepage),
    path("a_login/",views.a_login),
    path("a_panel/",views.a_panel),
    path("add_student/",views.add_stud),
    path("add_teacher/",views.add_teacher),
    path("delet_teacher/",views.del_teacher),
    path("feedback/",views.stud_feedback),
    path("feed_form/",views.feed_form),
    path("addteacher/", sign, name="sign"),
    path("addstudent/",signs, name="signs"),
    path("feeddata/",data,name="data") 
]
