from django.urls import path

from .views import Owners_List,Owners_Detail,PetList,PetDetail

urlpatterns = [
    path("owners/",Owners_List.as_view()),
    path("owners/<int:pk>",Owners_Detail.as_view()),
    path("pets/",PetList.as_view()),
    path("pets/<int:id>",PetDetail.as_view()),
    #path("test/",Test.as_view()),
    #path("pets/<int:pk>",PetDetail.as_view()),
    ]