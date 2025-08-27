# 🍽️ Tips Dataset Analysis - Exploratory Data Analysis (EDA)

Welcome to the **Tips Dataset Analysis** project!,
This repository showcases a detailed **Exploratory Data Analysis (EDA)**,
using **Python**, **Pandas**, **Seaborn**, and **Matplotlib** to uncover insights from restaurant bills and tips.  

---

## 🧠 Dataset Overview

The `tips` dataset contains information about restaurant bills and tips, including:

- 💵 **total_bill**: Total bill amount in USD  
- 💰 **tip**: Tip given by the customer  
- 👩‍🦰/👨‍🦰 **sex**: Gender of the customer  
- 🚬 **smoker**: Whether the customer is a smoker  
- 📅 **day**: Day of the week  
- 🕑 **time**: Lunch or Dinner  
- 👥 **size**: Size of the dining party  

---

## 🔍 Steps of Analysis

### 1️⃣ Understand the Data
- Display first few rows using `head()`  
- Check dataset info and types with `info()`  
- Generate descriptive statistics using `describe()`  

### 2️⃣ Descriptive Statistics
- Summary statistics such as mean, median, min, max, and quartiles  
- Helps understand the distribution and spread of numeric variables  

### 3️⃣ Data Visualization

- **📊 Histogram** – Distribution of `total_bill`
  
  ![Histogram](images/total_bill_histogram.png)

- **📈 Scatter Plot** – Relationship between `total_bill` and `tip` segmented by `time`
  
  ![Scatter Plot]("C:\Users\Dikesh Chavhan\OneDrive\Desktop\TASK\TASKS\CODTECH(DATA SCIENCE)\Task_1 output\Figure_2.png")

- **🟦 Heatmap** – Correlation matrix of numerical features
  
  ![Heatmap](images/correlation_heatmap.png)

- **📦 Boxplot** – Identify outliers in `total_bill`
  
  ![Boxplot](images/total_bill_boxplot.png)

---

## 📈 Key Insights

- ✅ Positive correlation between `total_bill` and `tip`  
- 🍽️ Dinner bills are generally higher than lunch bills  
- ⚠️ Some outliers are present in `total_bill`  
- 🔍 Correlation heatmap helps identify relationships for potential predictive modeling  

---

## 🛠️ Technologies Used

- **Python 3.x**  
- **Pandas** – Data manipulation  
- **Seaborn** – Statistical visualizations  
- **Matplotlib** – Plotting library  

---

