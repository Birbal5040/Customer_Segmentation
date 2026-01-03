
#Python Libraries


from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, fcluster




def kmeans_clustering(data, k):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)
    score = silhouette_score(data, labels)
    return labels, score





def hierarchical_clustering(data, k):
    linkage_matrix = linkage(data, method='ward')
    labels = fcluster(linkage_matrix, k, criterion='maxclust')
    score = silhouette_score(data, labels)
    return labels, score






def dbscan_clustering(data, eps=0.5, min_samples=5):
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(data)

    if len(set(labels)) > 1 and -1 not in set(labels):
        score = silhouette_score(data, labels)
    else:
        score = -1

    return labels, score
