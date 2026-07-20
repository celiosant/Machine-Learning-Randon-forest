#%%
import pandas as pd

df= pd.read_csv("dados/DadosComunidade(respostas).csv")
df.head()
# %%


df= df.replace({"Sim":1 , "Não":0})
df.head()# %%

# %%
num_vars = [
    "Curte games?",
    "Curte futebol?",
    "Curte livros?",
    "Curte jogos de tabuleiro?",
    "Curte jogos de fórmula 1?",
    "Curte jogos de MMA?",
]
dummy_vars= [ "Como conheceu o Téo Me Why?",
               "Quantos cursos acompanhou do Téo Me Why?",
               "Estado que mora atualmente",
               "Área de Formação",
               "Tempo que atua na área de dados",
               "Posição da cadeira (senioridade)",]


# 1. As colunas do seu df original não tenham espaços extras nas pontas
df.columns= df.columns.str.strip()

# 2. Cria o DataFrame de dummies (convertendo para 0 e 1)
df_analise= pd.get_dummies(df[dummy_vars]).astype(int)


# 3. Copia as variáveis binárias
# Se elas já forem 0/1 ou True/False, o código abaixo basta:
df_analise[num_vars] = df[num_vars].astype(int)

df_analise["Pessoa feliz?"] = df["Você se considera uma pessoa feliz?"].astype(int)

df_analise

# %%

features= df_analise.columns[:-1].tolist()
y_temp = df_analise["Pessoa feliz?"].astype(str).str.strip()
mascara_validos = y_temp.isin(["1.0", "1", "0", "0.0"])

X_treino = df_analise.loc[mascara_validos, features].copy()
y_treino = y_temp[mascara_validos].astype(float).astype(int)


from sklearn import tree
from sklearn import naive_bayes
from sklearn import linear_model

arvore = tree.DecisionTreeClassifier(
    random_state=42, 
    min_samples_leaf=6
)

# Passando as novas variáveis limpas
arvore.fit(X_treino, y_treino)

naive = naive_bayes.GaussianNB()
naive.fit(X_treino, y_treino)

reg = linear_model.LogisticRegression(penalty=None, fit_intercept=True)
reg.fit(X_treino,y_treino)


# %%

arvore_predict= arvore.predict(X_treino)
arvore_predict

df_predict = df_analise[['Pessoa feliz?']].copy()
df_predict['predict_arvore'] = arvore_predict
df_predict['proba_arvore'] = arvore.predict_proba(X_treino)[:,1]

df_predict['predict_naive'] = naive.predict(X_treino)
df_predict['proba_naive'] = naive.predict_proba(X_treino)[:,1]

df_predict['predict_reg'] = reg.predict(X_treino)
df_predict['proba_reg'] = reg.predict_proba(X_treino)[:,1]


# %%
#acuracia

(df_predict["Pessoa feliz?"]) == df_predict["predict_arvore"].mean()
# %%
 # matriz de confusão

pd.crosstab(df_predict["Pessoa feliz?"], df_predict["predict_arvore"])
# %%

total_feliz=(df_predict["Pessoa feliz?"] == 1).sum()
print(total_feliz)

df_analise["Pessoa feliz?"].mean()

 # %%
from sklearn import metrics

gabarito = df_predict["Pessoa feliz?"].astype(int)
previsoes = df_predict["predict_arvore"].astype(int)

# Calcula a acurácia
acc_arvore = metrics.accuracy_score(gabarito, previsoes)
acc_arvore

#Precisão

presisao_arvore = metrics.precision_score(gabarito, previsoes)
presisao_arvore

#Recall 

recall_arvore = metrics.recall_score(gabarito, previsoes)
recall_arvore

#Especificidade

especificidade_arvore = metrics.recall_score(gabarito, previsoes, pos_label=0)
especificidade_arvore


acc_naive = metrics.accuracy_score(df_predict['Pessoa feliz?'], df_predict['predict_naive'])
precisao_naive = metrics.precision_score(df_predict['Pessoa feliz?'], df_predict['predict_naive'])
recall_naive = metrics.recall_score(df_predict['Pessoa feliz?'], df_predict['predict_naive'])
roc_naive = metrics.roc_curve(df_predict['Pessoa feliz?'], df_predict['proba_naive'])
auc_naive = metrics.roc_auc_score(df_predict['Pessoa feliz?'], df_predict['proba_naive'])
auc_naive

acc_reg = metrics.accuracy_score(df_predict['Pessoa feliz?'], df_predict['predict_reg'])
precisao_reg = metrics.precision_score(df_predict['Pessoa feliz?'], df_predict['predict_reg'])
recall_reg = metrics.recall_score(df_predict['Pessoa feliz?'], df_predict['predict_reg'])
roc_reg = metrics.roc_curve(df_predict['Pessoa feliz?'], df_predict['proba_reg'])
auc_reg = metrics.roc_auc_score(df_predict['Pessoa feliz?'], df_predict['proba_reg'])
auc_reg



# %%

# Curva Roc
import matplotlib.pyplot as plt

roc_arvore= metrics.roc_curve(gabarito, df_predict["proba_arvore"])

auc_arvore= metrics.roc_auc_score(gabarito, df_predict["proba_arvore"])



import matplotlib.pyplot as plt

plt.figure(dpi=400)
plt.plot(roc_arvore[0], roc_arvore[1], "o-")
plt.plot(roc_naive[0], roc_naive[1], 'o-')
plt.plot(roc_reg[0], roc_reg[1], 'o-')
plt.grid(True)
plt.title("Curva ROC")
plt.xlabel("1 - Especificidade (FPR)")
plt.ylabel("Sensibilidade / Recall (TPR)")

plt.legend([
    f"Árvore: {auc_arvore:.2f}",
    f"Naive: {auc_naive:.2f}",
    f"Reg Log.: {auc_reg:.2f}",
])

plt.show()



# %%
plt.hist(df_predict["proba_arvore"])
# %%

# %%
# import do modelo 


pd.Series({"model": reg, "features":features}).to_pickle("model_feliz.pkl")
# %%
