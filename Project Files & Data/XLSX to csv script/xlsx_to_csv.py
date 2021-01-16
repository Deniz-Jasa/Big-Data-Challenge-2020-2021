#importing pandas as pd 
import pandas as pd 
  
# Read and store content of an excel file  
read_file = pd.read_excel ("xlsx/academic_performance.xlsx") 
  
# Write the dataframe object into csv file format 
read_file.to_csv ("csv/academic_performance_data.csv", index = None, header=True) 
    
# read csv file and convert into a dataframe object 
df = pd.DataFrame(pd.read_csv("csv/academic_performance_data.csv")) 
  
# show the dataframe 
df