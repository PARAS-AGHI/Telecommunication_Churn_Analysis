import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df= pd.read_csv('C:/Users\LENOVO\OneDrive/Desktop/Telecom churn analysis/Customer Churn.csv')
# print(df)

# In eda the first thing we do is to inspect our data , To inspect we use some functions

# df.info()   # info tells us no of rows and columns  and if the data type is object, customer id is object as we can see its alpha-numeric
# why total charges is showing as an object not int , because there are some blanks there, and tenure zero hone ki vjh se total charges me blanks hai and charges hai 

df["TotalCharges"]= df["TotalCharges"].replace(" ","0")        #we re replacing blank values with 0 here in total charges and 0 ko string me rakha h kyunki string me hi data fill krana h
df["TotalCharges"]= df["TotalCharges"].astype("float")         #we want to change data type of the column as well

#df.info()
#isnull tells where are the null values in the dataframe and makes it true
# print(df.isnull().sum())   #true false toh smhj nhi ayega toh you can sum it parameterwise and uska bhi sum krr skte hai

#print(df.isnull().sum().sum())    #0 tells aapke data me koi null values nhi hai

#print(df.describe())   #describe taki hum thdi descriptive analysis le ske - count,mean,std deviation, min, max

# print(df.duplicated().sum())   # 0 - it means zero duplicates are there

#Make sure you are also checking duplicates on the basis of unique id- ki 2 baar entry toh nhi hgyi hai

# print(df["customerID"].duplicated().sum())


#We also need to fix senior citizens as they re given 0 and 1 we will convert it to yes and no

def conv(value):
    if value == 1:
        return "Yes"
    else:
        return "No"
    


#now applying the conv function to senior citizen

df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv);

#print(df.head(30))





#To bring the understanding of how many % customers have churned out or not, we can use countplot
# The countplot is used to represent the occurrence(counts) of the observation present in the categorical variable.

# bar_label helps in getting labels,which means the exact amount

# ax = sns.countplot(x= "Churn", data= df)
# ax.bar_label(ax.containers[0])     # this helped in getting exact  numbers, earlier exact numbers were not visible
# plt.title("Count of customers by churn")
# # plt.show()









#groupby takes out the unique values which is yes or no
# agg functions allows various operations like sum, mean, count etc.
# we re specifically taking churn:count   here because if we only take agg("count"), it ll give groupby count of all the parameters

# gb= df.groupby("Churn").agg({'Churn': "count"})        
#gb= df.groupby("Churn").agg("count")
# print(gb)

# plt.figure(figsize= (3,4))   #size of pie chart
# plt.pie(gb['Churn'],labels = gb.index , autopct= "%1.2f%%")
# plt.title("Percentage of Churned customers")
#plt.show()






#from the given pie chart we can conclude that 26.54% of our customers have churned out

#NOW LETS EXPLORE REASON BEHIND IT

#print(df["gender"].value_counts())


# sns.countplot(x="gender", data= df,hue="Churn")
# plt.title("Churn by gender")
# plt.show()


#CHURN BY SENIOR CITIZEN

ax= sns.countplot(x="SeniorCitizen", data= df,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn by Senior Citizen")
#plt.show()







# First, calculate the percentage for each group
df_grouped = df.groupby(['SeniorCitizen', 'Churn']).size().unstack(fill_value=0)
df_grouped_percent = df_grouped.div(df_grouped.sum(axis=1), axis=0) * 100  # Calculate percentage

# Plotting
ax = df_grouped_percent.plot(kind='bar', stacked=True, figsize=(8, 6), color=['#1f77b4', '#ff7f0e'])

# Adding percentage labels
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')  # Add percentages inside bars

# Customizing plot
plt.title('Churn by Senior Citizen (as % of total)')
plt.xlabel('Senior Citizen')
plt.ylabel('Percentage')
plt.legend(title='Churn',bbox_to_anchor= (0.9,0.9))
plt.tight_layout()

#plt.show()


#COMPARITIVEL A GREATER % OF SENIOR CITIZEN HAVE CHURNED OUT




## ON THE BASIS OF TENURE

sns.histplot(x= "tenure",data= df, bins= 72, hue= "Churn");
#plt.show()

#People who have used our services for a long time have stayed and people who used it for one or two months churned out




#ON THE BASIS OF CONTRACTS

ax= sns.countplot(x="Contract", data= df,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn by Contract")
#plt.show()


#People with month to month contract are likely to churn than from those who have one or two years of contract


print(df.columns.values)


################################33



# Assuming you have the data in a DataFrame called df
columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 
           'StreamingMovies']

# Set up the subplots grid (3 rows, 3 columns for 9 plots)
fig, axes = plt.subplots(3, 3, figsize=(15, 12))

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Loop through the columns and create a countplot for each
for i, col in enumerate(columns):
    sns.countplot(data=df, x=col, ax=axes[i], hue= df["Churn"])
    axes[i].set_title(f'Countplot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

# Adjust layout for better spacing
plt.tight_layout()
plt.show()












# The countplots show that customers who lack services
#  like **OnlineSecurity**, **TechSupport**, and **DeviceProtection** are 
# more likely to churn. Additionally, users with **fiber optic internet** tend
#  to churn more than those with DSL or no internet service. Overall, not subscribing 
# to value-added services seems to be correlated with higher churn rates.