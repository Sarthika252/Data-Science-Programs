import pandas as pd
import numpy as np
from scipy.stats import zscore
# ------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------
df = pd.read_csv("students.csv")

print("\n--- ORIGINAL DATASET ---")
print(df.to_string(index=False))

print("\n--- FIRST FIVE RECORDS ---")
print(df.head())

# ------------------------------------------------
# 2. CHECK DATASET INFORMATION
# ------------------------------------------------
print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- DATASET INFORMATION ---")
df.info()

# ------------------------------------------------
# 3. DETECT MISSING VALUES
# ------------------------------------------------
print("\n--- MISSING VALUES IN EACH COLUMN ---")
print(df.isnull().sum())

print("\n--- TOTAL MISSING VALUES ---")
print(df.isnull().sum().sum())

# ------------------------------------------------
# 4. REMOVE ROWS WITH MISSING VALUES
# ------------------------------------------------
df_drop_rows = df.dropna()

print("\n--- AFTER REMOVING ROWS WITH MISSING VALUES ---")
print(df_drop_rows)
print("Rows remaining:", len(df_drop_rows))

# ------------------------------------------------
# 5. REMOVE COLUMNS WITH MISSING VALUES
# ------------------------------------------------
df_drop_columns = df.dropna(axis=1)

print("\n--- AFTER REMOVING COLUMNS WITH MISSING VALUES ---")
print(df_drop_columns.head())
print("Remaining columns:", df_drop_columns.columns.tolist())

# ------------------------------------------------
# 6. FILL NUMERICAL MISSING VALUES WITH MEAN
# ------------------------------------------------
df_mean = df.copy()

age_mean = df_mean["Age"].mean()

df_mean["Age"] = df_mean["Age"].fillna(age_mean)

print("\n--- AGE FILLED WITH MEAN ---")
print("Mean age:", age_mean)
print(df_mean[["Name", "Age"]])

# ------------------------------------------------
# 7. FILL NUMERICAL MISSING VALUES WITH MEDIAN
# ------------------------------------------------
df_median = df.copy()

salary_median = df_median["Salary"].median()

df_median["Salary"] = df_median["Salary"].fillna(
    salary_median
)

print("\n--- SALARY FILLED WITH MEDIAN ---")
print("Median salary:", salary_median)
print(df_median[["Name", "Salary"]])

# ------------------------------------------------
# 8. FILL CATEGORICAL VALUES WITH MODE
# ------------------------------------------------
df_mode = df.copy()

gender_mode = df_mode["Gender"].mode()[0]

df_mode["Gender"] = df_mode["Gender"].fillna(gender_mode)

print("\n--- GENDER FILLED WITH MODE ---")
print("Most common gender:", gender_mode)
print(df_mode[["Name", "Gender"]])

# ------------------------------------------------
# 9. FORWARD FILL AND BACKWARD FILL
# ------------------------------------------------

df_ffill = df.copy()
df_ffill["Age"] = df_ffill["Age"].ffill()

print("\n--- FORWARD FILL ---")
print(df_ffill[["Name", "Age"]])

df_bfill = df.copy()
df_bfill["Age"] = df_bfill["Age"].bfill()

print("\n--- BACKWARD FILL ---")
print(df_bfill[["Name", "Age"]])

# ------------------------------------------------
# 10. DETECT OUTLIERS USING IQR
# ------------------------------------------------

salary = df["Salary"]

Q1 = salary.quantile(0.25)
Q3 = salary.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\n--- IQR OUTLIER DETECTION ---")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)

outliers_iqr = df[
    (df["Salary"] < lower_bound) |
    (df["Salary"] > upper_bound)
]

print("\n--- OUTLIERS FOUND USING IQR ---")
print(outliers_iqr[["Name", "Salary"]])

# ------------------------------------------------
# 11. DETECT OUTLIERS USING Z-SCORE
# ------------------------------------------------

df_zscore = df.copy()

df_zscore["Z_Score"] = zscore(df_zscore["Salary"])

outliers_zscore = df_zscore[
    df_zscore["Z_Score"].abs() > 3
]

print("\n--- Z-SCORE OUTLIERS ---")
print(outliers_zscore[["Name", "Salary", "Z_Score"]])

# ------------------------------------------------
# 12. REMOVE OUTLIERS
# ------------------------------------------------

df_removed = df[
    (df["Salary"] >= lower_bound) &
    (df["Salary"] <= upper_bound)
].copy()

print("\n--- AFTER REMOVING OUTLIERS ---")
print(df_removed[["Name", "Salary"]])
print("Rows remaining:", len(df_removed))

# ------------------------------------------------
# 13. CAP OUTLIERS USING CLIP
# ------------------------------------------------

df_capped = df.copy()

df_capped["Salary"] = df_capped["Salary"].clip(
    lower=lower_bound,
    upper=upper_bound
)

print("\n--- AFTER CAPPING OUTLIERS ---")
print(df_capped[["Name", "Salary"]])

# ------------------------------------------------
# 14. LOG TRANSFORMATION
# ------------------------------------------------

df_log = df.copy()

df_log["Salary_Log"] = np.log1p(df_log["Salary"])

print("\n--- LOG-TRANSFORMED SALARY ---")
print(df_log[["Name", "Salary", "Salary_Log"]])

# ------------------------------------------------
# 15. REPLACE HIGH OUTLIERS WITH MEDIAN
# ------------------------------------------------

df_replaced = df.copy()

original_median = df_replaced["Salary"].median()

df_replaced.loc[
    df_replaced["Salary"] > upper_bound,
    "Salary"
] = original_median

print("\n--- OUTLIERS REPLACED WITH MEDIAN ---")
print(df_replaced[["Name", "Salary"]])

# ------------------------------------------------
# 16. COMPLETE DATA-CLEANING WORKFLOW
# ------------------------------------------------

df_clean = df.copy()

# Fill missing numerical values
df_clean["Age"] = df_clean["Age"].fillna(
    df_clean["Age"].median()
)

# Fill missing categorical values
df_clean["Gender"] = df_clean["Gender"].fillna(
    df_clean["Gender"].mode()[0]
)

# Recalculate salary bounds from the original salary data
salary_data = df_clean["Salary"]

q1 = salary_data.quantile(0.25)
q3 = salary_data.quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Cap extreme salaries
df_clean["Salary"] = df_clean["Salary"].clip(
    lower=lower,
    upper=upper
)

print("\n--- FINAL CLEANED DATASET ---")
print(df_clean.to_string(index=False))

print("\n--- MISSING VALUES AFTER CLEANING ---")
print(df_clean.isnull().sum())

# Save cleaned dataset
df_clean.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved as cleaned_students.csv")