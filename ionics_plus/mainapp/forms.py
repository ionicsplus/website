from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import contact_us,user_service


class RegisterForm(UserCreationForm):

    class meta:
        model = User
        fields = ['username','password1','password2']



class ContactUs(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ['Full_name','email','whatsapp_number','country', 'subject']

        widgets = {
            'Full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'subject': forms.Textarea(attrs={'placeholder': 'Write a brief description about your request.'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'Example:-> 00965 - 94964095'})
        }
    def clean_email(self,*args,**kwargs):
    	email = self.cleaned_data.get('email')
    	if "@" in email and ".com" in email:
    		return email
    	else:
    		raise forms.ValidationError("Error in Email Format")



class AddingRequest(forms.ModelForm):
    class Meta:
        model = user_service
        fields = ['title','services','subject','email', 'whatsapp_number','country','delivery_date','file1','file2','file3']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add title to your request.'}),
            'subject': forms.Textarea(attrs={'placeholder': 'Write a brief description about your request.'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'Example:-> 00965 - 94964095'}),
            'delivery_date': forms.TextInput(attrs={'placeholder': 'Place the delivery date Year-Month-Day'})
        }

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        if "@" in email and ".com" in email:
            return email
        else:
            raise forms.ValidationError("Error in Email Format")



class editform(forms.ModelForm):
    class Meta:
        model = user_service
        fields = ['title','services','solving','rejected','accepted','in_progress','finished','Price','solution_file_1','solution_file_2','solution_file_3','payment_file','payment_link_Knet','payment_link_visa']



class paymentform(forms.ModelForm):
    class Meta:
        model = user_service
        fields = ['payment_file']


