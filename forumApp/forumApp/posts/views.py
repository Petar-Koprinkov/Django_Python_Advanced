from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView

from forumApp.decorators import limit_work_time
from forumApp.posts.form_mixins import TimeDistrictMixin
from forumApp.posts.forms import AddBookForm, DeleteBookForm, EditBookForm, SearchForm, CommentFormSet
from forumApp.posts.models import Books


@method_decorator(limit_work_time, name='dispatch')
class IndexView(TimeDistrictMixin, TemplateView):
    template_name = 'forum/index.html'


class DashboardView(ListView, FormView):
    template_name = 'forum/dashboard.html'
    model = Books
    context_object_name = 'books'
    form_class = SearchForm
    success_url = reverse_lazy('dashboard')
    paginate_by = 2

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'title' in self.request.GET:
            query = self.request.GET.get('title')
            queryset = queryset.filter(title__icontains=query)

        return queryset


class AddBookView(CreateView):
    template_name = 'forum/add-book.html'
    form_class = AddBookForm
    success_url = reverse_lazy('index')
    model = Books
    context_object_name = 'book'


class EditBookView(UpdateView):
    template_name = 'forum/edit-page.html'
    form_class = EditBookForm
    success_url = reverse_lazy('dashboard')
    model = Books
    context_object_name = 'book'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Books, fields=('title', 'content', 'author', 'language'))
        else:
            return modelform_factory(Books, fields=('content',))


class DeleteBookView(DeleteView):
    context_object_name = 'book'
    model = Books
    success_url = reverse_lazy('index')
    template_name = 'forum/delete-page.html'
    form_class = DeleteBookForm

    def get_initial(self):
        book = self.get_object()
        return book.__dict__


class DetailPageView(DetailView):
    model = Books
    template_name = 'forum/details-page.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        formset = CommentFormSet()
        context = super().get_context_data(**kwargs)
        context['formset'] = formset
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.book = self.object
                    comment.save()

            return redirect('details-book', pk=self.object.pk)

        context = self.get_context_data(**kwargs)
        context['formset'] = formset

        return self.render_to_response(context)
