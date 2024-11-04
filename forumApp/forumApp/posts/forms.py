from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.form_mixins import DisabledMixin
from forumApp.posts.models import Books, Comments


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ('approved', )

        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
        }

        error_messages = {
            'title': {
                'required': 'You must enter a title.',
                'max_length': 'Your length have to be maximum 30 characters.',
            },
        }


class AddBookForm(BookBaseForm):

    # clean_fields is a method which get every field of the form and clean it after is_valid() method is called.
    # To make validation in the current filed we have to call method clean_<fieldname> and write the logic there.
    def clean_author(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        if author[0] != author[0].upper():
            raise ValidationError('The name of the author must be capitalized.')

        return author

    # clean() method is to validate the business logic between the fields.
    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get('title')
    #     content = cleaned_data.get('content')
    #     if title and content and title in content:
    #         raise ValidationError('The title must not be in the content')
    #     return cleaned_data

    # save() method is used to modify the instance right before it is saved in the db.
    # With save(commit=False) we get the instance without save it in the db, and we can modify it how we want.
    def save(self, commit=True):
        book = super().save(commit=False)
        book.title = book.title.capitalize()

        if commit:
            book.save()

        return book


class EditBookForm(BookBaseForm):
    pass


class DeleteBookForm(BookBaseForm, DisabledMixin):
    disabled_fields = '__all__'


class SearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label='',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for book...',
        })
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'You must enter an author.',
                'max_length': 'Your length have to be maximum 30 characters.',
            },
            'content': {
                'required': 'You must enter a content.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your comment...',
        })


CommentFormSet = formset_factory(CommentForm, extra=1)














