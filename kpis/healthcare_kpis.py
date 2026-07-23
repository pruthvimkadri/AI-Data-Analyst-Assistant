"""
====================================================
Healthcare KPI Generator
====================================================

Generates KPIs for:
- Hospital Datasets
- Patient Records
- Healthcare Analytics
"""

import pandas as pd


def get_healthcare_kpis(df):
    """
    Generate Healthcare KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # =====================================
    # Total Patients
    # =====================================

    kpis["🏥 Total Patients"] = len(df)

    # =====================================
    # Average Age
    # =====================================

    age_col = get_column("age")

    if age_col:

        avg_age = pd.to_numeric(
            df[age_col],
            errors="coerce"
        ).mean()

        kpis["🎂 Average Age"] = f"{avg_age:.1f}"

    # =====================================
    # Most Common Disease
    # =====================================

    disease_col = get_column("disease")

    if disease_col is None:
        disease_col = get_column("diagnosis")

    if disease_col:

        disease = df[disease_col].mode()

        if not disease.empty:

            kpis["🩺 Common Diagnosis"] = disease.iloc[0]

    # =====================================
    # Top Doctor
    # =====================================

    doctor_col = get_column("doctor")

    if doctor_col:

        doctor = df[doctor_col].mode()

        if not doctor.empty:

            kpis["👨‍⚕️ Top Doctor"] = doctor.iloc[0]

    # =====================================
    # Top Hospital
    # =====================================

    hospital_col = get_column("hospital")

    if hospital_col:

        hospital = df[hospital_col].mode()

        if not hospital.empty:

            kpis["🏨 Top Hospital"] = hospital.iloc[0]

    # =====================================
    # Gender Distribution
    # =====================================

    gender_col = get_column("gender")

    if gender_col:

        gender = df[gender_col].mode()

        if not gender.empty:

            kpis["👤 Majority Gender"] = gender.iloc[0]

    # =====================================
    # Average Stay
    # =====================================

    stay_col = get_column("stay_days")

    if stay_col:

        avg_stay = pd.to_numeric(
            df[stay_col],
            errors="coerce"
        ).mean()

        kpis["🛏 Avg Stay"] = f"{avg_stay:.1f} Days"

    return kpis