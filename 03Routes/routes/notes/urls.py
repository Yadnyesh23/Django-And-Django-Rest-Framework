from django.urls import path
from .views import notes, get_note_by_id

urlpatterns = [
   path('notes/',notes , name="notes" ),
   path('notes/<int:note_id>/',get_note_by_id, name='get_note_by_id' ),
]