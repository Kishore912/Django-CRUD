
from django.urls import path
from .views import Final_view,get_view



urlpatterns = [
    path("request",Final_view.as_view()),
    path("get",get_view.as_view()),
#    path('delete/<int:sno>/', Delete_view.as_view())


]
