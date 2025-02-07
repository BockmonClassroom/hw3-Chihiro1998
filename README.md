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
The goal of this study is to analyze user engagement before and after an experiment. Specifically, we want to:
- Compare active minutes between the control group and the treatment group.
- Determine if the new platform changes impact user engagement.
- Use statistical methods to test if the changes are significant.

### 2. What data do we need to reach that objective?
For this section, we focus on two datasets:

✅ `t1_users_active_mins.csv` (User Activity Data)  
✅ `t2_users_variant.csv` (Experiment Group Assignment)  

These two datasets allow us to analyze engagement by experiment group.

### 3. How is the data in t1 currently organized?
The `t1_user_active_min.csv` file contains user activity logs, where each row represents **a specific user’s active minutes on a given date**.

### 4. How should it be organized for better utility?
To make the data useful for statistical analysis, we need to:  
1. **Merge `t1_user_active_min.csv` with `t2_user_variant.csv`** using `uid` as the key.  
2. **Add the `variant_number` column** to label each user as **control (0)** or **treatment (1)**.  
3. **Ensure the data is structured for comparison**, allowing us to analyze activity levels per experiment group.  

### 5. Organize the data.
After merging, the dataset (Data/merged_t1_t2.csv) now includes experiment labels, enabling statistical analysis.

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
