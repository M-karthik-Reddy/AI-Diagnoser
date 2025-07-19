from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="detect_page"),
    path("upload/",views.detect_retinopathy,name="detect_retinopathy"),
    path('result/', views.retino_result, name='retino_result'),
    path('history/',views.get_history,name="get_history"),
]