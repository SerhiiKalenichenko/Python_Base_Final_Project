from rich.table import Table

from src.data_models.notes_manager import NotesManager, Tag, Note
from src.data_models.record_fields import ListField
from src.error_handling.error_handler import input_error

@input_error
def add_note(args, notes: NotesManager):
    title = " ".join(args)
    if len(title) == 0:
        raise ValueError("Title is required.")
    note_id = notes.new(title)
    return f"Created note: {note_id}"

@input_error
def edit_note(args, notes: NotesManager):
    note_id, *_ = args
    return notes.edit_in_editor(int(note_id))

@input_error
def delete_note(args, notes: NotesManager):
    note_id, *_ = args
    return notes.delete(int(note_id))

@input_error
def list_notes(notes: NotesManager):
    return as_table(notes.notes)

@input_error
def add_tag(args, notes: NotesManager):
    note_id, tag, *_ = args
    note = notes.get(int(note_id))
    if not note:
        raise KeyError("Note not found in the notebook.")
    note.add_tag(Tag(tag))
    return note

@input_error
def remove_tag(args, notes: NotesManager):
    note_id, tag, *_ = args
    note = notes.get(int(note_id))
    if not note:
        raise KeyError("Note not found in the book.")
    note.remove_tag(Tag(tag))
    return note

@input_error
def search_notes(args, notes: NotesManager):
    tag, *_ = args
    found_notes = dict(notes.search(tag))
    if len(found_notes) == 0:
        raise KeyError("Matching notes not found in the book.")
    return as_table(found_notes)

def as_table(notes: dict[int, Note] | None) -> Table:

    table = Table(title="Note Book", show_lines=True, show_header=True)
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Tags")
    table.add_column("Created")
    table.add_column("Updated")

    for id, note in notes.items():
        table.add_row(
            str(id),
            note,
            ListField(note.tags),
            note.created_at,
            note.updated_at,
        )

    return table
