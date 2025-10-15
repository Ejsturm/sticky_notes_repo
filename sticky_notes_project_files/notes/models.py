"""sticky_notes_project_files/notes/models.py
The models to represent sticky notes. 2025-09-09 EJS"""

from django.db import models


class Note(models.Model):
    """Represents a (sticky) note post.

    Fields:
    title (CharField): sticky note title w/max length of 255 characters.
    content (TextField): sticky note contents.
    created_at (DateTimeField): set to current date & time upon
        instantiation.

    Relationships:
    author (ForiegnKey): represents note creator.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True,
                               blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    """Represents an author of a sticky note.

    Field:
    name (CharField): the author's name.
    """

    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name
