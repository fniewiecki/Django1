from django import forms
from .models import ocenaEKG

class OcenaEKGForm(forms.ModelForm):
    class Meta:
        model = ocenaEKG
        fields = ['BlokAV_1stopnia', 'BlokAV_2stopnia1','BlokAV_2stopnia2', 'BlokAV_3stopnia', 'RBBB', 'LBBB', 'Bradykardia', 'Tachykardia', 'Migotanie', 'ZalamekQ','CzyTrudne']
        labels = {
            'BlokAV_1stopnia': 'Blok AV 1 stopnia',
            'BlokAV_2stopnia1': 'Blok AV 2 stopnia Mobitz I ',
            'BlokAV_2stopnia2': 'Blok AV 2 stopnia Mobitz II ',
            'BlokAV_3stopnia': 'Blok AV 3stopnia',
            'RBBB': 'RBBB',
            'LBBB': 'LBBB',
            'Bradykardia': 'Bradykardia zatokowa',
            'Tachykardia': 'Tachykardia zatokowa',
            'Migotanie': 'Migotanie przedsionków',
            'ZalamekQ': 'Patologiczny Zalamek Q',
            'CzyTrudne': 'Czy było trudne w ocenie ?'

        }
        exclude = ['numer_zdjecia','ocenil']
class WybierzEKGForm(forms.Form):
    numer = forms.IntegerField(min_value=0, label="Numer EKG do oceny")
