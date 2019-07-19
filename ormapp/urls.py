from django.urls import path,include
from ormapp import views

urlpatterns = [
    path('',views.EmployeeView.as_view(),name='home'),
    path('company/',views.CompanyView.as_view(),name='company')

]