from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistroForm

class RegisterUserView(View):

    def get(self, request):
        template_name="accounts/registration.html"
        form = RegistroForm()
        context = {'form':form}

        return render(request, template_name, context)

    def post(self, request):

        form = RegistroForm(request.POST)

        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.set_password(form.cleaned_data['password'])
            form_data.save()

        return redirect('login')

