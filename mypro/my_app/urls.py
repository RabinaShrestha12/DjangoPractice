from django.urls import path
from .views.auth_view import loginpage, register
from .views.main_view import indexs, createdemployee,edit,delete_data, ind,index


urlpatterns = [
    path('indexs/', indexs, name='indexs'),
    path('login/', loginpage, name='login'),
    path('create/', createdemployee, name="create"),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:emp_id>', delete_data, name='delete'),
    path('register/', register, name='register'),
    path('', ind, name='ind'),
    path('index/', index, name='index')
]