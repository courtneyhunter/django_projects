from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from athletes.models import Athlete, Sport
from athletes.forms import SportForm

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Sport.objects.all().count();
        al = Athlete.objects.all();

        ctx = { 'sport_count': mc, 'athlete_list': al };
        return render(request, 'athletes/athlete_list.html', ctx)

class SportView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Sport.objects.all();
        ctx = { 'sport_list': ml };
        return render(request, 'athletes/sport_list.html', ctx)

class SportCreate(LoginRequiredMixin, View):
    template = 'athletes/sport_form.html'
    success_url = reverse_lazy('athletes')
    def get(self, request) :
        form = SportForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = SportForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        sport = form.save()
        return redirect(self.success_url)

class SportUpdate(LoginRequiredMixin, View):
    model = Sport
    success_url = reverse_lazy('athletes')
    template = 'athletes/sport_form.html'
    def get(self, request, pk) :
        sport = get_object_or_404(self.model, pk=pk)
        form = SportForm(instance=sport)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        sport = get_object_or_404(self.model, pk=pk)
        form = SportForm(request.POST, instance = sport)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class SportDelete(LoginRequiredMixin, DeleteView):
    model = Sport
    success_url = reverse_lazy('athletes')
    template = 'athletes/sport_confirm_delete.html'

    def get(self, request, pk) :
        sport = get_object_or_404(self.model, pk=pk)
        form = SportForm(instance=sport)
        ctx = { 'sport': sport }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        sport = get_object_or_404(self.model, pk=pk)
        sport.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class AthleteCreate(LoginRequiredMixin,CreateView):
    model = Athlete
    fields = '__all__'
    success_url = reverse_lazy('athletes')

class AthleteUpdate(LoginRequiredMixin, UpdateView):
    model = Athlete
    fields = '__all__'
    success_url = reverse_lazy('athletes')

class AthleteDelete(LoginRequiredMixin, DeleteView):
    model = Athlete
    fields = '__all__'
    success_url = reverse_lazy('athletes')
