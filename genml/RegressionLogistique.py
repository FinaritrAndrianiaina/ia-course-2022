import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('telecom.csv')

data["Churn?"] = data["Churn?"].astype('category')

# on définit x et y
y = data["Churn?"].cat.codes
# on ne prend que les colonnes quantitatives
x = data.select_dtypes(np.number).drop(["Account Length","Area Code"],axis=1)

modele_logit = LogisticRegression(penalty='none',solver='newton-cg')
modele_logit.fit(x,y)

pd.DataFrame(np.concatenate([modele_logit.intercept_.reshape(-1,1),
                             modele_logit.coef_],axis=1),
                             index = ["coef"],
                             columns = ["constante"]+list(x.columns)).T

# on ajoute une colonne pour la constante
x_stat = sm.add_constant(x)
# on ajuste le modèle
model = sm.Logit(y, x_stat)
result = model.fit()

result.summary()