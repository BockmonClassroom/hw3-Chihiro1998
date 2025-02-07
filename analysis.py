import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, shapiro, skew, kurtosis

# Data folder path
data_dir = "/root/DS5110/hw3-Chihiro1998/Data"

# Load data files
t1_data = pd.read_csv(os.path.join(data_dir, "t1_user_active_min.csv"))
t2_data = pd.read_csv(os.path.join(data_dir, "t2_user_variant.csv"))
t3_data = pd.read_csv(os.path.join(data_dir, "t3_user_active_min_pre.csv"))
t4_data = pd.read_csv(os.path.join(data_dir, "t4_user_attributes.csv"))
t4_data = pd.read_csv(os.path.join(data_dir, "t4_user_attributes.csv"))

# Part 1-1
print(t1_data.head())
print(t2_data.head())
print(t3_data.head())
print(t4_data.head())

# Part 2-5
merged_t1_t2 = pd.merge(t1_data, t2_data[['uid', 'variant_number']], on="uid")
print("Merged Data (T1 + T2):")
print(merged_t1_t2.head(), "\n")


# Part 3-1
control_group = merged_t1_t2[merged_t1_t2["variant_number"] == 0]
treatment_group = merged_t1_t2[merged_t1_t2["variant_number"] == 1]
# t-test
t_stat, p_value = ttest_ind(control_group["active_mins"], treatment_group["active_mins"], equal_var=False)
print(f"T-test Statistic: {t_stat}, P-value: {p_value}")
if p_value < 0.05:
    print("There is a statistically significant difference between the two groups (p < 0.05).")
else:
    print("No statistically significant difference was found (p >= 0.05).")

# Part 3-2
# mean and median
control_mean = control_group["active_mins"].mean()
control_median = control_group["active_mins"].median()
treatment_mean = treatment_group["active_mins"].mean()
treatment_median = treatment_group["active_mins"].median()
print(f"Control Group - Mean: {control_mean}, Median: {control_median}")
print(f"Treatment Group - Mean: {treatment_mean}, Median: {treatment_median}")


# Part 4-2
# Is the data normally distributed?
# Shapiro-Wilk test
control_shapiro = shapiro(control_group["active_mins"])
treatment_shapiro = shapiro(treatment_group["active_mins"])
print(f"Shapiro-Wilk Test for Normality (Control Group): p-value = {control_shapiro[1]}")
print(f"Shapiro-Wilk Test for Normality (Treatment Group): p-value = {treatment_shapiro[1]}")

# Part 4-3
plt.figure(figsize=(8, 6))
plt.boxplot(
    [control_group["active_mins"], treatment_group["active_mins"]],
    tick_labels=["Control", "Treatment"]  # 修正参数，避免 Matplotlib 警告
)
plt.title("Boxplot of Active Minutes for Control and Treatment Groups")
plt.ylabel("Active Minutes")
plt.grid(True)
plt.show()

# Part 4-4
# Calculate IQR
Q1 = merged_t1_t2["active_mins"].quantile(0.25)
Q3 = merged_t1_t2["active_mins"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
filtered_data = merged_t1_t2[(merged_t1_t2["active_mins"] >= lower_bound) & (merged_t1_t2["active_mins"] <= upper_bound)]
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
print(f"Data Size Before Removing Outliers: {len(merged_t1_t2)}")
print(f"Data Size After Removing Outliers: {len(filtered_data)}")


# Part 4-5
n_outliers = (t1_data.active_mins > 1440).sum()
print(f"Number of outliers: {n_outliers}")


# Part 4-6
clean_t1_data = t1_data[t1_data.active_mins < 1440]


# Part 4-7
clean_merged_t1_t2 = pd.merge(clean_t1_data, t2_data[['uid', 'variant_number']], on="uid")
control_group = clean_merged_t1_t2[clean_merged_t1_t2["variant_number"] == 0]
treatment_group = clean_merged_t1_t2[clean_merged_t1_t2["variant_number"] == 1]

# calculate mean and median
control_mean = control_group["active_mins"].mean()
control_median = control_group["active_mins"].median()
treatment_mean = treatment_group["active_mins"].mean()
treatment_median = treatment_group["active_mins"].median()
print(f"Control Group - Mean: {control_mean}, Median: {control_median}")
print(f"Treatment Group - Mean: {treatment_mean}, Median: {treatment_median}")

t_stat, p_value = ttest_ind(control_group["active_mins"], treatment_group["active_mins"], equal_var=False)
print(f"T-test Statistic: {t_stat}, P-value: {p_value}")

if p_value < 0.05:
    print("There is a statistically significant difference between the two groups (p < 0.05).")
else:
    print("No statistically significant difference was found (p >= 0.05).")


# Part 5-2
clean_t3_data = t3_data[t3_data.active_mins < 1440]
merged_t1_t2 = pd.merge(clean_t1_data, t2_data[['uid', 'variant_number']], on="uid")
merged_t3_t2 = pd.merge(clean_t3_data, t2_data[['uid', 'variant_number']], on="uid")

# Normalize post-experiment data by subtracting pre-experiment activity per user
pre_experiment_totals = merged_t3_t2.groupby('uid')['active_mins'].sum().reset_index()
post_experiment_totals = merged_t1_t2.groupby('uid')['active_mins'].sum().reset_index()
normalized_data = pd.merge(post_experiment_totals, pre_experiment_totals, on='uid', suffixes=('_post', '_pre'), how='left')
normalized_data['normalized_active_mins'] = normalized_data['active_mins_post'] - normalized_data['active_mins_pre'].fillna(0)
clean_merged_t1_t2 = pd.merge(normalized_data[['uid', 'normalized_active_mins']], t2_data[['uid', 'variant_number']], on='uid')

# Separate control and treatment groups
control_group = clean_merged_t1_t2[clean_merged_t1_t2["variant_number"] == 0]
treatment_group = clean_merged_t1_t2[clean_merged_t1_t2["variant_number"] == 1]

# Calculate mean and median
control_mean = control_group["normalized_active_mins"].mean()
control_median = control_group["normalized_active_mins"].median()
treatment_mean = treatment_group["normalized_active_mins"].mean()
treatment_median = treatment_group["normalized_active_mins"].median()
print(f"Control Group - Mean: {control_mean}, Median: {control_median}")
print(f"Treatment Group - Mean: {treatment_mean}, Median: {treatment_median}")

# Perform t-test
t_stat, p_value = ttest_ind(control_group["normalized_active_mins"], treatment_group["normalized_active_mins"], equal_var=False)
print(f"T-test Statistic: {t_stat}, P-value: {p_value}")

if p_value < 0.05:
    print("There is a statistically significant difference between the two groups (p < 0.05).")
else:
    print("No statistically significant difference was found (p >= 0.05).")



# Part 6-1
merged_t1_t2_t4 = pd.merge(clean_merged_t1_t2, t4_data, on='uid')
# Further exploration using user attributes
gender_comparison = merged_t1_t2_t4.groupby(['gender', 'variant_number'])['active_mins'].mean()
print("Mean Active Minutes by Gender and Experiment Group:\n", gender_comparison)

user_type_comparison = merged_t1_t2_t4.groupby(['user_type', 'variant_number'])['active_mins'].mean()
print("Mean Active Minutes by User Type and Experiment Group:\n", user_type_comparison)

# Visualization of engagement by gender and user type
plt.figure(figsize=(10,5))
gender_comparison.unstack().plot(kind='bar', title='Active Minutes by Gender and Experiment Group')
plt.ylabel("Mean Active Minutes")
plt.show()

plt.figure(figsize=(10,5))
user_type_comparison.unstack().plot(kind='bar', title='Active Minutes by User Type and Experiment Group')
plt.ylabel("Mean Active Minutes")
plt.show()
