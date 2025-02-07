# HW3 - Hypothesis Testing / A/B Testing

**Author:** Yuchen (Olivia) Kuang  
**Date:** 1/31/2025  

## 📌 Overview  
This project focuses on **A/B testing and hypothesis testing** to analyze whether a new platform layout increases user engagement. The dataset consists of user activity logs, experiment group assignments, and user attributes.

---

## 📂 Part 1 : Getting to know your data (5 Points)  
We are given **four CSV files** and **one text file** containing essential data for this study. Below is a description of each dataset:

### 📌 t1_user_active_min.csv  
This file records **user activity minutes** on the platform for specific dates.

- **Columns:**
  - `uid` → User ID  
  - `dt` → Date of recorded activity  
  - `active_mins` → Number of minutes the user was active  

- **Purpose:**  
  - Measures user engagement.  
  - Helps evaluate whether the experiment influenced time spent on the platform.  

### 📌 t2_user_variant.csv  
This file contains **experiment group assignments** for each user.

- **Columns:**
  - `uid` → User ID  
  - `variant_number` → Experiment group (`0 = control`, `1 = treatment`)  
  - `dt` → Date when the user entered the experiment  
  - `signup_date` → User’s original signup date  

- **Purpose:**  
  - Distinguishes between **control** and **treatment groups**.  
  - Enables A/B testing to compare user activity.  

### 📌 t3_user_active_min_pre.csv  
This file contains **user activity data before the experiment started**, following the same format as `t1_users_active_mins.csv`.

- **Columns:**
  - `uid` → User ID  
  - `dt` → Date of recorded activity  
  - `active_mins` → Number of minutes the user was active  

- **Purpose:**  
  - Allows for **before-and-after** analysis.  
  - Helps assess whether the new platform layout had an impact on engagement.  

### 📌 t4_user_attributes.csv  
This file provides **user demographic and behavioral attributes**.

- **Columns:**
  - `uid` → User ID  
  - `gender` → Male or Female  
  - `user_type` → Reader, Non-Reader, New User, or Contributor  

- **Purpose:**  
  - Enables segmentation analysis based on **user behavior and demographics**.  
  - Helps identify whether specific user groups were more affected by the experiment.  

### 📌 table_schema.txt   
This file contains **metadata and schema definitions** for all datasets.

- **Purpose:**  
  - Describes column names, data types, and meanings of variables.  
  - Ensures consistency and proper interpretation of the dataset.  

---

## 📂 Part 2 : Organizing the Data (15 Points)  

### 1. What is the overall objective of this study?
The primary objective of this study is to determine whether the new platform layout increases user engagement by analyzing user activity before and after the experiment. This is done through A/B testing, where users are divided into control (variant_number = 0) and treatment (variant_number = 1) groups. By comparing the active minutes of users in both groups, we can statistically evaluate whether the experiment had a significant impact.

### 2. What data do we need to reach that objective?
To conduct this analysis, we need the following datasets:
-	User activity data (t1_users_active_mins.csv) → Tracks how long users spend on the platform.
-	Experiment group assignment (t2_users_variant.csv) → Identifies whether a user is in the control or treatment group.
By merging these datasets, we can compare average active minutes between the two groups and perform statistical tests to determine the impact of the new platform layout.

### 3. How is the data in t1 currently organized?
The t1_user_active_min.csv file contains user activity logs, where each row represents a specific user’s active minutes on a given date. It has the following structure:
 ![image](https://github.com/user-attachments/assets/4f8ef152-25ac-4ac9-8c8b-a0128b61dfa2)

Currently, the data does not include experiment group labels, making it difficult to analyze differences between the control and treatment groups.  


### 4. How should it be organized for better utility?
To make the data useful for statistical analysis, we need to:
-	Merge t1_user_active_min.csv with t2_user_variant.csv using uid as the key.
-	Add the variant_number column to label each user as control (0) or treatment (1).
-	Ensure the data is structured for comparison, allowing us to analyze activity levels per experiment group.
The reorganized data should look like this:
![image](https://github.com/user-attachments/assets/bbcceadd-7ba9-4100-9533-73813ea2b529)

This format will allow us to calculate mean, median, and statistical significance between the control and treatment groups.  

### 5. Organize the data.
After merging `t1_user_active_min.csv` (user activity data) with `t2_user_variant.csv` (experiment group assignments), we successfully structured the dataset (Data/merged_t1_t2.csv) for statistical analysis. The merged dataset now contains an additional column, variant_number, which labels users as either control (0) or treatment (1) groups, enabling direct comparison of user engagement between these two groups.

---

## 📂 Part 3 : Statistical Analysis (10 Points)

### 1. Is there a statistical difference between Group 1 and Group 2?
Using the organized data from Part 2, we conducted statistical analysis to determine whether there is a significant difference between the control group (`variant_number = 0`) and the treatment group (`variant_number = 1`). To test whether there is a significant difference in user activity between the two groups, we performed an independent t-test. The results are:  
- **T-test Statistic:** `-1.4674`
- **P-value:** `0.1423`  
Since the p-value (0.1423) is greater than 0.05, we fail to reject the null hypothesis. This means that there is no statistically significant difference between the control and treatment groups in terms of active minutes.

### 2. What are the mean and median for both groups?
| Group | Mean Active Minutes | Median Active Minutes |
|-----------------|--------------------|----------------------|
| **Control** (0) | **35.34** | **5.0** |
| **Treatment** (1) | **40.24** | **7.0** |
Although the treatment group shows a slightly higher mean and median (40.24 vs. 35.34 and 7.0 vs. 5.0, respectively), the difference is not statistically significant.

### 3. What conclusions can you draw?
✅ The treatment group shows slightly higher engagement.  
❌ However, the difference is **not statistically significant**.  
⚠ The new platform layout did **not have a measurable impact** on user engagement.  

---

## 📂 Part 4: Digging a Little Deeper (25 Points)

### 1. Can you trust that the results? Why or why not? 
The results should be interpreted with caution. Factors like outliers, data distribution, and missing data can impact the accuracy. Further checks are needed.

### 2.  Is the data normally distributed?
Based on the Shapiro-Wilk test results, both the control group (p-value=1.15e-215) and treatment group (p-value=4.50e-182) have extremely low p-values (<< 0.05). This strongly indicates that the data does not follow a normal distribution.

### 3.  Plot a box plot of group 1 and group 2
![image](https://github.com/user-attachments/assets/41da1870-fafd-464f-8335-926dde25161f)

### 4.  Are there any outliers?
We identify outliers using the Interquartile Range (IQR) method. The Interquartile Range (IQR) method is a common way to detect outliers in a dataset. We can calculate the first quartile (Q1) and third quartile (Q3) to determine the IQR. Outliers are typically defined as values that fall below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR. After removing, there are 931953 rows left.

### 5. What might be causing those outliers? (Hint, look at the data in t1. What is the maximum time a user should possibly have?).
Users logging more than 1440 minutes (24 hours) of activity in a single day, which is physically impossible. These values could be due to data entry errors or logging artifacts. We can identify 172 outliers in the dataset.

### 6. Remove any data point that might be causing outliers.
We remove the outliers of the first table by filtering out the rows where the active minutes are less than or equal to 1440. After removing, there are 1066230 rows left.

### 7. Redo part 2 and 3 with the new data without those data points.
We use the cleaned dataset to redo the statistical analysis. The t-test results are as follows:
-	T-test Statistic: -30.686846737487123
-	P-value: 2.219758340477041e-206

### 8. What is the new conclusion based on the new data?
The p-value is significantly less than 0.05, indicating a statistically significant difference between the control and treatment groups in terms of active minutes.




---

## 📂 Part 5: Digging Even Deeper (25 Points)
- **Incorporating pre-experiment data (t3)** shows a statistically significant impact of the new layout.
- The treatment group had a substantial increase in engagement.

---

## 📂 Part 6: Exploring Other Conclusions (10 Points)
- **Gender Differences**: Females and unknown gender users showed higher engagement increases.
- **User Type Impact**: Contributors and readers benefited the most from the new layout.

---

## 📂 Part 7: Summarizing Results (10 Points)

- **Part 1**: Explored datasets.
- **Part 2**: Merged data for statistical testing.
- **Part 3**: Found no significant impact at first.
- **Part 4**: Outlier removal revealed significant differences.
- **Part 5**: Pre-experiment data confirmed impact.
- **Part 6**: User attributes influenced engagement.

### **Final Conclusion**
The **new platform layout effectively increased user engagement**, particularly among certain user groups. However, **raw data initially suggested no impact due to outliers and pre-experiment differences.** Accounting for these factors reveals a **statistically significant improvement.**
