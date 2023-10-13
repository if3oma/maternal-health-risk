import pandas as pd

data = pd.DataFrame([[1, 2, 3],[1,2,5], [1, 2, 3], [1,2,5], [1,2,5]], columns=['a','b','c'])

train = data.sample(frac=0.7, random_state=0)
test = data.drop(train.index)


print(test.shape)
print("------------------------------------------------")
print(train.shape)