import re
import os

from django.conf import settings
from django.shortcuts import render, redirect
from .forms import OcenaEKGForm
from .models import ocenaEKG


def ocen_zdjecie(request):
    folder = os.path.join(settings.MEDIA_ROOT, 'ekg')
    lista_plikow = os.listdir(folder)

    #wyciągamy numery zdjęć z nazw zdjęć
    wzorzec = re.compile(r"ekg_(\d+)\-min.png")
    wszystkie_numery  = sorted([
        int(wzorzec.match(nazwa).group(1))
        for nazwa in lista_plikow if wzorzec.match(nazwa)
    ])

    #numery ocenione
    ocenione = set(ocenaEKG.objects.values_list('numer_zdjecia', flat=True))

    #szukanie 1 zdjęcia do oceny

    dostepne = [n for n in wszystkie_numery if n not in ocenione]

    if not dostepne:
        return render(request,'brak_zdjec.html')

    numer = dostepne[0]
    nazwa_pliku = f"ekg_{numer}-min.png"

    if request.method == 'POST':
        print(request.POST)
        form = OcenaEKGForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ocen')
    else:
        form = OcenaEKGForm(initial={'numer_zdjecia': numer})

    return render(request, 'ocena_form.html', {
        "form": form,
        'zdjecie': f'ekg/{nazwa_pliku}',

    })
