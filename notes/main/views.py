from django.shortcuts import render, redirect

# Create your views here.
from notes.main.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes.main.helpers import get_profile, get_notes, get_note_by_pk
from notes.main.models import Note


def show_index(request):
    profile = get_profile()
    notes = get_notes()
    context = {
        'profile': profile,
        'notes': notes,

    }
    if not profile:
        return redirect('show register')

    return render(request, 'home-with-profile.html', context)


def show_register(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True
    }
    return render(request, 'home-no-profile.html', context)


def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = get_note_by_pk(pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = get_note_by_pk(pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'form': form
    }
    return render(request, 'note-delete.html', context)


def show_details(request, pk):
    note = get_note_by_pk(pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def show_profile(request):
    try:
        note_count = len(get_notes())
    except:
        note_count = 0
    profile = get_profile()
    context = {
        'profile': profile,
        'note_count': note_count
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    instance = get_profile()
    instance.delete()
    get_notes().delete()
    return redirect('show index')
