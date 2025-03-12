import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

#generate a larger simulated dataset for initial training
data = pd.DataFrame({
    'user_id': np.random.randint(1000, 9999, 1000),
    'login_attempts': np.random.randint(1, 10, 1000),
    'location': np.random.choice(['USA', 'India', 'China', 'Brazil'], 1000),
    'time_spent_seconds': np.random.randint(1, 600, 1000),
    'device': np.random.choice(['mobile', 'web', 'tablet'], 1000),
    'is_fraud': np.random.choice([0, 1], p=[0.95, 0.05], size=1000)
})

#preprocessing
X=pd.get_dummies(data.drop(['user_id','is_fraud'],axis=1))
y=data['is_fraud']

model=RandomForestClassifier(class_weight='balanced')
model.fit(X,y)

#save model
joblib.dump(model, 'fraud_model.pkl')