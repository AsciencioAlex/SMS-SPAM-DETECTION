
# sms_spam_detection
It is written in Python.

Prerequisites for running this project are:

Python-2.x(used 3.9.)
Numpy-1.8.x(used 1.8.2)
scikit-learn-0.15.x(used 0.15.2)

A Machine Learning project using Python libraries to cluster a data set of 'sms' messages into 'spam' and 'ham' using k-means clustering.

The dataset is a collection of 5,574 SMS meesages taken from UCI Machine Learning repository, need to be tagged as "spam" and "ham".

The whole pipeline conists of the following steps:
1--> Loading data
2--> Data wrangling and pre-processing
3--> Feature Selection
4--> Feature Matrix Modelling
5--> k-means clustering and evaluation
6--> Saving results to a csv file

Although there are multiple methods for solving the problem, tfidf approach is employed here to obtain high prediction accuracy.

    ###################### USING WEKA #####################################

1. Install Weka using following instructions
	- You can download Weka from "http://www.cs.waikato.ac.nz/ml/weka/downloading.html".
	- Before running the setup install JRE on your machine.
	- Run the setup now to install Weka.

2. How to load file in Weka
	- Weka supports multiple file formats as input like CSV, Arff etc.
	- Go to preprocess step click on "open file" to select your input file.
	- To clean your data you can choose appropriate filter from the "Choose" dropdown list.

3. How to classify
	- Click on "classify" tab.
	- Click on "Choose" to select your classifier from the dropdown (in this case Classifier -> functions ->LibSVM)
	- Click on the textbox in front of "Choose" button, it will open a window from where you can set your parameters.
	- In this case set the "kerneltype" as "linear".
	- Set "seed" to specify number of random points to be selected in the dataset to start learning.
	- Set "cost" parameter to specify the error tolerance.
	- press ok.
	- select "cross-validation" under "Test option" and specify number of folds (in this case 5 to 15).
	- Press start to learn.

Note: while supplying data for classification remember to change the data type of the label row from NUMERIC to NOMINAL

4. How to run the spam-detector.py file 
	- Download python and install python 
	- To install the necessar packages (matplotlib, numpy, scipy and scikit-learn), 
	- Once the installation is complete,
        - open the spam-detector.py file

