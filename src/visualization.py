

#Python Libraries

import plotly.express as px
from sklearn.decomposition import PCA
import pandas as pd

def pca_visualization(data, labels):
    pca = PCA(n_components=2)
    components = pca.fit_transform(data)

    df_plot = pd.DataFrame({
        'PC1': components[:, 0],
        'PC2': components[:, 1],
        'Cluster': labels.astype(str)
    })

    fig = px.scatter(
        df_plot,
        x='PC1',
        y='PC2',
        color='Cluster',
        title='Customer Segments (PCA)'
    )
    return fig




#BAR CHART

def cluster_bar_chart(df):
    count_df = df['Cluster'].value_counts().reset_index()
    count_df.columns = ['Cluster', 'Customers']

    fig = px.bar(
        count_df,
        x='Cluster',
        y='Customers',
        text='Customers',
        title='Number of Customers per Cluster'
    )
    return fig





# PIE CHART
def cluster_pie_chart(df):
    count_df = df['Cluster'].value_counts().reset_index()
    count_df.columns = ['Cluster', 'Customers']

    fig = px.pie(
        count_df,
        names='Cluster',
        values='Customers',
        title='Customer Distribution by Cluster'
    )
    return fig



