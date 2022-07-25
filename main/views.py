from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Tweet
from .forms import LoginForm

class IndexView(ListView):
    queryset = Tweet.objects.order_by('-id')
    template_name = 'index.html'
    context_object_name = 'tweets'

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'loginform': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data.get('username'), password=login_form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect(reverse_lazy('index'))
        return redirect(reverse_lazy('login'))

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('index'))

class CreateTweetView(CreateView):
    model = Tweet
    template_name = 'createtweet.html'
    fields = ['image', 'description']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html', {'tweets': Tweet.objects.filter(user=request.user).order_by('-id')})
