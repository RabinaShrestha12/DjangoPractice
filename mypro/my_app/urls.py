from django.urls import path
from .views.auth_view import loginpage
from .views.main_view import index, createdemployee,edit,update


urlpatterns = [
    path('', index, name='index'),
    path('login/', loginpage, name='loginpage'),
    path('create/', createdemployee, name="create"),
    path('edit/<int:id>', edit, name='edit'),
    path('update/', update, name='update')
]