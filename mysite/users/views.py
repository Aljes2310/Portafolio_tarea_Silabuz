from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import NewUserForm
from django.views.generic import CreateView
from .models import IPregistradas
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      return redirect('login')


def ips(request):
    lista=IPregistradas.objects.all()
    return render(request, "ips.html", {'lista' :lista} )

@login_required
def deletetime(request, id):
    ipes = IPregistradas.objects.get(id=id)
    ipes.delete()
    return redirect("ips")


