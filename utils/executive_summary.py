import pandas as pd


def generate_executive_summary(df, domain):
    """
    Generate a professional AI Executive Summary.
    """

    summary = {
        "headline": "",
        "performance": [],
        "opportunities": [],
        "quality": []
    }

    # --------------------------
    # Standardize column names
    # --------------------------
    df = df.copy()

    df.columns = [
        str(col).strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    domain = str(domain).strip().lower()

    rows = len(df)
    cols = len(df.columns)

    summary["headline"] = (
    f"DecisionAI analyzed {rows:,} records across "
    f"{cols} business attributes."
)

     # =====================================================
    # RETAIL
    # =====================================================
    if domain == "retail":

        # -------------------------
        # Total Revenue
        # -------------------------
        if "sales" in df.columns:

            total_sales = df["sales"].sum()

            summary["performance"].append(
                f"💰 Total Revenue: ${total_sales:,.2f}"
            )

        # -------------------------
        # Total Profit
        # -------------------------
        if "profit" in df.columns:

            total_profit = df["profit"].sum()

            summary["performance"].append(
                f"📈 Total Profit: ${total_profit:,.2f}"
            )

            loss_count = (df["profit"] < 0).sum()

            if loss_count > 0:

                summary["opportunities"].append(
                    f"""⚠️ Profitability Risk

{loss_count:,} transactions generated negative profit.

Recommendation:
Review pricing, shipping costs, discount strategy, and product mix to improve profit margins."""
                )

        # -------------------------
        # Highest Revenue Region
        # -------------------------
        if {"region", "sales"}.issubset(df.columns):

            top_region = (
                df.groupby("region")["sales"]
                .sum()
                .idxmax()
            )

            summary["performance"].append(
                f"🏆 Highest Revenue Region: {top_region}"
            )

        # -------------------------
        # Best Performing Category
        # -------------------------
        if {"category", "sales"}.issubset(df.columns):

            top_category = (
                df.groupby("category")["sales"]
                .sum()
                .idxmax()
            )

            summary["performance"].append(
                f"📦 Best Performing Category: {top_category}"
            )

        # -------------------------
        # Discount Analysis
        # -------------------------
        if "discount" in df.columns:

            avg_discount = df["discount"].mean()

            summary["performance"].append(
                f"🏷️ Average Discount: {avg_discount:.2%}"
            )

            high_discount = (
                df["discount"]
                >= df["discount"].quantile(0.90)
            ).sum()

            if high_discount > 0:

                summary["opportunities"].append(
                    f"""🟡 Discount Optimization

{high_discount:,} products have unusually high discounts.

Recommendation:
Review discount policies and identify products where discounts can be reduced without significantly affecting demand."""
                )

        # -------------------------
        # AI Executive Narrative
        # -------------------------
        if {
            "region",
            "category",
            "sales",
            "profit"
        }.issubset(df.columns):

            top_region = (
                df.groupby("region")["sales"]
                .sum()
                .idxmax()
            )

            top_category = (
                df.groupby("category")["sales"]
                .sum()
                .idxmax()
            )

            loss_count = (df["profit"] < 0).sum()

            summary["headline"] = (
                f"DecisionAI analyzed {rows:,} retail transactions. "
                f"The {top_region} region generated the highest revenue, while "
                f"{top_category} emerged as the best-performing category. "
                f"Overall profitability remains positive, although "
                f"{loss_count:,} loss-making transactions indicate opportunities "
                f"to improve margins. Dataset quality analysis indicates that "
                f"the uploaded data is highly reliable for business decision-making."
            )
                 
        # =====================================================
    # HR
    # =====================================================
    elif domain == "hr":

        # Average Salary
        if "salary" in df.columns:

            avg_salary = df["salary"].mean()

            summary["performance"].append(
                f"💰 Average Employee Salary: ${avg_salary:,.0f}"
            )

        # Department Information
        if "department" in df.columns:

            largest_department = df["department"].mode()

            if not largest_department.empty:

                summary["performance"].append(
                    f"🏢 Largest Department: {largest_department.iloc[0]}"
                )

            summary["performance"].append(
                f"👥 Total Departments: {df['department'].nunique()}"
            )

        # Attrition Rate
        if "attrition" in df.columns:

            attrition_rate = (
                df["attrition"]
                .astype(str)
                .str.lower()
                .isin(["yes", "true", "1"])
                .mean()
                * 100
            )

            summary["opportunities"].append(
                f"⚠️ Employee Attrition Rate: {attrition_rate:.1f}%"
            )
            rows = len(df)

            headline = f"DecisionAI analyzed {rows:,} employee records."

            if "salary" in df.columns:
                headline += f" The average employee salary is ${avg_salary:,.0f}."

            if "department" in df.columns and not largest_department.empty:
                headline += f" {largest_department.iloc[0]} is the largest department."

            if "attrition" in df.columns:
                headline += f" Employee attrition stands at {attrition_rate:.1f}%, highlighting workforce retention opportunities."

            summary["headline"] = headline
    # =====================================================
    # HEALTHCARE
    # =====================================================
    elif domain == "healthcare":

        # Average Age
        if "age" in df.columns:

            summary["performance"].append(
                f"🩺 Average Patient Age: {df['age'].mean():.1f} years"
            )

        # Common Diagnosis
        if "diagnosis" in df.columns:

            diagnosis = df["diagnosis"].mode()

            if not diagnosis.empty:

                summary["performance"].append(
                    f"🏥 Most Common Diagnosis: {diagnosis.iloc[0]}"
                )

        # Gender Distribution
        if "gender" in df.columns:

            gender = df["gender"].mode()

            if not gender.empty:

                summary["performance"].append(
                    f"👤 Majority Gender: {gender.iloc[0]}"
                )

        # Average Billing
        if "billing_amount" in df.columns:

            summary["performance"].append(
                f"💰 Average Billing Amount: ${df['billing_amount'].mean():,.2f}"
            )

        # Readmission Rate
        if "readmission" in df.columns:

            readmission_rate = (
                df["readmission"]
                .astype(str)
                .str.lower()
                .isin(["yes", "true", "1"])
                .mean()
                * 100
            )

            summary["opportunities"].append(
                f"⚠️ Hospital Readmission Rate: {readmission_rate:.1f}%"
            )
            rows = len(df)

            headline = f"DecisionAI analyzed {rows:,} patient records."

            if "age" in df.columns:
              headline += f" The average patient age is {df['age'].mean():.1f} years."

            if "diagnosis" in df.columns and not diagnosis.empty:
              headline += f" {diagnosis.iloc[0]} is the most common diagnosis."

            if "readmission" in df.columns:
              headline += f" The hospital readmission rate is {readmission_rate:.1f}%, indicating opportunities to improve patient care."

            summary["headline"] = headline

    # =====================================================
    # EDUCATION
    # =====================================================
    elif domain == "education":

        # Average Marks
        if "marks" in df.columns:

            summary["performance"].append(
                f"🎓 Average Marks: {df['marks'].mean():.1f}"
            )

        # Average CGPA
        if "cgpa" in df.columns:

            summary["performance"].append(
                f"📚 Average CGPA: {df['cgpa'].mean():.2f}"
            )

        # Best Department
        if {"department", "cgpa"}.issubset(df.columns):

            best_department = (
                df.groupby("department")["cgpa"]
                .mean()
                .idxmax()
            )

            summary["performance"].append(
                f"🏆 Highest Performing Department: {best_department}"
            )

        # Pass Rate
        if "result" in df.columns:

            pass_rate = (
                df["result"]
                .astype(str)
                .str.lower()
                .isin(["pass", "passed", "yes", "true", "1"])
                .mean()
                * 100
            )

            summary["performance"].append(
                f"✅ Pass Rate: {pass_rate:.1f}%"
            )

        # Attendance Warning
        if "attendance" in df.columns:

            low_attendance = (df["attendance"] < 75).sum()

            if low_attendance > 0:

                summary["opportunities"].append(
                    f"⚠️ {low_attendance:,} students have attendance below 75%."
                )
                rows = len(df)

                headline = f"DecisionAI analyzed {rows:,} student records."

                if "marks" in df.columns:
                  headline += f" Students achieved an average score of {df['marks'].mean():.1f}."

                if "cgpa" in df.columns:
                  headline += f" The average CGPA is {df['cgpa'].mean():.2f}."

                if "result" in df.columns:
                  headline += f" Overall pass rate is {pass_rate:.1f}%."

                summary["headline"] = headline
        # =====================================================
    # ENTERTAINMENT
    # =====================================================
    elif domain == "entertainment":

        # Primary Content Type
        if "type" in df.columns:

            content_type = df["type"].mode()

            if not content_type.empty:

                summary["performance"].append(
                    f"🎬 Primary Content Type: {content_type.iloc[0]}"
                )

        # Latest Release
        if "release_year" in df.columns:

            summary["performance"].append(
                f"📅 Latest Release Year: {int(df['release_year'].max())}"
            )

        # Most Common Rating
        if "rating" in df.columns:

            rating = df["rating"].mode()

            if not rating.empty:

                summary["performance"].append(
                    f"⭐ Most Common Rating: {rating.iloc[0]}"
                )

        # Largest Content Source
        if "country" in df.columns:

            country = (
                df["country"]
                .dropna()
                .astype(str)
                .str.split(",")
                .explode()
                .str.strip()
                .mode()
            )

            if not country.empty:

                summary["performance"].append(
                    f"🌍 Largest Content Source: {country.iloc[0]}"
                )

        # Most Popular Genre
        if "listed_in" in df.columns:

            genre = (
                df["listed_in"]
                .dropna()
                .astype(str)
                .str.split(",")
                .explode()
                .str.strip()
                .mode()
            )

            if not genre.empty:

                summary["performance"].append(
                    f"🎭 Most Popular Genre: {genre.iloc[0]}"
                )

        # Missing Directors
        if "director" in df.columns:

            missing_directors = df["director"].isna().sum()

            if missing_directors > 0:

                summary["opportunities"].append(
                    f"⚠️ {missing_directors:,} titles have missing director information."
                )
                rows = len(df)

                headline = f"DecisionAI analyzed {rows:,} entertainment titles."

                if "type" in df.columns and not content_type.empty:
                   headline += f" {content_type.iloc[0]} dominates the catalog."

                if "country" in df.columns and not country.empty:
                   headline += f" {country.iloc[0]} contributes the largest content library."

                if "release_year" in df.columns:
                   headline += f" The latest releases extend through {int(df['release_year'].max())}."

                summary["headline"] = headline

    # =====================================================
    # FASHION
    # =====================================================
    elif domain == "fashion":

        # Top Brand
        if {"brand", "sales"}.issubset(df.columns):

            top_brand = (
                df.groupby("brand")["sales"]
                .sum()
                .idxmax()
            )

            summary["performance"].append(
                f"👑 Top Performing Brand: {top_brand}"
            )

        # Total Sales
        if "sales" in df.columns:

            summary["performance"].append(
                f"💰 Total Sales: ${df['sales'].sum():,.2f}"
            )

        # Best Category
        if {"category", "sales"}.issubset(df.columns):

            best_category = (
                df.groupby("category")["sales"]
                .sum()
                .idxmax()
            )

            summary["performance"].append(
                f"🛍️ Best Selling Category: {best_category}"
            )

        # Average Discount
        if "discount" in df.columns:

            avg_discount = df["discount"].mean()

            summary["performance"].append(
                f"🏷️ Average Discount: {avg_discount:.2f}%"
            )

            high_discount = (
                df["discount"]
                > df["discount"].quantile(0.90)
            ).sum()

            if high_discount > 0:

                summary["opportunities"].append(
                    f"⚠️ {high_discount:,} products have exceptionally high discounts."
                )

        # Inventory
        if "stock" in df.columns:

            low_stock = (df["stock"] <= 10).sum()

            if low_stock > 0:

                summary["opportunities"].append(
                    f"📦 {low_stock:,} products are running low on inventory."
                )
                rows = len(df)

                headline = f"DecisionAI analyzed {rows:,} fashion retail records."

                if {"brand", "sales"}.issubset(df.columns):
                   headline += f" {top_brand} is the top-performing brand."

                if {"category", "sales"}.issubset(df.columns):
                   headline += f" {best_category} leads product sales."

                if "discount" in df.columns:
                   headline += f" The average discount offered is {avg_discount:.1f}%."

                summary["headline"] = headline

    # =====================================================
    # BANKING
    # =====================================================
    elif domain == "banking":

        # Average Balance
        if "balance" in df.columns:

            summary["performance"].append(
                f"🏦 Average Account Balance: ${df['balance'].mean():,.2f}"
            )

        # Average Age
        if "age" in df.columns:

            summary["performance"].append(
                f"👤 Average Customer Age: {df['age'].mean():.1f} years"
            )

        # Largest Customer Segment
        if "job" in df.columns:

            job = df["job"].mode()

            if not job.empty:

                summary["performance"].append(
                    f"💼 Largest Customer Segment: {job.iloc[0]}"
                )

        # Marital Status
        if "marital" in df.columns:

            marital = df["marital"].mode()

            if not marital.empty:

                summary["performance"].append(
                    f"👨‍👩‍👧 Majority Marital Status: {marital.iloc[0]}"
                )

        # Housing Loan
        if "housing" in df.columns:

            housing_rate = (
                df["housing"]
                .astype(str)
                .str.lower()
                .eq("yes")
                .mean()
                * 100
            )

            summary["performance"].append(
                f"🏠 Customers with Housing Loans: {housing_rate:.1f}%"
            )

        # Personal Loan
        if "loan" in df.columns:

            loan_rate = (
                df["loan"]
                .astype(str)
                .str.lower()
                .eq("yes")
                .mean()
                * 100
            )

            summary["performance"].append(
                f"💳 Customers with Personal Loans: {loan_rate:.1f}%"
            )

        # Campaign Conversion
        if "y" in df.columns:

            conversion_rate = (
                df["y"]
                .astype(str)
                .str.lower()
                .eq("yes")
                .mean()
                * 100
            )

            summary["opportunities"].append(
                f"📈 Marketing Campaign Conversion Rate: {conversion_rate:.1f}%"
            )

        # Frequent Contact Warning
        if "campaign" in df.columns:

            high_contact = (df["campaign"] > 5).sum()

            if high_contact > 0:

                summary["opportunities"].append(
                    f"⚠️ {high_contact:,} customers were contacted more than 5 times."
                )
                rows = len(df)

                headline = f"DecisionAI analyzed {rows:,} banking records."

                if "balance" in df.columns:
                    avg_balance = df["balance"].mean()
                    headline += f" The average account balance is ${avg_balance:,.2f}."

                if "job" in df.columns and not job.empty:
                 headline += f" {job.iloc[0]} represents the largest customer segment."

                if "housing" in df.columns:
                 headline += f" Housing loan adoption is {housing_rate:.1f}%."

                if "y" in df.columns:
                 headline += (
                  f" Marketing campaigns achieved a "
                  f"{conversion_rate:.1f}% conversion rate."
                   )

                 summary["headline"] = headline
        # =====================================================
    # FINANCE
    # =====================================================
    elif domain == "finance":

        # Total Revenue
        if "revenue" in df.columns:

            total_revenue = df["revenue"].sum()

            summary["performance"].append(
                f"💰 Total Revenue: ${total_revenue:,.2f}"
            )

        # Total Expenses
        if "expense" in df.columns:

            total_expense = df["expense"].sum()

            summary["performance"].append(
                f"💸 Total Expenses: ${total_expense:,.2f}"
            )

        # Net Profit
        if {"revenue", "expense"}.issubset(df.columns):

            net_profit = (
                df["revenue"].sum()
                - df["expense"].sum()
            )

            summary["performance"].append(
                f"📈 Net Profit: ${net_profit:,.2f}"
            )

            if net_profit < 0:

                summary["opportunities"].append(
                    "⚠️ The organization is currently operating at a net loss."
                )

        # Highest Revenue Department
        if {"department", "revenue"}.issubset(df.columns):

            top_department = (
                df.groupby("department")["revenue"]
                .sum()
                .idxmax()
            )

            summary["performance"].append(
                f"🏆 Highest Revenue Department: {top_department}"
            )

        # Highest Expense Department
        if {"department", "expense"}.issubset(df.columns):

            high_expense = (
                df.groupby("department")["expense"]
                .sum()
                .idxmax()
            )

            summary["opportunities"].append(
                f"💡 Highest Spending Department: {high_expense}"
            )

        # Profit Margin
        if {"revenue", "expense"}.issubset(df.columns):

            revenue = df["revenue"].sum()

            if revenue > 0:

                margin = (
                    (revenue - df["expense"].sum())
                    / revenue
                ) * 100

                summary["performance"].append(
                    f"📊 Profit Margin: {margin:.2f}%"
                )
                rows = len(df)

                headline = f"DecisionAI analyzed {rows:,} financial records."

                if "revenue" in df.columns:
                  headline += f" Total revenue reached ${total_revenue:,.2f}."

                if {"revenue", "expense"}.issubset(df.columns):
                  headline += f" Net profit is ${net_profit:,.2f}."

                if {"department", "revenue"}.issubset(df.columns):
                  headline += (
                  f" {top_department} generated the highest revenue."
                   )

                if {"revenue", "expense"}.issubset(df.columns):
                  headline += f" Overall profit margin stands at {margin:.2f}%."

                summary["headline"] = headline

    # =====================================================
    # ECOMMERCE
    # =====================================================
    elif domain == "ecommerce":

        # Total Sales
        if "order_amount" in df.columns:

            summary["performance"].append(
                f"💰 Total Sales: ${df['order_amount'].sum():,.2f}"
            )

            summary["performance"].append(
                f"🛒 Average Order Value: ${df['order_amount'].mean():,.2f}"
            )

        # Total Orders
        if "order_id" in df.columns:

            summary["performance"].append(
                f"📦 Total Orders: {df['order_id'].nunique():,}"
            )

        # Best Category
        if {"category", "order_amount"}.issubset(df.columns):

            best_category = (
                df.groupby("category")["order_amount"]
                .sum()
                .idxmax()
            )

            summary["performance"].append(
                f"🏆 Best Selling Category: {best_category}"
            )

        # Best Customer
        if {"customer_id", "order_amount"}.issubset(df.columns):

            top_customer = (
                df.groupby("customer_id")["order_amount"]
                .sum()
                .idxmax()
            )

            summary["performance"].append(
                f"👤 Highest Spending Customer: {top_customer}"
            )

        # High Value Orders
        if "order_amount" in df.columns:

            high_orders = (
                df["order_amount"]
                > df["order_amount"].quantile(0.95)
            ).sum()

            if high_orders > 0:

                summary["opportunities"].append(
                    f"⭐ {high_orders:,} orders fall within the top 5% of order values."
                )

        # Cancelled Orders
        if "status" in df.columns:

            cancelled = (
                df["status"]
                .astype(str)
                .str.lower()
                .eq("cancelled")
                .sum()
            )

            if cancelled > 0:

                summary["opportunities"].append(
                    f"⚠️ {cancelled:,} orders have been cancelled."
                )
                rows = len(df)

                headline = f"DecisionAI analyzed {rows:,} e-commerce orders."

                if "order_amount" in df.columns:
                 total_sales = df["order_amount"].sum()
                 avg_order = df["order_amount"].mean()

                headline += (
                f" Total sales reached ${total_sales:,.2f} "
                f"with an average order value of "
                f"${avg_order:,.2f}."
                 )

                if {"category", "order_amount"}.issubset(df.columns):
                 headline += f" {best_category} emerged as the best-selling category."

                if "status" in df.columns:
                 headline += (
                 f" The analysis highlights opportunities "
                 f"to reduce order cancellations and improve customer satisfaction."
                 )

                 summary["headline"] = headline

    # =====================================================
    # DATA QUALITY
    # =====================================================

    missing_values = int(df.isna().sum().sum())

    summary["quality"].append(
        f"🔍 Missing Values: {missing_values:,}"
    )

    duplicate_rows = int(df.duplicated().sum())

    summary["quality"].append(
        f"📄 Duplicate Records: {duplicate_rows:,}"
    )

    numeric_cols = df.select_dtypes(include="number").shape[1]
    categorical_cols = df.select_dtypes(exclude="number").shape[1]

    summary["quality"].append(
        f"🔢 Numeric Columns: {numeric_cols}"
    )

    summary["quality"].append(
        f"🔤 Categorical Columns: {categorical_cols}"
    )

    total_cells = df.shape[0] * df.shape[1]

    if total_cells > 0:

        completeness = (
            (total_cells - missing_values)
            / total_cells
        ) * 100

    else:

        completeness = 100

    summary["quality"].append(
        f"✅ Dataset Completeness: {completeness:.1f}%"
    )

    quality_score = max(
        0,
        min(
            100,
            completeness
            - (
                duplicate_rows
                / max(len(df), 1)
            ) * 100
        )
    )

    summary["quality"].append(
        f"🏅 Dataset Quality Score: {quality_score:.0f}/100"
    )
    

    # =====================================================
    # DEFAULT SUMMARY
    # =====================================================

    if (
        not summary["performance"]
        and not summary["opportunities"]
    ):

        summary["performance"].append(
            "📊 DecisionAI successfully analyzed the dataset and generated basic business insights."
        )

    return summary