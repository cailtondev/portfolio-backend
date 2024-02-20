from django.contrib import admin
from .models import (
    Home,
    WebDevelopmentOffer,
    WebDevelopmentCard,
    WebDevelopmentTechnologies,
    WebDevelopmentProjects,
    ResumeME,
    Contact
)


class WebDevelopmentProjectsAdmin(admin.ModelAdmin):
    list_display = ('tag', 'image_link', 'link_preview')


admin.site.register(Home)
admin.site.register(WebDevelopmentOffer)
admin.site.register(WebDevelopmentCard)
admin.site.register(WebDevelopmentTechnologies)
admin.site.register(WebDevelopmentProjects, WebDevelopmentProjectsAdmin)
admin.site.register(ResumeME)
admin.site.register(Contact)
