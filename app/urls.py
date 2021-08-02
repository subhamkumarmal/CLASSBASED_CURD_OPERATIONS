from django.urls import path
from . import views

urlpatterns=[
    path('',views.CreateDetails.as_view()),
    path('list',views.DetailList.as_view()),
    path('details/<int:pk>',views.DetailsViews.as_view()),
    path('update/<int:pk>',views.DetailsUpdata.as_view()),
    path('delete/<int:pk>',views.DetailsDelete.as_view())
]