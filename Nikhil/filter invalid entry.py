#1. Write a program to filter out the invalid records and store invalid records in separate files.


import pandas as pd
input_file_path="F:\\TIB Accademy\\Git\\TVSale\\data-analysis-tvsalesdata\\television.txt"
separator="|"
is_header=None
tv_sales_data=pd.read_csv(input_file_path,header=is_header,sep=separator)
tv_sales_data_column=["Company Name","Product Name","Size" ,"State","Pin_Code","Price"]
tv_sales_data.columns=tv_sales_data_column
print(tv_sales_data)
tv_sales_data_invalid_records=tv_sales_data[tv_sales_data["Company Name"].isnull() | tv_sales_data["Product Name"].isnull() | tv_sales_data["Size"].isnull() | tv_sales_data["State"].isnull() | tv_sales_data["Pin_Code"].isnull() | tv_sales_data["Price"].isnull()]
tv_sales_data_valid_records=tv_sales_data[tv_sales_data["Company Name"].notna() & tv_sales_data["Product Name"].notna() & tv_sales_data["Size"].notna() & tv_sales_data["State"].notna() & tv_sales_data["Pin_Code"].notna() &  tv_sales_data["Price"].notna() ]

tv_sales_data_invalid_records.to_csv("F:\\TIB Accademy\\Git\\TVSale\\data-analysis-tvsalesdata\\Nikhil\\invalidtelevision.txt")
tv_sales_data_valid_records.to_csv("F:\\TIB Accademy\\Git\\TVSale\\data-analysis-tvsalesdata\\Nikhil\\valid television.txt")
print("=======================")
print(tv_sales_data_invalid_records)
