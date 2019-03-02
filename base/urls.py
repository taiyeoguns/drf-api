from django.urls import path, include
from base.router import router

urlpatterns = [path("", include(router.urls))]
