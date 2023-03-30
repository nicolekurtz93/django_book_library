from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookInstance, BookInstanceAdmin)