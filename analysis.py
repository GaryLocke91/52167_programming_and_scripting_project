import pandas as pd
import numpy as np

df = pd.read_csv('iris_data.csv')
text_lst_overall = []

text_lst_overall.append('Minimum value of sepal length: ' + str(df['sepal_length'].min()))
text_lst_overall.append('Minimum value of sepal width: ' + str(df['sepal_width'].min()))
text_lst_overall.append('Minimum value of petal length: ' + str(df['petal_length'].min()))
text_lst_overall.append('Minimum value of petal width: ' + str(df['petal_width'].min()))
text_lst_overall.append('Maximum value of sepal length: ' + str(df['sepal_length'].max()))
text_lst_overall.append('Maximum value of sepal width: ' + str(df['sepal_width'].max()))
text_lst_overall.append('Maximum value of petal length: ' + str(df['petal_length'].max()))
text_lst_overall.append('Maximum value of petal width: ' + str(df['petal_width'].max()))
text_lst_overall.append('Average sepal length: ' + str(round(df['sepal_length'].mean(), 1)))
text_lst_overall.append('Average sepal width: ' + str(round(df['sepal_width'].mean(), 1)))
text_lst_overall.append('Average petal length: ' + str(round(df['petal_length'].mean(), 1)))
text_lst_overall.append('Average petal width: ' + str(round(df['petal_width'].mean(), 1)))

print(df['sepal_length'][1:12].max())
'''
# Source: https://stackoverflow.com/questions/44405123/convert-csv-to-dictionary
data_dict = {col: list(df[col]) for col in df.columns}

sepal_length_lst = data_dict['sepal_length']
sepal_width_lst = data_dict['sepal_width']
petal_length_lst = data_dict['petal_length']
petal_width_lst = data_dict['petal_width']

#with open('summary.py', 'w') as f:
#    for val in text_lst_overall:
#        f.write(val)
#        f.write('\n')
#f.close()'''