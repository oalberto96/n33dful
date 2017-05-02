from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.iniciar_sesion, name='n33dful_login'),
    url(r'^sesion', views.solicitud_login, name = 'solicitud_login'),
    url(r'^registrar', views.registrar, name = 'solicitud_signup'),
    url(r'^crear-cuenta',views.crear_cuenta, name = 'n33dful_signup'),
    url(r'^salir', views.salir, name='n33dful_logout'),
    url(r'^', views.home, name = 'home'),

]
