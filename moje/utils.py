# moje/utils.py

import h5py
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import io
import base64
import os
from django.conf import settings


def jatz_plot_base64(pacjent_numer):
    path = os.path.join(settings.MEDIA_ROOT, "ekg", "ecg_tracings.hdf5")

    with h5py.File(path, "r") as dane:
        x = np.array(dane['tracings'])
        patient_data = x[pacjent_numer]

    czas = np.arange(patient_data.shape[0]) / 400
    leads = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']

    fig, axes = plt.subplots(4, 3, figsize=(22, 10))
    axes = axes.flatten()

    for i in range(12):
        axes[i].plot(czas, patient_data[:, i], linewidth=0.4)
        axes[i].set_title(leads[i])
        axes[i].set_xlim(0, 10)
        axes[i].set_ylim(-3, 3)
        axes[i].axline((0, 0), (1, 0), color='r', alpha=0.45, linewidth=0.4)
        axes[i].xaxis.set_minor_locator(MultipleLocator(0.04))
        axes[i].xaxis.set_major_locator(MultipleLocator(0.2))
        axes[i].yaxis.set_minor_locator(MultipleLocator(0.1))
        axes[i].yaxis.set_major_locator(MultipleLocator(0.5))
        axes[i].grid(which='minor', alpha=0.35, linewidth=0.15)
        axes[i].grid(which='major', alpha=0.85, linewidth=0.3)
        axes[i].set_aspect(0.4)
        axes[i].tick_params(labelbottom=False, labelleft=False, which='both')

    plt.tight_layout()
    plt.suptitle(f'Pacjent #{pacjent_numer}')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')
