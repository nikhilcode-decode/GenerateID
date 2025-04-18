
from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):
    training_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2030)))
    expiry_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2030)))

    class Meta:
        model = Driver
        fields = ['name', 'aadhar_card', 'driver_license_no', 'transporter_name', 'training_date', 'expiry_date']

    def clean(self):
        cleaned_data = super().clean()
        training_date = cleaned_data.get('training_date')
        expiry_date = cleaned_data.get('expiry_date')

        if training_date and expiry_date:
            if expiry_date < training_date:
                raise forms.ValidationError('Expiry date must be after the training date.')

        return cleaned_data

    def clean_aadhar_card(self):
        aadhar_card = self.cleaned_data.get('aadhar_card')
        if len(aadhar_card) != 12:
            raise forms.ValidationError("Aadhar card number must be 12 digits long.")
        return aadhar_card

