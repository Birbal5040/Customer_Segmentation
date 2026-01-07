#  --->>>>Python Libraries---->>>>
import streamlit as st
import pandas as pd

from src.visualization import (
    pca_visualization,
    cluster_bar_chart,
    cluster_pie_chart
)


from src.preprocessing import load_data, preprocess_data
from src.clustering import (
    kmeans_clustering,
    hierarchical_clustering,
    dbscan_clustering
)
from src.visualization import pca_visualization


#  ---->>>>PAGE CONFIG---->>>>
st.set_page_config(page_title="Customer Segmentation", layout="wide")

#st.title(" Customer Segmentation Project")

st.markdown(
    """
    <h1 style='text-align: center; color: #03A9F4;'>
        Customer Segmentation Project
    </h1>
    """,
    unsafe_allow_html=True
)

# ---->>>>Upload Data Set---->>>> 

st.sidebar.header(" Upload Dataset")
file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
else:
    df = load_data("data/Mall_Customers.csv")

st.subheader(" Raw Data")
st.dataframe(df.head())

# ---->>>> PREPROCESS ---->>>>
df_processed, scaled_data = preprocess_data(df)

# ---->>>> ALGORITHM SELECTION ---->>>>
st.sidebar.header(" Clustering Options")
algo = st.sidebar.selectbox(
    "Choose Algorithm",
    ["K-Means", "Hierarchical", "DBSCAN"]
)

# -CLUSTERING -

if algo == "K-Means":
    k = st.sidebar.slider("Number of Clusters (K)", 2, 10, 5)
    labels, score = kmeans_clustering(scaled_data, k)

elif algo == "Hierarchical":
    k = st.sidebar.slider("Number of Clusters", 2, 10, 5)
    labels, score = hierarchical_clustering(scaled_data, k)

else:
    eps = st.sidebar.slider("EPS", 0.1, 2.0, 0.5)
    min_samples = st.sidebar.slider("Min Samples", 2, 10, 5)
    labels, score = dbscan_clustering(scaled_data, eps, min_samples)


# ---->>>> RESULTS ---->>>>
df_processed["Cluster"] = labels


# CUSTOMER SEARCH
#st.subheader("Search Customer")

# Input Customer ID
# customer_id = st.number_input(
#     "Enter Customer ID",
#     min_value=int(df_processed["CustomerID"].min()),
#     max_value=int(df_processed["CustomerID"].max()),
#     step=1
# )
#
# # Search button
# if st.button("Search"):
#     result = df_processed[df_processed["CustomerID"] == customer_id]
#
#     if not result.empty:
#         st.success("Customer Found ✅")
#         st.dataframe(result)
#     else:
#         st.error("Customer ID not found ❌")



st.subheader("Clustered Data")
st.dataframe(df_processed.head())

st.metric("Silhouette Score", round(score, 3))

st.subheader("Cluster Distribution")

col1, col2 = st.columns(2)

with col1:
    bar_fig = cluster_bar_chart(df_processed)
    st.plotly_chart(bar_fig, use_container_width=True)

with col2:
    pie_fig = cluster_pie_chart(df_processed)
    st.plotly_chart(pie_fig, use_container_width=True)

# ---->>>> PCA VISUALIZATION ---->>>>
st.subheader("Cluster Visualization")
fig = pca_visualization(scaled_data, labels)
st.plotly_chart(fig, use_container_width=True)


# ---->>>>CLUSTER PROFILING ---->>>>
st.subheader("Cluster Profiling")

profile = df_processed.groupby("Cluster")[["Age", "Income", "Spending"]].mean()
st.dataframe(profile)


# Birbal Kumar


# ---->>>> DOWNLOAD RESULT ---->>>>
st.subheader("Download Results")

csv = df_processed.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Segmented Customers",
    csv,
    "customer_segments.csv",
    "text/csv"
)

#---->>>> CUSTOMER SEARCH ---->>>>
st.subheader("Search Customer")

cust_id = st.number_input("Enter Customer ID", min_value=1)

if cust_id in df_processed["CustomerID"].values:
    result = df_processed[df_processed["CustomerID"] == cust_id]
    st.write(result)
else:
    st.warning("Customer ID not found")


