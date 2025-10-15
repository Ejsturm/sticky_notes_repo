"""sticky_notes_project_files/notes/views.py
These are the views that define the URL pattern behaviors. Here, there
will be views for creating, reading, updating, and deleting (CRUD) the
various (sticky) notes. 2025-09-09 EJS """

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def show_all_notes(request):
    """View that displays all sticky notes titles and authors. Satisifes
    the R part of CRUD functionality.

    Param:
    request (HTTP request object)

    Returns: rendered template with all sticky notes listed.
    """
    all_notes = Note.objects.all()
    context_dict = {"all_notes": all_notes,
                    "page_title": "All Sticky Notes"}

    return render(request, "notes/show_all_notes.html", context_dict)


def show_one_note(request, pk):
    """View that displays a single specified stikcy note and its
    contents. Also satisifies the R part of CRUD functionality.

    Params:
    request (HTTP request object)
    pk: primary key of the target sticky note

    Returns: renedered template with all details for one sticky note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/show_one_note.html", {"note": note})


def create_note(request):
    """View that enables the user to create a new sticky note. Satisfies
    the C part of CRUD functionality.

    Param:
    request (HTTP request object)

    Returns: rendered template for creating a new sticky note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("show_all_notes")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def update_note(request, pk):
    """View that updates an exisiting sticky note. Satisifies the U part
    of CRUD functionality.

    Params:
    request (HTTP request object)
    pk: primary key of the target sticky note

    Return: rendered template for updating specified sticky note.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("show_all_notes")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def delete_note(request, pk):
    """View that deletes an exisiting sticky note. Satisfies the D part
    of CRUD functionality.

    Params:
    request (HTTP request object)
    pk: primary key of the target sticky note

    Return: Redirect to post list.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("show_all_notes")
