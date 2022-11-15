import pandas as pd
import numpy as np
import openpyxl
import warnings
import os
warnings.simplefilter("ignore")

#데이터 전처리
df = pd.read_excel('/Users/User/Downloads/NTIS_SearchDownload_ashryu_20221110135400.xlsx')
df.shape
df.drop(['검색결과'], axis = 1, inplace=True) #delete the first column (useless)
col = dataset.loc[0]
df.columns = col
#dataset.drop([labels='0'], axis=0) #delete the first row (repeated already)

is_2015 = df['기준년도'] == '2015'
df_2015 = df[is_2015]
df_2015 = df[is_2015]
df_2015.shape


is_2016 = df['기준년도'] == '2016'
df_2016 = df[is_2016]
df_2016.shape
#2016 sum
sum_2016 = df_2016.sum(axis=0)
sum_2016['연구비합계']

ai_2016 = df_2016[df_2016['과제명(국문)'].str.contains("인공지능|딥러닝|인공신경망|AI|기계학습")]
sum_2016 = ai_2016.sum(axis=0)


#조건들을 만족하는 데이터 필터링
ai_df = df[df['과제명(국문)'].str.contains("인공지능|딥러닝|인공신경망|AI|기계학습|Artifical Intelligence|GAN|Machine Learning|Deep Learning|DNN")]
ai_df.shape
is_venezuela = df['country'] == 'Venezuela'


