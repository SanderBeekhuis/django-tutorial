from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    site_header = 'Polls admin'
    site_title = 'Polls admin'
