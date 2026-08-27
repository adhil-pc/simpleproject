from django.urls import path
from . import views
from .views import LoginView,RegisterView,ListExpense,UpdateExpense,DeleteExpense,CreateExpense
urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',LoginView,name='login'),
    path('register/',RegisterView,name='register'),
    path('list/',ListExpense.as_view(),name='list'),
    path('add/',CreateExpense.as_view(),name='add'),
    path('edit/<int:pk>/',UpdateExpense.as_view(),name='edit'),
    path('delete/<int:pk>/',DeleteExpense.as_view(),name='delete'),
    path('logout/',views.LogoutView,name='logout')
]
