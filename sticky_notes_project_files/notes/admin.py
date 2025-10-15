"""sticky_notes_project_files/notes/admin.py
This file registers the models for the admin, making them accessible to
an admin and letting them manage (create/edit/delete) those models.
2025-09-11 EJS"""

from django.contrib import admin
from .models import Note
from .models import Author

# Register your models here.

# Note model
admin.site.register(Note)

# Author model
admin.site.register(Author)
