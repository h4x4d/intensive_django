from django.contrib.auth import login
from django.views.generic import FormView, ListView, DetailView
from users.forms import ProfileForm, SignUpForm
from users.models import Account
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpFormView(FormView):
    template_name = 'users/signup.html'
    success_url = reverse_lazy('homepage:home')
    form_class = SignUpForm

    def form_valid(self, form):
        user = Account.objects.create_user(**form.cleaned_data)
        login(self.request, user)
        return super().form_valid(form)


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Account.objects.all().filter(
            is_active=True
            ).values('id', 'email', 'first_name')
        return context


class UserDetailView(DetailView):
    model = Account
    template_name = 'users/user_detail.html'


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    form_class = ProfileForm

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.birthday = form.cleaned_data['birthday']
        user.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.request.user})
        return kwargs
