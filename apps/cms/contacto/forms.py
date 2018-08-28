from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)


class ContactoRecursosHumanosForm(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    departamento = forms.ChoiceField()
    archivo = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = [("", "Departamento")]

        for choice in kwargs['initial']['departamento']:
            choices += [(choice.correo, choice.nombre)]

        print(choices)
        self.fields["departamento"].choices = choices