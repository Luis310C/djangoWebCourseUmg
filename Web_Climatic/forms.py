from django import forms
from .models import articulo_Cientifico,Usuario


class formulario1(forms.ModelForm):
   
    class Meta:
        model=articulo_Cientifico

        fields=('titulo','url','autor','descripcion','contenido','estado','image')
        widgets={
            'titulo':forms.TextInput(attrs={"class":"form-control"}),
            'url':forms.TextInput(attrs={"class":"form-control"}),
            'autor':forms.Select(attrs={"class":"form-control"}),
            'contenido':forms.Textarea(attrs={"class":"form-control","cols":"45"}),
            'estado':forms.Select(attrs={"class":"form-control"}),
            'image':forms.FileInput(attrs={"class":"form-control"}),
            'descripcion':forms.TextInput(attrs={"class":"form-control","cols":"45"})
        }
class formulario2(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=('Id_Usuario','Nombre','Email','rol','contasena','Estilo')
        widgets={
            'Id_Usuario':forms.TextInput(attrs={"class":"form-control","type":"number"}),
            'Nombre':forms.TextInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
            'rol':forms.Select(attrs={"class":"form-control"}),
            'contasena':forms.PasswordInput(attrs={"class":"form-control","cols":"45"}),
            'Estilo':forms.Select(attrs={"class":"form-control"}),
            
        }
