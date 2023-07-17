## Project Name

Data Science Project: Glassdoor Scraper and Model Deployment

## Description

This repository contains a comprehensive data science project that involves scraping job data from Glassdoor, performing data cleaning and exploratory data analysis (EDA), building a predictive model, and deploying the model using a Flask API.

The project is structured into the following components:

1. **Glassdoor Scraper**: A Python script (`scraper.py`) that utilizes web scraping techniques to extract job listings, including job titles, companies, locations, salaries, and other relevant information from Glassdoor. The scraped data is stored in a structured format for further analysis.

2. **Data Cleaning**: A Jupyter Notebook (`data_cleaning.ipynb`) that demonstrates the process of cleaning and preprocessing the scraped data. This includes handling missing values, removing duplicates, standardizing formats, and transforming variables to make them suitable for analysis.

3. **Exploratory Data Analysis (EDA)**: A Jupyter Notebook (`data_analysis.ipynb`) that showcases the EDA process to gain insights and extract meaningful patterns from the cleaned data. This includes data visualization, statistical analysis, and feature engineering.

4. **Model Building**: A Jupyter Notebook (`model_building.ipynb`) that presents the construction and evaluation of a predictive model using machine learning techniques. The notebook covers data splitting, feature selection, model training, hyperparameter tuning, and model evaluation metrics.

5. **Flask API**: A Flask application (`app.py`) that deploys the trained model as an API. The API allows users to submit job details and receive predictions for the expected salary or any other relevant outcome based on the trained model.

## Usage

1. **Run the Glassdoor scraper**: Use the Python script `scraper.py` to scrape Glassdoor job listings and save the data in a structured format.

2. **Perform data cleaning**: Open the Jupyter Notebook `data_cleaning.ipynb` using Jupyter Notebook or any compatible environment. Follow the code within the notebook to clean and preprocess the scraped data.

3. **Conduct exploratory data analysis**: Open the Jupyter Notebook `data_analysis.ipynb` using Jupyter Notebook or any compatible environment. Follow the code notebook to explore and visualize the cleaned data.

4. **Build and evaluate the predictive model**: Open the Jupyter Notebook `model_building.ipynb` using Jupyter Notebook or any compatible environment. Follow the code to train, tune, and evaluate the predictive model using the cleaned data.

5. **Deploy the model as a Flask API**: Run the Flask application using the file `app.py`. The API will be accessible through http://localhost:5000 or the specified host and port.

## License
This project is licensed under the MIT License.
