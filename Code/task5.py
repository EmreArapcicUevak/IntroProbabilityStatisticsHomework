# Please make sure all the packages are installed :)
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assumes the file 'cereal.csv' is in the current directory)
data = pd.read_csv("../DataSets/cereal.csv")

# Drop the first 3 columns as they are text and not useful for numerical analysis
data = data.drop(data.columns[:3], axis=1)


def do_analysis(dataframe, column_name):
    # (a) Calculate mean, median, data range, quartiles, and IQR
    mean_value = dataframe[column_name].mean()
    median_value = dataframe[column_name].median()
    data_range = dataframe[column_name].max() - dataframe[column_name].min()
    quartile_1 = dataframe[column_name].quantile(0.25)
    quartile_3 = dataframe[column_name].quantile(0.75)
    iqr_value = quartile_3 - quartile_1

    # Print the calculated statistics
    print(f"Mean of {column_name}: {mean_value}")
    print(f"Median of {column_name}: {median_value}")
    print(f"Range of {column_name}: {data_range}")
    print(f"1st Quartile of {column_name}: {quartile_1}")
    print(f"3rd Quartile of {column_name}: {quartile_3}")
    print(f"IQR of {column_name}: {iqr_value}")

    # (b) Create a histogram and box plot
    plt.figure(figsize=(12, 6))

    # Histogram
    plt.subplot(1, 2, 1)
    plt.hist(dataframe[column_name], bins=10, edgecolor="black")
    plt.title(f"Histogram of {column_name}")

    # Box plot
    plt.subplot(1, 2, 2)
    plt.boxplot(dataframe[column_name])
    plt.title(f"Box Plot of {column_name}")

    plt.show()


# Perform analysis before removing outliers
print("Analysis before removing all the outliers")
for column in data.columns:
    do_analysis(data, column)

# Remove outliers for each column in the dataset
data_no_outliers = data.copy()
for column in data_no_outliers.columns:
    q1 = data_no_outliers[column].quantile(0.25)
    q3 = data_no_outliers[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    data_no_outliers = data_no_outliers[
        (data_no_outliers[column] >= lower_bound) & (data_no_outliers[column] <= upper_bound)]

# Perform analysis after removing outliers
print("Analysis after removing all the outliers")
for column in data_no_outliers.columns:
    do_analysis(data_no_outliers, column)
