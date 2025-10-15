"""sticky_notes_project_files/notes/tests.py
This is the unit test file. Part of the M06T05 lesson.
2025-09-22 EJS

EJS: to test the integration of the views and forms, I consulted this
website for guidance:
https://adamj.eu/tech/2020/06/15/how-to-unit-test-a-django-form/
Note that I did not test the form directly as it has no subroutines."""

from django.test import TestCase
from django.urls import reverse
from notes.models import Note, Author


class NoteModelTest(TestCase):
    '''Tests for the Note model class subroutines.'''
    def setUp(self):
        '''Set up a note object with an author for subsequent tests.'''
        author = Author.objects.create(name='Test Author')
        Note.objects.create(title='Test Note',
                            content='This is a test.',
                            author=author)

    def test_note_has_title(self):
        '''Test to ensure the title populates correctly.'''
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        '''Test to ensure that content populates correctly.'''
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test.')


class NoteViewTest(TestCase):
    '''Tests for the Note view class subroutines.'''
    def setUp(self):
        '''Set up a note object with an author for subsequent tests.'''
        author = Author.objects.create(name='Test Author')
        Note.objects.create(title='Test Note',
                            content='This is a test.',
                            author=author)

    def test_show_all_notes_view(self):
        '''Test for showing all notes.'''
        response = self.client.get(reverse('show_all_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_show_one_note_view(self):
        '''Test for showing the detail of a single note.'''
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('show_one_note',
                                           args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test.')

    def test_create_note_view_initial_access(self):
        '''Test to create a new note. See note at the top of this file.
        Note that this test only ensures the right webpage is accessed.
        '''
        response = self.client.get(reverse('create_note'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'create_note()')

    def test_update_note_view(self):
        '''Test to update a note.'''
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('update_note',
                                           args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)

    def test_delete_note_view(self):
        '''Test to ensure note deletion; after deletion, the redirect
        goes to the 'main page' with all notes displayed.'''
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('delete_note',
                                   args=[str(note.id)]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("show_all_notes"))
