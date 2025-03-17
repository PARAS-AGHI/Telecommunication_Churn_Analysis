# **Telecom Churn Analysis**

## **Overview**

This project analyzes customer churn in a telecom company using Python and data visualization techniques. The dataset contains various customer attributes, and the goal is to identify key factors influencing churn.

## **Dataset**

The dataset used in this project is Customer Churn.csv, which includes customer demographics, service details, and churn status.

## Installation

To run this analysis, install the required dependencies:

pip install pandas matplotlib numpy seaborn

## Data Cleaning & Preprocessing

Handling Missing Values: Replaced blanks in TotalCharges with 0 and converted the column to float.

Handling Duplicates: Checked for duplicate customer IDs.

Encoding Senior Citizen: Converted SeniorCitizen from 0/1 to "Yes"/"No".

## Exploratory Data Analysis (EDA)

The following insights were extracted:

Churn Distribution: Visualized using count plots and pie charts.

Gender & Churn: Analyzed customer churn based on gender.

Senior Citizen & Churn: Senior citizens have a higher churn percentage.

Tenure & Churn: Customers with shorter tenure are more likely to churn.

Contract Type & Churn: Month-to-month contract users have the highest churn rate.

Service Subscription & Churn: Customers without value-added services like OnlineSecurity, TechSupport, and DeviceProtection are more likely to churn.

## Visualizations

Countplots for categorical variables (e.g., Churn by gender, Churn by contract type).

Pie Chart for churn distribution.

Histogram for tenure analysis.

Stacked Bar Chart for senior citizen churn percentages.

## Running the Analysis

Run the script using:

python analysis.py

Ensure the dataset is in the correct directory.

## Conclusion

The analysis highlights key customer behaviors leading to churn. Insights can help improve customer retention strategies by focusing on contract types, tenure-based retention efforts, and promoting value-added services.

## License

This project is open-source under the MIT License.
