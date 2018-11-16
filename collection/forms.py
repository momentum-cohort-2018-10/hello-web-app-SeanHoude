from django.forms import ModelForm
from collection.models import ClimbingShoe


class ClimbingShoeForm(ModelForm):
    class Meta:
        model = ClimbingShoe
        fields = ('name', 'description')