from django.urls import path

from .views import NewsList, NewDetail, NewCreate, NewEdit, NewDelete, NewSearch

urlpatterns = [

    path('', NewsList.as_view(), name="new_list"),
    path('<int:pk>', NewDetail.as_view(), name="new_detail"),
    path('create/', NewCreate.as_view(), name="new_create"),
    path('search/', NewSearch.as_view(), name="new_search"),
    path('<int:pk>/edit/', NewEdit.as_view(), name="new_edit"),
    path('<int:pk>/delete/', NewDelete.as_view(), name="new_delete"),

    path('', NewsList.as_view(), name="new_list"),
    path('<int:pk>', NewDetail.as_view(), name="new_detail"),
    path('create/', NewCreate.as_view(), name="new_create"),
    path('search/', NewSearch.as_view(), name="new_search"),
    path('<int:pk>/edit/', NewEdit.as_view(), name="new_edit"),
    path('<int:pk>/delete/', NewDelete.as_view(), name="new_delete"),

]
