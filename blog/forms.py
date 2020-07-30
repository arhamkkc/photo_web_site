from django import forms
from blog.models import Photo,Contact

class PhotoForm(forms.ModelForm):
    class Meta():
        model = Photo
        fields = '__all__'



class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'

        widgets = {
            'Full_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Contact_No':forms.TextInput(attrs={'class':'form-control'}),
            'purpose':forms.Select(attrs={'class':'form-control'}),
            'requirements':forms.Textarea(attrs={'class':'form-control'}),
        }