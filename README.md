# Customer_conversion_prediction-Insurance

**Introduction**

The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts whether a customer is likely to be attracted to a loan offer. This predictive model, based on historical financial telemarketing data, aims to help financial companies efficiently identify and target potential customers who are most likely to respond positively to loan promotions.


**Table of Contents**

1. Key Technologies and Skills
2. Installation
3. Usage
4. Features
5. Contributing
6. License
7. Contact

**Key Technologies and Skills**
- Python
- Pandas
- Streamlit
- Plotly
- GridSearch CV
- SkLearn
- Pickle

**Installation**

To run this project, you need to install the following packages:

```python
pip install pandas
pip install streamlit
pip install plotly
pip install scikit-learn
pip install xgboost
pip install matplotlib
pip install seaborn
```

**Features**

**Data Preprocessing**
- **Dataset Overview :** The dataset consists of 45,211 rows and 11 columns related to a marketing campaign. Each row represents an individual's interaction with the campaign, and the goal is to predict the outcome (Outcome column) based on features such as age, job, marital status, education, and others.
- **Data Understanding :** Before embarking on modeling, it's essential to thoroughly comprehend your dataset. Begin by categorizing the variables, distinguishing between continuous and categorical ones, and examining their distributions.
- **Handling Null Values:** In our dataset, addressing missing values is critical. Depending on the nature of the data and the specific feature, we may opt for imputation methods such as mean, median, or mode to handle these null values effectively.
- **Encoding and Data Type Conversion:** When preparing categorical features for modeling, we utilize ordinal encoding. This method converts categorical values into numerical representations that reflect their inherent order and relationship with the target variable. Additionally, it's crucial to ensure that all data types are appropriately converted to meet the modeling requirements.
- **Skewness - Feature Scaling:** Skewness is a common challenge in datasets. Identifying skewness in the data is essential, and appropriate data transformations must be applied to mitigate it. One widely-used method is the log transformation, which is particularly effective in addressing high skewness in continuous variables. This transformation helps achieve a more balanced and normally-distributed dataset, which is often a prerequisite for many machine learning algorithms.
- **Outliers Handling:** Outliers have the potential to greatly influence model accuracy. To address outliers in our dataset, we employ the Interquartile Range (IQR) method. This approach entails identifying data points that lie outside the boundaries defined by the IQR and subsequently adjusting them to values that better align with the majority of the data. By applying this technique, we aim to enhance the robustness and reliability of our model predictions.
- **Train-Test Split :** The dataset is split into training and testing sets to evaluate the model's performance. The training set is used to train the model, while the testing set is reserved for assessing how well the model generalizes to unseen data. This step is crucial to avoid overfitting and to ensure that the model performs well on new data.
- **Resampling with SMOTETomek :** In cases where the dataset is imbalanced (i.e., the number of instances in each class is not equal), SMOTETomek is employed to balance the classes in the training set. SMOTETomek combines the SMOTE (Synthetic Minority Over-sampling Technique) and Tomek links methods to improve the balance between classes, which is critical for training a robust and fair model.

**Results**

The project provides significant value to financial institutions by enabling them to identify and target customers who are most likely to respond positively to loan offers. The user-friendly web application allows marketing teams to efficiently filter potential customers, optimizing their outreach efforts and improving conversion rates. Additionally, the project highlights the practical application of machine learning in the financial sector, demonstrating how predictive models can be effectively integrated into decision-making processes to enhance business outcomes.


**Contact**

📧 Email:aquibjaved04@gmail.com

🌐 LinkedIn: [linkedin.com/in/akib-javith-37bbbb324/](https://www.linkedin.com/in/akib-javith-37bbbb324/)

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.
