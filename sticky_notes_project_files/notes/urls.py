"""sticky_notes_project_files/notes/urls.py
Here we define the URL patterns that the views refer to. This is the
mapping which connects the view to the actual desired page by creating
the path to get there. 2025-09-10 EJS """

from django.urls import path
from .views import (
    show_all_notes,
    show_one_note,
    create_note,
    update_note,
    delete_note,
)

urlpatterns = [
    # Displays all notes
    path("", show_all_notes, name="show_all_notes"),

    # Displays one note
    path("note/<int:pk>/", show_one_note, name="show_one_note"),

    # Create new note
    path("note/create_note/", create_note, name="create_note"),

    # Update existing note
    path("note/<int:pk>/edit/", update_note, name="update_note"),

    # Delete exisiting note
    path("note/<int:pk>/delete_note/", delete_note, name="delete_note"),
]
