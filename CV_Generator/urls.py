from django.contrib import admin
from django.urls import path
from pdf.views import accept, resume, list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accept, name='accept'),
    path('<int:id>/', resume, name='resume'),
    path('list/', list, name='list'),
]
