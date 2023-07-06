from django.urls import path,include

urlpatterns=[
    path('app/apis/',include('userprofile.app_apis.urls'))
]