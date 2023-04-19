from django.forms import ModelForm
from hi.models import Name

class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = '__all__'