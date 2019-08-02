from django.urls import path
from crawler.views import index
urlpatterns = [
    path('more/<link>',index, name ='find_businesses')
]