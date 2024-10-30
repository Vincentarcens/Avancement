# Sauvegarde ce script sous le nom app.py pour le déployer sur Streamlit
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Demande des noms des réactifs et des produits
st.title("Simulation de réaction chimique")
nom_A = st.text_input("Nom du réactif A", "A")
nom_B = st.text_input("Nom du réactif B", "B")
nom_C = st.text_input("Nom du produit C", "C")
nom_D = st.text_input("Nom du produit D", "D")

# Demande des coefficients stoechiométriques des réactifs et des produits
coeff_A = st.number_input(f"Coefficient stœchiométrique de {nom_A}", value=1.0)
coeff_B = st.number_input(f"Coefficient stœchiométrique de {nom_B}", value=1.0)
coeff_C = st.number_input(f"Coefficient stœchiométrique de {nom_C}", value=1.0)
coeff_D = st.number_input(f"Coefficient stœchiométrique de {nom_D}", value=1.0)

# Quantité initiale des réactifs
quantite_initiale_A = st.number_input(f"Quantité initiale de {nom_A}", value=10.0)
quantite_initiale_B = st.number_input(f"Quantité initiale de {nom_B}", value=10.0)

# Calcul de l'avancement où l'un des réactifs est consommé (réactif limitant)
avancement_A_epuise = quantite_initiale_A / coeff_A
avancement_B_epuise = quantite_initiale_B / coeff_B

# L'avancement maximal de la réaction est déterminé par le réactif limitant
avancement_max = min(avancement_A_epuise, avancement_B_epuise)

# Définir le pas d'avancement pour obtenir une bonne résolution
n_points = 100  # Par exemple, 100 points de données
avancement = np.linspace(0, avancement_max, n_points)

# Quantités en fonction de l'avancement
quantite_A = quantite_initiale_A - coeff_A * avancement  # réactif A
quantite_B = quantite_initiale_B - coeff_B * avancement  # réactif B
quantite_C = coeff_C * avancement                       # produit C
quantite_D = coeff_D * avancement                       # produit D

# Calcul du maximum pour l'axe des ordonnées
y_max = max(quantite_initiale_A, quantite_initiale_B, quantite_C[-1], quantite_D[-1]) * 1.1  # un peu d'espace au-dessus

# Slider pour contrôler l'avancement
avancement_val = st.slider("Avancement de la réaction", 0.0, avancement_max, step=avancement_max / (n_points - 1))

# Trouver l'indice correspondant à l'avancement actuel
frame = int((avancement_val / avancement_max) * (n_points - 1))

# Préparation du graphique
fig, ax = plt.subplots()
ax.bar([nom_A, nom_B, nom_C, nom_D], [quantite_A[frame], quantite_B[frame], quantite_C[frame], quantite_D[frame]],
       color=['blue', 'orange', 'green', 'red'])
ax.set_ylim(0, y_max)
ax.set_title(f"{int(coeff_A)}{nom_A} + {int(coeff_B)}{nom_B} → {int(coeff_C)}{nom_C} + {int(coeff_D)}{nom_D}")

# Afficher les quantités au-dessus des barres
for i, (height, label) in enumerate(zip([quantite_A[frame], quantite_B[frame], quantite_C[frame], quantite_D[frame]], [nom_A, nom_B, nom_C, nom_D])):
    ax.text(i, height + 0.1, f'{height:.2f}', ha='center')

# Afficher le graphique dans Streamlit
st.pyplot(fig)
