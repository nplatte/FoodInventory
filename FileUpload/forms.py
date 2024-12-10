from django import forms

class FileForm(forms.Form):

    new_file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "class" : "form",
                "id" : "pdf_upload"
            }
        )
        )

    def clean_new_file(self):
        file = self.cleaned_data['new_file']
        if file.name[-3:] != 'pdf':
            raise forms.ValidationError("bad")
        return file