from django import forms

# Create your forms here.

class ContactForm(forms.Form):
	name = forms.CharField()
	subject = forms.CharField(max_length=255)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea, required=True)