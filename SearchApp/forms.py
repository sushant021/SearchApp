from django import forms

class SearchForm(forms.Form):
	book_name = forms.CharField(label = 'Book Name',max_length= 100)
	author_name = forms.CharField(label='Author Name',max_length=100)