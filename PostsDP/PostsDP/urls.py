from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from backend_api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostsViews.as_view(), name="posts view")
]
