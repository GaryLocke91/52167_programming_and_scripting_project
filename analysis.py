import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sn

#Reads the file into DataFrame
#https://pandas.pydata.org/pandas-docs/version/0.21.1/generated/pandas.read_csv.html
df = pd.read_csv('iris_data.csv')

#Creates empty lists for the overall data set and individual species
#To be populated with strings to be written to file
lst_tot = []
lst_set = []
lst_ver = []
lst_vir = []

#Applies the min, max and mean functions on each column and appends the string to the total list
lst_tot.append('Minimum sepal length: ' + str(df['sepal_length'].min()))
lst_tot.append('Minimum sepal width: ' + str(df['sepal_width'].min()))
lst_tot.append('Minimum petal length: ' + str(df['petal_length'].min()))
lst_tot.append('Minimum petal width: ' + str(df['petal_width'].min()))
lst_tot.append('Maximum sepal length: ' + str(df['sepal_length'].max()))
lst_tot.append('Maximum sepal width: ' + str(df['sepal_width'].max()))
lst_tot.append('Maximum petal length: ' + str(df['petal_length'].max()))
lst_tot.append('Maximum petal width: ' + str(df['petal_width'].max()))
lst_tot.append('Average sepal length: ' + str(round(df['sepal_length'].mean(), 1)))
lst_tot.append('Average sepal width: ' + str(round(df['sepal_width'].mean(), 1)))
lst_tot.append('Average petal length: ' + str(round(df['petal_length'].mean(), 1)))
lst_tot.append('Average petal width: ' + str(round(df['petal_width'].mean(), 1)))

#Applies the min, max and mean functions on each colum and appends the string to the setosa list
lst_set.append('Minimum sepal length: ' + str(df['sepal_length'][0:50].min()))
lst_set.append('Minimum sepal width: ' + str(df['sepal_width'][0:50].min()))
lst_set.append('Minimum petal length: ' + str(df['petal_length'][0:50].min()))
lst_set.append('Minimum petal width: ' + str(df['petal_width'][0:50].min()))
lst_set.append('Maximum sepal length: ' + str(df['sepal_length'][0:50].max()))
lst_set.append('Maximum sepal width: ' + str(df['sepal_width'][0:50].max()))
lst_set.append('Maximum petal length: ' + str(df['petal_length'][0:50].max()))
lst_set.append('Maximum petal width: ' + str(df['petal_width'][0:50].max()))
lst_set.append('Average sepal length: ' + str(round(df['sepal_length'][0:50].mean(), 1)))
lst_set.append('Average sepal width: ' + str(round(df['sepal_width'][0:50].mean(), 1)))
lst_set.append('Average petal length: ' + str(round(df['petal_length'][0:50].mean(), 1)))
lst_set.append('Average petal width: ' + str(round(df['petal_width'][0:50].mean(), 1)))

#Applies the min, max and mean functions on each colum and appends the string to the versicolor list
lst_ver.append('Minimum sepal length: ' + str(df['sepal_length'][50:100].min()))
lst_ver.append('Minimum sepal width: ' + str(df['sepal_width'][50:100].min()))
lst_ver.append('Minimum petal length: ' + str(df['petal_length'][50:100].min()))
lst_ver.append('Minimum petal width: ' + str(df['petal_width'][50:100].min()))
lst_ver.append('Maximum sepal length: ' + str(df['sepal_length'][50:100].max()))
lst_ver.append('Maximum sepal width: ' + str(df['sepal_width'][50:100].max()))
lst_ver.append('Maximum petal length: ' + str(df['petal_length'][50:100].max()))
lst_ver.append('Maximum petal width: ' + str(df['petal_width'][50:100].max()))
lst_ver.append('Average sepal length: ' + str(round(df['sepal_length'][50:100].mean(), 1)))
lst_ver.append('Average sepal width: ' + str(round(df['sepal_width'][50:100].mean(), 1)))
lst_ver.append('Average petal length: ' + str(round(df['petal_length'][50:100].mean(), 1)))
lst_ver.append('Average petal width: ' + str(round(df['petal_width'][50:100].mean(), 1)))

#Applies the min, max and mean functions on each colum and appends the string to the virginica list
lst_vir.append('Minimum sepal length: ' + str(df['sepal_length'][100:].min()))
lst_vir.append('Minimum sepal width: ' + str(df['sepal_width'][100:].min()))
lst_vir.append('Minimum petal length: ' + str(df['petal_length'][100:].min()))
lst_vir.append('Minimum petal width: ' + str(df['petal_width'][100:].min()))
lst_vir.append('Maximum sepal length: ' + str(df['sepal_length'][100:].max()))
lst_vir.append('Maximum sepal width: ' + str(df['sepal_width'][100:].max()))
lst_vir.append('Maximum petal length: ' + str(df['petal_length'][100:].max()))
lst_vir.append('Maximum petal width: ' + str(df['petal_width'][100:].max()))
lst_vir.append('Average sepal length: ' + str(round(df['sepal_length'][100:].mean(), 1)))
lst_vir.append('Average sepal width: ' + str(round(df['sepal_width'][100:].mean(), 1)))
lst_vir.append('Average petal length: ' + str(round(df['petal_length'][100:].mean(), 1)))
lst_vir.append('Average petal width: ' + str(round(df['petal_width'][100:].mean(), 1)))

#Creats a writable text file and writes each element of each list in turn
with open('summary.py', 'w') as f:
    
    f.write('ALL SPECIES:\n')

    for val in lst_tot:
        f.write(val + '\n')

    f.write('\nSETOSA:\n')    

    for val in lst_set:
        f.write(val + '\n')

    f.write('\nVERSICOLOR:\n')

    for val in lst_ver:
        f.write(val + '\n')

    f.write('\nVIRGINICA:\n')

    for val in lst_vir:
        f.write(val + '\n')

f.close()

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
data_set = np.genfromtxt('iris_data.csv', delimiter=',', skip_header=1)

#http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html 
col_1 = data_set[:,0]
pl.hist(col_1, bins=20, color='#3F5D7D')
pl.title('Sepal Length', fontsize=16)
pl.xlabel('Length (cm)')
pl.ylabel('Frequency')
pl.show()

col_2 = data_set[:,1]
pl.hist(col_2, bins=20, color='#5c3f7d')
pl.title('Sepal Width', fontsize=16)
pl.xlabel('Width (cm)')
pl.ylabel('Frequency')
pl.show()

col_3 = data_set[:,2]
pl.hist(col_3, bins=20, color='#396131')
pl.title('Petal Length', fontsize=16)
pl.xlabel('Length (cm)')
pl.ylabel('Frequency')
pl.show()

col_4 = data_set[:,3]
pl.hist(col_4, bins=20, color='#80451f')
pl.title('Petal Width', fontsize=16)
pl.xlabel('Width (cm)')
pl.ylabel('Frequency')

pl.show()

'''
iris = pd.read_csv('iris_data.csv')
iris['Sepal Length (cm)'] = iris['sepal_length']
iris['Sepal Width (cm)'] = iris['sepal_width']
sn.lmplot(x='Sepal Length (cm)', y='Sepal Width (cm)', data=iris, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.title('Sepal Length vs. Sepal Width')
pl.show()

iris['Petal Length (cm)'] = iris['petal_length']
iris['Petal Width (cm)'] = iris['petal_width']
sn.lmplot(x='Petal Length (cm)', y='Petal Width (cm)', data=iris, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.title('Petal Length vs. Petal Width')
pl.show()

iris['Sepal Length (cm)'] = iris['sepal_length']
iris['Petal Length (cm)'] = iris['petal_length']
sn.lmplot(x='Sepal Length (cm)', y='Petal Length (cm)', data=iris, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.title('Sepal Length vs. Petal Length')
pl.show()

iris['Sepal Width (cm)'] = iris['sepal_width']
iris['Petal Width (cm)'] = iris['petal_width']
sn.lmplot(x='Sepal Width (cm)', y='Petal Width (cm)', data=iris, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.title('Sepal Width vs. Petal Width')
pl.show()

iris['Sepal Width (cm)'] = iris['sepal_width']
iris['Petal Length (cm)'] = iris['petal_length']
sn.lmplot(x='Sepal Width (cm)', y='Petal Length (cm)', data=iris, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.title('Sepal Width vs. Petal Length')
pl.show()

iris['Sepal Length (cm)'] = iris['sepal_length']
iris['Petal Width (cm)'] = iris['petal_width']
sn.lmplot(x='Sepal Length (cm)', y='Petal Width (cm)', data=iris, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.title('Sepal Length vs. Petal Width')
pl.show()
'''