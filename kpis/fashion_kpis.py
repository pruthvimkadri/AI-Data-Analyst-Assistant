"""
====================================================
Fashion KPI Generator
====================================================

Generates KPIs for:
- Myntra
- Zara
- H&M
- Ajio
- Fashion Retail
"""

import pandas as pd


def get_fashion_kpis(df):
    """
    Generate Fashion KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # =====================================
    # Total Products
    # =====================================

    kpis["👗 Total Products"] = len(df)

    # =====================================
    # Average Price
    # =====================================

    price_col = get_column("price")

    if price_col:

        price = pd.to_numeric(df[price_col], errors="coerce").mean()

        kpis["💰 Average Price"] = f"${price:,.2f}"

    # =====================================
    # Highest Price
    # =====================================

    if price_col:

        highest = pd.to_numeric(df[price_col], errors="coerce").max()

        kpis["💎 Highest Price"] = f"${highest:,.2f}"

    # =====================================
    # Top Brand
    # =====================================

    brand_col = get_column("brand")

    if brand_col:

        brand = df[brand_col].mode()

        if not brand.empty:

            kpis["🏷 Top Brand"] = brand.iloc[0]

    # =====================================
    # Most Common Color
    # =====================================

    color_col = get_column("color")

    if color_col:

        color = df[color_col].mode()

        if not color.empty:

            kpis["🎨 Popular Color"] = color.iloc[0]

    # =====================================
    # Most Common Size
    # =====================================

    size_col = get_column("size")

    if size_col:

        size = df[size_col].mode()

        if not size.empty:

            kpis["📏 Popular Size"] = size.iloc[0]

    # =====================================
    # Top Category
    # =====================================

    category_col = get_column("category")

    if category_col:

        category = df[category_col].mode()

        if not category.empty:

            kpis["👜 Top Category"] = category.iloc[0]

    # =====================================
    # Top Season
    # =====================================

    season_col = get_column("season")

    if season_col:

        season = df[season_col].mode()

        if not season.empty:

            kpis["🍂 Popular Season"] = season.iloc[0]

    return kpis