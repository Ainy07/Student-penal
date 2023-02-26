from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
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
    path('addstudent/', views.addstudent, name='addstudent'),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete"),
    path('update_student/',views.update_student),
    path('updatestu/<int:uid>/',views.updatestu),
    path('teacher/',views.teacher),
    path('addteacher/',views.addteacher),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete"),
    path('updatetech/<int:uid>/',views.updatetech),
    path('update_teacher/',views.update_teacher),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)