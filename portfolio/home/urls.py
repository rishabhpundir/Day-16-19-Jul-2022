from django.contrib import admin
from django.urls import path, include
from home import views


#django admin header customisation

admin.site.site_header = "Admin Page"
admin.site.site_title = "Welcome to the Jungle"
admin.site.index_title = "Welcome to Dwight Shrute Blog Admin portal"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
]
