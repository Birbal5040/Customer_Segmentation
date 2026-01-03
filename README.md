# 🧩 Customer Segmentation Using Clustering Algorithms

This project is an **interactive Customer Segmentation web application** built using **Streamlit** and **Machine Learning clustering techniques**.  
It allows users to upload customer data, apply different clustering algorithms, visualize results, and download segmented customer data.

---

## 🚀 Features

- 📂 Upload your own CSV dataset or use the default dataset
- 🔍 Data preprocessing and scaling
- 🤖 Multiple clustering algorithms:
  - K-Means
  - Hierarchical Clustering
  - DBSCAN
- 📊 Interactive visualizations:
  - PCA-based cluster visualization
  - Cluster distribution (Bar chart & Pie chart)
- 📈 Silhouette score evaluation
- 🧠 Cluster profiling (mean of customer attributes)
- 🔎 Search customers by Customer ID
- ⬇️ Download segmented dataset as CSV

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Plotly**
- **NumPy**

---

## 📁 Project Structure

customer-segmentation/

│

├── app.py # Main Streamlit application

├── data/

│ └── Mall_Customers.csv # Default dataset

│

├── src/

│ ├── preprocessing.py # Data loading & preprocessing

│ ├── clustering.py # Clustering algorithms

│ └── visualization.py # Plotly visualizations

│

├── requirements.txt # Required Python libraries

└── README.md # Project documentation


---

## 📊 Clustering Algorithms Used

### 1. K-Means Clustering
- User-defined number of clusters (K)
- Fast and effective for well-separated data

### 2. Hierarchical Clustering
- Agglomerative approach
- Suitable for discovering hierarchical relationships

### 3. DBSCAN
- Density-based clustering
- Detects noise and outliers automatically

---

## 📈 Visualizations

- **PCA Scatter Plot** for cluster separation
- **Bar Chart** for cluster counts
- **Pie Chart** for cluster distribution

---

## 📥 Dataset Format

The dataset should contain:
- `CustomerID`
- `Age`
- `Income`
- `Spending`

(Default dataset: *Mall Customers Dataset*)

---

## ▶️ How to Run the Application

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation


###2️⃣ Install Dependencies
pip install -r requirements.txt


###3️⃣ Run Streamlit App
streamlit run app.py
