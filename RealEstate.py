from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *
from datetime import datetime

# ---------------------------------------------
# Function to display the user menu
# ---------------------------------------------
def menu() -> int:
    print("********************************************************")
    print("|  1: Total property sales by year/month               |")
    print("|  2: Sales distribution by property type              |")
    print("|  3: Top performing cities by revenue                 |")
    print("|  4: Average sale price over time                     |")
    print("|  5: Most common payment methods                      |")
    print("|  6: Agent-wise total sales                           |")
    print("|  7: Repeat vs one-time buyers                        |")
    print("|  8: Daily sales trend                                |")
    print("|  0: Exit                                             |")
    print("********************************************************")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return -1

# ---------------------------------------------
# Q1: Total sales by year and month
# ---------------------------------------------
def q1_total_sales_by_month(df):
    print("Running Q1: Monthly Sales Trend...")
    result = df.withColumn("year", F.year("sale_date")) \
               .withColumn("month", F.month("sale_date")) \
               .groupBy("year", "month") \
               .agg(F.sum("price").alias("total_sales")) \
               .orderBy("year", "month")
    result.show()

# ---------------------------------------------
# Q2: Sales by property type
# ---------------------------------------------
def q2_sales_by_property_type(df):
    print("Running Q2: Sales Distribution by Property Type...")
    result = df.groupBy("property_type") \
               .agg(F.sum("price").alias("total_revenue")) \
               .orderBy(F.desc("total_revenue"))
    result.show()

# ---------------------------------------------
# Q3: Revenue by city
# ---------------------------------------------
def q3_revenue_by_city(df):
    print("Running Q3: Top Performing Cities...")
    result = df.groupBy("city") \
               .agg(F.sum("price").alias("city_revenue")) \
               .orderBy(F.desc("city_revenue"))
    result.show()

# ---------------------------------------------
# Q4: Average sale price over time
# ---------------------------------------------
def q4_avg_sale_price(df):
    print("Running Q4: Average Sale Price by Month...")
    result = df.withColumn("year", F.year("sale_date")) \
               .withColumn("month", F.month("sale_date")) \
               .groupBy("year", "month") \
               .agg(F.avg("price").alias("avg_price")) \
               .orderBy("year", "month")
    result.show()

# ---------------------------------------------
# Q5: Most common payment methods
# ---------------------------------------------
def q5_payment_methods(df):
    print("Running Q5: Payment Methods...")
    result = df.groupBy("payment_method") \
               .agg(F.count("sale_id").alias("num_sales")) \
               .orderBy(F.desc("num_sales"))
    result.show()

# ---------------------------------------------
# Q6: Total sales by agent
# ---------------------------------------------
def q6_agent_sales(df):
    print("Running Q6: Agent-wise Total Sales...")
    result = df.groupBy("agent_name") \
               .agg(F.count("sale_id").alias("total_properties_sold"),
                    F.sum("price").alias("total_sales")) \
               .orderBy(F.desc("total_sales"))
    result.show()

# ---------------------------------------------
# Q7: Repeat vs one-time customers
# ---------------------------------------------
def q7_repeat_vs_one_time(df):
    print("Running Q7: Repeat vs One-Time Buyers...")
    customer_sales = df.groupBy("customer_id") \
                       .agg(F.countDistinct("sale_id").alias("purchase_count"))
    result = customer_sales.withColumn(
        "buyer_type",
        F.when(F.col("purchase_count") > 1, "Repeat").otherwise("One-Time")
    ).groupBy("buyer_type").agg(F.count("*").alias("num_customers"))
    result.show()

# ---------------------------------------------
# Q8: Daily sales trend
# ---------------------------------------------
def q8_daily_sales(df):
    print("Running Q8: Daily Sales Trend...")
    result = df.groupBy("sale_date") \
               .agg(F.sum("price").alias("daily_revenue")) \
               .orderBy("sale_date")
    result.show(30)

# ---------------------------------------------
# Main function
# ---------------------------------------------
def main():
    spark = SparkSession.builder \
        .appName("RealEstate Sales Analytics") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # Load the data
    df = spark.read.option("header", "true") \
                   .option("sep", "\t") \
                   .option("inferSchema", "true") \
                   .csv("data/realestate_data.tsv") \
                   .withColumn("sale_date", F.to_date("sale_date", "yyyy-MM-dd"))

    while True:
        choice = menu()
        if choice == 1:
            q1_total_sales_by_month(df)
        elif choice == 2:
            q2_sales_by_property_type(df)
        elif choice == 3:
            q3_revenue_by_city(df)
        elif choice == 4:
            q4_avg_sale_price(df)
        elif choice == 5:
            q5_payment_methods(df)
        elif choice == 6:
            q6_agent_sales(df)
        elif choice == 7:
            q7_repeat_vs_one_time(df)
        elif choice == 8:
            q8_daily_sales(df)
        elif choice == 0:
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# ---------------------------------------------
# Entry point
# ---------------------------------------------
if __name__ == "__main__":
    main()
