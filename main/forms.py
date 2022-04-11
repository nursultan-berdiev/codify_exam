from django import forms


class WorkerForm(forms.ModelForm):
    class Meta:
        widgets = {
            'experience': forms.widgets.DateInput(attrs={'type': 'date'}),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
