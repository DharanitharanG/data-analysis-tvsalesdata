'''
Write a program to filter out the invalid records
and store invalid records in separate files.
'''

import pandas as pd

input_file_path = "/home/dharani/Desktop/GitHubProjects/data-analysis-tvsalesdata/television.txt"
output_file_path_validRecords = \
    "/home/dharani/Desktop/GitHubProjects/data-analysis-tvsalesdata/dharani/outputfiles/television_validRecords"
output_file_path_invalidRecords = \
    "/home/dharani/Desktop/GitHubProjects/data-analysis-tvsalesdata/dharani/outputfiles/television_invalidRecords"

separator = "|"
is_header = None
tv_sales_data_columns = ['CompanyName', 'ProductName', 'Size', 'State', 'PinCode', 'Price']

tv_sales_data = pd.read_csv(input_file_path, header=is_header, sep=separator)
tv_sales_data.columns = tv_sales_data_columns

tv_sales_data_invalid_records = \
    tv_sales_data[tv_sales_data['CompanyName'].isnull() | tv_sales_data['ProductName'].isnull()]

tv_sales_data_valid_records = \
    tv_sales_data[tv_sales_data['CompanyName'].notna() & tv_sales_data['ProductName'].notna()]

tv_sales_data_valid_records.\
    to_csv(output_file_path_validRecords, header=None, sep=separator)

tv_sales_data_invalid_records.\
    to_csv(output_file_path_invalidRecords, header=None, sep=separator)

