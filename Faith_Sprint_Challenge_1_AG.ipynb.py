{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Autograded Notebook (Canvas & CodeGrade)\n",
    "\n",
    "This notebook will be automatically graded. It is designed to test your answers and award points for the correct answers. Following the instructions for each Task carefully.\n",
    "Instructions\n",
    "\n",
    "- **Download** this notebook as you would any other ipynb file \n",
    "- **Upload** to Google Colab or work locally (if you have that set-up)\n",
    "- **Delete** `raise NotImplementedError()`\n",
    "\n",
    "- **Write** your code in the `# YOUR CODE HERE` space\n",
    "\n",
    "\n",
    "- **Execute** the Test cells that contain assert statements - these help you check your work (others contain hidden tests that will be checked when you submit through Canvas)\n",
    "\n",
    "- **Save** your notebook when you are finished\n",
    "- **Download** as a ipynb file (if working in Colab)\n",
    "- **Upload** your complete notebook to Canvas (there will be additional instructions in Slack and/or Canvas)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Sprint Challenge\n",
    "## *Data Science Unit 4 Sprint 1*\n",
    "\n",
    "After a week of Natural Language Processing, you've learned some cool new stuff: how to process text, how turn text into vectors, and how to model topics from documents. Apply your newly acquired skills to one of the most famous NLP datasets out there: [Yelp](https://www.yelp.com/dataset). As part of the job selection process, some of my friends have been asked to create analysis of this dataset, so I want to empower you to have a head start.  \n",
    "\n",
    "The real dataset is massive (almost 8 gigs uncompressed). I've sampled the data for you to something more managable for the Sprint Challenge. You can analyze the full dataset as a stretch goal or after the sprint challenge. As you work on the challenge, I suggest adding notes about your findings and things you want to analyze in the future.\n",
    "\n",
    "## Challenge Objectives\n",
    "Successfully complete all these objectives to earn full credit. \n",
    "\n",
    "**Successful completion is defined as passing all the unit tests in each objective.**  \n",
    "\n",
    "Each unit test that you pass is 1 point. \n",
    "\n",
    "There are 5 total possible points in this sprint challenge. \n",
    "\n",
    "\n",
    "There are more details on each objective further down in the notebook.*\n",
    "* <a href=\"#p1\">Part 1</a>: Write a function to tokenize the yelp reviews\n",
    "* <a href=\"#p2\">Part 2</a>: Create a vector representation of those tokens\n",
    "* <a href=\"#p3\">Part 3</a>: Use your tokens in a classification model on yelp rating\n",
    "* <a href=\"#p4\">Part 4</a>: Estimate & Interpret a topic model of the Yelp reviews\n",
    "\n",
    "____\n",
    "\n",
    "# Before you submit your notebook you must first\n",
    "\n",
    "1) Restart your notebook's Kernal\n",
    "\n",
    "2) Run all cells sequentially, from top to bottom, so that cell numbers are sequential numbers (i.e. 1,2,3,4,5...)\n",
    "- Easiest way to do this is to click on the **Cell** tab at the top of your notebook and select **Run All** from the drop down menu. \n",
    "\n",
    "3) Comment out the cell that generates a pyLDAvis visual in objective 4 (see instructions in that section). \n",
    "____"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "### Import Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "7bec125eb29f89460cf0c19ba9aa9a2f",
     "grade": false,
     "grade_id": "cell-395851cd95d17235",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load reviews from URL\n",
    "data_url = 'https://raw.githubusercontent.com/LambdaSchool/data-science-practice-datasets/main/unit_4/unit1_nlp/review_sample.json'\n",
    "\n",
    "# Import data into a DataFrame named df\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "356579363f311da83f4ef7abaf3c9212",
     "grade": true,
     "grade_id": "cell-cb5006475e42b8f9",
     "locked": true,
     "points": 1,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Visible Testing\n",
    "assert isinstance(df, pd.DataFrame), 'df is not a DataFrame. Did you import the data into df?'\n",
    "assert df.shape[0] == 10000, 'DataFrame df has the wrong number of rows.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 1: Tokenize Function\n",
    "<a id=\"#p1\"></a>\n",
    "\n",
    "Complete the function `tokenize`. Your function should\n",
    "- accept one document at a time\n",
    "- return a list of tokens\n",
    "\n",
    "You are free to use any method you have learned this week."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Optional: Consider using spaCy in your function. The spaCy library can be imported by running this cell.\n",
    "# A pre-trained model (en_core_web_sm) has been made available to you in the CodeGrade container.\n",
    "# If you DON'T need use the en_core_web_sm model, you can comment it out below.\n",
    "\n",
    "import spacy\n",
    "nlp = spacy.load('en_core_web_sm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "4837ed2a1cc13057ba40203859d46ff6",
     "grade": false,
     "grade_id": "cell-3d570d5a1cd6cb64",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "def tokenize(doc):\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "2181ca9d36070260b1f75dcfd9e58965",
     "grade": true,
     "grade_id": "cell-02da164f6fbe730a",
     "locked": true,
     "points": 1,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "'''Testing'''\n",
    "assert isinstance(tokenize(df.sample(n=1)[\"text\"].iloc[0]), list), \"Make sure your tokenizer function accepts a single document and returns a list of tokens!\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 2: Vector Representation\n",
    "<a id=\"#p2\"></a>\n",
    "1. Create a vector representation of the reviews (i.e. create a doc-term matrix).\n",
    "2. Write a fake review and query for the 10 most similiar reviews, print the text of the reviews. Do you notice any patterns?\n",
    "    - Given the size of the dataset, use `NearestNeighbors` model for this. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "9f570a35b1d17ce543ee41f516a0828c",
     "grade": false,
     "grade_id": "cell-0e96491cb529202c",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Create a vector representation of the reviews \n",
    "# Name that doc-term matrix \"dtm\"\n",
    "\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "32b220e23c9aa1f602f08d1c2e879d0a",
     "grade": false,
     "grade_id": "cell-3d5bc610a8ec6b24",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Create and fit a NearestNeighbors model named \"nn\"\n",
    "from sklearn.neighbors import NearestNeighbors\n",
    "\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "d270ed23df3c7d3c6cf08ab174ccaf9e",
     "grade": true,
     "grade_id": "cell-c43704dcff67e99b",
     "locked": true,
     "points": 1,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "'''Testing.'''\n",
    "assert nn.__module__ == 'sklearn.neighbors._unsupervised', ' nn is not a NearestNeighbors instance.'\n",
    "assert nn.n_neighbors == 10, 'nn has the wrong value for n_neighbors'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "3da2ced9f187ed0aa1a890785e2ba00e",
     "grade": false,
     "grade_id": "cell-496203e8746296ca",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Create a fake review and find the 10 most similar reviews\n",
    "\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 3: Classification\n",
    "<a id=\"#p3\"></a>\n",
    "Your goal in this section will be to predict `stars` from the review dataset. \n",
    "\n",
    "1. Create a pipeline object with a sklearn `CountVectorizer` or `TfidfVector` and any sklearn classifier.\n",
    "    - Use that pipeline to train a model to predict the `stars` feature (i.e. the labels). \n",
    "    - Use that Pipeline to predict a star rating for your fake review from Part 2. \n",
    "\n",
    "\n",
    "\n",
    "2. Create a parameter dict including `one parameter for the vectorizer` and `one parameter for the model`. \n",
    "    - Include 2 possible values for each parameter\n",
    "    - **Use `n_jobs` = 1** \n",
    "    - Due to limited computational resources on CodeGrader `DO NOT INCLUDE ADDITIONAL PARAMETERS OR VALUES PLEASE.`\n",
    "    \n",
    "    \n",
    "3. Train the entire pipeline with a GridSearch\n",
    "    - Name your GridSearch object as `gs`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "e1d18da8521d51d8bfc4b5b9d005fa34",
     "grade": false,
     "grade_id": "cell-e2beb0252d274bba",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "\n",
    "# Name the gridsearch instance \"gs\"\n",
    "\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "b9e2378efb868f104a4eb39e4f25563c",
     "grade": true,
     "grade_id": "cell-d07134c6fe5d056e",
     "locked": true,
     "points": 1,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Visible Testing\n",
    "prediction = gs.predict([\"I wish dogs knew how to speak English.\"])[0]\n",
    "assert prediction in df.stars.values, 'You gs object should be able to accept raw text within a list. Did you include a vectorizer in your pipeline?'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 4: Topic Modeling\n",
    "\n",
    "Let's find out what those yelp reviews are saying! :D\n",
    "\n",
    "1. Estimate a LDA topic model of the review text\n",
    "    - Set num_topics to `5`\n",
    "    - Name your LDA model `lda`\n",
    "2. Create 1-2 visualizations of the results\n",
    "    - You can use the most important 3 words of a topic in relevant visualizations. Refer to yesterday's notebook to extract. \n",
    "3. In markdown, write 1-2 paragraphs of analysis on the results of your topic model\n",
    "\n",
    "When you instantiate your LDA model, it should look like this: \n",
    "\n",
    "```python\n",
    "lda = LdaModel(corpus=corpus,\n",
    "               id2word=id2word,\n",
    "               random_state=723812,\n",
    "               num_topics = num_topics,\n",
    "               passes=1\n",
    "              )\n",
    "\n",
    "```\n",
    "\n",
    "__*Note*__: You can pass the DataFrame column of text reviews to gensim. You do not have to use a generator."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Note about  pyLDAvis\n",
    "\n",
    "**pyLDAvis** is the Topic modeling package that we used in class to visualize the topics that LDA generates for us.\n",
    "\n",
    "You are welcomed to use pyLDAvis if you'd like for your visualization. However, **you MUST comment out the code that imports the package and the cell that generates the visualization before you submit your notebook to CodeGrade.** \n",
    "\n",
    "Although you should leave the print out of the visualization for graders to see (i.e. comment out the cell after you run it to create the viz). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from gensim import corpora\n",
    "# Due to limited computationalresources on CodeGrader, use the non-multicore version of LDA \n",
    "from gensim.models.ldamodel import LdaModel\n",
    "import gensim\n",
    "import re"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Estimate a LDA topic model of the review tex"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "9514841e71735eaa255bccc53b257896",
     "grade": false,
     "grade_id": "cell-66331a185ff52f15",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Remember to read the LDA docs for more information on the various class attirbutes and methods available to you\n",
    "# in the LDA model: https://radimrehurek.com/gensim/models/ldamodel.html\n",
    "\n",
    "# don't change this value \n",
    "num_topics = 5\n",
    "\n",
    "# use tokenize function you created earlier to create tokens \n",
    "\n",
    "# create a id2word object (hint: use corpora.Dictionary)\n",
    "\n",
    "# create a corpus object (hint: id2word.doc2bow)\n",
    "\n",
    "# instantiate an lda model\n",
    "\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "6479db0fa59c99d3ae3201c1f10ebca1",
     "grade": true,
     "grade_id": "cell-5a3c181311134fa9",
     "locked": true,
     "points": 1,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Visible Testing\n",
    "assert lda.get_topics().shape[0] == 5, 'Did your model complete its training? Did you set num_topics to 5?'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Create 1-2 visualizations of the results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "189591ed7b9e6e6146d59761fb418268",
     "grade": false,
     "grade_id": "cell-9b043e992fbd218c",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Use pyLDAvis (or a ploting tool of your choice) to visualize your results \n",
    "\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "f44a26c754500ff0bf585296075bf754",
     "grade": false,
     "grade_id": "cell-bf9e63d9645bba84",
     "locked": true,
     "points": 0,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "#### 3. In markdown, write 1-2 paragraphs of analysis on the results of your topic model"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Stretch Goals\n",
    "\n",
    "Complete one of more of these to push your score towards a three: \n",
    "* Incorporate named entity recognition into your analysis\n",
    "* Compare vectorization methods in the classification section\n",
    "* Analyze more (or all) of the yelp dataset - this one is v. hard. \n",
    "* Use a generator object on the reviews file - this would help you with the analyzing the whole dataset.\n",
    "* Incorporate any of the other yelp dataset entities in your analysis (business, users, etc.)"
   ]
  }
 ],
 "metadata": {
  "kernel_info": {
   "name": "u4-s1-nlp"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "nteract": {
   "version": "0.15.0"
  },
  "toc-autonumbering": false
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
