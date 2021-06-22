from django.contrib import admin

from . models import User, Areas
# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'nombres',
        'Departamento',
    )

    search_fields = (
        'username',
        'nombres',
        'Departamento',
    )

    list_filter = (
        'Departamento',
    )


admin.site.register (User, UserAdmin)
admin.site.register (Areas)