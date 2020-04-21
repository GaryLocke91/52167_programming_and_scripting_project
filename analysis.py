#Gary Locke, 11-04-2020
#A program that analyses Fisher's Iris Data Set

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sn

#Reads the file into DataFrame
df = pd.read_csv('iris_data.csv')

#Creates empty lists for the overall data set and individual species
#To be populated with strings to be written to file
lst_tot = []
lst_set = []
lst_ver = []
lst_vir = []

#Applies the min, max mean, and standard deviation functions on each column and appends the string to the total list
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
lst_tot.append('Standard deviation of sepal length: ' + str(round(df['sepal_length'].std(), 1)))
lst_tot.append('Standard deviation of sepal width: ' + str(round(df['sepal_width'].std(), 1)))
lst_tot.append('Standard deviation of petal length: ' + str(round(df['petal_length'].std(), 1)))
lst_tot.append('Standard deviation of petal width: ' + str(round(df['petal_width'].std(), 1)))

#Applies the min, max, mean, and standard deviation functions on each colum and appends the string to the setosa list
lst_set.append('Minimum sepal length: ' + str(df['sepal_length'][:50].min()))
lst_set.append('Minimum sepal width: ' + str(df['sepal_width'][:50].min()))
lst_set.append('Minimum petal length: ' + str(df['petal_length'][:50].min()))
lst_set.append('Minimum petal width: ' + str(df['petal_width'][:50].min()))
lst_set.append('Maximum sepal length: ' + str(df['sepal_length'][:50].max()))
lst_set.append('Maximum sepal width: ' + str(df['sepal_width'][:50].max()))
lst_set.append('Maximum petal length: ' + str(df['petal_length'][:50].max()))
lst_set.append('Maximum petal width: ' + str(df['petal_width'][:50].max()))
lst_set.append('Average sepal length: ' + str(round(df['sepal_length'][:50].mean(), 1)))
lst_set.append('Average sepal width: ' + str(round(df['sepal_width'][:50].mean(), 1)))
lst_set.append('Average petal length: ' + str(round(df['petal_length'][:50].mean(), 1)))
lst_set.append('Average petal width: ' + str(round(df['petal_width'][:50].mean(), 1)))
lst_set.append('Standard deviation of sepal length: ' + str(round(df['sepal_length'][:50].std(), 1)))
lst_set.append('Standard deviation of sepal width: ' + str(round(df['sepal_width'][:50].std(), 1)))
lst_set.append('Standard deviation of petal length: ' + str(round(df['petal_length'][:50].std(), 1)))
lst_set.append('Standard deviation of petal width: ' + str(round(df['petal_width'][:50].std(), 1)))

#Applies the min, max, mean, and standard deviation functions on each colum and appends the string to the versicolor list
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
lst_ver.append('Standard deviation of sepal length: ' + str(round(df['sepal_length'][50:100].std(), 1)))
lst_ver.append('Standard deviation of sepal width: ' + str(round(df['sepal_width'][50:100].std(), 1)))
lst_ver.append('Standard deviation of petal length: ' + str(round(df['petal_length'][50:100].std(), 1)))
lst_ver.append('Standard deviation of petal width: ' + str(round(df['petal_width'][50:100].std(), 1)))

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
lst_vir.append('Standard deviation of sepal length: ' + str(round(df['sepal_length'][100:].std(), 1)))
lst_vir.append('Standard deviation of sepal width: ' + str(round(df['sepal_width'][100:].std(), 1)))
lst_vir.append('Standard deviation of petal length: ' + str(round(df['petal_length'][100:].std(), 1)))
lst_vir.append('Standard deviation of petal width: ' + str(round(df['petal_width'][100:].std(), 1)))

#Creats a writable text file and writes each element of each list in turn
with open('summary.txt', 'w') as f:
    
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

#Reads the file, separates the values using a comma as the delimiter and excludes the headers
data_set = np.genfromtxt('iris_data.csv', delimiter=',', skip_header=1)

#Creates a histogram for sepal length 
col_1 = data_set[:,0]
pl.hist(col_1, bins=20, color='#3F5D7D')
pl.title('Sepal Length', fontsize=16)
pl.grid(which='major', axis='y')
pl.xlabel('Length (cm)')
pl.ylabel('Frequency')
pl.show()

#Creates a histogram for sepal width
col_2 = data_set[:,1]
pl.hist(col_2, bins=20, color='#3F5D7D')
pl.title('Sepal Width', fontsize=16)
pl.grid(which='major', axis='y')
pl.xlabel('Width (cm)')
pl.ylabel('Frequency')
pl.show()

#Creates a histogram for petal length
col_3 = data_set[:,2]
pl.hist(col_3, bins=20, color='#3F5D7D')
pl.title('Petal Length', fontsize=16)
pl.grid(which='major', axis='y')
pl.xlabel('Length (cm)')
pl.ylabel('Frequency')
pl.show()

#Creates a histogram for petal width
col_4 = data_set[:,3]
pl.hist(col_4, bins=20, color='#3F5D7D')
pl.title('Petal Width', fontsize=16)
pl.grid(which='major', axis='y')
pl.xlabel('Width (cm)')
pl.ylabel('Frequency')
pl.show()

#Reads the file into DataFrame
iris_data = pd.read_csv('iris_data.csv')

#Creates a scatterplot for sepal length vs. sepal width
iris_data['Sepal Length (cm)'] = iris_data['sepal_length']
iris_data['Sepal Width (cm)'] = iris_data['sepal_width']
sn.lmplot(x='Sepal Length (cm)', y='Sepal Width (cm)', data=iris_data, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.suptitle('Sepal Length vs. Sepal Width', fontsize=16)
pl.subplots_adjust(top=0.9)
pl.show()

#Creates a scatterplot for petal length vs. petal width
iris_data['Petal Length (cm)'] = iris_data['petal_length']
iris_data['Petal Width (cm)'] = iris_data['petal_width']
sn.lmplot(x='Petal Length (cm)', y='Petal Width (cm)', data=iris_data, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.suptitle('Petal Length vs. Petal Width', fontsize=16)
pl.subplots_adjust(top=0.9)
pl.show()

#Creates a scatterplot for sepal length vs. petal length
iris_data['Sepal Length (cm)'] = iris_data['sepal_length']
iris_data['Petal Length (cm)'] = iris_data['petal_length']
sn.lmplot(x='Sepal Length (cm)', y='Petal Length (cm)', data=iris_data, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.suptitle('Sepal Length vs. Petal Length', fontsize=16)
pl.subplots_adjust(top=0.9)
pl.show()

#Creates a scatterplot for sepal width vs. petal width
iris_data['Sepal Width (cm)'] = iris_data['sepal_width']
iris_data['Petal Width (cm)'] = iris_data['petal_width']
sn.lmplot(x='Sepal Width (cm)', y='Petal Width (cm)', data=iris_data, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.suptitle('Sepal Width vs. Petal Width', fontsize=16)
pl.subplots_adjust(top=0.9)
pl.show()

#Creates a scatterplot for sepal width vs. petal length
iris_data['Sepal Width (cm)'] = iris_data['sepal_width']
iris_data['Petal Length (cm)'] = iris_data['petal_length']
sn.lmplot(x='Sepal Width (cm)', y='Petal Length (cm)', data=iris_data, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.suptitle('Sepal Width vs. Petal Length', fontsize=16)
pl.subplots_adjust(top=0.9)
pl.show()

#Creates a scatterplot for sepal length vs. petal width
iris_data['Sepal Length (cm)'] = iris_data['sepal_length']
iris_data['Petal Width (cm)'] = iris_data['petal_width']
sn.lmplot(x='Sepal Length (cm)', y='Petal Width (cm)', data=iris_data, hue='species', fit_reg=False, legend=False)
pl.legend()
pl.grid(which='major', axis='both')
pl.suptitle('Sepal Length vs. Petal Width', fontsize=16)
pl.subplots_adjust(top=0.9)
pl.show()

#Creates a scatterplot matrix for all variables
header_lst = ['Sepal Length (cm)', 'Sepal Width (cm)', 'Petal Length (cm)', 'Petal Width (cm)', 'Species']
iris_data = pd.read_csv('iris_data.csv', skiprows=1, names=header_lst)

g = sn.pairplot(iris_data, hue='Species', markers='+')
g.fig.suptitle("Fisher's Iris Data Set", size=16)
g.fig.subplots_adjust(top=.9)
g._legend.get_title().set_fontsize(12)
pl.show()