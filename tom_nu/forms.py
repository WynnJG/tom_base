from django import forms

class SearchForm(forms.Form):
	username = forms.CharField(label='TOM Username', max_length=100)
	collection_display_name = forms.CharField(label='The display name of your subject...')