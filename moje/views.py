import re
import os
import h5py

from .utils import jatz_plot_base64
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import OcenaEKGForm,WybierzEKGForm
from .models import ocenaEKG
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def wybierz_ekg(request):
    if request.method == 'POST' and 'wybierz' in request.POST:
        wybierz_form = WybierzEKGForm(request.POST)
        if wybierz_form.is_valid():
            numer = wybierz_form.cleaned_data['numer']
            return redirect('ocen_ekg_z_numerem', numer=numer)
    else:
        wybierz_form = WybierzEKGForm()

    return render(request, 'wybierz_ekg.html', {'form': wybierz_form})

@login_required
def ocen_zdjecie(request):
    numer = None
    ekg_image = None
    form = None
    oceny_dla_numeru = None
    if request.method == 'POST':
        if 'wybierz' in request.POST:
            wybierz_form = WybierzEKGForm(request.POST)
            if wybierz_form.is_valid():
                numer = wybierz_form.cleaned_data['numer']
                ekg_image = jatz_plot_base64(numer)
                form = OcenaEKGForm(initial={'numer_zdjecia': numer})
                oceny_dla_numeru = ocenaEKG.objects.filter(numer_zdjecia=numer)
        elif 'ocen' in request.POST:
            form = OcenaEKGForm(request.POST)
            wybierz_form = WybierzEKGForm(request.POST)
            if form.is_valid() and wybierz_form.is_valid():
                numer = wybierz_form.cleaned_data['numer']
                ocena = form.save(commit=False)
                ocena.numer_zdjecia=numer
                ocena.ocenil = request.user
                ocena.save()
                return redirect('ocen')
            # w razie błędu — wygeneruj EKG ponownie
            numer = form.cleaned_data.get('numer_zdjecia')
            ekg_image = jatz_plot_base64(numer)
        wybierz_form = WybierzEKGForm(initial={'numer': numer})
    else:
        wybierz_form = WybierzEKGForm()

    return render(request, 'ocena_form.html', {
        'form': form,
        'wybierz_form': wybierz_form,
        'ekg_base64': ekg_image,
        'numer': numer,
        'oceny_dla_numeru': oceny_dla_numeru
    })
