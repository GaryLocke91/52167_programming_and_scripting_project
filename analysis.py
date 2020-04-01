import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

#Reads the data set
df = pd.read_csv('iris_data.csv')

#Creates a list for overall and each species
txt_lst_tot = []
txt_lst_set = []
txt_lst_ver = []
txt_lst_vir = []

#Uses the min, max and mean functions and appends the string to a list
txt_lst_tot.append('Minimum sepal length: ' + str(df['sepal_length'].min()))
txt_lst_tot.append('Minimum sepal width: ' + str(df['sepal_width'].min()))
txt_lst_tot.append('Minimum petal length: ' + str(df['petal_length'].min()))
txt_lst_tot.append('Minimum petal width: ' + str(df['petal_width'].min()))
txt_lst_tot.append('Maximum sepal length: ' + str(df['sepal_length'].max()))
txt_lst_tot.append('Maximum sepal width: ' + str(df['sepal_width'].max()))
txt_lst_tot.append('Maximum petal length: ' + str(df['petal_length'].max()))
txt_lst_tot.append('Maximum petal width: ' + str(df['petal_width'].max()))
txt_lst_tot.append('Average sepal length: ' + str(round(df['sepal_length'].mean(), 1)))
txt_lst_tot.append('Average sepal width: ' + str(round(df['sepal_width'].mean(), 1)))
txt_lst_tot.append('Average petal length: ' + str(round(df['petal_length'].mean(), 1)))
txt_lst_tot.append('Average petal width: ' + str(round(df['petal_width'].mean(), 1)))

#Uses the min, max and mean functions and appends the string to a list
txt_lst_set.append('Minimum sepal length: ' + str(df['sepal_length'][0:50].min()))
txt_lst_set.append('Minimum sepal width: ' + str(df['sepal_width'][0:50].min()))
txt_lst_set.append('Minimum petal length: ' + str(df['petal_length'][0:50].min()))
txt_lst_set.append('Minimum petal width: ' + str(df['petal_width'][0:50].min()))
txt_lst_set.append('Maximum sepal length: ' + str(df['sepal_length'][0:50].max()))
txt_lst_set.append('Maximum sepal width: ' + str(df['sepal_width'][0:50].max()))
txt_lst_set.append('Maximum petal length: ' + str(df['petal_length'][0:50].max()))
txt_lst_set.append('Maximum petal width: ' + str(df['petal_width'][0:50].max()))
txt_lst_set.append('Average sepal length: ' + str(round(df['sepal_length'][0:50].mean(), 1)))
txt_lst_set.append('Average sepal width: ' + str(round(df['sepal_width'][0:50].mean(), 1)))
txt_lst_set.append('Average petal length: ' + str(round(df['petal_length'][0:50].mean(), 1)))
txt_lst_set.append('Average petal width: ' + str(round(df['petal_width'][0:50].mean(), 1)))

#Uses the min, max and mean functions and appends the string to a list
txt_lst_ver.append('Minimum sepal length: ' + str(df['sepal_length'][50:100].min()))
txt_lst_ver.append('Minimum sepal width: ' + str(df['sepal_width'][50:100].min()))
txt_lst_ver.append('Minimum petal length: ' + str(df['petal_length'][50:100].min()))
txt_lst_ver.append('Minimum petal width: ' + str(df['petal_width'][50:100].min()))
txt_lst_ver.append('Maximum sepal length: ' + str(df['sepal_length'][50:100].max()))
txt_lst_ver.append('Maximum sepal width: ' + str(df['sepal_width'][50:100].max()))
txt_lst_ver.append('Maximum petal length: ' + str(df['petal_length'][50:100].max()))
txt_lst_ver.append('Maximum petal width: ' + str(df['petal_width'][50:100].max()))
txt_lst_ver.append('Average sepal length: ' + str(round(df['sepal_length'][50:100].mean(), 1)))
txt_lst_ver.append('Average sepal width: ' + str(round(df['sepal_width'][50:100].mean(), 1)))
txt_lst_ver.append('Average petal length: ' + str(round(df['petal_length'][50:100].mean(), 1)))
txt_lst_ver.append('Average petal width: ' + str(round(df['petal_width'][50:100].mean(), 1)))

#Uses the min, max and mean functions and appends the string to a list
txt_lst_vir.append('Minimum sepal length: ' + str(df['sepal_length'][100:].min()))
txt_lst_vir.append('Minimum sepal width: ' + str(df['sepal_width'][100:].min()))
txt_lst_vir.append('Minimum petal length: ' + str(df['petal_length'][100:].min()))
txt_lst_vir.append('Minimum petal width: ' + str(df['petal_width'][100:].min()))
txt_lst_vir.append('Maximum sepal length: ' + str(df['sepal_length'][100:].max()))
txt_lst_vir.append('Maximum sepal width: ' + str(df['sepal_width'][100:].max()))
txt_lst_vir.append('Maximum petal length: ' + str(df['petal_length'][100:].max()))
txt_lst_vir.append('Maximum petal width: ' + str(df['petal_width'][100:].max()))
txt_lst_vir.append('Average sepal length: ' + str(round(df['sepal_length'][100:].mean(), 1)))
txt_lst_vir.append('Average sepal width: ' + str(round(df['sepal_width'][100:].mean(), 1)))
txt_lst_vir.append('Average petal length: ' + str(round(df['petal_length'][100:].mean(), 1)))
txt_lst_vir.append('Average petal width: ' + str(round(df['petal_width'][100:].mean(), 1)))

#Creats a text file and writes each list in turn
with open('summary.py', 'w') as f:
    
    f.write('ALL SPECIES:\n')

    for val in txt_lst_tot:
        f.write(val + '\n')

    f.write('\nSETOSA:\n')    

    for val in txt_lst_set:
        f.write(val + '\n')

    f.write('\nVERSICOLOR:\n')

    for val in txt_lst_ver:
        f.write(val + '\n')

    f.write('\nVIRGINICA:\n')

    for val in txt_lst_vir:
        f.write(val + '\n')

f.close()

data_set = np.genfromtxt('iris_data.csv', delimiter=',')

col_1 = data_set[:,0]

pl.hist(col_1)
pl.title('Sepal Length')
pl.xlabel("Centimetres")
pl.ylabel("Frequency")
pl.grid(which='major', axis='both')
pl.show()

col_2 = data_set[:,1]

pl.hist(col_2)
pl.title('Sepal Width')
pl.xlabel("Centimetres")
pl.ylabel("Frequency")
pl.grid(which='major', axis='both')
pl.show()

col_3 = data_set[:,2]

pl.hist(col_3)
pl.title('Petal Length')
pl.xlabel("Centimetres")
pl.ylabel("Frequency")
pl.grid(which='major', axis='both')
pl.show()

col_4 = data_set[:,3]

pl.hist(col_4)
pl.title('Petal Width')
pl.xlabel("Centimetres")
pl.ylabel("Frequency")
pl.grid(which='major', axis='both')
pl.show()