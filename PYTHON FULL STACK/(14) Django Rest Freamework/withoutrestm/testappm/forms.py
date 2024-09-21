from django import forms
from testappm.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal=self.cleaned_data['esal']
        if inputsal<4000:
            raise forms.ValidationError('the minimum salary should be 5000')
        return inputsal
    
    class Meta:
        model = Employee
        fields='__all__'