# Customer Churn Prediction

##  Live Demo

Try the deployed application here:

👉 **[Open Customer Churn Prediction App](https://customer-churn-prediction-awaq3i2cecyze6ahafrwjd.streamlit.app/)**

## About the Project

This project predicts whether a customer is likely to leave a service using Machine Learning.

The goal is to understand customer behavior and identify customers who may churn so that businesses can take steps to retain them.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Jupyter Notebook

## Project Workflow

1. Loaded and explored the dataset.
2. Cleaned and prepared the data.
3. Performed Exploratory Data Analysis (EDA).
4. Created visualizations to understand customer behavior.
5. Trained a Machine Learning model using XGBoost.
6. Evaluated the model using classification metrics.
7. Saved the trained model for future use.
8. Built a Streamlit app for customer churn prediction.

## Model Performance

The following results were obtained in my current experiments:

| Metric | Score |
|---|---:|
| Test Accuracy | 98.18% |
| Precision | 93.23% |
| Recall | 98.41% |
| F1-Score | 95.75% |
| Mean 5-Fold CV Accuracy | 97.61% |

*Note: These results are preliminary and should be validated for data leakage and reproducibility before being treated as final performance.*

## Visualizations

The project includes graphs to understand customer churn, customer behavior, and model performance.

## How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/s56874/customer-churn-prediction.git
   ```

2. Open the project folder:

   ```bash
   cd customer-churn-prediction
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

To explore the analysis, open the notebook in the `notebooks` folder using Jupyter Notebook.

Make sure the required dataset is available in the expected location before running the notebook.

## What I Learned

- Data cleaning and exploratory data analysis.
- Training a Machine Learning classification model.
- Evaluating models using precision, recall, F1-score, and cross-validation.
- Building a Streamlit application for model predictions.
- Understanding how Machine Learning can help businesses identify potential customer churn.

## Author

Created as a Machine Learning project to practice data analysis, model development, and deployment.

