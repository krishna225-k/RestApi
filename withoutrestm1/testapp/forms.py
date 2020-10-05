from django import forms
from testapp.models import Employee

class EmployeeForm(forms.ModelForm):
    '''
    Blow lines was Implementing the validataion on form
    '''
    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('The mininum salary should be 5000')
        return inputsal

    class Meta:
        model = Employee
        fields = '__all__'
 
