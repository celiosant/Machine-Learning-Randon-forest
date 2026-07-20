#%%
import pandas as pd

df= pd.read_csv("../dados/abt_churn.csv")

df.head()
df.shape()
# %%
oot = df[df["dtRef"] == df["dtRef"].max()].copy()
oot.shape
# %%

df_train= df[df["dtRef"] < df["dtRef"].max()].copy()

df_train.shape


# %%
#separação do das features e target


#variaveis
features =df_train.columns[2:-1]
target= "flagChurn"

X, y = df_train[features], df_train[target]


# %%
from sklearn import model_selection

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,
                                                               random_state=42,
                                                                test_size=0.2,
                                                                stratify=y
                                                                             )
# %%
print("Taxa variável resposta Base: ",y.mean())
print("Taxa variável resposta Treino: ",y_train.mean())
print("Taxa variável resposta Teste: ",y_test.mean())
# %%
