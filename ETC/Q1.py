# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UnuQV7U42mA9LN0bdXaEjUgp7ItCmuQK
"""

"""
[전국 커피숍 규모 파악]
Q1. 'data_coffee.csv' 데이터 읽어오기
    # /content/drive/MyDrive/data/data_coffee.csv
Q2. 매장의 규모(sizeOfsite)변수를 요약하기
Q3. sizeOfsite의 결측치(NA)를 제거하고 히스토그램 그려보기
Q4. 매장 규모가 500이상인 outlier를 제외하고 히스토그램 그려보기

"""
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Q1.
df = pd.read_csv("/content/drive/MyDrive/data/data_coffee.csv", encoding='cp949') # data_coffee.csv 파일 읽어오기

# Q2.
summarize = df['sizeOfsite'].describe()
print(summarize)

# Q3.
is_empty_df = np.isnan(df['sizeOfsite']) + (df['sizeOfsite'] == 0)
# print(is_empty_df)
# empty_df = df[is_empty_df]
# print(empty_df)

filled_df = df[~is_empty_df]
# print(filled_df)
plt.hist(filled_df['sizeOfsite'])

plt.title("Histogram without Nan")
plt.xlabel("sizeOfsite")
plt.ylabel("samples")

plt.show()

# Q4.
# small_filled_df = filled_df[filled_df['sizeOfsite'] < 500]
is_large_df = filled_df['sizeOfsite'] >= 500

# large_filled_df = filled_df[is_large_df]
# print(large_filled_df)

small_filled_df = filled_df[~is_large_df]
# print(small_filled_df)

plt.hist(small_filled_df['sizeOfsite'])

plt.title("outlier < 500")
plt.xlabel("sizeOfsite")
plt.ylabel("samples")

plt.show()