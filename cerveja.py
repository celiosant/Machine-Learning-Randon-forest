#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree


df= pd.read_excel("dados/dados_cerveja.xlsx")
#%%
features= ["temperatura", "copo","espuma", "cor"]
target= ["classe"]

#%%
#tratar os dado 
X= df[features]
Y= df[target]

X = pd.get_dummies(df[features])
Y = df["classe"]
#%%
# treinamento do dados 

model=tree.DecisionTreeClassifier()
model.fit(X,Y)

# %%
#plot da arvore

plt.figure(dpi=400)

tree.plot_tree( model, 
               feature_names=X.columns,
               class_names=model.classes_,
               filled=True)
plt.show
# %%
