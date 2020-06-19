from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Movie, Person, Role


class MovieResource(resources.ModelResource):
    class Meta:
        model = Movie


class MovieAdmin(ImportExportModelAdmin):
    list_filter = ('year', )
    resource_class = MovieResource


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person


class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource


admin.site.register(Movie, MovieAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role)
