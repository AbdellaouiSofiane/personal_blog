from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	to = forms.EmailField()
	comments = forms.CharField(required=False,
							   widget=forms.Textarea)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
	query = forms.CharField(widget=forms.TextInput(attrs={
		'id': 'query',
		'class' : 'form-control me-2',
		'placeholder': 'Search',
		'type': 'search',
		'aria-label': "Search"
	}))