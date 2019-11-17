from django.urls import path,include
from .views import *
app_name = "medical"
urlpatterns = [
   path('patientreg', patientreg , name  = "patientreg"),
   path('patientregister', patientregister , name  = "patientregister"),
   path('search', searchpatient , name  = "search"),
   path('searchresult' , searchresult,name ='searchresult'),
   path('doctors', doctors , name  = "doctors"),
   path('doctor_p/<int:pk>',doctor_p  , name = "doctor_p"),
   path('doctor/<int:pk>/<int:pid>', doctor , name  = "doctor"),
   path('search_p_result',search_p_result,name="search_p_result"),
   path('propic' , propic , name = 'propic'),
   path('patientrecord/<int:pk>/' , patientrecord , name = "patientrecord"),
   path('done/<int:pk>/<int:dk>' , patientrecordadd , name = "done")
]