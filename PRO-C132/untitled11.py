# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r46NlG3pvkpXKeLAJqymoc7T72o3NBG6
"""

import pandas as pd


final_planets_df = pd.read_csv("stars_with_gravity.csv")

print(final_planets_df.shape)

final_planets_df.head()

final_planets_df.columns

final_planets_df.dropna()

print(final_planets_df.shape)

final_planets_df.head()

#save to csv file
final_planets_df.to_csv('final_data.csv')

from google.colab import files
files.download('final_data.csv')