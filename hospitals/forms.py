from django import forms

from .models import Hospital, Centre

class BasicDetailModelForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name', 'rc_number', 'phone', 'email',  'city', 'state', 'address']

class CertUploadModelForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['cac_certificate', 'practice_license']



class CentreForm(forms.ModelForm):
    class Meta:
        model = Centre
        fields = ['centre_name', 'rc_number', 'phone', 'email', 'state', 'city', 'address', 'reg_date', 'cac_certificate', 'practice_license']
