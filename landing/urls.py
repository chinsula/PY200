from django.urls import path
from landing.views import TemplView

urlpatterns = [
    path('', TemplView.as_view()),
]