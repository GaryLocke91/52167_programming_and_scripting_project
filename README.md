# Programming and Scripting Project
## Problem Statement
This project concerns the well-known Fisher's Iris data set. You must research the data set and write documentation and code in Python to investigate it. An online search for information on the data set will convince you that many people have investigated it previously. You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed.

**1. Summary**

![Ronald Fischer](Ronald_Fisher.jpg)

Sir Ronald Fisher (1890-1962) was a British statistician and geneticist, and has been described as "the single most important figure in 20th century statistics". In 1936 he introducted the multivariate data set referred to as the Iris flower data set, or Fisher's Iris data set, in his paper *The use of multiple measurements in taxonomic problems* as an example of linear discriminant analysis. It is sometimes referred to as Anderson's Iris data set, as it was Edgar Anderson who collected the data to quantify the morphologic variation of Iris flowers of three related species. There are 150 rows of data in the data set, with each row representing an iris flower. [Ref: Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)    

![Iris Species](Iris_Species.png)

The images above show the three species in the data set: Iris setosa, Iris virginica and Iris versicolor. The data set comprises 50 records of each of these species with their botanical dimensions, sepal and petal, included in each row. The sepal is described as the part of the flower with angiosperms (flowering plants). Sepals typically function as protection for the flower in bud, and often as support for the petals when in bloom. [Ref: Sepal](https://en.wikipedia.org/wiki/Sepal) Petals are described as modified leaves that surround the reproductive parts of flowers.

Although the initial purpose of the data set was to identify the botanical variations of Iris flowers, it has since become a commonly used data set for testing purposes in computer science. It is a well-known data set which programmers repeatedly use as input to examine how various technologies sort and handle data sets. It is also used for testing machine learning algorithms and visualisations. The table below comprises the 150 samples, which include the sepal length, sepal width, petal length, petal width, and species of each record.

|sepal_length | sepal_width | petal_length | petal_width | species |
| --- | --- | --- | --- | --- |
5.1 | 3.5 | 1.4 | 0.2 | Iris-setosa
4.9 | 3.0 | 1.4 | 0.2 | Iris-setosa
4.7 | 3.2 | 1.3 | 0.2 | Iris-setosa
4.6 | 3.1 | 1.5 | 0.2 | Iris-setosa
5.0 | 3.6 | 1.4 | 0.2 | Iris-setosa
5.4 | 3.9 | 1.7 | 0.4 | Iris-setosa
4.6 | 3.4 | 1.4 | 0.3 | Iris-setosa
5.0 | 3.4 | 1.5 | 0.2 | Iris-setosa
4.4 | 2.9 | 1.4 | 0.2 | Iris-setosa
4.9 | 3.1 | 1.5 | 0.1 | Iris-setosa
5.4 | 3.7 | 1.5 | 0.2 | Iris-setosa
4.8 | 3.4 | 1.6 | 0.2 | Iris-setosa
4.8 | 3.0 | 1.4 | 0.1 | Iris-setosa
4.3 | 3.0 | 1.1 | 0.1 | Iris-setosa
5.8 | 4.0 | 1.2 | 0.2 | Iris-setosa
5.7 | 4.4 | 1.5 | 0.4 | Iris-setosa
5.4 | 3.9 | 1.3 | 0.4 | Iris-setosa
5.1 | 3.5 | 1.4 | 0.3 | Iris-setosa
5.7 | 3.8 | 1.7 | 0.3 | Iris-setosa
5.1 | 3.8 | 1.5 | 0.3 | Iris-setosa
5.4 | 3.4 | 1.7 | 0.2 | Iris-setosa
5.1 | 3.7 | 1.5 | 0.4 | Iris-setosa
4.6 | 3.6 | 1.0 | 0.2 | Iris-setosa
5.1 | 3.3 | 1.7 | 0.5 | Iris-setosa
4.8 | 3.4 | 1.9 | 0.2 | Iris-setosa
5.0 | 3.0 | 1.6 | 0.2 | Iris-setosa
5.0 | 3.4 | 1.6 | 0.4 | Iris-setosa
5.2 | 3.5 | 1.5 | 0.2 | Iris-setosa
5.2 | 3.4 | 1.4 | 0.2 | Iris-setosa
4.7 | 3.2 | 1.6 | 0.2 | Iris-setosa
4.8 | 3.1 | 1.6 | 0.2 | Iris-setosa
5.4 | 3.4 | 1.5 | 0.4 | Iris-setosa
5.2 | 4.1 | 1.5 | 0.1 | Iris-setosa
5.5 | 4.2 | 1.4 | 0.2 | Iris-setosa
4.9 | 3.1 | 1.5 | 0.1 | Iris-setosa
5.0 | 3.2 | 1.2 | 0.2 | Iris-setosa
5.5 | 3.5 | 1.3 | 0.2 | Iris-setosa
4.9 | 3.1 | 1.5 | 0.1 | Iris-setosa
4.4 | 3.0 | 1.3 | 0.2 | Iris-setosa
5.1 | 3.4 | 1.5 | 0.2 | Iris-setosa
5.0 | 3.5 | 1.3 | 0.3 | Iris-setosa
4.5 | 2.3 | 1.3 | 0.3 | Iris-setosa
4.4 | 3.2 | 1.3 | 0.2 | Iris-setosa
5.0 | 3.5 | 1.6 | 0.6 | Iris-setosa
5.1 | 3.8 | 1.9 | 0.4 | Iris-setosa
4.8 | 3.0 | 1.4 | 0.3 | Iris-setosa
5.1 | 3.8 | 1.6 | 0.2 | Iris-setosa
4.6 | 3.2 | 1.4 | 0.2 | Iris-setosa
5.3 | 3.7 | 1.5 | 0.2 | Iris-setosa
5.0 | 3.3 | 1.4 | 0.2 | Iris-setosa
7.0 | 3.2 | 4.7 | 1.4 | Iris-versicolor
6.4 | 3.2 | 4.5 | 1.5 | Iris-versicolor
6.9 | 3.1 | 4.9 | 1.5 | Iris-versicolor
5.5 | 2.3 | 4.0 | 1.3 | Iris-versicolor
6.5 | 2.8 | 4.6 | 1.5 | Iris-versicolor
5.7 | 2.8 | 4.5 | 1.3 | Iris-versicolor
6.3 | 3.3 | 4.7 | 1.6 | Iris-versicolor
4.9 | 2.4 | 3.3 | 1.0 | Iris-versicolor
6.6 | 2.9 | 4.6 | 1.3 | Iris-versicolor
5.2 | 2.7 | 3.9 | 1.4 | Iris-versicolor
5.0 | 2.0 | 3.5 | 1.0 | Iris-versicolor
5.9 | 3.0 | 4.2 | 1.5 | Iris-versicolor
6.0 | 2.2 | 4.0 | 1.0 | Iris-versicolor
6.1 | 2.9 | 4.7 | 1.4 | Iris-versicolor
5.6 | 2.9 | 3.6 | 1.3 | Iris-versicolor
6.7 | 3.1 | 4.4 | 1.4 | Iris-versicolor
5.6 | 3.0 | 4.5 | 1.5 | Iris-versicolor
5.8 | 2.7 | 4.1 | 1.0 | Iris-versicolor
6.2 | 2.2 | 4.5 | 1.5 | Iris-versicolor
5.6 | 2.5 | 3.9 | 1.1 | Iris-versicolor
5.9 | 3.2 | 4.8 | 1.8 | Iris-versicolor
6.1 | 2.8 | 4.0 | 1.3 | Iris-versicolor
6.3 | 2.5 | 4.9 | 1.5 | Iris-versicolor
6.1 | 2.8 | 4.7 | 1.2 | Iris-versicolor
6.4 | 2.9 | 4.3 | 1.3 | Iris-versicolor
6.6 | 3.0 | 4.4 | 1.4 | Iris-versicolor
6.8 | 2.8 | 4.8 | 1.4 | Iris-versicolor
6.7 | 3.0 | 5.0 | 1.7 | Iris-versicolor
6.0 | 2.9 | 4.5 | 1.5 | Iris-versicolor
5.7 | 2.6 | 3.5 | 1.0 | Iris-versicolor
5.5 | 2.4 | 3.8 | 1.1 | Iris-versicolor
5.5 | 2.4 | 3.7 | 1.0 | Iris-versicolor
5.8 | 2.7 | 3.9 | 1.2 | Iris-versicolor
6.0 | 2.7 | 5.1 | 1.6 | Iris-versicolor
5.4 | 3.0 | 4.5 | 1.5 | Iris-versicolor
6.0 | 3.4 | 4.5 | 1.6 | Iris-versicolor
6.7 | 3.1 | 4.7 | 1.5 | Iris-versicolor
6.3 | 2.3 | 4.4 | 1.3 | Iris-versicolor
5.6 | 3.0 | 4.1 | 1.3 | Iris-versicolor
5.5 | 2.5 | 4.0 | 1.3 | Iris-versicolor
5.5 | 2.6 | 4.4 | 1.2 | Iris-versicolor
6.1 | 3.0 | 4.6 | 1.4 | Iris-versicolor
5.8 | 2.6 | 4.0 | 1.2 | Iris-versicolor
5.0 | 2.3 | 3.3 | 1.0 | Iris-versicolor
5.6 | 2.7 | 4.2 | 1.3 | Iris-versicolor
5.7 | 3.0 | 4.2 | 1.2 | Iris-versicolor
5.7 | 2.9 | 4.2 | 1.3 | Iris-versicolor
6.2 | 2.9 | 4.3 | 1.3 | Iris-versicolor
5.1 | 2.5 | 3.0 | 1.1 | Iris-versicolor
5.7 | 2.8 | 4.1 | 1.3 | Iris-versicolor
6.3 | 3.3 | 6.0 | 2.5 | Iris-virginica
5.8 | 2.7 | 5.1 | 1.9 | Iris-virginica
7.1 | 3.0 | 5.9 | 2.1 | Iris-virginica
6.3 | 2.9 | 5.6 | 1.8 | Iris-virginica
6.5 | 3.0 | 5.8 | 2.2 | Iris-virginica
7.6 | 3.0 | 6.6 | 2.1 | Iris-virginica
4.9 | 2.5 | 4.5 | 1.7 | Iris-virginica
7.3 | 2.9 | 6.3 | 1.8 | Iris-virginica
6.7 | 2.5 | 5.8 | 1.8 | Iris-virginica
7.2 | 3.6 | 6.1 | 2.5 | Iris-virginica
6.5 | 3.2 | 5.1 | 2.0 | Iris-virginica
6.4 | 2.7 | 5.3 | 1.9 | Iris-virginica
6.8 | 3.0 | 5.5 | 2.1 | Iris-virginica
5.7 | 2.5 | 5.0 | 2.0 | Iris-virginica
5.8 | 2.8 | 5.1 | 2.4 | Iris-virginica
6.4 | 3.2 | 5.3 | 2.3 | Iris-virginica
6.5 | 3.0 | 5.5 | 1.8 | Iris-virginica
7.7 | 3.8 | 6.7 | 2.2 | Iris-virginica
7.7 | 2.6 | 6.9 | 2.3 | Iris-virginica
6.0 | 2.2 | 5.0 | 1.5 | Iris-virginica
6.9 | 3.2 | 5.7 | 2.3 | Iris-virginica
5.6 | 2.8 | 4.9 | 2.0 | Iris-virginica
7.7 | 2.8 | 6.7 | 2.0 | Iris-virginica
6.3 | 2.7 | 4.9 | 1.8 | Iris-virginica
6.7 | 3.3 | 5.7 | 2.1 | Iris-virginica
7.2 | 3.2 | 6.0 | 1.8 | Iris-virginica
6.2 | 2.8 | 4.8 | 1.8 | Iris-virginica
6.1 | 3.0 | 4.9 | 1.8 | Iris-virginica
6.4 | 2.8 | 5.6 | 2.1 | Iris-virginica
7.2 | 3.0 | 5.8 | 1.6 | Iris-virginica
7.4 | 2.8 | 6.1 | 1.9 | Iris-virginica
7.9 | 3.8 | 6.4 | 2.0 | Iris-virginica
6.4 | 2.8 | 5.6 | 2.2 | Iris-virginica
6.3 | 2.8 | 5.1 | 1.5 | Iris-virginica
6.1 | 2.6 | 5.6 | 1.4 | Iris-virginica
7.7 | 3.0 | 6.1 | 2.3 | Iris-virginica
6.3 | 3.4 | 5.6 | 2.4 | Iris-virginica
6.4 | 3.1 | 5.5 | 1.8 | Iris-virginica
6.0 | 3.0 | 4.8 | 1.8 | Iris-virginica
6.9 | 3.1 | 5.4 | 2.1 | Iris-virginica
6.7 | 3.1 | 5.6 | 2.4 | Iris-virginica
6.9 | 3.1 | 5.1 | 2.3 | Iris-virginica
5.8 | 2.7 | 5.1 | 1.9 | Iris-virginica
6.8 | 3.2 | 5.9 | 2.3 | Iris-virginica
6.7 | 3.3 | 5.7 | 2.5 | Iris-virginica
6.7 | 3.0 | 5.2 | 2.3 | Iris-virginica
6.3 | 2.5 | 5.0 | 1.9 | Iris-virginica
6.5 | 3.0 | 5.2 | 2.0 | Iris-virginica
6.2 | 3.4 | 5.4 | 2.3 | Iris-virginica
5.9 | 3.0 | 5.1 | 1.8 | Iris-virginica

