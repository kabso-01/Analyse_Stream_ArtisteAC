import streamlit as st
import pandas as pd
import math


st.set_page_config(
    page_title="Central Africa Artists Dashboard",
    page_icon="🎵",
    layout="wide"
)

# chargement des images des artistes


data = [
    {
        "artist": "Blanche Bailly",
        "country": "Cameroun",
        "spotify_monthly_listeners": 60566,
        "spotify_followers": 78173,
        "spotify_total_streams": None,
        "image_url": "https://i.ytimg.com/vi/GZZHrZ2ou58/oar2.jpg?sqp=-oaymwEkCJUDENAFSFqQAgHyq4qpAxMIARUAAAAAJQAAyEI9AICiQ3gB&rs=AOn4CLA2VzaMpBf3Mwn8lNLPMkx_mybfWw",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Stanley Enow",
        "country": "Cameroun",
        "spotify_monthly_listeners": 23061,
        "spotify_followers": 30125,
        "spotify_total_streams": None,
        "image_url": "https://lh6.googleusercontent.com/j76OcslOUALJkh2M-3JaEfeFX420e0PRgQct-TfKDEcLYxWGQfD7N11fm6k-9NtCywrBN7QGhV71aMIq4mV7st5pM6jSvEtg04nbPV-foUHabTka_tGhjkKju1dFxutEIfawe6gA=s16000",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Aveiro Djess",
        "country": "Cameroun",
        "spotify_monthly_listeners": 53521,
        "spotify_followers": 40278,
        "spotify_total_streams": None,
        "image_url": "https://i.scdn.co/image/ab6761610000e5eb156e8b1aed40e015e31358e4",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Magasco",
        "country": "Cameroun",
        "spotify_monthly_listeners": 47214,
        "spotify_followers": 46710,
        "spotify_total_streams": None,
        "image_url": "https://tse4.mm.bing.net/th/id/OIP.FseOL79QprLHW55mREHx2wHaFB?rs=1&pid=ImgDetMain&o=7&rm=3",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Damso",
        "country": "RDC",
        "spotify_monthly_listeners": 5900000,
        "spotify_followers": 5900000,
        "spotify_total_streams": None,
        "image_url": "https://tse1.mm.bing.net/th/id/OIP.uxMGaFcdT9Ai6of0wCZOfgHaEo?rs=1&pid=ImgDetMain&o=7&rm=3",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Fally Ipupa",
        "country": "RDC",
        "spotify_monthly_listeners": 1400000,
        "spotify_followers": 2000000,
        "spotify_total_streams": 780300000,
        "image_url": "https://tse3.mm.bing.net/th/id/OIP.PR0gVmKtsuXc9v5N3PyPZQHaEu?rs=1&pid=ImgDetMain&o=7&rm=3",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Innoss'B",
        "country": "RDC",
        "spotify_monthly_listeners": 281146,
        "spotify_followers": 248335,
        "spotify_total_streams": None,
        "image_url": "https://b-onetv.cd/wp-content/uploads/2022/02/Innoncent-balume.jpeg",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Ferre Gola",
        "country": "RDC",
        "spotify_monthly_listeners": 171261,
        "spotify_followers": 395705,
        "spotify_total_streams": None,
        "image_url": "https://i.ytimg.com/vi/WVLQ8IhUx9c/maxresdefault.jpg",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Gaz Mawete",
        "country": "RDC",
        "spotify_monthly_listeners": 237675,
        "spotify_followers": 223424,
        "spotify_total_streams": None,
        "image_url": "https://tse3.mm.bing.net/th/id/OIP.Ji2Bqkk3wcv-PuIl229IQQHaHa?rs=1&pid=ImgDetMain&o=7&rm=3",
        "source": "Music Metrics Vault"
    },
    {
        "artist": "Koffi Olomide",
        "country": "RDC",
        "spotify_monthly_listeners": 395071,
        "spotify_followers": 693449,
        "spotify_total_streams": 224100000,
        "image_url": "https://tse1.mm.bing.net/th/id/OIP.rYXFrSL3lGriJkE5NYxDmAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3",
        "source": "Music Metrics Vault"
    }
]

# ============================================================
# Création du DataFrame
# ============================================================
df = pd.DataFrame(data)

# Paramètres d'analyse

# Hypothèse pédagogique :
# 1 monthly listener ~ 4 streams / mois
# 1 stream rapporte ~ 0.004 USD
stream_par_utilisateur = 4
revenu_pr_stream = 0.004

# Colonnes calculées
# - monthly listeners = personnes qui passent dans le magasin
# - estimated streams = nombre de produits consommés
# - estimated revenue = argent approximatif généré

df["estimated_monthly_streams"] = df["spotify_monthly_listeners"] * stream_par_utilisateur 
df["estimated_monthly_revenue_usd"] = df["estimated_monthly_streams"] * revenu_pr_stream 
df["followers_listeners_ratio"] = df["spotify_followers"] / df["spotify_monthly_listeners"]

#sidebar=
st.sidebar.title("Filtres")

selected_countries = st.sidebar.multiselect(
    "Choisir un ou plusieurs pays",
    options=sorted(df["country"].unique()),
    default=sorted(df["country"].unique())
)

min_listeners = int(df["spotify_monthly_listeners"].min())
max_listeners = int(df["spotify_monthly_listeners"].max())

listeners_range = st.sidebar.slider(
    "Filtrer par monthly listeners",
    min_value=min_listeners,
    max_value=max_listeners,
    value=(min_listeners, max_listeners)
)

filtered_df = df[
    (df["country"].isin(selected_countries)) &
    (df["spotify_monthly_listeners"] >= listeners_range[0]) &
    (df["spotify_monthly_listeners"] <= listeners_range[1])
].copy()


st.title("🎵  Dashboard des artistes d'afrique Central ")
st.caption("Analyse Spotify d'artistes d'Afrique centrale avec estimation simple des revenus.")


# KPIs principaux

col1, col2, col3, col4 = st.columns(4)

col1.metric("Artistes", len(filtered_df))
col2.metric("Pays", filtered_df["country"].nunique())
col3.metric("Listeners totaux", f"{int(filtered_df['spotify_monthly_listeners'].sum()):,}".replace(",", " "))
col4.metric("Revenu estimé / mois ($)", f"{filtered_df['estimated_monthly_revenue_usd'].sum():,.0f}".replace(",", " "))

st.divider()

# Tableau principal

st.subheader("Dataset analysé")
st.dataframe(
    filtered_df[[
        "artist", "country", "spotify_monthly_listeners", "spotify_followers",
        "spotify_total_streams", "estimated_monthly_streams",
        "estimated_monthly_revenue_usd", "followers_listeners_ratio", "source"
    ]],
    use_container_width=True
)


# Classements

left, right = st.columns(2)

with left:
    st.subheader("Top artistes par monthly listeners")
    top_listeners = filtered_df.sort_values("spotify_monthly_listeners", ascending=False)
    st.bar_chart(top_listeners.set_index("artist")["spotify_monthly_listeners"])

with right:
    st.subheader("Top artistes par followers")
    top_followers = filtered_df.sort_values("spotify_followers", ascending=False)
    st.bar_chart(top_followers.set_index("artist")["spotify_followers"])

st.divider()

# Analyse par pays

st.subheader("Analyse par pays")

country_stats = filtered_df.groupby("country", as_index=False).agg(
    artists_count=("artist", "count"),
    total_listeners=("spotify_monthly_listeners", "sum"),
    avg_listeners=("spotify_monthly_listeners", "mean"),
    total_followers=("spotify_followers", "sum"),
    estimated_revenue_usd=("estimated_monthly_revenue_usd", "sum")
).sort_values("total_listeners", ascending=False)

st.dataframe(country_stats, use_container_width=True)
st.bar_chart(country_stats.set_index("country")["estimated_revenue_usd"])

st.divider()

#galerie des artistes 
st.subheader("Galerie des artistes")

cards_per_row = 3
rows = math.ceil(len(filtered_df) / cards_per_row)
artists_list = filtered_df.to_dict("records")

for row_idx in range(rows):
    cols = st.columns(cards_per_row)
    for col_idx in range(cards_per_row):
        item_idx = row_idx * cards_per_row + col_idx
        if item_idx < len(artists_list):
            artist = artists_list[item_idx]
            with cols[col_idx]:
                st.image(artist["image_url"], use_container_width=True)
                st.markdown(f"**{artist['artist']}**")
                st.write(f"Pays : {artist['country']}")
                st.write(f"Listeners : {artist['spotify_monthly_listeners']:,}".replace(",", " "))
                st.write(f"Followers : {artist['spotify_followers']:,}".replace(",", " "))
                revenue = artist["estimated_monthly_revenue_usd"]
                st.write(f"Revenu estimé : {revenue:,.0f} $".replace(",", " "))

st.divider()



#st.subheader("Télécharger les données")
#csv_data = filtered_df.to_csv(index=False).encode("utf-8")

#st.download_button(
#   label="Télécharger le CSV filtré",
#    data=csv_data,
#   file_name="central_africa_artists_filtered.csv",
#   mime="text/csv"
#)
#'''
# methodologie et conclusion

st.subheader("Méthodologie")
st.write(
    "Les revenus Spotify affichés ici sont des estimations pédagogiques. "
    "On suppose qu'un auditeur mensuel produit environ 4 streams par mois, "
    "et qu'un stream rapporte environ 0.004 USD. Dans la réalité, le paiement "
    "dépend de plusieurs facteurs."
)
st.subheader("Petite conclusion personnelle")
st.write(
    "Soutenons nos artistes cheres camerounais ils sont bourrés de talents et meritent d'etre reconnu a leur juste valeur"
    "on ne devrait pas envier le congo parce qu'il a des artistes qui font plus de streams que les nôtres, mais plutôt s'inspirer de leur succès pour booster notre propre industrie musicale."
    "\n"
   
)

st.write(
    "PS: Tenor est plus fort que Chétté"
)