"""
====================================================
Domain Router
====================================================

Routes KPI and Recommendation generation
based on detected dataset domain.
"""

# ==========================
# KPI Imports
# ==========================

from kpis.retail_kpis import get_retail_kpis
from kpis.hr_kpis import get_hr_kpis
from kpis.finance_kpis import get_finance_kpis
from kpis.healthcare_kpis import get_healthcare_kpis
from kpis.education_kpis import get_education_kpis
from kpis.banking_kpis import get_banking_kpis
from kpis.ecommerce_kpis import get_ecommerce_kpis
from kpis.fashion_kpis import get_fashion_kpis
from kpis.entertainment_kpis import get_entertainment_kpis

# ==========================
# Recommendation Imports
# ==========================

from recommendations.retail_recommendations import RETAIL_RECOMMENDATIONS
from recommendations.banking_recommendations import BANKING_RECOMMENDATIONS
from recommendations.finance_recommendation import FINANCE_RECOMMENDATIONS
from recommendations.healthcare_recommendation import HEALTHCARE_RECOMMENDATIONS
from recommendations.hr_recommendation import HR_RECOMMENDATIONS
from recommendations.education_recommendation import EDUCATION_RECOMMENDATIONS
from recommendations.ecommerce_recommendation import ECOMMERCE_RECOMMENDATIONS
from recommendations.entertainment_recommendations import ENTERTAINMENT_RECOMMENDATIONS
from recommendations.fashion_recommendations import FASHION_RECOMMENDATIONS



# ==================================================
# KPI ROUTER
# ==================================================

def get_domain_kpis(df, domain):
    """
    Returns KPIs based on detected dataset domain.
    """

    routers = {
        "Retail": get_retail_kpis,
        "HR": get_hr_kpis,
        "Finance": get_finance_kpis,
        "Healthcare": get_healthcare_kpis,
        "Education": get_education_kpis,
        "Banking": get_banking_kpis,
        "E-commerce": get_ecommerce_kpis,
        "Fashion": get_fashion_kpis,
        "Entertainment": get_entertainment_kpis,
    }

    func = routers.get(domain)

    if func:
        return func(df)

    return get_retail_kpis(df)


# ==================================================
# RECOMMENDATION ROUTER
# ==================================================

def get_domain_recommendations(df, domain):
    """
    Returns recommendations based on detected dataset domain.
    """

    routers = {
        "Retail": generate_retail_recommendations,
        "HR": generate_hr_recommendations,
        "Finance": generate_finance_recommendations,
        "Healthcare": generate_healthcare_recommendations,
        "Education": generate_education_recommendations,
        "Banking": generate_banking_recommendations,
        "E-commerce": generate_ecommerce_recommendations,
        "Fashion": generate_fashion_recommendations,
        "Entertainment": generate_entertainment_recommendations,
    }

    func = routers.get(domain)

    if func:
        return func(df)

    return generate_retail_recommendations(df)