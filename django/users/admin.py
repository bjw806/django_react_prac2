from django.contrib import admin
from users.models import NewUser, TransferReport
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('id','email', 'user_name', 'account_address',)
    list_filter = ('id','email', 'user_name', 'is_active', 'is_staff', 'account_address', 'account_money')
    ordering = ('-start_date',)
    list_display = ('id','email', 'user_name','is_active', 'is_staff', 'account_address', 'account_money')
    fieldsets = (
        (None, {'fields': ('email', 'user_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about', 'account_address', 'account_money')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff', 'account_address', 'account_money',)}
         ),
    )

@admin.register(TransferReport)
class AccountTransferReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'send_account', 'receive_account', 'amount', 'datetime')

admin.site.register(NewUser, UserAdminConfig)


