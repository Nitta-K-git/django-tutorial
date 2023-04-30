from django import forms

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'my-class my-class2'
            field.widget.attrs['foo'] = '3'
        # 任意のfieldに属性を追加できる
        self.fields['name'].widget.attrs['name-attr'] = '1'
