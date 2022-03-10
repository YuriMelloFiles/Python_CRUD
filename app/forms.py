from django.forms import ModelForm
from app.models import Projetos

# Create the form class.
class ProjetosForm(ModelForm):
     class Meta:
         model = Projetos
         fields = ['projeto', 'concessionaria', 'situacao', 'responsavel']