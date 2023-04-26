from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    choice_dict = (
        ("1", "hoge"),
        ("2","foo"),
    )
    choice = forms.ChoiceField(choices=choice_dict)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass