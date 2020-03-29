# Programming and Scripting Project
## Problem Statement
This project concerns the well-known Fisher's Iris data set. You must research the data set and write documentation and code in Python to investigate it. An online search for information on the data set will convince you that many people have investigated it previously. You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed.

## Summary of Fisher's Iris Data Set

![Ronald Fischer](Ronald_Fisher.jpg)

Sir Ronald Fisher (1890-1962) was a British statistician and geneticist, and has been described as "the single most important figure in 20th century statistics". In 1936 he introducted the multivariate data set referred to as the Iris flower data set, or Fisher's Iris data set, in his paper *The use of multiple measurements in taxonomic problems* as an example of linear discriminant analysis. It is sometimes referred to as Anderson's Iris data set, as it was Edgar Anderson who collected the data to quantify the morphologic variation of Iris flowers of three related species. There are 150 rows of data in the data set, with each row representing an iris flower. [Ref: Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)    

![Iris Species](Iris_Species.png)

The images above show the three species included in the data set: setosa, virginica and versicolor. The data set comprises 50 records of each species with their botanical dimensions, sepal and petal, on each row. The sepal is described as the part of the flower with angiosperms (flowering plants). Sepals typically function as protection for the flower in bud, and often as support for the petals when in bloom. [Ref: Sepal](https://en.wikipedia.org/wiki/Sepal) Petals are described as modified leaves that surround the reproductive parts of flowers. They are often brightly coloured or unusually shaped to attract pollinators. [Ref: Petal](https://en.wikipedia.org/wiki/Petal)

![Neural Network](Neural_Network.png)

Although the initial purpose of the data set was to identify the botanical variations of Iris flowers, it has since become a staple test case in computer science. It is a well-known data set which programmers repeatedly use as input to examine how various technologies sort and handle data sets. [Ref: Alternative uses](https://www.techopedia.com/definition/32880/iris-flower-data-set) The data set is often used in data mining, classification and clustering examples. [Ref: Visualising and understanding Iris dataset](https://mc.ai/visualization-and-understanding-iris-dataset/). The diagram above illustrates a neural network used in machine learning to categorize Iris flowers by species. [Ref: Machine learning](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough) The table below comprises the 150 samples, which include the sepal length, sepal width, petal length, petal width, and species of each record.

|Sepal Length | Sepal Width | Petal Length | Petal Width | Species |
| --- | --- | --- | --- | --- |
5.1 | 3.5 | 1.4 | 0.2 | setosa
4.9 | 3.0 | 1.4 | 0.2 | setosa
4.7 | 3.2 | 1.3 | 0.2 | setosa
4.6 | 3.1 | 1.5 | 0.2 | setosa
5.0 | 3.6 | 1.4 | 0.2 | setosa
5.4 | 3.9 | 1.7 | 0.4 | setosa
4.6 | 3.4 | 1.4 | 0.3 | setosa
5.0 | 3.4 | 1.5 | 0.2 | setosa
4.4 | 2.9 | 1.4 | 0.2 | setosa
4.9 | 3.1 | 1.5 | 0.1 | setosa
5.4 | 3.7 | 1.5 | 0.2 | setosa
4.8 | 3.4 | 1.6 | 0.2 | setosa
4.8 | 3.0 | 1.4 | 0.1 | setosa
4.3 | 3.0 | 1.1 | 0.1 | setosa
5.8 | 4.0 | 1.2 | 0.2 | setosa
5.7 | 4.4 | 1.5 | 0.4 | setosa
5.4 | 3.9 | 1.3 | 0.4 | setosa
5.1 | 3.5 | 1.4 | 0.3 | setosa
5.7 | 3.8 | 1.7 | 0.3 | setosa
5.1 | 3.8 | 1.5 | 0.3 | setosa
5.4 | 3.4 | 1.7 | 0.2 | setosa
5.1 | 3.7 | 1.5 | 0.4 | setosa
4.6 | 3.6 | 1.0 | 0.2 | setosa
5.1 | 3.3 | 1.7 | 0.5 | setosa
4.8 | 3.4 | 1.9 | 0.2 | setosa
5.0 | 3.0 | 1.6 | 0.2 | setosa
5.0 | 3.4 | 1.6 | 0.4 | setosa
5.2 | 3.5 | 1.5 | 0.2 | setosa
5.2 | 3.4 | 1.4 | 0.2 | setosa
4.7 | 3.2 | 1.6 | 0.2 | setosa
4.8 | 3.1 | 1.6 | 0.2 | setosa
5.4 | 3.4 | 1.5 | 0.4 | setosa
5.2 | 4.1 | 1.5 | 0.1 | setosa
5.5 | 4.2 | 1.4 | 0.2 | setosa
4.9 | 3.1 | 1.5 | 0.1 | setosa
5.0 | 3.2 | 1.2 | 0.2 | setosa
5.5 | 3.5 | 1.3 | 0.2 | setosa
4.9 | 3.1 | 1.5 | 0.1 | setosa
4.4 | 3.0 | 1.3 | 0.2 | setosa
5.1 | 3.4 | 1.5 | 0.2 | setosa
5.0 | 3.5 | 1.3 | 0.3 | setosa
4.5 | 2.3 | 1.3 | 0.3 | setosa
4.4 | 3.2 | 1.3 | 0.2 | setosa
5.0 | 3.5 | 1.6 | 0.6 | setosa
5.1 | 3.8 | 1.9 | 0.4 | setosa
4.8 | 3.0 | 1.4 | 0.3 | setosa
5.1 | 3.8 | 1.6 | 0.2 | setosa
4.6 | 3.2 | 1.4 | 0.2 | setosa
5.3 | 3.7 | 1.5 | 0.2 | setosa
5.0 | 3.3 | 1.4 | 0.2 | setosa
7.0 | 3.2 | 4.7 | 1.4 | versicolor
6.4 | 3.2 | 4.5 | 1.5 | versicolor
6.9 | 3.1 | 4.9 | 1.5 | versicolor
5.5 | 2.3 | 4.0 | 1.3 | versicolor
6.5 | 2.8 | 4.6 | 1.5 | versicolor
5.7 | 2.8 | 4.5 | 1.3 | versicolor
6.3 | 3.3 | 4.7 | 1.6 | versicolor
4.9 | 2.4 | 3.3 | 1.0 | versicolor
6.6 | 2.9 | 4.6 | 1.3 | versicolor
5.2 | 2.7 | 3.9 | 1.4 | versicolor
5.0 | 2.0 | 3.5 | 1.0 | versicolor
5.9 | 3.0 | 4.2 | 1.5 | versicolor
6.0 | 2.2 | 4.0 | 1.0 | versicolor
6.1 | 2.9 | 4.7 | 1.4 | versicolor
5.6 | 2.9 | 3.6 | 1.3 | versicolor
6.7 | 3.1 | 4.4 | 1.4 | versicolor
5.6 | 3.0 | 4.5 | 1.5 | versicolor
5.8 | 2.7 | 4.1 | 1.0 | versicolor
6.2 | 2.2 | 4.5 | 1.5 | versicolor
5.6 | 2.5 | 3.9 | 1.1 | versicolor
5.9 | 3.2 | 4.8 | 1.8 | versicolor
6.1 | 2.8 | 4.0 | 1.3 | versicolor
6.3 | 2.5 | 4.9 | 1.5 | versicolor
6.1 | 2.8 | 4.7 | 1.2 | versicolor
6.4 | 2.9 | 4.3 | 1.3 | versicolor
6.6 | 3.0 | 4.4 | 1.4 | versicolor
6.8 | 2.8 | 4.8 | 1.4 | versicolor
6.7 | 3.0 | 5.0 | 1.7 | versicolor
6.0 | 2.9 | 4.5 | 1.5 | versicolor
5.7 | 2.6 | 3.5 | 1.0 | versicolor
5.5 | 2.4 | 3.8 | 1.1 | versicolor
5.5 | 2.4 | 3.7 | 1.0 | versicolor
5.8 | 2.7 | 3.9 | 1.2 | versicolor
6.0 | 2.7 | 5.1 | 1.6 | versicolor
5.4 | 3.0 | 4.5 | 1.5 | versicolor
6.0 | 3.4 | 4.5 | 1.6 | versicolor
6.7 | 3.1 | 4.7 | 1.5 | versicolor
6.3 | 2.3 | 4.4 | 1.3 | versicolor
5.6 | 3.0 | 4.1 | 1.3 | versicolor
5.5 | 2.5 | 4.0 | 1.3 | versicolor
5.5 | 2.6 | 4.4 | 1.2 | versicolor
6.1 | 3.0 | 4.6 | 1.4 | versicolor
5.8 | 2.6 | 4.0 | 1.2 | versicolor
5.0 | 2.3 | 3.3 | 1.0 | versicolor
5.6 | 2.7 | 4.2 | 1.3 | versicolor
5.7 | 3.0 | 4.2 | 1.2 | versicolor
5.7 | 2.9 | 4.2 | 1.3 | versicolor
6.2 | 2.9 | 4.3 | 1.3 | versicolor
5.1 | 2.5 | 3.0 | 1.1 | versicolor
5.7 | 2.8 | 4.1 | 1.3 | versicolor
6.3 | 3.3 | 6.0 | 2.5 | virginica
5.8 | 2.7 | 5.1 | 1.9 | virginica
7.1 | 3.0 | 5.9 | 2.1 | virginica
6.3 | 2.9 | 5.6 | 1.8 | virginica
6.5 | 3.0 | 5.8 | 2.2 | virginica
7.6 | 3.0 | 6.6 | 2.1 | virginica
4.9 | 2.5 | 4.5 | 1.7 | virginica
7.3 | 2.9 | 6.3 | 1.8 | virginica
6.7 | 2.5 | 5.8 | 1.8 | virginica
7.2 | 3.6 | 6.1 | 2.5 | virginica
6.5 | 3.2 | 5.1 | 2.0 | virginica
6.4 | 2.7 | 5.3 | 1.9 | virginica
6.8 | 3.0 | 5.5 | 2.1 | virginica
5.7 | 2.5 | 5.0 | 2.0 | virginica
5.8 | 2.8 | 5.1 | 2.4 | virginica
6.4 | 3.2 | 5.3 | 2.3 | virginica
6.5 | 3.0 | 5.5 | 1.8 | virginica
7.7 | 3.8 | 6.7 | 2.2 | virginica
7.7 | 2.6 | 6.9 | 2.3 | virginica
6.0 | 2.2 | 5.0 | 1.5 | virginica
6.9 | 3.2 | 5.7 | 2.3 | virginica
5.6 | 2.8 | 4.9 | 2.0 | virginica
7.7 | 2.8 | 6.7 | 2.0 | virginica
6.3 | 2.7 | 4.9 | 1.8 | virginica
6.7 | 3.3 | 5.7 | 2.1 | virginica
7.2 | 3.2 | 6.0 | 1.8 | virginica
6.2 | 2.8 | 4.8 | 1.8 | virginica
6.1 | 3.0 | 4.9 | 1.8 | virginica
6.4 | 2.8 | 5.6 | 2.1 | virginica
7.2 | 3.0 | 5.8 | 1.6 | virginica
7.4 | 2.8 | 6.1 | 1.9 | virginica
7.9 | 3.8 | 6.4 | 2.0 | virginica
6.4 | 2.8 | 5.6 | 2.2 | virginica
6.3 | 2.8 | 5.1 | 1.5 | virginica
6.1 | 2.6 | 5.6 | 1.4 | virginica
7.7 | 3.0 | 6.1 | 2.3 | virginica
6.3 | 3.4 | 5.6 | 2.4 | virginica
6.4 | 3.1 | 5.5 | 1.8 | virginica
6.0 | 3.0 | 4.8 | 1.8 | virginica
6.9 | 3.1 | 5.4 | 2.1 | virginica
6.7 | 3.1 | 5.6 | 2.4 | virginica
6.9 | 3.1 | 5.1 | 2.3 | virginica
5.8 | 2.7 | 5.1 | 1.9 | virginica
6.8 | 3.2 | 5.9 | 2.3 | virginica
6.7 | 3.3 | 5.7 | 2.5 | virginica
6.7 | 3.0 | 5.2 | 2.3 | virginica
6.3 | 2.5 | 5.0 | 1.9 | virginica
6.5 | 3.0 | 5.2 | 2.0 | virginica
6.2 | 3.4 | 5.4 | 2.3 | virginica
5.9 | 3.0 | 5.1 | 1.8 | virginica

## References

Iris flower data set available at: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

Wikipedia contributors. "Iris flower data set" Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 27 Feb. 2020. Web. 27 Feb 2020.< https://en.wikipedia.org/wiki/Iris_flower_data_set

Wikipedia contributors. "Petal" Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 28 Mar. 2020. Web. 28 Mar. 2020.< https://en.wikipedia.org/wiki/Petal

Wikipedia contributors. "Sepal" Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 28 Mar. 2020. Web. 28 Mar. 2020.<
https://en.wikipedia.org/wiki/Sepal

Alternative uses of the Iris flower data set available at: https://www.techopedia.com/definition/32880/iris-flower-data-set

Visualising and understanding the Iris dataset available at: https://mc.ai/visualization-and-understanding-iris-dataset/

Using machine learning to categorise Iris flowers available at: https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)