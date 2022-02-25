

from notes.main.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def get_notes():
    notes = Note.objects.all()
    if notes:
        return notes
    return None


def get_note_by_pk(pk):
    note = Note.objects.get(pk=pk)
    return note
