from django.contrib import admin

from . models import User, Areas
# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'nombres',
        'Departamento',
    )


admin.site.register (User, UserAdmin)
admin.site.register (Areas)