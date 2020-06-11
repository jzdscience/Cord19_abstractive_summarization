import pandas as pd

df = pd.read_csv('metadata.csv')
df = df[["cord_uid", "title", "abstract"]]
print("Original dataset shape = " + str(df.shape))

df = df[(df["title"].str.len() > 5) & (df["abstract"].str.len() > 50)]
print("Filtered dataset shape = " + str(df.shape))

print(df.head(3))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["abstract"])

true_k = 10
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :4]:
        print(' %s' % terms[ind])
    print()

df["cluster"] = model.labels_
for i in range(true_k):
    df_sub = df[df["cluster"] == i]
    print(df_sub.shape)
    print(df_sub.head(3))
    df_sub["abstract"].to_csv("train%d.article" % i, index=False)
    df_sub["title"].to_csv("train%d.summary" % i, index=False)
