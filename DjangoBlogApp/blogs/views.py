from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from blogs.models import AutherRegistration, BlogModel
from blogs.forms import AutherRegistrationForm, LoginForm, BlogDataForm

from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)





# Create your views here.

class BlogsTemplete(TemplateView):
    template_name = 'blogs/base.html'


class BlogView(TemplateView):
    template_name = 'blogs/blogpage.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        # here's the difference:
        context['blogs'] = BlogModel.objects.all()
        return context


class AutherCreateView(CreateView):
    form_class = AutherRegistrationForm
    template_name = "blogs/createauther.html"
    success_url = "/blogs/blogpage/"


@method_decorator(login_required, name="dispatch")
class BlogUploadView(CreateView):
    template_name = 'blogs/blogupload.html'
    form_class = BlogDataForm
    success_url = "/blogs/blogpage/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.auther_id = self.request.user.id
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class BlogDeleteView(DeleteView):
    success_url = '/blogs/blogpage/'

    def get_queryset(self):
        return BlogModel.objects.filter(
            auther_id=self.request.user.id
        )

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AutherUpdateView(UpdateView):
    template_name = 'blogs/autherupdate.html'
    fields = ['profileimage','first_name', 'middle_name', 'last_name', 'gender']
    success_url = "/blogs/blogdetails"

    def get_object(self): #and you have to override a get_object method
        return get_object_or_404(AutherRegistration, id=self.request.user.id)

@method_decorator(login_required, name="dispatch")
class BlogDetailsView(TemplateView):
    template_name = "blogs/usersallblogs.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailsView, self).get_context_data(**kwargs)
        # here's the difference:
        context['allblogs'] = BlogModel.objects.filter(auther_id=self.request.user.id)
        return context

class UpdateBlogView(UpdateView):
    template_name = 'blogs/blogupdate.html'
    model = BlogModel
    fields = ['tittle', 'description']
    success_url = reverse_lazy("/blogs/blogdetails")

    def get_object(self):
        id = self.request.user.id
        return get_object_or_404(BlogModel, auther_id=id)