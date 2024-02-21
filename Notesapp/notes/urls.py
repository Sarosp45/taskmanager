from django.urls import path
from .views import note_list, note_detail, add_edit_note, delete_note

urlpatterns = [
    path('', note_list, name='note_list'),
    path('<int:note_id>/', note_detail, name='note_detail'),
    path('add/', add_edit_note, name='add_note'),
    path('<int:note_id>/edit/', add_edit_note, name='edit_note'),
    path('<int:note_id>/delete/', delete_note, name='delete_note'),
]
