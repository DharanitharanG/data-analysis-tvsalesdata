# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:52:11 2019

@author: i
"""

import pandas as pd
input_file_path = "D:\\Arun E\\ML\\Github\\data-analysis-tvsalesdata\\television.txt"
output_file_path_validRecords = "D:\\Arun E\\ML\\Github\\data-analysis-tvsalesdata\\Arun\\Output files\\televesion_valid_records"
output_file_path_invalidRecords = "D:\\Arun E\\ML\\Github\\data-analysis-tvsalesdata\\Arun\\Output files\\televesion_invalid_records"
seperator = "|"
isheader = None
tv_sales_data_columns = ['CompanyName','ProductName','Size','State','PinCode','Price']

tv_sales_data = pd.read_csv(input_file_path,header=isheader,sep=seperator)
tv_sales_data.columns = tv_sales_data_columns

print(tv_sales_data)
tv_sales_data_invalid_records = tv_sales_data [tv_sales_data['CompanyName'].isnull() | tv_sales_data['ProductName'].isnull()]

tv_sales_data_valid_records = tv_sales_data [tv_sales_data['CompanyName'].notna() & tv_sales_data['ProductName'].notna()]


tv_sales_data_valid_records.to_csv(output_file_path_validRecords , header=None , sep=seperator)

tv_sales_data_invalid_records.to_csv(output_file_path_invalidRecords , header=None , sep=seperator)

print(tv_sales_data_valid_records)
print(tv_sales_data_invalid_records)