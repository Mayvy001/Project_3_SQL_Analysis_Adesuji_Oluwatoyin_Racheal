INPUT [1]
import pandas as pd
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")

Setting Up the Database
import pandas as pd
import sqlite3

# Read Excel file
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")

# Create SQLite database in memory
connection = sqlite3.connect(':memory:')

# Save DataFrame as a SQL table
df.to_sql('sales_data', connection, index=False, if_exists='replace')


# Test the connection by querying the first few rows of the table
INPUT [2]

query = """
SELECT *
FROM sales_data
LIMIT 5
"""
result = pd.read_sql_query(query, connection)
print(result)

RESULT [2]

 OrderID       Date CustomerID  ... CouponCode  ReferralSource  TotalPrice
0  ORD200000 2023-01-04     C72649  ...     SAVE10       Instagram     2853.10
1  ORD200001 2024-08-23     C75739  ...     SAVE10        Referral      302.70
2  ORD200002 2024-02-27     C81728  ...   FREESHIP           Email     2753.40
3  ORD200003 2023-10-15     C33540  ...     SAVE10        Facebook      273.19
4  ORD200004 2025-05-08     C81840  ...     SAVE10           Email     2504.04

INPUT [3]
How many orders are there in the dataset?

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
print(df.head())  
query_1 = """
SELECT COUNT(*) AS Total_Orders
FROM sales_data
"""
print(pd.read_sql_query(query_1, connection))

RESULT [3]

Total_Orders
0          1200


**Section 1: Revenue Analysis**

INPUT [4]
**1. What is the total revenue generated from all orders?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
print(df.head())  
query_1 = """
SELECT SUM(TotalPrice) AS Total_Revenue
FROM sales_data
"""
print(pd.read_sql_query(query_1, connection))

RESULT [4]

 Total_Revenue
0     1264761.96

FINDINGS:
The analysis revealed that the business generated a total revenue of **1,264,761.96** during the period covered by the dataset. 
This indicates strong sales performance and reflects the overall value generated from customer transactions. 
The revenue figure serves as a key performance indicator for evaluating business growth, measuring sales effectiveness, and supporting strategic decision-making.

This insight provides a foundation for further analysis into revenue drivers, including product performance, 
customer purchasing behavior, referral sources, payment methods, and order completion rates.



INPUT [5]
*2. What is the average order value?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_2 = """
SELECT AVG(TotalPrice) AS Average_Order_Value
FROM sales_data
"""
print(pd.read_sql_query(query_2, connection))

RESULT [5]
 Average_Order_Value
0            1053.9683

FINDINGS:
The analysis showed that the Average Order Value (AOV) was 1,053.97. This indicates that, on average, customers spent approximately 1,054 per transaction. 
The AOV provides valuable insight into customer spending behavior and serves as an important metric for evaluating sales performance and revenue generation.

A strong average order value suggests that customers are purchasing multiple items or higher-value products per order. 
This metric can be used to assess the effectiveness of pricing strategies, promotional campaigns, and upselling opportunities aimed at increasing customer spend.

INPUT [6]
**3. Which products generate the most total revenue?**

import pandas as pd
import sqlite3  
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')    
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_3 = """
SELECT Product,
       SUM(TotalPrice) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 10
"""
print(pd.read_sql_query(query_3, connection))

RESULT [6]

Product    Revenue
0    Chair  195620.11
1  Printer  195612.61
2   Laptop  192126.56
3   Tablet  186568.95
4  Monitor  175651.41
5     Desk  167459.93
6    Phone  151722.39

FINDINGS:
The top revenue-generating products are Chairs, Printers, and Laptops, with Chairs leading the list at 195,620.11 in revenue. 
This insight can guide inventory and marketing focus on these high-performing products.

INPUT [7]
**4. What is the total quantity sold for each product, and how many orders were placed for?**

import pandas as pd
import sqlite3  
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')    
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_3a = """
SELECT product, SUM(Quantity) AS Quantity, COUNT(OrderID) as OrderCount, AVG(Quantity) as AverageQuantity 
FROM sales_data 
GROUP BY product  
ORDER BY Quantity DESC
"""
print(pd.read_sql_query(query_3a, connection))

RESULT [7]

Product  Quantity  OrderCount  AverageQuantity
0    Chair       562         178         3.157303
1  Printer       542         181         2.994475
2   Laptop       535         173         3.092486
3     Desk       508         170         2.988235
4   Tablet       497         179         2.776536
5  Monitor       480         163         2.944785
6    Phone       411         156         2.634615

FINDINGS:
Chairs have the highest total quantity sold at 562 units, 
followed by Printers and Laptops. The average quantity per order varies, 
with Chairs averaging (3.16 units) per order, indicating that customers tend to purchase multiple units of this product.


INPUT [8]
**5. What is the distribution of orders by payment method?**

import pandas as pd
import sqlite3  
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')    
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_4 = """
SELECT PaymentMethod,
       COUNT(*) AS NumberOfOrders
FROM sales_data
GROUP BY PaymentMethod
ORDER BY NumberOfOrders DESC
"""
print(pd.read_sql_query(query_4, connection))

RESULT [8]
PaymentMethod  NumberOfOrders
0        Online             258
1          Cash             246
2   Credit Card             234
3    Debit Card             232
4     Gift Card             230

FINDINGS:
Online payments were the most preferred payment method, accounting for **258 orders**, 
followed by Cash (**246 orders**). Credit Card (**234 orders**), Debit Card (**232 orders**), 
and Gift Card (**230 orders**) showed relatively similar usage levels. Overall, 
customers demonstrated a slight preference for digital payment options, 
with Online payments leading in transaction volume.

INPUT [9]
**6. What is the distribution of orders by status?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_6 = """
SELECT OrderStatus,
       COUNT(*) AS Total
FROM sales_data
GROUP BY OrderStatus
"""
print(pd.read_sql_query(query_6, connection))

RESULT [9]
OrderStatus  Total
0    Shipped      258
1    Pending      246
2    Cancelled    234
3    Returned     232
4    Completed    230


FINDINGS:
Shipped orders were the most common order status, accounting for **258 orders**, 
followed by Pending (**246**) and Cancelled (**234**) orders.
Returned (**232**) and Completed (**230**) orders were recorded at similar levels.

Relatively high number of pending and cancelled orders highlights potential opportunities 
to improve order fulfillment processes and enhance customer retention.



INPUT [10]
**7. What is the average order value overall, and how does it vary by payment method?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_7 = """
SELECT
    PaymentMethod,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(TotalPrice), 2) AS Average_Order_Value,
    ROUND(SUM(TotalPrice), 2) AS Total_Revenue
FROM sales_data
GROUP BY PaymentMethod
ORDER BY Average_Order_Value DESC
"""
print(pd.read_sql_query(query_7, connection))

RESULT [10]
  PaymentMethod  Total_Orders  Average_Order_Value  Total_Revenue
0   Credit Card           234              1127.55      263847.63
1     Gift Card           230              1070.97      246323.92
2          Cash           246              1056.04      259786.29
3        Online           258              1017.22      262442.94
4    Debit Card           232              1001.56      232361.18

FINDINGS:
Credit Card payments generated the highest average order value (**1,127.55**) 
and the highest total revenue (**263,847.63**), indicating that customers using this payment method tend to spend more per transaction.
Online and Cash payments also contributed significantly to overall revenue, generating **262,442.94** and **259,786.29** respectively. 

Debit Card transactions recorded the lowest average order value (**1,001.56**) and total revenue (**232,361.18**), 
suggesting comparatively lower customer spending through this payment method.




**Section 2: Operational Patterns**

INPUT [11]
**8. Which month had the highest total revenue?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_8 = """
SELECT strftime('%Y-%m', Date) AS OrderMonth, SUM(TotalPrice) AS TotalRevenue FROM sales_data 
GROUP BY OrderMonth 
ORDER BY TotalRevenue DESC
LIMIT 10
"""
print(pd.read_sql_query(query_8, connection))

RESULT [11]
 OrderMonth  TotalRevenue
0    2024-06      68068.54
1    2023-05      63836.84
2    2023-01      56685.75
3    2023-08      54352.14
4    2025-06      53047.40
5    2023-10      52607.85
6    2024-04      49613.14
7    2023-06      49500.19
8    2023-03      48609.37
9    2023-12      43754.73

FINDINGS:
Revenue fluctuated across the analyzed periods, with **June 2024** generating the highest revenue of **68,068.54**. 
This was followed by **May 2023 (63,836.84)** and **January 2023 (56,685.75)**. 
The results indicate periods of stronger sales performance, suggesting the presence of seasonal trends 
or varying customer demand throughout the year. 
Monitoring these high-performing months can help support more effective sales and marketing planning.

INPUT [12]
**9. Which products have the highest cancellation rates?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_9 = """
SELECT Product, COUNT(Product) AS ProductCount 
FROM sales_data
WHERE OrderStatus = 'Cancelled'
GROUP BY Product 
ORDER BY ProductCount DESC
"""
print(pd.read_sql_query(query_9, connection))

RESULT [12]
Product  ProductCount
0    Chair            45
1  Printer            35
2  Monitor            35
3   Laptop            35
4     Desk            35
5   Tablet            34
6    Phone            31

FINDINGS:
Chair was the most frequently ordered product with **45 orders**, 
indicating the highest customer demand among all products. Printers, Monitors, Laptops, 
and Desks followed closely with **35 orders each**, while Tablets (**34**) and Phones (**31**) 
recorded slightly lower order volumes. Overall, demand was relatively balanced across most product categories, 
with Chairs standing out as the top-selling item.


INPUT [13]
**10. What is the cancellation rate by payment method?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_10 = """
SELECT 
    PaymentMethod,
    COUNT(*) AS TotalOrders,
    SUM(CASE WHEN OrderStatus = 'Cancelled' THEN 1 ELSE 0 END) AS CancelledOrders,
    ROUND(100.0 * SUM(CASE WHEN OrderStatus = 'Cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2) AS CancellationRatePercent
FROM sales_data
GROUP BY PaymentMethod
ORDER BY CancellationRatePercent DESC
"""
print(pd.read_sql_query(query_10, connection))

RESULT [13]
  PaymentMethod  TotalOrders  CancelledOrders  CancellationRatePercent
0   Credit Card          234               54                    23.08
1     Gift Card          230               50                    21.74
2        Online          258               53                    20.54
3          Cash          246               49                    19.92
4    Debit Card          232               44                    18.97

FINDINGS:
Credit Card transactions recorded the highest cancellation rate (**23.08%**), 
followed by Gift Card (**21.74%**) and Online payments (**20.54%**). 
In contrast, Debit Card payments had the lowest cancellation rate (**18.97%**). 
These results suggest variations in customer behavior across payment methods 
and may help inform strategies aimed at reducing order cancellations 
and improving transaction completion rates.


INPUT [14]
**11. What is the cancellation rate for orders with and without coupons?**

import pandas as pd
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_11 = """
SELECT
    CASE
        WHEN CouponCode IS NULL OR CouponCode = ''
        THEN 'Without Coupon'
        ELSE 'With Coupon'
    END AS Coupon_Usage,

    COUNT(*) AS Total_Orders,

    SUM(
        CASE
            WHEN OrderStatus = 'Cancelled' THEN 1
            ELSE 0
        END
    ) AS Cancelled_Orders,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN OrderStatus = 'Cancelled' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS Cancellation_Rate_Percent

FROM sales_data
GROUP BY Coupon_Usage
"""
print(pd.read_sql_query(query_11, connection))

RESULT [14]
Coupon_Usage  Total_Orders  Cancelled_Orders  Cancellation_Rate_Percent
0     With Coupon           891               192                      21.55
1  Without Coupon           309                58                      18.77

FINDINGS:
Orders with coupons have a higher cancellation rate (21.55%) compared to orders without coupons (18.77%). 
This suggests that customers using coupons may be more likely to cancel their orders, which could be due 
to various factors such as dissatisfaction with the product or service, or changes in their purchasing decisions. 
Businesses may want to investigate the reasons behind this trend and consider strategies to reduce cancellations among coupon users.



**Section 3: Customer Acquisition Insight**

INPUT [15]
**12. What is the distribution of delivered orders by referral source?**

import pandas as pd 
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_12 = """
SELECT ReferralSource, COUNT(OrderID) AS DeliveredOrderCount 
FROM sales_data 
WHERE OrderStatus = 'Delivered' 
GROUP BY ReferralSource 
ORDER by DeliveredOrderCount DESC
"""
print(pd.read_sql_query(query_12, connection))

RESULT [15]
ReferralSource  DeliveredOrderCount
0          Email                   60
1      Instagram                   52
2         Google                   44
3       Facebook                   42
4       Referral                   33

FINDINGS:
Email was the top-performing referral source with **60 delivered orders**, followed by **Instagram (52)** and **Google (44)**. 
This suggests that email marketing is the most effective channel for driving successful order deliveries.


INPUT [16]
**13. What is the delivery rate by referral source?**

import pandas as pd 
import sqlite3
df = pd.read_excel("Cleaned_orders_Dataset.xlsx")   
connection = sqlite3.connect(':memory:')
df.to_sql('sales_data', connection, index=False, if_exists='replace')
query_13 = """
SELECT 
    ReferralSource,
    COUNT(*) AS TotalOrders,
    SUM(CASE WHEN OrderStatus = 'Delivered' THEN 1 ELSE 0 END) AS DeliveredOrders,
    ROUND(100.0 * SUM(CASE WHEN OrderStatus = 'Delivered' THEN 1 ELSE 0 END) / COUNT(*), 2) AS DeliveryRatePercent
FROM sales_data
GROUP BY ReferralSource
ORDER BY DeliveryRatePercent DESC
"""
print(pd.read_sql_query(query_13, connection))

RESULT [16]  
ReferralSource  TotalOrders  DeliveredOrders  DeliveryRatePercent
0          Email          250               60                24.00
1      Instagram          259               52                20.08
2       Facebook          228               42                18.42
3         Google          241               44                18.26
4       Referral          222               33                14.86

FINDINGS:
Email emerged as the most effective referral source, recording the highest delivery rate of **24.00%**, 
with **60 successfully delivered orders** out of **250 total orders**. 
This suggests that customers acquired through email campaigns are more likely to complete the 
purchase journey and receive their orders successfully.

Instagram ranked second with a delivery rate of **20.08%**, followed by Facebook (**18.42%**) and Google (**18.26%**), 
which showed relatively similar performance. Referral traffic recorded the lowest delivery rate at **14.86%**, 
indicating that orders generated through referrals were less likely to result in successful deliveries.

Overall, the results suggest that email marketing not only drives orders but also attracts 
customers with a higher likelihood of completing the delivery process, making it a valuable channel for customer acquisition and retention.



**CONCLUSION:**
**This analysis provided valuable insights** into customer purchasing behavior, payment preferences, product demand, 
referral source performance, and order outcomes within the e-commerce business.

**The business generated a total revenue of** **1,264,761.96** with an average order value of **1,053.97**, 
indicating strong customer spending patterns. Credit Card transactions contributed the highest 
revenue and average order value, while Online payments emerged as the most frequently used payment method.

**From a marketing perspective,** Email proved to be the most effective referral source, generating the highest
number of delivered orders and the strongest delivery rate. Product analysis revealed that Chairs were the most 
frequently ordered item, highlighting strong customer demand within that category.

**sssThe analysis also identified areas for improvement.** Orders placed using coupons experienced a higher cancellation 
rate than those without coupons, suggesting the need to evaluate promotional strategies and customer purchasing behavior. 
Additionally, the significant number of pending and cancelled orders presents an opportunity to optimize order fulfillment processes and improve customer retention.

**Overall,** the findings provide actionable insights that can support data-driven decision-making, 
enhance operational efficiency, improve marketing effectiveness, and drive business growth.
