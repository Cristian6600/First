# from django.urls import reverse_lazy, reverse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseRedirect
# from django.views.generic import View

# from .models import User

# def check_ocupation_user(nombres, user_nombres):
#     #
    
#     if (nombres == User.ADMINISTRADOR or nombres == user_nombres):
        
#         return True
#     else:
#         return False

# class InventarioPermisoMixin(LoginRequiredMixin):
#     login_url = reverse_lazy('users_app:user-login')

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         #
#         if not check_nombres_user(request.user.nombres, User.ALMACEN):
#             # no tiene autorizacion
#             return HttpResponseRedirect(
#                 reverse(
#                     'users_app:user-login'
#                 )
#             )

#         return super().dispatch(request, *args, **kwargs)