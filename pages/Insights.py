import mysql.connector
import streamlit as st
import pandas as pd

# Display the title in Streamlit
st.title('Insights Analysis')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",         # Hostname of the MySQL server
    user="root",              # Your MySQL username
    password="Dinesh2802",    # Your MySQL password
    database="retail_orders"  # Name of the database
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Assuming 'df_products' has product details
# Assuming 'df_customers' has customer location info

# Fetch the total Sales Per Product Category
cursor.execute('''
    SELECT p.category, SUM(o.sale_price) AS total_sales
    FROM df_orders o 
    JOIN df_orders p ON o.order_id = p.order_id
    GROUP BY p.category
    ORDER BY total_sales DESC;
''')

# Fetch the total Sales Per Product Category
table1 = cursor.fetchall()

# Find the Revenue per Customer Segment
cursor.execute('''
    SELECT c.segment, SUM(o.sale_price) AS total_revenue
    FROM df_orders o
    JOIN df_orders c ON o.order_id = c.order_id
    GROUP BY c.segment
    ORDER BY total_revenue DESC;
''')
# Find the Revenue per Customer Segment
table2 = cursor.fetchall()

# Fetch the Products with the Highest Discounts
cursor.execute('''
	SELECT o.state, p.product_id, AVG(o.profit) AS total_profit
    FROM df_orders o
    JOIN df_orders p ON o.product_id = p.product_id
    GROUP BY p.product_id, o.state
    ORDER BY total_profit DESC
    LIMIT 5;
''')
# Fetch the Products with the Highest Discounts
table3 = cursor.fetchall()

# Fetch to Get total sales per product category
cursor.execute('''
    SELECT c.sub_category, SUM(o.discount) AS avg_discount
    FROM df_orders o
    JOIN df_orders c ON o.order_id = c.order_id
    GROUP BY c.sub_category
    ORDER BY avg_discount DESC;
''')
# Fetch to Get total sales per product category
table4 = cursor.fetchall()


# Fetch Find the Most Profitable Region
cursor.execute('''
    SELECT r.region, r.city, SUM(o.profit) AS total_profit
    FROM df_orders o
    JOIN df_orders r ON o.product_id = r.product_id
    GROUP BY r.region, r.city
    ORDER BY total_profit DESC
    LIMIT 1;
''')

# Fetch the Most Profitable Region
table5 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_1 = pd.DataFrame(table1, columns=["category", "total_sales"])
answer_2 = pd.DataFrame(table2, columns=["segment", "total_revenue"])
answer_3 = pd.DataFrame(table3, columns=["state", "product_id", "total_profit"])
answer_4 = pd.DataFrame(table4, columns=["category", "avg_discount"])
answer_5 = pd.DataFrame(table5, columns=["region", "city", "total_profit"])

# Button to trigger query execution for different options
selected_option = st.multiselect('Select any Question', 
                                ['1.Show the total Sales Per Product Category',
                                 '2.Find the Revenue per Customer Segment',
                                 '3.Find the Products with the Highest Discounts',
                                 '4.Get total sales per product category',
                                 '5.Find the Most Profitable Region'
                                 ])

# Execute queries based on selection
if '1.Show the total Sales Per Product Category' in selected_option and st.button('Execute'):
    st.subheader('Total Sales Per Product Category')
    st.dataframe(answer_1)

elif '2.Find the Revenue per Customer Segment' in selected_option and st.button('Execute'):
    st.subheader('Revenue per Customer Segment')
    st.dataframe(answer_2)

elif '3.Find the Products with the Highest Discounts' in selected_option and st.button('Execute'):
    st.subheader('Products with the Highest Discounts')
    st.dataframe(answer_3)

elif '4.Get total sales per product category' in selected_option and st.button('Execute'):
    st.subheader('Get total sales per product category')
    st.dataframe(answer_4)

elif '5.Find the Most Profitable Region' in selected_option and st.button('Execute'):
    st.subheader('Most Profitable Region')
    st.dataframe(answer_5)


# Close the database connection
cursor.close()
conn.close()
