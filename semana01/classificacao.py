#%%

import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_excel("dados/dados_cerveja_nota.xlsx")
df.head(50)


df["aprovado"]= (df["nota"] >5).astype(int)
df
# %%
plt.plot(df["cerveja"], df["aprovado"], "o", color = "darkblue")
plt.grid(True)
plt.title("Cervejas vs Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovação")
plt.legend()
plt.show()



# %%
#----------------- imports--------------------------------
from sklearn import linear_model
from sklearn import tree
from sklearn import naive_bayes



reg= linear_model.LogisticRegression(penalty=None, fit_intercept=True)
reg.fit(df[["cerveja"]], df[["aprovado"]])



# %%
# ---------Regressao--------------------

reg_predict = reg.predict(df[["cerveja"]].drop_duplicates())
reg_proba= reg.predict_proba(df[["cerveja"]].drop_duplicates())[:,1]


#------------------- Arvore-----------------------
arvore_full= tree.DecisionTreeClassifier(random_state=42)
arvore_full.fit(df[["cerveja"]], df[["aprovado"]])
arvore_full_predict=arvore_full.predict(df[["cerveja"]].drop_duplicates())
arvore_full_proba= arvore_full.predict_proba(df[["cerveja"]].drop_duplicates())[:,1]


# ---------Navie bayers--------------------------

nb=naive_bayes.GaussianNB()
nb.fit(df[["cerveja"]], df[["aprovado"]])

nb_predict = nb.predict(df[["cerveja"]].drop_duplicates())
nb_proba = nb.predict_proba(df[["cerveja"]].drop_duplicates())[:,1]

#%%
# ----------------- plots -------------------------------

plt.figure(dpi=400)
plt.plot(df["cerveja"], df["aprovado"], "o", color = "darkblue")
plt.grid(True)
plt.title("Cervejas vs Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovação")


plt.plot(df["cerveja"].drop_duplicates(), reg_predict, color="green")
plt.plot(df["cerveja"].drop_duplicates(), reg_proba, color="red")

plt.plot(df["cerveja"].drop_duplicates(), arvore_full_predict, color="darkorange")
plt.plot(df["cerveja"].drop_duplicates(), arvore_full_proba, color="magenta")

plt.plot(df["cerveja"].drop_duplicates(), nb_predict, color="gray")
plt.plot(df["cerveja"].drop_duplicates(), nb_proba, color="maroon")


plt.hlines(0.5, xmin=1, xmax=9, linestyles="--", color="black")

plt.legend(["observações",
            "Reg_predict",
            "Reg_proba", 
            "arvore_full_predict",
              "arvore_full_proba",
              "nb_predict",
              "nb_proba"])
# %%
