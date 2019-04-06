# Create your views here.
from ads.models import Ad

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.core.files.uploadedfile import InMemoryUploadedFile

from ads.util import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView

from ads.models import Ad, Comment
from ads.forms import CreateForm, CommentForm

class AdListView(AdListView):
    model = Ad
    template_name = "ad_list.html"

class AdDetailView(AdDetailView):
    model = Ad
    template_name = "ad_detail.html"
    def get(self, request, pk) :
        forum = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(forum=forum).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'forum' : forum, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)
#
# class AdCreateView(LoginRequiredMixin, View):
#     model = Ad
#     fields = ['title', 'text', 'price', 'picture']
#     template_name = "ad_form.html"
#
#     # template = 'ads/form.html'
#     success_url = reverse_lazy('ads')
#     def get(self, request, pk=None) :
#         form = CreateForm()
#         ctx = { 'form': form }
#         return render(request, self.template, ctx)
#
#     def post(self, request, pk=None) :
#         form = CreateForm(request.POST, request.FILES or None)
#
#         if not form.is_valid() :
#             ctx = {'form' : form}
#             return render(request, self.template, ctx)
#
#         # Add owner to the model before saving
#         ad = form.save(commit=False)
#         ad.ads = self.request.user
#         ad.save()
#         return redirect(self.success_url)

# class AdUpdateView(LoginRequiredMixin, View):
#     model = Ad
#     fields = ['title', 'text', 'price', 'picture']
#     template_name = "ad_form.html"
#
#     # template = 'ads/form.html'
#     success_url = reverse_lazy('ads')
#     def get(self, request, pk) :
#         ad = get_object_or_404(Ad, id=pk, ads=self.request.user)
#         form = CreateForm(instance=ad)
#         ctx = { 'form': form }
#         return render(request, self.template, ctx)
#
#     def post(self, request, pk=None) :
#         ad = get_object_or_404(Ad, id=pk, ads=self.request.user)
#         form = CreateForm(request.POST, request.FILES or None, instance=ad)
#
#         if not form.is_valid() :
#             ctx = {'form' : form}
#             return render(request, self.template, ctx)
#
#         ad.save()
#         return redirect(self.success_url)

class AdDeleteView(AdDeleteView):
    model = Ad
    template_name = "ad_delete.html"

def stream_file(request, pk) :
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response

# Another way to do it.
# This will handle create and update with an optional pk parameter on get and post
# We don't use the Generic or OwnerGeneric because (a) we need a form with a file
# and (b) we need to to populate the model with request.FILES
class AdFormView(LoginRequiredMixin, View):
    template = 'ad_form.html'
    success_url = reverse_lazy('ads')
    def get(self, request, pk=None) :
        if not pk :
            form = CreateForm()
        else:
            ad = get_object_or_404(Ad, id=pk, ads=self.request.user)
            form = CreateForm(instance=ad)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            ad = get_object_or_404(Ad, id=pk, ads=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model ads before saving
        ad = form.save(commit=False)
        ad.ads = self.request.user
        ad.save()
        return redirect(self.success_url)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], ads=request.user, forum=f)
        comment.save()
        return redirect(reverse_lazy('ad_detail', args=[pk]))

class CommentDeleteView(AdDeleteView):
    model = Comment
    template_name = "comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.forum
        return reverse_lazy('ad_detail', args=[ad.id])
