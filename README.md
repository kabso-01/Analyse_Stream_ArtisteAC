# Analyse_Stream_ArtisteAC

## Présentation du projet

Je me suis lancé dans un challenge autour d’un sujet concret et original : analyser la visibilité Spotify de plusieurs artistes d’Afrique centrale à partir de données publiques.

L’objectif était de construire un dashboard interactif pour observer quelques indicateurs simples, comme les auditeurs mensuels, les followers, les écarts entre artistes et certaines tendances par pays.

Ce projet m’a permis de pratiquer la data analyse et la visualisation de données, tout en cherchant à transformer des données brutes en informations plus claires et plus utiles.

L’application a été développée avec **Python**, **Pandas** et **Streamlit**.

## Limites de l’analyse

Il est important de préciser que certains résultats présentés dans ce projet reposent sur des **estimations**.

La source de données utilisée ne fournit pas toutes les informations pour chaque artiste, notamment :
- le nombre exact de streams totaux pour tous les profils
- le revenu exact généré par stream sur Spotify

Pour cette raison, certaines analyses, surtout celles liées aux revenus, doivent être comprises comme des approximations utiles pour comparer les artistes et les pays, et non comme des valeurs exactes.

## Technologies utilisées

### Langage
- Python

### Bibliothèques
- Pandas

### Application
- Streamlit

---

## Structure du projet

Le projet peut être organisé de cette manière :

## demarrer l'appli avec streamlit 
-- intaller les dependances necessaires
 pip install -r requirements.txt
-- contenu du fichier requirement.txt
  streamlit
  pandas
-- lancer l'application 
  streamlit run app.py


## Structuration de l'application 
```bash
Analyse_Stream_ArtisteAC/
│── app.py
│── README.md
│── requirements.txt
│── data/
│   └── artistes_afrique_centrale_spotify.csv
