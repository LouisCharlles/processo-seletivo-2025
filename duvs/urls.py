from django.urls import path
from duvs import views

app_name = 'duvs'

urlpatterns = [
    path('', views.home, name='home'),
    path('duv/<int:duv_id>/', views.get_duv, name='duv_detail'),
    path('duv/create/', views.duvs_forms.duv_create, name='duv_create'),
    path('duv/<int:duv_id>/update/', views.duvs_forms.duv_update, name='duv_update'),
    path('duv/<int:duv_id>/delete/', views.duvs_forms.duv_delete, name='duv_delete'),
    path('duv/search/',views.search,name='search'),
    path('navio/create/', views.navio_forms.navio_create, name='navio_create'),
    path('navio/<int:navio_id>/', views.navio_detail, name='navio_detail'),
    path('navio/<int:navio_id>/update/', views.navio_forms.navio_update, name='navio_update'),
    path('navio/<int:navio_id>/delete/', views.navio_forms.navio_delete, name='navio_delete'),
    path('passageiro/create/', views.passageiro_forms.passageiro_create, name='passageiro_create'),
    path('passageiros/search/', views.passageiro_search, name='passageiro_search'),
    path('passageiro/<int:passageiro_id>/', views.passageiro_detail, name='passageiro_detail'),
    path('passageiro/<int:passageiro_id>/update/', views.passageiro_forms.passageiro_update, name='passageiro_update'),
    path('passageiro/<int:passageiro_id>/delete/', views.passageiro_forms.passageiro_delete, name='passageiro_delete'),
]
