#%%
import pandas as pd
import sklearn 
import matplotlib.pyplot as plt
# %%

df=pd.read_parquet("dados/dados_clones.parquet")
from sklearn import tree
df
# %%
df.columns
df.shape
df
# %%

features=[ 'Massa(em kilos)', 'General Jedi encarregado',
       'Estatura(cm)', 'Distância Ombro a ombro', 'Tamanho do crânio',
       'Tamanho dos pés', 'Tempo de existência(em meses)']

target= ["Status "]

X = pd.get_dummies(df[features])
Y = df["Status "]
#%%
# treinamento do dados 

model=tree.DecisionTreeClassifier(max_depth=3, criterion="entropy")
model.fit(X,Y)

# %%
#plot da arvore
from sklearn.metrics import accuracy_score
y_pred= model.predict(X)
print (f"Acurácia do modelo:{accuracy_score(Y, y_pred):.2%}")
plt.figure(figsize=(20,10), dpi=400)

tree.plot_tree( model, 
               feature_names=X.columns,
               class_names=model.classes_,
               filled=True,
               rounded=True,
               fontsize=8)
plt.show()