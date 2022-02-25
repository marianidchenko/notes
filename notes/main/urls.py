from django.urls import path

from notes.main.views import show_index, create_note, edit_note, delete_note, show_details, show_profile, show_register, \
    delete_profile

urlpatterns = (
    path('', show_index, name='show index'),
    path('register/', show_register, name='show register'),
    path('profile/delete/', delete_profile, name='show delete profile'),
    path('add/', create_note, name='show create note'),
    path('edit/<int:pk>/', edit_note, name='show edit note'),
    path('delete/<int:pk>/', delete_note, name='show delete note'),
    path('details/<int:pk>/', show_details, name='show note details'),
    path('profile/', show_profile, name='show profile')
)