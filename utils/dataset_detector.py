"""
====================================================
DecisionAI Dataset Detection Module
====================================================

Automatically detects the business domain of an
uploaded dataset based on column names.

Supported Domains:
- Retail
- HR
- Finance
- Healthcare
- Education
- Banking
- E-commerce
- Fashion
- Entertainment
- Generic
"""

from collections import Counter


# =====================================================
# DOMAIN KEYWORDS
# =====================================================

DOMAIN_KEYWORDS = {

    "Retail": {

        "strong": {
            "store",
            "inventory",
            "stock",
            "discount",
            "profit",
            "ship_mode"
        },

        "weak": {
            "sales",
            "category",
            "sub_category",
            "product",
            "customer",
            "order",
            "quantity",
            "region"
        }

    },

    "HR": {

        "strong": {
            "employee",
            "department",
            "salary",
            "designation",
            "attrition",
            "experience"
        },

        "weak": {
            "gender",
            "age",
            "joining"
        }

    },

    "Finance": {

    "strong": {

        "revenue",
        "expense",
        "expenses",
        "budget",
        "invoice",
        "cost",
        "profit",
        "loss",
        "income",
        "tax",
        "financial",
        "finance",
        "ledger",
        "accounting",
        "balance_sheet"

    },

    "weak": {

        "transaction",
        "account",
        "payment",
        "amount"

    }

},

    "Healthcare": {

        "strong": {
            "patient",
            "doctor",
            "hospital",
            "diagnosis",
            "treatment",
            "medicine"
        },

        "weak": {
            "admission",
            "disease"
        }

    },

    "Education": {

    "strong": {

        "student",
        "marks",
        "grade",
        "teacher",
        "cgpa",
        "semester",
        "school",
        "college",
        "university",
        "exam",
        "result",
        "gpa"

    },

    "weak": {

        "subject",
        "attendance",
        "studytime",
        "failures",
        "guardian",
        "internet",
        "activities",
        "higher",
        "schoolsup",
        "famsup",
        "freetime",
        "health",
        "traveltime",
        "g1",
        "g2",
        "g3",
        "absences"

    }

},

    "Banking": {

        "strong": {
            "loan",
            "balance",
            "interest",
            "credit",
            "debit",
            "branch",
            "account"
        },

        "weak": {
            "customer",
            "transaction"
        }

    },

    "E-commerce": {

        "strong": {
            "payment",
            "payment_type",
            "shipping",
            "delivery",
            "seller",
            "buyer",
            "review",
            "wishlist",
            "cart"
        },

        "weak": {
            "customer",
            "order",
            "product",
            "rating"
        }

    },

    "Fashion": {

        "strong": {
            "brand",
            "collection",
            "size",
            "color",
            "style",
            "season",
            "fabric",
            "designer"
        },

        "weak": {
            "sku",
            "fashion"
        }

    },

    "Entertainment": {

        "strong": {
            "movie",
            "director",
            "cast",
            "actor",
            "netflix",
            "episode",
            "release_year"
        },

        "weak": {
            "title",
            "genre",
            "duration",
            "rating",
            "platform",
            "show"
        }

    }

}


# =====================================================
# COLUMN NORMALIZATION
# =====================================================

def normalize_columns(columns):
    """
    Converts column names into a normalized format.
    """

    normalized = []

    for col in columns:

        col = (
            str(col)
            .strip()
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
        )

        normalized.append(col)

    return normalized
# =====================================================
# DOMAIN RULE ENGINE
# =====================================================

def apply_domain_rules(columns, scores):
    """
    Apply additional domain-specific bonus rules.

    These rules improve detection accuracy for datasets
    that share common business columns.
    """

    column_set = set(columns)

    # -------------------------------------------------
    # Banking
    # -------------------------------------------------

    banking_columns = {

        "loan",
        "balance",
        "housing",
        "campaign",
        "contact",
        "pdays",
        "previous",
        "poutcome",
        "deposit"

    }

    matched = len(column_set & banking_columns)

    if matched >= 2:
        scores["Banking"] += matched * 5


    # -------------------------------------------------
    # E-commerce
    # -------------------------------------------------

    ecommerce_columns = {

        "payment_type",
        "payment_value",
        "seller_id",
        "customer_id",
        "order_id",
        "review_score",
        "freight_value",
        "shipping_limit_date"

    }

    matched = len(column_set & ecommerce_columns)

    if matched >= 2:
        scores["E-commerce"] += matched * 5


    # -------------------------------------------------
    # Fashion
    # -------------------------------------------------

    fashion_columns = {

        "brand",
        "size",
        "color",
        "fabric",
        "style",
        "season",
        "sku"

    }

    matched = len(column_set & fashion_columns)

    if matched >= 2:
        scores["Fashion"] += matched * 5


    # -------------------------------------------------
    # HR
    # -------------------------------------------------

    hr_columns = {

        "employeeid",
        "employee_number",
        "attrition",
        "department",
        "jobrole",
        "monthlyincome"

    }

    matched = len(column_set & hr_columns)

    if matched >= 2:
        scores["HR"] += matched * 5


    # -------------------------------------------------
    # Entertainment
    # -------------------------------------------------

    entertainment_columns = {

        "director",
        "cast",
        "listed_in",
        "release_year",
        "duration"

    }

    matched = len(column_set & entertainment_columns)

    if matched >= 2:
        scores["Entertainment"] += matched * 5
    # -------------------------------------------------
    # Education
    # -------------------------------------------------

    education_columns = {

        "student",
        "school",
        "college",
        "university",
        "semester",
        "cgpa",
        "grade",
        "marks",
        "subject",
        "attendance",
        "studytime",
        "failures",
        "guardian",
        "g1",
        "g2",
        "g3"

    }

    matched = len(column_set & education_columns)

    if matched >= 2:
        scores["Education"] += matched * 5
    # -------------------------------------------------
    # Finance
    # -------------------------------------------------

    finance_columns = {

        "revenue",
        "expense",
        "expenses",
        "budget",
        "invoice",
        "cost",
        "profit",
        "loss",
        "income",
        "tax",
        "amount",
        "payment"

    }

    matched = len(column_set & finance_columns)

    if matched >= 2:
        scores["Finance"] += matched * 5
        # -------------------------------------------------
    # Healthcare
    # -------------------------------------------------

    healthcare_columns = {

        "patient",
        "doctor",
        "hospital",
        "diagnosis",
        "treatment",
        "medicine",
        "disease",
        "admission",
        "discharge",
        "prescription",
        "blood_pressure",
        "heart_rate"

    }

    matched = len(column_set & healthcare_columns)

    if matched >= 2:
        scores["Healthcare"] += matched * 5

    return scores
# =====================================================
# DATASET DETECTION
# =====================================================

def detect_dataset_type(df):
    """
    Detect the business domain of the uploaded dataset.

    Returns:
    {
        "domain": "Retail",
        "confidence": 91.3,
        "matched_keywords": 18
    }
    """

    columns = normalize_columns(df.columns)

    scores = Counter()

    # -----------------------------------------------
    # Weighted keyword matching
    # -----------------------------------------------

    for domain, groups in DOMAIN_KEYWORDS.items():

        strong_keywords = groups["strong"]
        weak_keywords = groups["weak"]

        for column in columns:

            # Strong keywords
            for keyword in strong_keywords:

                if keyword in column:
                    scores[domain] += 5

            # Weak keywords
            for keyword in weak_keywords:

                if keyword in column:
                    scores[domain] += 1

    # -----------------------------------------------
    # Apply domain-specific rules
    # -----------------------------------------------

    scores = apply_domain_rules(columns, scores)

    # -----------------------------------------------
    # No domain detected
    # -----------------------------------------------

    if len(scores) == 0:

        return {

            "domain": "Generic",

            "confidence": 0.0,

            "matched_keywords": 0

        }

    # -----------------------------------------------
    # Best matching domain
    # -----------------------------------------------

    domain, matched = scores.most_common(1)[0]

    total_possible = (

        len(DOMAIN_KEYWORDS[domain]["strong"]) * 5

        +

        len(DOMAIN_KEYWORDS[domain]["weak"])

    )

    confidence = round(

        (matched / total_possible) * 100,

        1

    )

    confidence = min(confidence, 100.0)

    return {

        "domain": domain,

        "confidence": confidence,

        "matched_keywords": matched

    }
# =====================================================
# ALL DOMAIN SCORES
# =====================================================

def detect_dataset_scores(df):
    """
    Returns matching scores for all supported domains.

    Example:
    {
        "Retail": {
            "matched_keywords": 18,
            "confidence": 72.5
        },
        "HR": {
            "matched_keywords": 4,
            "confidence": 12.5
        }
    }
    """

    columns = normalize_columns(df.columns)

    scores = Counter()

    # -----------------------------------------------
    # Weighted keyword matching
    # -----------------------------------------------

    for domain, groups in DOMAIN_KEYWORDS.items():

        strong_keywords = groups["strong"]
        weak_keywords = groups["weak"]

        for column in columns:

            # Strong keywords
            for keyword in strong_keywords:

                if keyword in column:
                    scores[domain] += 5

            # Weak keywords
            for keyword in weak_keywords:

                if keyword in column:
                    scores[domain] += 1

    # -----------------------------------------------
    # Apply domain rules
    # -----------------------------------------------

    scores = apply_domain_rules(columns, scores)

    results = {}

    # -----------------------------------------------
    # Confidence for every domain
    # -----------------------------------------------

    for domain in DOMAIN_KEYWORDS:

        matched = scores.get(domain, 0)

        total_possible = (

            len(DOMAIN_KEYWORDS[domain]["strong"]) * 5

            +

            len(DOMAIN_KEYWORDS[domain]["weak"])

        )

        confidence = round(

            (matched / total_possible) * 100,

            1

        )

        confidence = min(confidence, 100.0)

        results[domain] = {

            "matched_keywords": matched,

            "confidence": confidence

        }

    return results
# =====================================================
# DATASET ICONS
# =====================================================

DATASET_ICONS = {

    "Retail": "🛒",

    "HR": "👨‍💼",

    "Finance": "💰",

    "Healthcare": "🏥",

    "Education": "🎓",

    "Banking": "🏦",

    "E-commerce": "📦",

    "Fashion": "👗",

    "Entertainment": "🎬",

    "Generic": "📊"

}


# =====================================================
# GET DATASET ICON
# =====================================================

def get_dataset_icon(domain):
    """
    Returns an emoji icon for the detected domain.
    """

    return DATASET_ICONS.get(domain, "📊")