import pandas as pd
import numpy as np
import openpyxl
import warnings
import os
warnings.simplefilter("ignore")
import pandas as pd
import matplotlib.pyplot as plt

import os

#Get current path
currentPath = os.getcwd()
currentPath

#Change working directory
os.chdir('/Users/User/Downloads')


############################ ETRI 2 0 1 8 ###########################################################
df_2018 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021897_PJT_2022-11-10 (6).xlsx')
df_2018.shape

#Column 이름 주기
col = df_2018.loc[0]
df_2018.columns = col
ai_2018 = df_2018[df_2018['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")] or  df_2018[df_2019['한글키워드'].str.contains("DeepLearning|AI|Reinforcement Learning|ReinforcementLearning|Artifical Intelligence|ArtificialIntelligence|NeuralNetwork|NeuralNetworks|Neural Networks|Neural Network|MachineLearning|Machine Learning|Deep Learning Model")]
ai_2018.shape


############################ ETRI 2 0 1 9 ###########################################################

df_2019 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021897_PJT_2022-11-10 (8).xlsx')
df_2019.shape

#Column 이름 주기
col = df_2019.loc[0]
df_2019.columns = col
# ai_2019 = df_2019[df_2019['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝")]
# ai_2019.shape
ai_2019 = df_2019[df_2019['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
ai_2019.shape

############################ ETRI 2 0 2 0 ###########################################################

df_2020 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021897_PJT_2022-11-10 (10).xlsx')
df_2020.shape

#Column 이름 주기
col = df_2020.loc[0]
df_2020.columns = col
ai_2020 = df_2020[df_2020['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
ai_2020.shape

############################ ETRI 2 0 2 1 ###########################################################

df_2021 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021897_PJT_2022-11-10 (11).xlsx')
df_2021.shape

#Column 이름 주기
col = df_2021.loc[0]
df_2021.columns = col
ai_2021 = df_2021[df_2021['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
ai_2021.shape

############################ ETRI 2 0 2 2 ###########################################################

df_2022 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021897_PJT_2022-11-10 (12).xlsx')
df_2022.shape

#Column 이름 주기
col = df_2022.loc[0]
df_2022.columns = col
ai_2022 = df_2022[df_2022['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
ai_2022.shape




############################ ETRI 2 0 2 2 ###########################################################

df_2022 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021897_PJT_2022-11-10 (12).xlsx')
df_2022.shape

#Column 이름 주기
col = df_2022.loc[0]
df_2022.columns = col
ai_2022 = df_2022[df_2022['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
ai_2022.shape


############################ KAERI 2 0 1 8 ###########################################################

KAERI_2018 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021884_PJT_2022-11-10.xlsx')
KAERI_2018.shape

#Column 이름 주기
col = KAERI_2018.loc[0]
KAERI_2018.columns = col
K_ai_2018 = KAERI_2018[KAERI_2018['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
K_ai_2018.shape

############################ KAERI 2 0 1 9 ###########################################################

KAERI_2019 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021884_PJT_2022-11-10 (1).xlsx')
KAERI_2019.shape

#Column 이름 주기
col = KAERI_2019.loc[0]
KAERI_2019.columns = col
K_ai_2019 = KAERI_2019[KAERI_2019['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
K_ai_2019.shape

############################ KAERI 2 0 2 0 ###########################################################

KAERI_2020 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021884_PJT_2022-11-10 (2).xlsx')
KAERI_2020.shape

#Column 이름 주기
col = KAERI_2020.loc[0]
KAERI_2020.columns = col
K_ai_2020 = KAERI_2020[KAERI_2020['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
K_ai_2020.shape


############################ KAERI 2 0 2 1 ###########################################################

KAERI_2021 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021884_PJT_2022-11-10 (3).xlsx')
KAERI_2021.shape

#Column 이름 주기
col = KAERI_2021.loc[0]
KAERI_2021.columns = col
K_ai_2021 = KAERI_2021[KAERI_2021['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
K_ai_2021.shape


############################ KAERI 2 0 2 2 ###########################################################

KAERI_2022 = pd.read_excel('/Users/User/Downloads/NTIS_PI_0021884_PJT_2022-11-10 (4).xlsx')
KAERI_2022.shape

#Column 이름 주기
col = KAERI_2022.loc[0]
KAERI_2022.columns = col
K_ai_2022 = KAERI_2022[KAERI_2022['한글키워드'].str.contains("뉴럴네트워크|인공 신경망|인공지능|딥러닝|인공신경망|기계학습|기계 학습|인공 지능|딥 러닝|AI|강화학습|강화 학습|앙상블 딥러닝|뉴럴 네트워크")]
K_ai_2022.shape