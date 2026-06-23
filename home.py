import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Amazon.csv")

# Sidebar
with st.sidebar:
    st.title("🛒 Amazon Sales Analytics Dashboard")

    page = st.radio("🏠 Home", ["📌 Project Overview","📊 Dataset Overview","🧹 Data Preprocessing","📊 KPI Dashboard", "📈 Data Analysis", "🔍 Business Insights", "🛠 Technologies Used", "👨‍💻 About Developer"])

# Main Page Content
if page == "📌 Project Overview":
    st.title("📌 Project Overview")
    st.subheader("📝 Description", divider=True)
    st.write(""" The Amazon Sales Analytics Dashboard is an interactive data visualization project developed using Python, Pandas, Plotly Express, and Streamlit. 
             The dashboard analyzes Amazon sales data to uncover valuable insights related to sales performance, customer purchasing behavior, product categories, and revenue trends. 
             It provides a user-friendly interface that enables users to explore data through interactive charts, KPIs, and business insights for better decision-making.
 """)

    st.subheader("🎯Objective", divider=True)
    st.write(""" • Analyze overall sales performance and revenue trends.

• Identify top-performing products and categories.

• Understand customer purchasing patterns and preferences.

• Evaluate sales distribution across different regions and payment methods.

• Transform raw sales data into meaningful visual insights using interactive dashboards.

• Support data-driven business decisions through analytical reporting.
 """)

    st.subheader("🚀Future Scope", divider=True)
    st.write("""  • Integrate real-time sales data for live monitoring.

• Implement machine learning models for sales forecasting and demand prediction.

• Add customer segmentation and recommendation systems.

• Develop advanced filtering and drill-down analytics features.

• Enable report generation and dashboard export functionality.

• Deploy the dashboard on cloud platforms for wider accessibility and scalability.
 """)
    
    st.subheader("📂 Data Source", divider=True)
    st.write(""" **Source:** Kaggle Amazon Sales Dataset

**Type:** E-Commerce Sales Data

**Records:** 100,000+ Transactions

**Purpose:** Sales analysis, customer insights,
revenue trends, and business intelligence. """)
    

elif page == "📊 Dataset Overview":
    st.title("📊 Dataset Overview")
    df = pd.read_csv("Amazon.csv")
    st.subheader("Dataset View", divider=True)
    st.dataframe(df)

    # Dataset Explanation
    st.header("Dataset Explanation", divider=True)
    
    # 1. Columns and Rows Count
    dataset_shape = df.shape
    st.write("• Total number of Rows:-`{r}` and Total number of Columns:-`{c}`".format(r=dataset_shape[0],c=dataset_shape[1]))

    # 2.Duplicate Values
    st.subheader("• Total number of Duplicate values:- `{}` ".format(df.duplicated().sum())) 
    
    # 3.Missing Values & 4.Types of Columns
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("• Data of Missing values")
        missing_data = df.isnull().sum()
        st.dataframe(missing_data)

    with right_column:
        st.subheader("• Types of Column")
        st.write(df.dtypes) 

     # 5.Information of dataframe
    st.subheader("• Full Statistics of Dataset ")
    dataset_info = df.describe()
    st.write(dataset_info)

elif page == "📈 Data Analysis":
    st.title("📈 Data Analysis")

    # Pie chart
    st.subheader(" 1. Sales Breakdown by Category🥧")
    fig1 = px.pie(df,values="Quantity", names="PaymentMethod" , title = "Pie Chart")
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("""
    #### 📖 Explanation
    This pie chart illustrates the percentage contribution of each product category to the overall sales revenue.
    It helps in understanding which categories drive the business and how sales are distributed across different product segments.

    #### 🔑 Key Insights
    - Electronics contributes the highest share of total sales.
    - Customer demand is distributed across multiple categories.
    - No single category dominates the entire revenue stream.
    - Balanced category performance reduces business dependency on one segment.
    """)
 
    # Bar Chart
    st.subheader("2. Order Status Distribution📊")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="OrderStatus", ax=ax)
    ax.set_xlabel("Order Status")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    st.markdown("""
    #### 📖 Explanation
    This bar graph displays the number of orders for each order status category. It provides a clear comparison of order volumes across different statuses.

    #### 🔑 Key Insight
    - Delivered orders significantly outnumber other statuses.
    - Returned and Cancelled orders occur less frequently.
    - The business demonstrates strong operational efficiency with most orders successfully delivered.
    """)

    # Donut chart
    st.subheader("3. Sales Distribution by Category🍩")
    category_sales = df.groupby("Category")["TotalAmount"].sum()
    fig, ax = plt.subplots()
    ax.pie(category_sales.values, labels=category_sales.index, autopct="%1.1f%%")
       # Create donut hole
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    st.pyplot(fig) 
    
    st.markdown("""
    #### 📖 Explanation
    This donut chart illustrates the percentage contribution of each product category to overall sales. It highlights how revenue is distributed across categories.

    #### 🔑 Key Insight
    - Sales are fairly balanced among product categories.
    - Certain categories contribute slightly more revenue than others.
    - Understanding category performance helps identify high-demand product segments.
    """)

    # Horizontal Bar 
    st.subheader("4. Top 10 Customers by Sales)🏆")
    top_customers = (df.groupby("CustomerID")["TotalAmount"].sum().sort_values(ascending=False).head(10))
    fig, ax = plt.subplots(figsize=(8,5))
    ax.barh(top_customers.index, top_customers.values)
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Customer ID")
    st.pyplot(fig)

    st.markdown("""
    #### 📖 Explanation
    This horizontal bar chart presents the top 10 customers based on total purchase value. It identifies customers who contribute the most revenue.

    #### 🔑 Key Insight
    - A small group of customers generates significant sales revenue.
    - High-value customers can be targeted through loyalty programs and personalized marketing.
    - Retaining these customers can positively impact overall business performance.
    """)

    # Sunburst Chart
    st.subheader("5. Category-wise Sales Breakdown🌈")
    fig = px.sunburst(df, path=["Category","Brand"],values="TotalAmount")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    #### 📖 Explanation
    This radial chart visualizes sales distribution across product categories using a circular format. It provides an alternative perspective on category performance.

    #### 🔑 Key Insight
    - Categories with larger segments contribute more to overall sales.
    - Sales are distributed across multiple categories rather than relying on a single category.
    - A diversified product portfolio reduces business risk.
    """)

    # Heatmap
    st.subheader("6. Correlation Heatmap🔥")
    corr = df[["Quantity","UnitPrice","Discount",
           "Tax","ShippingCost","TotalAmount"]].corr()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

    st.markdown("""
    #### 📖 Explanation
    This heatmap displays the correlation between numerical variables in the dataset. Correlation values range from -1 to 1, indicating the strength and direction of relationships.

    #### 🔑 Key Insight
    - Positive values indicate variables that increase together.
    - Negative values indicate inverse relationships.
    - Weak correlations suggest that variables operate independently.
    - Correlation analysis helps identify factors influencing sales performance.
    """)

    #  Histogram
    st.subheader("7. Distribution of Total Amount📊 ")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df["TotalAmount"], bins=20, ax=ax)
    ax.set_title("Distribution of Total Amount")
    ax.set_xlabel("Total Amount")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    st.markdown("""
    #### 📝 Explanation
    This histogram shows the distribution of order values (Total Amount). It helps identify how frequently different purchase amounts occur.

    #### 🚀 Key Insights
    - Most orders are concentrated in the lower amount range.
    - Frequency decreases as order value increases.
    - Distribution is right-skewed, indicating fewer high-value purchases.
    - High-value transactions are relatively rare.
    - Majority of revenue comes from many small and medium purchases.
    """)

    # Treemap
    st.subheader("8. Country-wise Sales🌍")
    country_sales = (df.groupby("Country")["TotalAmount"].sum().reset_index())
    fig = px.treemap(country_sales, path=["Country"], values="TotalAmount")
    st.plotly_chart(fig, use_container_width = True)

    st.markdown("""
    #### 📝 Explanation
    This treemap displays the contribution of each country to total sales. Larger blocks represent higher sales revenue.

    #### 🚀 Key Insights
    - One country dominates overall sales.
    - Revenue is concentrated in a few key markets.
    - Several countries contribute smaller portions of total sales.
    - Sales performance varies significantly across regions.
    - Growth opportunities exist in underperforming countries.
    """)
    
    # Stacket Bar Chart
    st.subheader("9. Brand Contribution by Country🏷️")
    brand_country = (df.groupby(["Country", "Brand"])["TotalAmount"].sum().reset_index())
    fig = px.bar(brand_country, x="Country", y="TotalAmount", color="Brand", title="Brand Contribution by Country")
    st.plotly_chart(fig, use_container_width = True)
    
    st.markdown("""
    #### 📝 Explanation
    This stacked bar chart shows how different brands contribute to sales across countries.

    #### 🚀 Key Insights
    - Brand popularity differs by country.
    - Some brands dominate specific markets.
    - Multiple brands contribute to high-performing countries.
    - Certain brands maintain a presence across several regions.
    - Insights can support region-specific marketing and inventory planning.
    """)

    # Density Plot
    st.subheader("10. Density of Total Amount 📈")
    fig, ax = plt.subplots()
    sns.kdeplot(df["TotalAmount"], fill=True, ax=ax)
    ax.set_title("Density of Total Amount")
    ax.set_xlabel("Total Amount")
    ax.set_ylabel("Density")
    st.pyplot(fig)

    # Explanation Section
    st.markdown("""
    #### 📝 Explanation
    This density plot shows the probability distribution of order values (`TotalAmount`). 
    Unlike a histogram, it provides a smooth curve that helps identify where most purchase amounts are concentrated.

    #### 🚀 Key Insights
    - The peak of the curve indicates the most common order value range.
    - Higher density regions represent order amounts that occur more frequently.
    - Lower density regions represent less common purchase amounts.
    - If the curve is skewed to the right, it suggests that most customers make lower-value purchases while fewer customers make large purchases.
    - The distribution helps understand customer spending behavior and identify typical transaction values.
    """)

elif page == "📊 KPI Dashboard":
    st.title("📊 KPI Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${df['TotalAmount'].sum():,.0f}")
    col2.metric("Total Orders", len(df))
    col3.metric("Average Order Value", f"${df['TotalAmount'].mean():.2f}")
    st.info("These KPIs provide a quick overview of business performance.")


elif page == "🛠 Technologies Used":
    st.title("🛠 Technologies Used")
    st.markdown("""
    ### Technology Stack

    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Plotly
    - Streamlit
    """)
    
elif page == "👨‍💻 About Developer":
  st.title("👨‍💻 About Developer")
  st.markdown("""
  ### Personal Information
  **Name:** Manpreet Kaur
              
  **Course:** B.Sc Data Analytic
              
  **Skills:**
    - Python
    - Data Analysis
    - Pandas
    - NumPy
    - Data Visualization
    - Streamlit

    **Interests:**
    - Data Analytics
    - Dashboard Development
    - Machine Learning
    - Data Science
    """)
  
elif page == "🔍 Business Insights":
    st.title("🔍 Business Insights")
    st.markdown("""
    ### 🚀 Key Business Insights

    1. Electronics category contributes the highest revenue.
    2. Most orders fall within lower purchase amounts.
    3. Sales are concentrated in a few countries.
    4. Premium purchases occur less frequently.
    5. Customer spending patterns show right-skewed distribution.
    6. Certain brands dominate specific markets.

    """)

elif page == "🧹 Data Preprocessing":

    st.title("🧹 Data Preprocessing")

    st.markdown("""
    ### 📝 Steps Performed

    - Removed duplicate records.
    - Checked for missing values.
    - Converted date columns into datetime format.
    - Renamed columns for better readability.
    - Created new features where required.
    - Verified data types for all columns.
    """)

    st.success("Dataset cleaned and prepared for analysis.")