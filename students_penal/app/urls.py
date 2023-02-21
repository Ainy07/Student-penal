from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('courses/',views.courses),
    path('addcourse/',views.addcourse),
    path('update_view/<int:uid>/',views.update_view, name='Updatecourse'),
    path('updatecourse/',views.updatecourse),
    path('deletecourse/',views.delete),
    path('dashboard/',views.dashboard),
    path('employees/',views.employees),
    path('notifications/',views.notifications),
    path('pg_dashboard/',views.pg_dashboard),
    path('profile/',views.profile),
    path('signup/',views.signup),
    path('formdata/',views.formdata),
    path('tables/',views.tables),
    path('tenants/',views.tenants),
    path('viewstudents/',views.viewstudents),
]