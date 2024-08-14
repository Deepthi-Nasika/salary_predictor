## Software Employee Salary Predictor - Streamlit Application
This application predicts software developer salaries based on user input and explores the real-world data from the Stack Overflow Developer Survey 2020 dataset. It is built using Python's scikit-learn library for machine learning and Streamlit framework for the front end.

### Features
**Explore:** Allows users to explore the dataset with visualizations like bar graphs, line charts, and pie graphs.\
**Predict:** Predicts the salary based on the user inputs - Country, Education Level, and Years of Experience with the flexibility to choose the regressor model based on the user requirements.\
**Model Performance**: Displays performance metrics of the 3 regressor models for the user to choose the best one.

### Dataset
Link to dataset: https://www.kaggle.com/datasets/aitzaz/stack-overflow-developer-survey-2020 \
File name: survey_results_public.csv

### Setting up Python Environment
1) Execute the following command to install all the Python libraries and packages that the notebook is dependent on
 ```pip install -r requirements.txt```
2) Execute the following command to install H2O AutoML to find the best possible model to predict the salary
 ```pip install -f http://h2o-release.s3.amazonaws.com/h20/latest_stable_Py.html h2o```

### Execution
1) Execute the code.ipynb file
2) Command prompt: ```streamlit run app.py```

### Analysis

