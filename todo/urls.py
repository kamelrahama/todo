from django.urls import path
from .import views

urlpatterns = [
    
    path('addTask/', views.addTask, name='addTask'),
    path('mark_As_done/<int:id>/', views.mark_As_done, name='mark_As_done'),
]
 