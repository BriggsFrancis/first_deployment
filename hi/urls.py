from django.urls import path,include
from hi.views import hi,name


urlpatterns = [
    path('hi/', hi,name="hi"),
    path('',name,name='name'),
]