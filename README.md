# ADM HW2 - Books and Authors datasets Analysis
## Group 16
### Introduction
This project was carried out by Group 16 of Algorithmic Methods for Data Mining, consisting of Gabriele (parisini.1964381@studenti.uniroma1.it), Pasquale (tommasino.1912107@studenti.uniroma1.it) and Habib (bashar.2102742@studenti.uniroma1.it). The purpose of the project is to apply different data analysis algorithms that may help discover and interpret meaningful data patterns and eventually understand how readers and authors behave.
### Datasets descripton
Four datasets, which can be downloaded on [kaggle](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries), were analyzed:
1. __`books_lighter.json`__:
   > Data related to book publications, with 7027431 records.
2. __`authors_lighter.json`__:
   > Data related to authors of books/publications, with 351767 records.
3. __`list.json`__:
   > Data related to a peculiar list named "The Worst Books of All Time", with 81512 records.
4. __`series.json`__:
   > Data related to series of books, with 226659 records.

Several questions were posed, such as:
1. Research Questions (RQ): A total of eight questions with the objective of analyzing every aspect of the __`books_lighter.json`__ and __`authors_lighter.json`__ datasets.
2. Command Line Question (CLQ): two questions with the objective of analyzing the __`series.json`__ dataset using only command line tools.
3. AWS Question (AWSQ): One question with the objective of analyzing the __`list.json`__ dataset using AWS EC2 platform: by using it, we can run complex programs that deal with large datasets using a simpler device (e.g. laptop). The instance type we used for this Homework is r7i.large running ubuntu. One of the biggest features of this platform is that we can at times increase the size and the type of the instance with our requirements.
4. Algorithmic Question (AQ): We were asked to implement an algorithm of one problem, ask ChatGPT or any other LLM chatbot tool to check code's time complexity (the Big O notation) and ask ourselves if the algorithm proposed in the first point is the optimal one or not.
 
The analysis was performed mainly on a Jupyter Notebook file. Here follows a list of the files inside the repository:
1. __`main.ipynb`__:
   > This notebook is the core file of our work. It provides both functions and code to answer Reaserch Questions (RQ), Command Line Question (CLQ), Amazon WebServices Question (AWSQ) and Algorithmic Question (AQ). There are also comments for each question written in MarkDown cells.
2. __`commandline_original.sh`__:
   > This script can be run in the command line to print the top 5 series by number of books, along with their titles and ids.
3. __`commandline_LLM.sh`__:
   > This script, as __`commandline_original.sh`__ can be run in the command line to print the top 5 series by number of books, along with their titles and ids. It was written with the aid of a LLM.
4. __`top_five_list.py`__:
   > This script goes through the list.json file and finds the top five tags for the books.

If the notebook file doesn't show plots/gets some errors, you can access it from [this]() link.
