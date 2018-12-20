# Data Science Portfolio/Projects

-------------------
###  [Books and Courses Completed]()

### Books

* Econometrics (Hanson 2018) - Great introduction to graduate econometrics [[pdf]](https://www.ssc.wisc.edu/~bhansen/econometrics/Econometrics.pdf)

* Econometric Analysis of Cross Section and Panel Data, Second Edition (Wooldridge 2010) - Standard reference that should be on every shelf [[Book Description]](https://mitpress.mit.edu/books/econometric-analysis-cross-section-and-panel-data-second-edition)

* Regression Modeling Strategies (Harrell 2001) - The first three chapters are required reading -- Frank Harrell knows his statistics. [[Book Description]](https://www.springer.com/us/book/9781441929181)

* Applied Nonparametric Econometrics (Henderson and Parmeter 2015) - Start to finish nonparametric econometrics with applications and R code [[Book Website]](http://www.the-smooth-operators.com/) [[Personal Bookdown Notes]](https://beta.rstudioconnect.com/content/1550/)

* Introduction to Statistical Learning (James et. al 2017) - Perfect introduction to statistical learning and predictions [[Book Website]](https://www-bcf.usc.edu/~gareth/ISL/) [[pdf]](https://www-bcf.usc.edu/~gareth/ISL/ISLR%20Seventh%20Printing.pdf) [[Personal Notes]](Notes-Intro-to-Stat-Learning/Notes-Intro-to-Stat-Learning.pdf) [[Python Code]](https://github.com/johnwoodill/Notes-Intro-to-Stat-Learning/tree/master/code)

* **(In Progress)** Hands on Machine Learning with Scikit-Learn and TensorFlow (Geron 2017) -  [[Book Description]](http://shop.oreilly.com/product/0636920052289.do) [[Personal Notes]](https://github.com/johnwoodill/Hands-On-ML-with-scikit-learn-and-TF/blob/master/Notes-Hands-On-ML-with-scikit-learn-and-TF.pdf) [[Github]](https://github.com/johnwoodill/Hands-On-ML-with-scikit-learn-and-TF)

### Courses

* Introduction to Data Science with R (O'Reilly 2014) [[Course Website]](https://www.oreilly.com/library/view/introduction-to-data/9781491915028/)

* [Data Camp](www.datacamp.com)
    * [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)
    * [Intermediate Python for Data Science](https://www.datacamp.com/courses/intermediate-python-for-data-science)
    * [Python Data Science Toolbox (Part 1)](https://www.datacamp.com/courses/python-data-science-toolbox-part-1)
    * [Cleaning Data in Python](https://www.datacamp.com/courses/cleaning-data-in-python)
    * [Deep Learning in Python](https://www.datacamp.com/courses/deep-learning-in-python)
    * [Supervised Learning with scikit-learn](https://www.datacamp.com/courses/supervised-learning-with-scikit-learn)
    * [Intro to SQL for Data Science](https://www.datacamp.com/courses/intro-to-sql-for-data-science)
    * **Data Camp Projects**
        * [Where Are the Fishes](https://www.datacamp.com/projects/547) - Explore acoustic backscatter data to find fish in the U.S. Atlantic Ocean.
        * [Exploring the evolution of Linus](https://www.datacamp.com/projects/111) - Find out about the development of the Linux operating system by exploring its Git repository history.
        * [Dr. Semmelweis and the Discovery of Handwashing](https://www.datacamp.com/projects/20) - Reanalyse the data behind one of the most important discoveries of modern medicine: Handwashing.

-------------------
###  [Statistical Models from Scratch]()

I find the best way to learn a specific algorithm or statistical model is to build one from scratch. The following files are classes and functions that accomplish the most common statistical learning methods on a limited level.

* Linear Regression (Gradient Descent): [LinearRegression_GD.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/LinearRegression_GD.py)

* Logistic Regression (Gradient Descent): [LogisticRegression_GD.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/LogisticRegression_GD.py)

* Decision Tree: [DecisionTree.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/DecisionTree.py)

* Random Forest: [RandomForest.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/RandomForest.py)

* KNN: [KNN.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/KNN.py)

* SVM: [SVM.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/SVM.py)

* PCA: [PCA.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/PCA.py)

* Neural Network: [NeuralNetwork.py](https://github.com/johnwoodill/Data-Science-Portfolio/blob/master/Scratch%20Models/NeuralNetwork.py)

<img src="https://github.com/johnwoodill/Data-Science-Portfolio/raw/master/figures/scratch_logo.png" width="700">

* **Keywords**(R, Python, Statistical Modeling, Algorithms)

###  [Fine Scale Weather Data from 1900-2013](https://github.com/johnwoodill/Fine-Scale-Weather-Interpolation)

* Builds daily gridded weather data for the continental United States from 1900-2013.

* Relative anomaly spline interpolation technique calculates daily weather data for 460,000 2.5km x 2.5km grids in the US. [[Tech. Example](https://github.com/johnwoodill/Data-Science-Portfolio/raw/master/docs/interpolation_technique.pdf)]

* Aggregates down to county level weather data.

* **Keywords**(R, Economics, Climate Change, Weather)

<img src="https://github.com/johnwoodill/Data-Science-Portfolio/raw/master/figures/daily_temp_spline.png" width="500">

-------------------

###  Nonlinear Temperature Distributions [[R package](https://github.com/johnwoodill/nonlineartempr)] [[Python Package](https://github.com/johnwoodill/nonlineartemppy)]

* Calcuate nonlinear temperature distributions degree days and time in each degree.

* Measure accounts for the rise and fall of temperatures during the day.

* Degree days define time above a specified temperature threshold (e.g. degree days above 30C) and time in each degree define time within a specified temperature threshold (e.g. time in 30C).

* **Keywords**(R, Python, Economics, Climate Change, Agronomy)

<img src="https://github.com/johnwoodill/US-Degree-Days-Heat-Map/raw/master/dd30.png?raw=true" width="500">

-------------------
 
###  [Business Case: Wine Quality and Price](https://www.kaggle.com/johnwoodill/business-case-predicting-quality-wine-and-prices/notebook)

* Predict wine quality based on biophysical characteristics.

* Model using Multinomial logit, Linear Discriminant Analysis, Random Forest, and Extreme Gradient Boosting


* **Keywords**(R, Classification, Economics)

<img src="https://github.com/johnwoodill/Data-Science-Portfolio/raw/master/figures/wine_quality_final_plot.png" width="500">

 -------------------
