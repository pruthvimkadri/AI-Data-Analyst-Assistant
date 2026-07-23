from recommendations.retail_recommendations import RETAIL_RECOMMENDATIONS
from recommendations.banking_recommendations import BANKING_RECOMMENDATIONS
from recommendations.finance_recommendation import FINANCE_RECOMMENDATIONS
from recommendations.healthcare_recommendation import HEALTHCARE_RECOMMENDATIONS
from recommendations.hr_recommendation import HR_RECOMMENDATIONS
from recommendations.education_recommendation import EDUCATION_RECOMMENDATIONS
from recommendations.ecommerce_recommendation import ECOMMERCE_RECOMMENDATIONS
from recommendations.entertainment_recommendations import ENTERTAINMENT_RECOMMENDATIONS
from recommendations.fashion_recommendations import FASHION_RECOMMENDATIONS


DOMAIN_RECOMMENDATIONS = {

    "Retail": RETAIL_RECOMMENDATIONS,
    "HR": HR_RECOMMENDATIONS,
    "Finance": FINANCE_RECOMMENDATIONS,
    "Healthcare": HEALTHCARE_RECOMMENDATIONS,
    "Education": EDUCATION_RECOMMENDATIONS,
    "Banking": BANKING_RECOMMENDATIONS,
    "E-commerce": ECOMMERCE_RECOMMENDATIONS,
    "Entertainment": ENTERTAINMENT_RECOMMENDATIONS,
    "Fashion": FASHION_RECOMMENDATIONS

}


def get_recommendations(domain):

    return DOMAIN_RECOMMENDATIONS.get(
        domain,
        {
            "kpis": [],
            "charts": [],
            "insights": []
        }
    )