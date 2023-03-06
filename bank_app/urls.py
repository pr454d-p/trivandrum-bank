from . import views
from django.urls import path

app_name = 'bank_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='logout'),
    path('details',views.details_client,name='details'),
    path('ajax/load-branches/',views.load_branches, name='ajax_load_branches'), # AJAX
]