"""
====================================================
Entertainment KPI Generator
====================================================

Generates KPIs for:
- Netflix
- Amazon Prime
- Disney+
- Spotify
- Movie datasets
- TV Show datasets
"""

import pandas as pd


def get_entertainment_kpis(df):
    """
    Generate Entertainment KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    # ======================================================
    # Total Content
    # ======================================================

    kpis["🎬 Total Content"] = len(df)

    # ======================================================
    # Movies
    # ======================================================

    if "type" in columns:

        original = df.columns[columns.index("type")]

        movies = (df[original]
                  .astype(str)
                  .str.lower()
                  .eq("movie")
                  .sum())

        kpis["🎥 Movies"] = int(movies)

    # ======================================================
    # TV Shows
    # ======================================================

    if "type" in columns:

        original = df.columns[columns.index("type")]

        shows = (df[original]
                 .astype(str)
                 .str.lower()
                 .eq("tv show")
                 .sum())

        kpis["📺 TV Shows"] = int(shows)

    # ======================================================
    # Genres
    # ======================================================

    if "listed_in" in columns:

        original = df.columns[columns.index("listed_in")]

        genre = (
            df[original]
            .dropna()
            .astype(str)
            .str.split(",")
            .explode()
            .str.strip()
            .mode()
        )

        if not genre.empty:

            kpis["🎭 Top Genre"] = genre.iloc[0]

    # ======================================================
    # Directors
    # ======================================================

    if "director" in columns:
    
        original = df.columns[columns.index("director")]

        director = (
              df[original]
              .dropna()
              .astype(str)
              .loc[lambda s: s.str.lower() != "nan"]
              .mode()
    )

    if not director.empty:
        kpis["🎬 Top Director"] = director.iloc[0]

    # ======================================================
    # Rating
    # ======================================================

    if "rating" in columns:

        original = df.columns[columns.index("rating")]

        rating = (
            df[original]
            .dropna()
            .astype(str)
            .mode()
        )

        if not rating.empty:

            kpis["⭐ Most Common Rating"] = rating.iloc[0]

    # ======================================================
    # Country
    # ======================================================

    if "country" in columns:

        original = df.columns[columns.index("country")]

        country = (
            df[original]
            .dropna()
            .astype(str)
            .str.split(",")
            .explode()
            .str.strip()
            .mode()
        )

        if not country.empty:

            kpis["🌍 Top Country"] = country.iloc[0]

    # ======================================================
    # Release Year
    # ======================================================

    # ======================================================
# Release Year
# ======================================================

    if "release_year" in columns:
           original = df.columns[columns.index("release_year")]

           latest = df[original].max()
           earliest = df[original].min()

    # Latest
           if hasattr(latest, "year"):
              kpis["📅 Latest Release"] = latest.year
           else:
              kpis["📅 Latest Release"] = int(latest)

    # Earliest
           if hasattr(earliest, "year"):
              kpis["🗓 Earliest Release"] = earliest.year
           else:
              kpis["🗓 Earliest Release"] = int(earliest)
    return kpis