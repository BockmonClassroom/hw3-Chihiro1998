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
•	User activity data (t1_users_active_mins.csv) → Tracks how long users spend on the platform.
•	Experiment group assignment (t2_users_variant.csv) → Identifies whether a user is in the control or treatment group.
By merging these datasets, we can compare average active minutes between the two groups and perform statistical tests to determine the impact of the new platform layout.

### 3. How is the data in t1 currently organized?
The t1_user_active_min.csv file contains user activity logs, where each row represents a specific user’s active minutes on a given date. It has the following structure:
 ![image](https://github.com/user-attachments/assets/4f8ef152-25ac-4ac9-8c8b-a0128b61dfa2)

Currently, the data does not include experiment group labels, making it difficult to analyze differences between the control and treatment groups.  


### 4. How should it be organized for better utility?
To make the data useful for statistical analysis, we need to:
1.	Merge t1_user_active_min.csv with t2_user_variant.csv using uid as the key.
2.	Add the variant_number column to label each user as control (0) or treatment (1).
3.	Ensure the data is structured for comparison, allowing us to analyze activity levels per experiment group.
The reorganized data should look like this:
![image](https://github.com/user-attachments/assets/bbcceadd-7ba9-4100-9533-73813ea2b529)
This format will allow us to calculate mean, median, and statistical significance between the control and treatment groups.  

### 5. Organize the data.
After merging `t1_user_active_min.csv` (user activity data) with `t2_user_variant.csv` (experiment group assignments), we successfully structured the dataset (Data/merged_t1_t2.csv) for statistical analysis. The merged dataset now contains an additional column, variant_number, which labels users as either control (0) or treatment (1) groups, enabling direct comparison of user engagement between these two groups.

---

## 📂 Part 3 : Statistical Analysis (10 Points)

### 1. Is there a statistical difference between Group 1 and Group 2?
- **T-test Statistic:** `-1.4674`  
- **P-value:** `0.1423`  
- Since p-value > 0.05, there is **no statistically significant difference** between the two groups.

### 2. What are the mean and median for both groups?
| Group | Mean Active Minutes | Median Active Minutes |
|-----------------|--------------------|----------------------|
| **Control** (0) | **35.34** | **5.0** |
| **Treatment** (1) | **40.24** | **7.0** |

### 3. What conclusions can you draw?
✅ The treatment group shows slightly higher engagement.  
❌ However, the difference is **not statistically significant**.  
⚠ The new platform layout did **not have a measurable impact** on user engagement.  

---

## 📂 Part 4: Digging a Little Deeper (25 Points)
- The dataset is **not normally distributed**.
- **Outliers exist** (e.g., users logging more than 1440 minutes/day).
- After removing outliers, **a significant difference emerges (p < 0.05).**

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
