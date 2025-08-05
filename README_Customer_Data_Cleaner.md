
# Customer Data Cleaner

##  Project Title
**Customer Data Cleaner**

---

##  Objective
To clean a messy customer sales dataset by:
- Removing blank/unnecessary columns
- Handling missing values
- Fixing data type inconsistencies
- Removing duplicate records
- Exporting a clean dataset for analysis or visualization

---

##  Tools & Libraries Used
- **Python**
- **Pandas** – for data manipulation
- **NumPy** – for numerical operations
- **Matplotlib & Seaborn** – visualization (optional)
- **Google Colab** – development environment

---

##  Dataset
- File Name: `Customer sale Data.csv`
- Source: `Kaggle`
- Cleaned File Output: `Customer_sale_clean Data.csv`

---

##  Data Cleaning Steps

### Step 1: Drop Unrelated Columns
Removed columns like `Status`, `unnamed1`.

### Step 2: Handle Missing Values
- Checked for missing values
- Dropped rows containing null entries

### Step 3: Change Data Types
Converted `Amount` column to integer type.

### Step 4: Summary Statistics
Reviewed descriptive statistics for `Age`, `Orders`, and `Amount`.

### Step 5: Check for Duplicates
Checked for duplicate rows in the dataset.

### Step 6: Export Cleaned Data
Saved cleaned dataset to CSV for further analysis or use in dashboards.

---

## Expected Result

A **clean and well-formatted dataset** that is:
- Free of missing and duplicate values
- Correctly formatted with appropriate data types
- Suitable for:
  - Data analysis
  - Dashboard creation (Power BI, Tableau, etc.)
  - Further machine learning or reporting tasks

---

##  Conclusion
This project demonstrates fundamental data cleaning techniques using Python and Pandas. The resulting dataset is structured, reliable, and ready for real-world analytical applications.
