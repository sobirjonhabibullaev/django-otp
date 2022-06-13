from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, token
from django.utils.translation import gettext_lazy as _
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email','password1', 'password2',),
        }),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
   
    ordering = ['email']

@admin.register(token)
class tokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token',  'is_used']
    pass