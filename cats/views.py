from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from cats.models import Cat, Breed
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class CatsListView(LoginRequiredMixin, ListView):
    model = Cat
    context_object_name = 'cats_list'
    template_name = 'cats/cats_list.html'

    def get_queryset(self):
        queryset = {'all_cats': Cat.objects.all(),
                    'breed_count': Breed.objects.all().count()}
        return queryset


class CatsCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')


class CatsUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')


class CatsDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')


class BreedsListView(LoginRequiredMixin, ListView):
    model = Breed
    context_object_name = 'breeds_list'
    template_name = 'cats/breeds_list.html'


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')
