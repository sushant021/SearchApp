from django.contrib import admin
from .models import Book,Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['title','slug','author','published']
	list_editable = ['slug','author','published']
	list_filter = ['published','author']
	prepopulated_fields = {'slug':('title',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display =['name']


