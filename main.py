from urllib.request import urlretrieve
import pandas as pd
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
urlretrieve(medical_charges_url, "medical.csv")

medical_df = pd.read_csv('medical.csv')


print(medical_df.describe())