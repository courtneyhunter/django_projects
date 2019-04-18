# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from fruits.models import Fruit, Comment
from django.views import View
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from fruits.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from fruits.forms import CreateForm, CommentForm

class FruitListView(OwnerListView):
    model = Fruit
    template_name = "fruit_list.html"

class FruitDetailView(OwnerDetailView):
    model = Fruit
    template_name = "fruit_detail.html"
    def get(self, request, pk) :
        fruit = Fruit.objects.get(id=pk)
        comments = Comment.objects.filter(fruit=fruit).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'fruit' : fruit, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class FruitDeleteView(OwnerDeleteView):
    model = Fruit
    template_name = "fruit_delete.html"

# def stream_file(request, pk) :
#     fruit = get_object_or_404(Fruit, id=pk)
#     response = HttpResponse()
#     response['Content-Type'] = fruit.content_type
#     response['Content-Length'] = len(fruit.picture)
#     response.write(fruit.picture)
#     return response

# Another way to do it.
# This will handle create and update with an optional pk parameter on get and post
# We don't use the Generic or OwnerGeneric because (a) we need a form with a file
# and (b) we need to to populate the model with request.FILES
class FruitFormView(LoginRequiredMixin, View):
    template = 'fruit_form.html'
    success_url = reverse_lazy('fruits')
    def get(self, request, pk=None) :
        if not pk :
            form = CreateForm()
        else:
            fruit = get_object_or_404(Fruit, id=pk, owner=self.request.user)
            form = CreateForm(instance=fruit)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            fruit = get_object_or_404(Fruit, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=fruit)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model ads before saving
        fruit = form.save(commit=False)
        fruit.owner = self.request.user
        fruit.save()
        return redirect(self.success_url)


class CommentCreateView(LoginRequiredMixin, View):
    template = 'fruit_form.html'
    success_url = reverse_lazy('fruits')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        f = get_object_or_404(Fruit, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, fruit=f)
        comment.save()
        return redirect(reverse_lazy('fruit_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "fruit_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        fruit = self.object.fruit
        return reverse_lazy('fruit_detail', args=[fruit.id])
#
# class FruitListView(OwnerListView):
#     model = Fruit
#     template_name = "fruit_list.html"

    # def get(self, request) :
    #     fruit_list = Fruit.objects.all()
    #     favorites = list()
    #     if request.user.is_authenticated:
    #         # rows = [{'id': 2}]  (A list of rows)
    #         rows = request.user.favorite_fruits.values('id')
    #         favorites = [ row['id'] for row in rows ]
    #     ctx = {'fruit_list' : fruit_list, 'favorites': favorites}
    #     return render(request, self.template_name, ctx)

# # https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.db.utils import IntegrityError
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AddFavoriteView(LoginRequiredMixin, View):
#     def post(self, request, pk) :
#         print("Add PK",pk)
#         t = get_object_or_404(Fruit, id=pk)
#         fav = Fav(user=request.user, fruit=t)
#         try:
#             fav.save()  # In case of duplicate key
#         except IntegrityError as e:
#             pass
#         return HttpResponse()
#
# @method_decorator(csrf_exempt, name='dispatch')
# class DeleteFavoriteView(LoginRequiredMixin, View):
#     def post(self, request, pk) :
#         print("Delete PK",pk)
#         t = get_object_or_404(Fruit, id=pk)
#         try:
#             fav = Fav.objects.get(user=request.user, fruit=t).delete()
#         except Fav.DoesNotExist as e:
#             pass
#
#         return HttpResponse()
