import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import tree
import matplotlib.pyplot as plt

# 1. Gerando dados sintéticos (para demonstração)
np.random.seed(42)
cerveja = np.sort(np.random.uniform(0, 10, 50))
nota = 2 + 0.5 * cerveja + np.random.normal(0, 0.5, 50)
df = pd.DataFrame({"cerveja": cerveja, "nota": nota})

X = df[["cerveja"]]
y = df["nota"]

# 2. Machine Learning - Regressão Linear
reg = linear_model.LinearRegression(fit_intercept=True)
reg.fit(X, y)
a, b = reg.intercept_, reg.coef_[0]

predict_reg = reg.predict(X)

# 3. Árvores de Decisão
# Árvore sem limite de profundidade (tende ao overfit)
arvore_full = tree.DecisionTreeRegressor(random_state=42)
arvore_full.fit(X, y)
predict_arvore_full = arvore_full.predict(X)

# Árvore com profundidade limitada
arvore_d2 = tree.DecisionTreeRegressor(random_state=42, max_depth=2)
arvore_d2.fit(X, y)
predict_arvore_d2 = arvore_d2.predict(X)

# 4. Visualização
plt.figure(figsize=(10, 6))
plt.scatter(X["cerveja"], y, label="Observado", color="gray", alpha=0.6)
plt.plot(X["cerveja"], predict_reg, label=f'Linear: y= {a:.2f} + {b:.2f}x', color="blue", linewidth=2)
plt.plot(X["cerveja"], predict_arvore_full, label='Árvore Full', color="green", linestyle="--")
plt.plot(X["cerveja"], predict_arvore_d2, label='Árvore Profundidade 2', color="red", linewidth=2)

plt.grid(True)
plt.title("Comparação: Regressão Linear vs. Árvores de Decisão")
plt.xlabel("Cerveja")
plt.ylabel("Nota")
plt.legend()
plt.show()