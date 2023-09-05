from urllib.request import urlretrieve
import pandas as pd

medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
urlretrieve(medical_charges_url, "medical.csv")

medical_df = pd.read_csv('medical.csv')
# Press the green button in the gutter to run the script.
print(medical_df)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
