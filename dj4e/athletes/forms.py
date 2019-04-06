
from django.forms import ModelForm
from athletes.models import Sport

# Create the form class.
class SportForm(ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'
