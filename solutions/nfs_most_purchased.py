import pandas as pd
import dask.dataframe as dd

df = dd.read_csv("data/nfs/NFS*.csv")
food_mapping = pd.read_csv("data/nfs/food_mapping.csv")

df1974 = df.get_partition(0)
minfd74 = (df1974.groupby('minfd')
           .apply(len, meta='size')
           .compute()
           .idxmax())

# alternatively, use the category type
# you first have to materialize the categorical
# though this should work with fixes in pandas 0.18.2

df1974.minfd.astype('category').compute().describe()['top']
