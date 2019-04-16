# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from dogs.models import Dog, Type
from dogs.forms import TypeForm

# Create your views here.

class DogList(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Type.objects.all().count();
        al = Dog.objects.all();

        ctx = { 'type_count': mc, 'dog_list': al };
        return render(request, 'dogs/dog_list.html', ctx)

class TypeView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Type.objects.all();
        ctx = { 'type_list': ml };
        return render(request, 'dogs/type_list.html', ctx)

class TypeCreate(LoginRequiredMixin, View):
    template = 'dogs/type_form.html'
    success_url = reverse_lazy('dogs')
    def get(self, request) :
        form = TypeForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = TypeForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        type = form.save()
        return redirect(self.success_url)

class TypeUpdate(LoginRequiredMixin, View):
    model = Type
    success_url = reverse_lazy('dogs')
    template = 'dogs/type_form.html'
    def get(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        form = TypeForm(instance=type)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        form = TypeForm(request.POST, instance = type)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    success_url = reverse_lazy('dogs')
    template = 'dogs/type_confirm_delete.html'

    def get(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        form = TypeForm(instance=type)
        ctx = { 'type': type }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        type = get_object_or_404(self.model, pk=pk)
        type.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class DogCreate(LoginRequiredMixin,CreateView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs')

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs')

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs')
