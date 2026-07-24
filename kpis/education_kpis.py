"""
====================================================
Education KPI Generator
====================================================

Generates KPIs for:
- Student Performance
- College Analytics
- School Analytics
- Examination Results
"""

import pandas as pd


def get_education_kpis(df):
    """
    Generate Education KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # =====================================
    # Total Students
    # =====================================

    kpis["🎓 Total Students"] = len(df)

    # =====================================
    # Average Marks
    # =====================================

    marks_col = get_column("marks")

    if marks_col:

        avg_marks = pd.to_numeric(
            df[marks_col],
            errors="coerce"
        ).mean()

        kpis["📖 Average Marks"] = f"{avg_marks:.2f}"

    # =====================================
    # Highest Marks
    # =====================================

    if marks_col:

        highest = pd.to_numeric(
            df[marks_col],
            errors="coerce"
        ).max()

        kpis["🏆 Highest Marks"] = highest

    # =====================================
    # Average CGPA
    # =====================================

    cgpa_col = get_column("cgpa")

    if cgpa_col:

        avg_cgpa = pd.to_numeric(
            df[cgpa_col],
            errors="coerce"
        ).mean()

        kpis["🎯 Average CGPA"] = f"{avg_cgpa:.2f}"

    # =====================================
    # Top Subject
    # =====================================

    subject_col = get_column("subject")

    if subject_col:

        subject = df[subject_col].mode()

        if not subject.empty:

            kpis["📚 Popular Subject"] = subject.iloc[0]

    # =====================================
    # Attendance
    # =====================================

    attendance_col = get_column("attendance")

    if attendance_col:

        attendance = pd.to_numeric(
            df[attendance_col],
            errors="coerce"
        ).mean()

        kpis["📝 Avg Attendance"] = f"{attendance:.1f}%"

    # =====================================
    # Grade
    # =====================================

    grade_col = get_column("grade")

    if grade_col:

        grade = df[grade_col].mode()

        if not grade.empty:

            kpis["⭐ Most Common Grade"] = grade.iloc[0]

    # =====================================
    # Semester
    # =====================================

    semester_col = get_column("semester")

    if semester_col:

        semester = df[semester_col].mode()

        if not semester.empty:

            kpis["📅 Current Semester"] = semester.iloc[0]

    return kpis