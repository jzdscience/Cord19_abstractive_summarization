import pandas as pd
import numpy as np

df = pd.read_csv("train_dataset.csv")
print(df.head)

'''
def split_data_on_idx(df, idx):
    df_sub = df[df["topic_cluster_number"] == idx]
    df_sub = df_sub[["paper_id", "title", "abstract"]]

    df_sub = df_sub[(df_sub["title"].str.len() > 5) & (df_sub["abstract"].str.len() > 30)]
    df_sub["title"] = df_sub["title"].str.strip(' \"')
    df_sub["abstract"] = df_sub["abstract"].str.strip(' \"')
    df_sub["abstract"] = df_sub["abstract"].str[9:]
    df_sub["title"] = df_sub["title"].astype(str) + " <S_SEP>"
    df_sub["abstract"] = df_sub["abstract"].astype(str) + " <S_SEP>"
    print(df_sub.head)
    assignmnt = np.random.rand(len(df_sub))
    msk_train = assignmnt < 0.6
    msk_dev = np.logical_and((0.6 <= assignmnt), (assignmnt < 0.8))
    msk_test = 0.8 <= assignmnt
    df_sub[msk_train]["abstract"].to_csv("original_data/train_%d.article" % idx, index=False)
    df_sub[msk_train]["title"].to_csv("original_data/train_%d.summary" % idx, index=False)
    df_sub[msk_dev]["abstract"].to_csv("original_data/dev_%d.article" % idx, index=False)
    df_sub[msk_dev]["title"].to_csv("original_data/dev_%d.summary" % idx, index=False)
    df_sub[msk_test]["abstract"].to_csv("original_data/test_%d.article" % idx, index=False)
    df_sub[msk_test]["title"].to_csv("original_data/test_%d.summary" % idx, index=False)

split_data_on_idx(df, 9)
split_data_on_idx(df, 2)
'''


def combine_titles_on_idx(df, idx):
    df_sub = df[df["topic_cluster_number"] == idx]
    df_sub = df_sub[["paper_id", "title", "abstract"]]

    df_sub = df_sub[(df_sub["title"].str.len() > 5) & (df_sub["abstract"].str.len() > 30)]
    df_sub["title"] = df_sub["title"].str.strip(' \"')
    df_sub["abstract"] = df_sub["abstract"].str.strip(' \"')
    df_sub["abstract"] = df_sub["abstract"].str[9:]
    df_sub["title"] = df_sub["title"].astype(str) + " <S_SEP>"
    df_sub["abstract"] = df_sub["abstract"].astype(str) + " <S_SEP>"
    print(df_sub.head)

    output = []
    buf = []
    char_count = 0
    for title in df_sub["title"]:
        len_title = len(title.strip().split())
        if char_count + len_title >= 512:
            output.append(' '.join(buf))
            buf = []
            char_count = 0
        buf.append(title)
        char_count += len_title
    output.append(' '.join(buf))

    with open("original_data/all_%d.article" % idx, "w+") as f:
        f.write('\n'.join(output))

combine_titles_on_idx(df, 9)
combine_titles_on_idx(df, 2)