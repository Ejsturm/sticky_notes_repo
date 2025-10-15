"""sticky_notes_project_files/notes/forms.py
This file will take user input for creating and updating sticky note
instances. 2025-09-10 EJS"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form that instantiates new sticky note objects or updates pre-
    existing sticky notes objects by taking user input.

    Fields:
    title (CharField): sticky note title w/max length of 255 characters.
    content (TextField): sticky note contents
    """

    class Meta:
        model = Note
        fields = ["title", "content", "author"]
