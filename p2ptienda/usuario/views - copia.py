from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
# FormView vista basada en clase que permite directamente 
#trabajar con formularios
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from usuario.forms import FormularioLogin, RegistroForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class RegistroUsuario(CreateView):
    model = User
    template_name = "registrar.html"
    form_class = UserCreationForm #RegistroForm se coloca este cuando se quiera personalizar
    success_url = reverse_lazy('login')

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    #permite que no se guarde en cache info
    @method_decorator(never_cache)
    #verifica el metodo de la peticion realizada para saber 
    #si es metodo a usar es post o get y decidir que hacer una vez reciba la peticion
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            #si esta logeado te lleva al url success
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    #metodo de formView , valida el formulario
    def form_valid(self,form):
        #recibe la peticion, y una instancia del user
        #ese user viaja en el formulario que recibo como parametro form
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
