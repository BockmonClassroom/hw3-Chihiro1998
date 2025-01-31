[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tQ2iv1EY)
# HW3 - Hypothesis Testing / A/B Testing

**Author:** Yuchen (Olivia) Kuang  
**Date:** 1/31/2025  

## 📌 Overview  
This project focuses on **A/B testing and hypothesis testing** to analyze whether a new platform layout increases user engagement. The dataset consists of user activity logs, experiment group assignments, and user attributes.

---

## 📂 Part 1 : Getting to know your data (5 Points)  
We are given **four CSV files** and **one text file** containing essential data for this study. Below is a description of each dataset:

### 📌 t1_users_active_mins.csv
This file records **user activity minutes** on the platform for specific dates.

- **Columns:**
  - `uid` → User ID  
  - `dt` → Date of recorded activity  
  - `active_mins` → Number of minutes the user was active  

- **Purpose:**  
  - Measures user engagement.  
  - Helps evaluate whether the experiment influenced time spent on the platform.  

### 📌 t2_users_variant.csv
This file contains **experiment group assignments** for each user.

- **Columns:**
  - `uid` → User ID  
  - `variant_number` → Experiment group (`0 = control`, `1 = treatment`)  
  - `dt` → Date when the user entered the experiment  
  - `signup_date` → User’s original signup date  

- **Purpose:**  
  - Distinguishes between **control** and **treatment groups**.  
  - Enables A/B testing to compare user activity.  


### 📌 t3_users_active_mins_pre.csv
This file contains **user activity data before the experiment started**, following the same format as `t1_users_active_mins.csv`.

- **Columns:**
  - `uid` → User ID  
  - `dt` → Date of recorded activity  
  - `active_mins` → Number of minutes the user was active  

- **Purpose:**  
  - Allows for **before-and-after** analysis.  
  - Helps assess whether the new platform layout had an impact on engagement.  

### 📌 t4_users_attributes.csv
This file provides **user demographic and behavioral attributes**.

- **Columns:**
  - `uid` → User ID  
  - `gender` → Male or Female  
  - `user_type` → Reader, Non-Reader, New User, or Contributor  

- **Purpose:**  
  - Enables segmentation analysis based on **user behavior and demographics**.  
  - Helps identify whether specific user groups were more affected by the experiment.  

---

### 📌 table_schema.txt 
This file contains **metadata and schema definitions** for all datasets.

- **Purpose:**  
  - Describes column names, data types, and meanings of variables.  
  - Ensures consistency and proper interpretation of the dataset.  

---

## 📂 Part 2 : Organizing the Data (15 Points)  

### 1.	What is the overall objective of this study?
The primary objective of this study is to determine whether the new platform layout increases user engagement by analyzing user activity before and after the experiment. This is done through A/B testing, where users are divided into control (variant_number = 0) and treatment (variant_number = 1) groups. By comparing the active minutes of users in both groups, we can statistically evaluate whether the experiment had a significant impact.

### 2.	What data do we need to reach that objective?


### 3.	How is the data in t1 currently organized?

### 4.	How should it be organized for better utility?

### 5.	Organize the data.

---


## 📂 Part 3 : Statistical Analysis (10 Points)

---