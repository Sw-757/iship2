from django.contrib import admin
from django.urls import path, include, re_path
from core.views import *

from django.views.static import serve

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', ReactView.as_view(), name="something"),

]

