from django import forms
from testapp.models import Student

class StduentForm(forms.ModelForm):
    '''
    Blow lines was Implementing the validataion on form
    '''
    def clean_marks(self):
        inputmarks = self.cleaned_data['marks']
        if inputmarks < 35:
            raise forms.ValidationError('The mininum salary should be 35')
        return inputmarks

    class Meta:
        model = Student
        fields = '__all__'
