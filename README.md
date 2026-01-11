👥 Customer Segmentation Project Using Machine Learning

Analyzing customer behavior to create meaningful customer segments for better marketing and business decisions using Machine Learning.

📌 Table of Contents

<a href="#overview">Overview</a>

<a href="#business-problem">Business Problem</a>

<a href="#dataset">Dataset</a>

<a href="#features-used">Features Used</a>

<a href="#tools--technologies">Tools & Technologies</a>

<a href="#project-structure">Project Structure</a>

<a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>

<a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>

<a href="#clustering-methods">Clustering Methods</a>

<a href="#key-insights">Key Insights</a>

<a href="#how-to-run-this-project">How to Run This Project</a>

<a href="#final-outcomes">Final Outcomes</a>

<a href="#author--contact">Author & Contact</a>

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project focuses on Customer Segmentation using Machine Learning techniques.
The goal is to group customers into different segments based on their behavior and spending patterns. These insights help businesses improve marketing strategies, customer targeting, and decision-making.

<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Understanding customers is very important for business growth. This project aims to :

=> Identify different types of customers

=> Find high-value and low-value customers

=> Improve targeted marketing strategies

=> Increase customer retention and satisfaction

=> Support data-driven business decisions

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

=> Customer data stored in CSV file(s)

=> Dataset includes customer behavior and spending information

=> Data files are stored in the /data/ folder

=> Final dataset prepared and used for clustering analysis

<h2><a class="anchor" id="features-used"></a>Features Used</h2>

The following features were used for customer segmentation <img width="1909" height="1027" alt="5" src="https://github.com/user-attachments/assets/7c3c394a-92dc-4db9-805b-2aa16f34a132" />
<img width="1109" height="450" alt="4" src="https://github.com/user-attachments/assets/f4af5f57-7664-4552-a0a5-8240397ac1b1" />
<img width="546" height="450" alt="3" src="https://github.com/user-attachments/assets/0e764641-2407-49c4-9d3e-3b58f5b89fb1" />
<img width="546" height="450" alt="2" src="https://github.com/user-attachments/assets/39bf7e9e-42e5-417a-b5c5-5c6af2627220" />
:

=> Customer ID

=> Age

=> Annual Income

=> Spending Score

=> Purchase Behavior Metrics
(Feature selection depends on data availability and relevance)

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

=> Python

=> Machine Learning

=> Pandas

=> NumPy

=> Matplotlib

=> Seaborn

=> Scikit-learn

=> Jupyter Notebook

=> GitHub

=> Git

=> PyCharm

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>
customer_segmentation/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── customers.csv
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── exploratory_data_analysis.ipynb
│   └── customer_segmentation.ipynb
│
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

=> Removed missing and duplicate values

=> Scaled numerical features for clustering

=> Checked for outliers

=> Prepared clean dataset for ML algorithms

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

=> Analyzed customer age, income, and spending patterns

=> Visualized distributions using histograms and box plots

=> Studied relationships between features using scatter plots

=> Identified patterns useful for clustering

<h2><a class="anchor" id="clustering-methods"></a>Clustering Methods</h2>

=> The following unsupervised learning algorithms were used:

=> K-Means Clustering

=> Used to create clear and well-separated customer groups

=> Hierarchical Clustering

=> Used to understand customer relationships using dendrograms

=> DBSCAN

=> Used to detect noise and outliers in customer data

<h2><a class="anchor" id="key-insights"></a>Key Insights</h2>

=> Identified multiple customer segments with different behaviors

=> Found high-spending and low-spending customer groups

=> Detected noise and outliers using DBSCAN

=> Compared results of different clustering algorithms

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

Clone the repository:

=> git clone https://github.com/Birbal5040/Customer_Segmentation.git


=> Install required libraries:

=> pip install -r requirements.txt


Open PyCharm:

=> PyCharm

=> Run PyCharm in order:

=> streamlit run app.py

=> wait some second

=> Now You will See Project

<h2><a class="anchor" id="final-outcomes"></a>Final Outcomes</h2>

=> Clear understanding of customer groups

=> Practical experience with unsupervised learning

=> Improved data analysis and visualization skills

=> Real world business use case of Machine Learning

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

Birbal Kumar
B.Tech Student | Machine Learning Enthusiast

🔗 LinkedIn: https://www.linkedin.com/in/birbalkumar-sf32/
🔗 GitHub: https://github.com/Birbal5040
