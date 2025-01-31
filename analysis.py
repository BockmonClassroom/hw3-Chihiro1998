import pandas as pd
import os
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind

# 定义数据文件夹路径
data_dir = "/root/DS5110/hw3-Chihiro1998/Data"

# 加载数据文件
t1_data = pd.read_csv(os.path.join(data_dir, "t1_user_active_min.csv"))
t2_data = pd.read_csv(os.path.join(data_dir, "t2_user_variant.csv"))
t3_data = pd.read_csv(os.path.join(data_dir, "t3_user_active_min_pre.csv"))
t4_data = pd.read_csv(os.path.join(data_dir, "t4_user_attributes.csv"))

# 打印每个数据集的前几行内容
# print("T1 Data (Active Minutes):")
# print(t1_data.head(), "\n")

# print("T2 Data (Variant Info):")
# print(t2_data.head(), "\n")

# print("T3 Data (Active Minutes Pre):")
# print(t3_data.head(), "\n")

# print("T4 Data (User Attributes):")
# print(t4_data.head(), "\n")

# 合并 T1（用户活动数据）与 T2（实验分组数据）
merged_t1_t2 = pd.merge(t1_data, t2_data[['uid', 'variant_number']], on="uid")

# 打印合并后的数据
print("Merged Data (T1 + T2):")
print(merged_t1_t2.head(), "\n")

# 保存合并后的数据到文件
merged_t1_t2.to_csv(os.path.join(data_dir, "merged_t1_t2.csv"), index=False)
print("Merged data saved to 'merged_t1_t2.csv'")

# 计算对照组（variant_number = 0）和实验组（variant_number = 1）的统计数据
control_group = merged_t1_t2[merged_t1_t2["variant_number"] == 0]
treatment_group = merged_t1_t2[merged_t1_t2["variant_number"] == 1]

# 计算均值和中位数
control_mean = control_group["active_mins"].mean()
control_median = control_group["active_mins"].median()
treatment_mean = treatment_group["active_mins"].mean()
treatment_median = treatment_group["active_mins"].median()

# 打印统计数据
print(f"Control Group - Mean: {control_mean}, Median: {control_median}")
print(f"Treatment Group - Mean: {treatment_mean}, Median: {treatment_median}")

from scipy.stats import ttest_ind

# 执行 t-test
t_stat, p_value = ttest_ind(control_group["active_mins"], treatment_group["active_mins"], equal_var=False)

# 打印 t-test 结果
print(f"T-test Statistic: {t_stat}, P-value: {p_value}")

# 解释结果
if p_value < 0.05:
    print("There is a statistically significant difference between the two groups (p < 0.05).")
else:
    print("No statistically significant difference was found (p >= 0.05).")


# 绘制箱线图
plt.figure(figsize=(8, 6))
plt.boxplot(
    [control_group["active_mins"], treatment_group["active_mins"]],
    tick_labels=["Control", "Treatment"]  # 修正参数，避免 Matplotlib 警告
)
plt.title("Boxplot of Active Minutes for Control and Treatment Groups")
plt.ylabel("Active Minutes")
plt.grid(True)

# 直接显示图像，而不保存
plt.show()

# 计算 IQR（四分位距）
Q1 = merged_t1_t2["active_mins"].quantile(0.25)
Q3 = merged_t1_t2["active_mins"].quantile(0.75)
IQR = Q3 - Q1

# 定义异常值范围
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 过滤掉异常值
filtered_data = merged_t1_t2[(merged_t1_t2["active_mins"] >= lower_bound) & (merged_t1_t2["active_mins"] <= upper_bound)]

# 打印异常值范围
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
print(f"Data Size Before Removing Outliers: {len(merged_t1_t2)}")
print(f"Data Size After Removing Outliers: {len(filtered_data)}")

# 重新保存去除异常值后的数据
filtered_data.to_csv(os.path.join(data_dir, "filtered_data.csv"), index=False)
print("Filtered data saved as 'filtered_data.csv'")