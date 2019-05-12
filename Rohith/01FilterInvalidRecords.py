# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:47:56 2019

@author: ROHITH G KRISHNA
"""

#Write a program to filter out the invalid records and store invalid records in separate files.

import pandas as pd
input_file_path = "file:///‪C:/Users/ROHITH G KRISHNA/Desktop/Github_Project/data-analysis-tvsalesdata/television.txt"
output_file_path_valid_records = "C://Users//ROHITH G KRISHNA//Desktop//Github_Project//data-analysis-tvsalesdata//Rohith//output//television_valid_records.txt"
output_file_path_invalid_records = "C://Users//ROHITH G KRISHNA//Desktop//Github_Project//data-analysis-tvsalesdata//Rohith//output//television_invalid_records.txt"
separator = "|"
is_header = None
tv_sales_data_columns =['CompanyName', 'ProductName', 'Size', 'State', 'Pincode', 'Price']
tv_sales_data = pd.read_csv(input_file_path,header = is_header,sep = separator)

tv_sales_data.columns = tv_sales_data_columns
print(tv_sales_data)

tv_sales_data_invalid_records = tv_sales_data[tv_sales_data['CompanyName'].isnull() | tv_sales_data['ProductName'].isnull()]
tv_sales_data_invalid_records.to_csv(output_file_path_invalid_records ,header =None ,sep = separator)

tv_sales_data_valid_records = tv_sales_data[tv_sales_data['CompanyName'].notna() & tv_sales_data['ProductName'].notna()]
tv_sales_data_valid_records.to_csv(output_file_path_valid_records ,header = None ,sep = separator)

print(tv_sales_data_invalid_records)
print(tv_sales_data_valid_records)

