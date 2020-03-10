from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from usuario.forms import FormularioLogin,RegistroForm
from django.contrib.auth.models import User
from django.views.generic import CreateView

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm #RegistroForm se coloca este cuando se quiera personalizar
    success_url = reverse_lazy('login')

class Login(FormView):

    template_name = 'usuario/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('p2pApp:consultar_producto')

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
