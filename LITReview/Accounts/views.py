from django import forms
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm as CreateUser
from django.views.generic import CreateView

from Review.models import Review

# Create your views here.
class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=15)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class Logins(View):
    form_class = LoginForm
    template_name = 'login.html'
    print('t')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
   

    def post(self, request):
        print('test')
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print('a')
            if user is not None:
                login(request, user)
                print('at')
                return redirect('feed') # rediriger vers la page d'accueil
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe invalide")
        print('y')
        return render(request, self.template_name, {'form': form})


class RegisterView(CreateView):
    form_class = CreateUser
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        print('succes')
        return redirect(self.success_url)
    
class Feed(View):

    template_name = 'feed.html'
    print('feed part')

    def get(self, request):
        reviews = Review.objects.all()
        context = {
            'reviews' : reviews
        }
        return render(request, self.template_name, context)


# Dde de critique -> reste a trouver pq elle ne s'affiche pas dans le feed malgré les modifs
# Erreur sur la méthode de recherche des users avec une method de finding au lieu d'une méthode de sélection *


#N'ait pas eu le temps de résoudre la primary key / mais j'ai fait les tests communiqués