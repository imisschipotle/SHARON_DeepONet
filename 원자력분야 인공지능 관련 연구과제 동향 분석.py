import pandas as pd
import numpy as np
import openpyxl
import warnings
import os
warnings.simplefilter("ignore")

#Get current path
currentPath = os.getcwd()
currentPath

#Change working directory
os.chdir('/Users/User/Downloads')

nuclear_ai_df = pd.read_excel('/Users/User/Downloads/NTIS_SearchDownload_ashryu_20221111101735.xlsx')
col = nuclear_ai_df.loc[0]
nuclear_ai_df.columns = col
nuclear_ai_df.shape




################# 2018 ~ 2022 데이터 각각 나누기 #####################################################

nuclear_ai_2018 = nuclear_ai_df[nuclear_ai_df['기준년도'] == '2018']
nuclear_ai_2018

nuclear_ai_2019 = nuclear_ai_df[nuclear_ai_df['기준년도'] == '2019']
nuclear_ai_2019

nuclear_ai_2020 = nuclear_ai_df[nuclear_ai_df['기준년도'] == '2020']
nuclear_ai_2020

nuclear_ai_2021 = nuclear_ai_df[nuclear_ai_df['기준년도'] == '2021']
nuclear_ai_2021

nuclear_ai_2022 = nuclear_ai_df[nuclear_ai_df['기준년도'] == '2022']
nuclear_ai_2022

print(nuclear_ai_2018, nuclear_ai_2019, nuclear_ai_2020, nuclear_ai_2021, nuclear_ai_2022)
################# 2018 ~ 2022 데이터 각각 나누기 #####################################################

python3 preProcess.py dataInExample
