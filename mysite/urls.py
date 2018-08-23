"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls')), #include() allows referencing other URLConfs, e.g. polls.urls. also include makes it easy to move polls/ to any other path.
]

#django starts with 1st pattern. so when we go to url 127.0.0.1:8080/polls/ it comes to urlpatterns and see 'admin/', does not patch and then go to 'polls/' and it matches
#Patterns don’t search GET and POST parameters, or the domain name.
# For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/.
# In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.
#path() has 4 argument, 2 required route and view and two optional: kwargs, and name.

