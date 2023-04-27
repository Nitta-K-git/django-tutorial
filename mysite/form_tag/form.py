from django import forms

class UserInputForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    choice_dict = (
        ("1", "hoge"),
        ("2","foo"),
    )
    choice = forms.ChoiceField(choices=choice_dict)

    # clean_<form名>でバリデーションチェックができる
    def clean_name(self):
        name = self.cleaned_data['name']
        if 'admin' in name:
            raise forms.ValidationError('adminを名前に含めることはできません')
        return name

    def form_func(self):
        print("do form function")

class UserConfirmForm(forms.Form):
    ...

