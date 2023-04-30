from django import forms


class UserCreateForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    choice_dict = (
        ("1", "hoge"),
        ("2", "foo"),
    )
    choice = forms.ChoiceField(choices=choice_dict)
    user_id = forms.CharField(initial="1234")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'my-class my-class2'
            field.widget.attrs['foo'] = '3'
        self.fields['name'].widget.attrs['name-attr'] = '1'
