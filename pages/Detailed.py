import mysql.connector
import streamlit as st
import pandas as pd

# Display the title in Streamlit
st.title('Retail Order Detailed')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",         # Hostname of the MySQL server
    user="root",              # Your MySQL username
    password="Dinesh2802",    # Your MySQL password
    database="retail_orders"  # Name of the database
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Fetch the top 10 products by sales
cursor.execute('''
    SELECT product_id, SUM(sale_price) AS sales 
    FROM df_orders 
    GROUP BY product_id 
    ORDER BY sales DESC
    LIMIT 10;
''')
# Fetch the results for top 10 products by sales
table1 = cursor.fetchall()

# Find the top 5 cities with the highest profit margins
cursor.execute('''
    SELECT city, SUM(profit) AS total_profit 
    FROM df_orders 
    GROUP BY city
    ORDER BY total_profit DESC
    LIMIT 5;
''')
# Fetch the results for top 5 cities by profit margin
table2 = cursor.fetchall()

# Query to calculate total discount given for each category
cursor.execute('''
    SELECT category, SUM(discount) AS total_discount
    FROM df_orders
    GROUP BY category
    ORDER BY total_discount DESC;
''')
# Fetch the results of the query
table3 = cursor.fetchall()

# Query to calculate the average sale price per product category
cursor.execute('''
    SELECT category, AVG(sale_price) AS avg_sale_price
    FROM df_orders
    GROUP BY category
    ORDER BY avg_sale_price DESC;
''')

# Fetch the results of the query
table4 = cursor.fetchall()

# Query to find the region with the highest average sale price
cursor.execute('''
    SELECT region, AVG(sale_price) AS avg_sale_price
    FROM df_orders
    GROUP BY region
    ORDER BY avg_sale_price DESC
    LIMIT 1;
''')
# Fetch the result for the region with the highest average sale price
table5 = cursor.fetchall()

# Query to calculate total profit per category
cursor.execute('''
    SELECT category, SUM(profit) AS total_profit
    FROM df_orders
    GROUP BY category
    ORDER BY total_profit DESC;
''')
# Fetch the results for total profit per category
table6 = cursor.fetchall()

# Query to find the top 3 segments with the highest quantity of orders
cursor.execute('''
    SELECT segment, COUNT(*) AS order_count
    FROM df_orders
    GROUP BY segment
    ORDER BY order_count DESC
    LIMIT 3;
''')
# Fetch the results for the top 3 segments
table7 = cursor.fetchall()

# Query to calculate the average discount percentage per region
cursor.execute('''
    SELECT region, 
           (SUM(discount) / SUM(sale_price)) * 100 AS avg_discount_percentage
    FROM df_orders
    GROUP BY region
    ORDER BY avg_discount_percentage DESC;
''')
# Fetch the results for the average discount percentage per region
table8 = cursor.fetchall()

# Query to find the product category with the highest total profit
cursor.execute('''
    SELECT category, 
           SUM(profit) AS total_profit
    FROM df_orders
    GROUP BY category
    ORDER BY total_profit DESC
    LIMIT 1;
''')
# Fetch the result for the product category with the highest total profit
table9 = cursor.fetchall()

# Query to calculate the total revenue generated per year
cursor.execute('''
    SELECT YEAR(order_date) AS year, 
           SUM(sale_price) AS total_revenue
    FROM df_orders
    GROUP BY year
    ORDER BY year;
''')
# Fetch the result for the total revenue per year
table10 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_1 = pd.DataFrame(table1, columns=["product_id", "sales"])
answer_2 = pd.DataFrame(table2, columns=["city", "total_profit"])
answer_3 = pd.DataFrame(table3, columns=["category", "total_discount"])
answer_4 = pd.DataFrame(table4, columns=["category", "avg_sale_price"])
answer_5 = pd.DataFrame(table5, columns=["region", "avg_sale_price"])
answer_6 = pd.DataFrame(table6, columns=["category", "total_profit"])
answer_7 = pd.DataFrame(table7, columns=["segment", "order_count"])
answer_8 = pd.DataFrame(table8, columns=["region", "avg_discount_percentage"])
answer_9 = pd.DataFrame(table9, columns=["category", "total_profit"])
answer_10 = pd.DataFrame(table10, columns=["year", "total_revenue"])


# Button to trigger query execution for different options
selected_option = st.multiselect('Select any Question', 
                                ['1.Find top 10 highest revenue generating products', 
                                 '2.Find the top 5 cities with the highest profit margins',
                                 '3.Calculate the total discount given for each category',
                                 '4.Find the average sale price per product category',
                                 '5.Find the region with the highest average sale price',
                                 '6.Find the total profit per category',
                                 '7.Identify the top 3 segments with the highest quantity of orders',
                                 '8.Determine the average discount percentage given per region',
                                 '9.Find the product category with the highest total profit',
                                 '10.Calculate the total revenue generated per year'
                                 ])

# Execute queries based on selection
if '1.Find top 10 highest revenue generating products' in selected_option and st.button('Execute'):
    st.subheader('Top 10 Products by Sales')
    st.dataframe(answer_1)

elif '2.Find the top 5 cities with the highest profit margins' in selected_option and st.button('Execute'):
    st.subheader('Top 5 Cities with Highest Profit')
    st.dataframe(answer_2)

elif '3.Calculate the total discount given for each category' in selected_option and st.button('Execute'):
    st.subheader('Total Discount by Category')
    st.dataframe(answer_3)

elif '4.Find the average sale price per product category' in selected_option and st.button('Execute'):
    st.subheader('Average Sale Price by Category')
    st.dataframe(answer_4)

elif '5.Find the region with the highest average sale price' in selected_option and st.button('Execute'):
    st.subheader('Region with the Highest Average Sale Price')
    st.dataframe(answer_5)

elif '6.Find the total profit per category' in selected_option and st.button('Execute'):
    st.subheader('Total Profit by Category')
    st.dataframe(answer_6)

elif '7.Identify the top 3 segments with the highest quantity of orders' in selected_option and st.button('Execute'):
    st.subheader('Top 3 Segments by Order Quantity')
    st.dataframe(answer_7)

elif '8.Determine the average discount percentage given per region' in selected_option and st.button('Execute'):
    st.subheader('Average Discount Percentage per Region')
    st.dataframe(answer_8)

elif '9.Find the product category with the highest total profit' in selected_option and st.button('Execute'):
    st.subheader('Product Category with Highest Total Profit')
    st.dataframe(answer_9)

elif '10.Calculate the total revenue generated per year' in selected_option and st.button('Execute'):
    st.subheader('Total Revenue Generated per Year')
    st.dataframe(answer_10)

# Close the database connection
cursor.close()
conn.close()
