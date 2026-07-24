import pandas as pd


def generate_recommendations(df, domain):

    # ------------------------------------------
    # Normalize Dataset
    # ------------------------------------------

    df_norm = df.copy()
    df_norm.columns = [
        c.lower().strip().replace(" ", "_")
        for c in df.columns
    ]

    columns = set(df_norm.columns)
    domain = domain.strip().lower()

    recommendations = {
    "kpis": [],
    "charts": [],
    "insights": [],
    "executive_summary": ""
}

    # ==========================================
    # RETAIL
    # ==========================================

    if domain == "retail":

        # KPIs
        if "sales" in columns:
            recommendations["kpis"].append("Total Sales")

        if "profit" in columns:
            recommendations["kpis"].extend([
                "Total Profit",
                "Profit Margin"
            ])

        if "discount" in columns:
            recommendations["kpis"].append("Average Discount")

        if "customer_id" in columns:
            recommendations["kpis"].append("Total Customers")

        if "order_id" in columns:
            recommendations["kpis"].append("Total Orders")

        if "quantity" in columns:
            recommendations["kpis"].append("Total Quantity Sold")

        # Charts
        if "order_date" in columns:
            recommendations["charts"].append("Sales Trend")

        if "region" in columns:
            recommendations["charts"].append("Sales by Region")

        if "category" in columns:
            recommendations["charts"].append("Sales by Category")

        if "sub_category" in columns:
            recommendations["charts"].append("Sales by Sub-Category")

        if "product_name" in columns:
            recommendations["charts"].append("Top Products")

        # Insights
        if "profit" in columns:
            recommendations["insights"].append(
                "Monitor product profitability."
            )

        if "discount" in columns:
            recommendations["insights"].append(
                "Review high-discount products."
            )

        if "region" in columns:
            recommendations["insights"].append(
                "Compare regional sales."
            )

    # ==========================================
    # HR
    # ==========================================

    elif domain == "hr":

        # KPIs
        if "salary" in columns:
            recommendations["kpis"].append("Average Salary")

        if "department" in columns:
            recommendations["kpis"].append("Department Count")

        if "age" in columns:
            recommendations["kpis"].append("Average Age")

        if "attrition" in columns:
            recommendations["kpis"].append("Attrition Rate")

        if "experience" in columns:
            recommendations["kpis"].append("Average Experience")

        # Charts
        if "department" in columns:
            recommendations["charts"].append(
                "Employees by Department"
            )

        if "salary" in columns:
            recommendations["charts"].append(
                "Salary Distribution"
            )

        if "age" in columns:
            recommendations["charts"].append(
                "Age Distribution"
            )

        if "attrition" in columns:
            recommendations["charts"].append(
                "Attrition Analysis"
            )

        # Insights
        if "salary" in columns:
            recommendations["insights"].append(
                "Compare salaries across departments."
            )

        if "attrition" in columns:
            recommendations["insights"].append(
                "Monitor employee attrition."
            )

    # -------- Continue in File 1.2 --------
        # ==========================================
    # FINANCE
    # ==========================================

    elif domain == "finance":

        # KPIs
        if "revenue" in columns:
            recommendations["kpis"].append("Total Revenue")

        if "expense" in columns or "expenses" in columns:
            recommendations["kpis"].append("Total Expenses")

        if "profit" in columns:
            recommendations["kpis"].append("Net Profit")

        if "budget" in columns:
            recommendations["kpis"].append("Budget Utilization")

        # Charts
        if "date" in columns:
            recommendations["charts"].append("Revenue Trend")

        if "expense" in columns or "expenses" in columns:
            recommendations["charts"].append("Expense Analysis")

        if "budget" in columns:
            recommendations["charts"].append("Budget vs Actual")

        # Insights
        if "profit" in columns:
            recommendations["insights"].append(
                "Track profit growth."
            )

        if "expense" in columns or "expenses" in columns:
            recommendations["insights"].append(
                "Monitor operating expenses."
            )

        if "budget" in columns:
            recommendations["insights"].append(
                "Compare actual spending against the budget."
            )

    # ==========================================
    # BANKING
    # ==========================================

    elif domain == "banking":

        # KPIs
        if "balance" in columns:
            recommendations["kpis"].append("Average Balance")

        if "loan" in columns:
            recommendations["kpis"].append("Total Loans")

        if "credit_score" in columns:
            recommendations["kpis"].append("Average Credit Score")

        if "transaction" in columns:
            recommendations["kpis"].append("Transaction Volume")

        # Charts
        if "balance" in columns:
            recommendations["charts"].append("Balance Distribution")

        if "loan" in columns:
            recommendations["charts"].append("Loan Analysis")

        if "credit_score" in columns:
            recommendations["charts"].append("Credit Score Distribution")

        if "transaction" in columns:
            recommendations["charts"].append("Transaction Trend")

        # Insights
        if "loan" in columns:
            recommendations["insights"].append(
                "Monitor loan performance."
            )

        if "balance" in columns:
            recommendations["insights"].append(
                "Identify customers with high account balances."
            )

        if "credit_score" in columns:
            recommendations["insights"].append(
                "Analyze credit score distribution."
            )

    # ==========================================
    # HEALTHCARE
    # ==========================================

    elif domain == "healthcare":

        # KPIs
        if "patient" in columns:
            recommendations["kpis"].append("Total Patients")

        if "doctor" in columns:
            recommendations["kpis"].append("Doctor Count")

        if "age" in columns:
            recommendations["kpis"].append("Average Age")

        # Charts
        if "diagnosis" in columns:
            recommendations["charts"].append("Disease Distribution")

        if "doctor" in columns:
            recommendations["charts"].append("Doctor Workload")

        if "admission" in columns:
            recommendations["charts"].append("Admission Trend")

        if "age" in columns:
            recommendations["charts"].append("Patient Age Distribution")

        # Insights
        if "diagnosis" in columns:
            recommendations["insights"].append(
                "Identify common diseases."
            )

        if "doctor" in columns:
            recommendations["insights"].append(
                "Evaluate doctor workload distribution."
            )

        if "admission" in columns:
            recommendations["insights"].append(
                "Monitor patient admission trends."
            )

    # -------- Continue in File 1.3 --------
        # ==========================================
    # EDUCATION
    # ==========================================

    elif domain == "education":

        # KPIs
        if "student" in columns:
            recommendations["kpis"].append("Total Students")

        if "marks" in columns:
            recommendations["kpis"].append("Average Marks")

        if "cgpa" in columns:
            recommendations["kpis"].append("Average CGPA")

        if "attendance" in columns:
            recommendations["kpis"].append("Attendance Rate")

        # Charts
        if "marks" in columns:
            recommendations["charts"].append("Marks Distribution")

        if "attendance" in columns:
            recommendations["charts"].append("Attendance Analysis")

        if "grade" in columns:
            recommendations["charts"].append("Grade Distribution")

        # Insights
        if "marks" in columns:
            recommendations["insights"].append(
                "Identify low-performing students."
            )

        if "attendance" in columns:
            recommendations["insights"].append(
                "Monitor student attendance."
            )

        if "cgpa" in columns:
            recommendations["insights"].append(
                "Compare CGPA across student groups."
            )

    # ==========================================
    # E-COMMERCE
    # ==========================================

    elif domain == "e-commerce":

        # KPIs
        if "sales" in columns:
            recommendations["kpis"].append("Revenue")

        if "order_id" in columns:
            recommendations["kpis"].append("Orders")

        if "customer_id" in columns:
            recommendations["kpis"].append("Customers")

        if "review_score" in columns:
            recommendations["kpis"].append("Average Rating")

        # Charts
        if "order_date" in columns:
            recommendations["charts"].append("Sales Trend")

        if "product_category" in columns:
            recommendations["charts"].append("Sales by Category")

        if "review_score" in columns:
            recommendations["charts"].append("Review Distribution")

        # Insights
        if "review_score" in columns:
            recommendations["insights"].append(
                "Track customer satisfaction."
            )

        if "sales" in columns:
            recommendations["insights"].append(
                "Monitor sales performance over time."
            )

        if "customer_id" in columns:
            recommendations["insights"].append(
                "Analyze customer purchasing behavior."
            )

    # ==========================================
    # ENTERTAINMENT
    # ==========================================

    elif domain == "entertainment":

        # KPIs
        if "title" in columns:
            recommendations["kpis"].append("Total Titles")

        if "director" in columns:
            recommendations["kpis"].append("Director Count")

        if "country" in columns:
            recommendations["kpis"].append("Countries")

        if "release_year" in columns:
            recommendations["kpis"].append("Latest Release Year")

        # Charts
        if "listed_in" in columns:
            recommendations["charts"].append("Genre Distribution")

        if "country" in columns:
            recommendations["charts"].append("Country Distribution")

        if "release_year" in columns:
            recommendations["charts"].append("Release Trend")

        if "director" in columns:
            recommendations["charts"].append("Titles by Director")

        # Insights
        if "listed_in" in columns:
            recommendations["insights"].append(
                "Identify popular genres."
            )

        if "country" in columns:
            recommendations["insights"].append(
                "Compare content production by country."
            )

        if "release_year" in columns:
            recommendations["insights"].append(
                "Analyze content release trends over time."
            )

    # -------- Continue in File 1.4 --------
        # ==========================================
    # FASHION
    # ==========================================

    elif domain == "fashion":

        # KPIs
        if "brand" in columns:
            recommendations["kpis"].append("Brands")

        if "sales" in columns:
            recommendations["kpis"].append("Revenue")

        if "price" in columns:
            recommendations["kpis"].append("Average Price")

        if "rating" in columns:
            recommendations["kpis"].append("Average Rating")

        # Charts
        if "brand" in columns:
            recommendations["charts"].append("Sales by Brand")

        if "category" in columns:
            recommendations["charts"].append("Sales by Category")

        if "color" in columns:
            recommendations["charts"].append("Color Distribution")

        if "size" in columns:
            recommendations["charts"].append("Size Distribution")

        # Insights
        if "brand" in columns:
            recommendations["insights"].append(
                "Identify top-performing brands."
            )

        if "price" in columns:
            recommendations["insights"].append(
                "Review product pricing strategy."
            )

        if "rating" in columns:
            recommendations["insights"].append(
                "Monitor customer ratings to improve product quality."
            )

   


   
    # ==========================================
    # PART C - SMART DATA INSIGHTS
    # ==========================================

    # Missing Values
    missing_percent = (
        df_norm.isnull().sum() / len(df_norm)
    ) * 100

    high_missing = missing_percent[
        missing_percent > 20
    ]

    if len(high_missing) > 0:

        recommendations["insights"].append(
            f"{len(high_missing)} column(s) contain more than 20% missing values."
        )

    # ------------------------------------------
    # Duplicate Records
    # ------------------------------------------

    duplicates = df_norm.duplicated().sum()

    if duplicates > 0:

        recommendations["insights"].append(
            f"{duplicates} duplicate record(s) detected."
        )

    # ------------------------------------------
    # Dataset Size
    # ------------------------------------------

    recommendations["insights"].append(
        f"Dataset contains {len(df_norm):,} rows and "
        f"{len(df_norm.columns)} columns."
    )

    # ------------------------------------------
    # Numeric & Categorical Summary
    # ------------------------------------------

    numeric_cols = df_norm.select_dtypes(
        include="number"
    ).columns

    categorical_cols = df_norm.select_dtypes(
        include=["object", "category"]
    ).columns

    recommendations["insights"].append(
        f"Detected {len(numeric_cols)} numeric column(s) "
        f"and {len(categorical_cols)} categorical column(s)."
    )

    # ------------------------------------------
    # Numeric Column Validation
    # ------------------------------------------

    for col in numeric_cols:

        # Negative Values

        negative_count = (
            df_norm[col] < 0
        ).sum()

        if negative_count > 0:

            recommendations["insights"].append(
                f"{col} contains {negative_count} negative value(s)."
            )

        # Zero Values

        zero_count = (
            df_norm[col] == 0
        ).sum()

        if zero_count > 0:

            recommendations["insights"].append(
                f"{col} contains {zero_count} zero value(s)."
            )

        # Constant Column

        if df_norm[col].nunique() == 1:

            recommendations["insights"].append(
                f"{col} has the same value in every row."
            )

    # -------- Continue in File 2.2 --------
        # ------------------------------------------
    # IQR Outlier Detection
    # ------------------------------------------

    for col in numeric_cols:

        q1 = df_norm[col].quantile(0.25)
        q3 = df_norm[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - (1.5 * iqr)
        upper = q3 + (1.5 * iqr)

        outliers = df_norm[
            (df_norm[col] < lower) |
            (df_norm[col] > upper)
        ]

        if not outliers.empty:

            recommendations["insights"].append(
                f"{col} contains {len(outliers)} potential outlier(s)."
            )

    # ------------------------------------------
    # Categorical Column Analysis
    # ------------------------------------------

    for col in categorical_cols:

        unique_values = df_norm[col].nunique(dropna=True)

        # High Cardinality

        if unique_values > 100:

            recommendations["insights"].append(
                f"{col} contains a large number of unique values ({unique_values})."
            )

        # Most Common Value

        mode = df_norm[col].mode(dropna=True)

        if not mode.empty:

            recommendations["insights"].append(
                f"Most common value in '{col}' is '{mode.iloc[0]}'."
            )

    # ------------------------------------------
    # Correlation Analysis
    # ------------------------------------------

    if len(numeric_cols) > 1:

        corr_matrix = df_norm[numeric_cols].corr()

        for i in range(len(corr_matrix.columns)):

            for j in range(i):

                corr_value = corr_matrix.iloc[i, j]

                if abs(corr_value) >= 0.85:

                    recommendations["insights"].append(
                        f"{corr_matrix.columns[i]} and "
                        f"{corr_matrix.columns[j]} are highly "
                        f"correlated ({corr_value:.2f})."
                    )

    # ------------------------------------------
    # Numeric Summary Statistics
    # ------------------------------------------

    if len(numeric_cols) > 0:

        recommendations["insights"].append(
            "Numeric columns have been summarized for trend analysis."
        )

    # ------------------------------------------
    # Categorical Summary Statistics
    # ------------------------------------------

    if len(categorical_cols) > 0:

        recommendations["insights"].append(
            "Categorical columns have been summarized for distribution analysis."
        )

    # -------- Continue in File 2.3 --------
        # ==========================================
    # PART D - BUSINESS INTELLIGENCE INSIGHTS
    # ==========================================

    # ------------------------------------------
    # Sales by Region
    # ------------------------------------------

    if {"region", "sales"}.issubset(df_norm.columns):

        region_sales = (
            df_norm.groupby("region")["sales"]
            .sum()
            .sort_values(ascending=False)
        )

        if not region_sales.empty:

            recommendations["insights"].append(
                f"🏆 Highest sales region: "
                f"{region_sales.index[0]} "
                f"({region_sales.iloc[0]:,.2f})"
            )

            recommendations["insights"].append(
                f"📉 Lowest sales region: "
                f"{region_sales.index[-1]} "
                f"({region_sales.iloc[-1]:,.2f})"
            )

    # ------------------------------------------
    # Sales by Category
    # ------------------------------------------

    if {"category", "sales"}.issubset(df_norm.columns):

        category_sales = (
            df_norm.groupby("category")["sales"]
            .sum()
            .sort_values(ascending=False)
        )

        if not category_sales.empty:

            recommendations["insights"].append(
                f"🏆 Best-selling category: "
                f"{category_sales.index[0]}"
            )

            recommendations["insights"].append(
                f"📉 Lowest-selling category: "
                f"{category_sales.index[-1]}"
            )

    # ------------------------------------------
    # Product Profitability
    # ------------------------------------------

    if {"product_name", "profit"}.issubset(df_norm.columns):

        product_profit = (
            df_norm.groupby("product_name")["profit"]
            .sum()
            .sort_values(ascending=False)
        )

        if not product_profit.empty:

            recommendations["insights"].append(
                f"💰 Most profitable product: "
                f"{product_profit.index[0]}"
            )

            loss_products = product_profit[
                product_profit < 0
            ]

            if not loss_products.empty:

                recommendations["insights"].append(
                    f"⚠️ {len(loss_products)} "
                    f"product(s) are operating at a loss."
                )

    # ------------------------------------------
    # Monthly Sales Trend
    # ------------------------------------------

    if {"order_date", "sales"}.issubset(df_norm.columns):

        temp = df_norm.copy()

        temp["order_date"] = pd.to_datetime(
            temp["order_date"],
            errors="coerce"
        )

        temp = temp.dropna(
            subset=["order_date"]
        )

        if not temp.empty:

            temp["month"] = (
                temp["order_date"]
                .dt.to_period("M")
            )

            monthly_sales = (
                temp.groupby("month")["sales"]
                .sum()
            )

            if not monthly_sales.empty:

                recommendations["insights"].append(
                    f"📅 Highest sales month: "
                    f"{monthly_sales.idxmax()}"
                )

                recommendations["insights"].append(
                    "📈 Monthly sales trend available."
                )

    # ------------------------------------------
    # Customer Spending
    # ------------------------------------------

    if {"customer_id", "sales"}.issubset(df_norm.columns):

        customer_sales = (
            df_norm.groupby("customer_id")["sales"]
            .sum()
            .sort_values(ascending=False)
        )

        if not customer_sales.empty:

            recommendations["insights"].append(
                f"👤 Highest spending customer generated "
                f"{customer_sales.iloc[0]:,.2f} in sales."
            )

    # ------------------------------------------
    # Inventory
    # ------------------------------------------

    if "inventory" in df_norm.columns:

        median_inventory = (
            df_norm["inventory"].median()
        )

        low_inventory = (
            df_norm["inventory"] < median_inventory
        ).sum()

        recommendations["insights"].append(
            f"📦 {low_inventory} item(s) are below "
            f"the median inventory."
        )

    # ------------------------------------------
    # Discount
    # ------------------------------------------

    if "discount" in df_norm.columns:

        high_discount = (
            df_norm["discount"] >=
            df_norm["discount"].quantile(0.90)
        ).sum()

        recommendations["insights"].append(
            f"🎯 {high_discount} product(s) have "
            f"unusually high discounts."
        )

    # -------- Continue in File 2.4 --------
        # ------------------------------------------
    # Ratings
    # ------------------------------------------

    if "rating" in df_norm.columns:
    
     if pd.api.types.is_numeric_dtype(df_norm["rating"]):

        recommendations["insights"].append(
            f"⭐ Average rating: {df_norm['rating'].mean():.2f}"
        )

     else:

        top_rating = (
            df_norm["rating"]
            .dropna()
            .astype(str)
            .mode()
        )

        if not top_rating.empty:

            recommendations["insights"].append(
                f"⭐ Most common content rating: {top_rating.iloc[0]}"
            )
    # ------------------------------------------
    # Salary
    # ------------------------------------------

    if "salary" in df_norm.columns:

        recommendations["insights"].append(
            f"💼 Average salary: {df_norm['salary'].mean():,.2f}"
        )

    # ------------------------------------------
    # Age
    # ------------------------------------------

    if "age" in df_norm.columns:

        recommendations["insights"].append(
            f"👥 Average age: {df_norm['age'].mean():.1f} years"
        )

    # ------------------------------------------
    # Revenue
    # ------------------------------------------

    if "revenue" in df_norm.columns:

        recommendations["insights"].append(
            f"💵 Total revenue: {df_norm['revenue'].sum():,.2f}"
        )

    # ------------------------------------------
    # Profit
    # ------------------------------------------

    if "profit" in df_norm.columns:

        recommendations["insights"].append(
            f"💹 Total profit: {df_norm['profit'].sum():,.2f}"
        )

    # ------------------------------------------
    # Top Brand
    # ------------------------------------------

    if {"brand", "sales"}.issubset(df_norm.columns):

        brand_sales = (
            df_norm.groupby("brand")["sales"]
            .sum()
            .sort_values(ascending=False)
        )

        if not brand_sales.empty:

            recommendations["insights"].append(
                f"👕 Top-performing brand: {brand_sales.index[0]}"
            )

    # ------------------------------------------
    # Department Salary
    # ------------------------------------------

    if {"department", "salary"}.issubset(df_norm.columns):

        department_salary = (
            df_norm.groupby("department")["salary"]
            .mean()
            .sort_values(ascending=False)
        )

        if not department_salary.empty:

            recommendations["insights"].append(
                f"🏢 Highest average salary department: "
                f"{department_salary.index[0]}"
            )

    # ------------------------------------------
    # Attendance
    # ------------------------------------------

    if "attendance" in df_norm.columns:

        recommendations["insights"].append(
            f"📚 Average attendance: "
            f"{df_norm['attendance'].mean():.2f}%"
        )

    # ------------------------------------------
    # Diagnosis
    # ------------------------------------------

    if "diagnosis" in df_norm.columns:

        diagnosis_mode = df_norm["diagnosis"].mode(dropna=True)

        if not diagnosis_mode.empty:

            recommendations["insights"].append(
                f"🩺 Most common diagnosis: "
                f"{diagnosis_mode.iloc[0]}"
            )

    # ------------------------------------------
    # Education
    # ------------------------------------------

    if "marks" in df_norm.columns:

        recommendations["insights"].append(
            f"🎓 Average marks: {df_norm['marks'].mean():.2f}"
        )

    if "cgpa" in df_norm.columns:

        recommendations["insights"].append(
            f"🎓 Average CGPA: {df_norm['cgpa'].mean():.2f}"
        )

    # ------------------------------------------
    # Entertainment
    # ------------------------------------------

    if "release_year" in df_norm.columns:

        latest_year = df_norm["release_year"].max()

        recommendations["insights"].append(
            f"🎬 Latest release year in dataset: "
            f"{latest_year}"
        )

    # ------------------------------------------
    # Finance
    # ------------------------------------------

    if {"revenue", "expense"}.issubset(df_norm.columns):

        net_profit = (
            df_norm["revenue"].sum()
            - df_norm["expense"].sum()
        )

        recommendations["insights"].append(
            f"💰 Estimated net profit: "
            f"{net_profit:,.2f}"
        )

    # ------------------------------------------
    # Banking
    # ------------------------------------------

    if "balance" in df_norm.columns:

        recommendations["insights"].append(
            f"🏦 Average account balance: "
            f"{df_norm['balance'].mean():,.2f}"
        )

    if "credit_score" in df_norm.columns:

        recommendations["insights"].append(
            f"📊 Average credit score: "
            f"{df_norm['credit_score'].mean():.1f}"
        )

    # ==========================================
    # DEFAULT
    # ==========================================

    if not recommendations["kpis"]:
        recommendations["kpis"].append("Dataset Overview")

    if not recommendations["charts"]:
        recommendations["charts"].append("Column Distribution")

    if not recommendations["insights"]:
        recommendations["insights"].append(
            "Explore the dataset to identify business opportunities."
        )

    # ------------------------------------------
    # Remove Duplicate Recommendations
    # ------------------------------------------

    recommendations["kpis"] = list(
        dict.fromkeys(recommendations["kpis"])
    )

    recommendations["charts"] = list(
        dict.fromkeys(recommendations["charts"])
    )

    recommendations["insights"] = list(
        dict.fromkeys(recommendations["insights"])
    )

    return recommendations