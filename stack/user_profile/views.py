from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView, View
from user_profile import forms


class Login(FormView):
    form_class = forms.UserLoginForm
    success_url = '/home/'
    template_name = 'login.html'


class LogOut(View):
    success_url = '/regist/'
    template_name = 'base.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')


class Registration(FormView):
    form_class = forms.UserRegistrForm
    success_url = '/home/'
    template_name = 'registration.html'

    def form_valid(self, form):
        self.object = form.save()
        return super(Registration, self).form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})