# Step 1: Install SDV if you haven't
# pip install sdv

from sdv.tabular import CTGAN
import pandas as pd
import numpy as np

# Step 2: Create sample fraud + legitimate transaction dataset
np.random.seed(42)
n_legit = 1000
n_fraud = 50

legit = pd.DataFrame({
    'amount': np.random.normal(50, 10, n_legit),
    'merchant_id': np.random.randint(1000, 1100, n_legit),
    'user_id': np.random.randint(2000, 3000, n_legit),
    'is_fraud': [0] * n_legit
})

fraud = pd.DataFrame({
    'amount': np.random.normal(200, 50, n_fraud),
    'merchant_id': np.random.randint(1000, 1100, n_fraud),
    'user_id': np.random.randint(2000, 3000, n_fraud),
    'is_fraud': [1] * n_fraud
})

df = pd.concat([legit, fraud]).sample(frac=1).reset_index(drop=True)

# Step 3: Train CTGAN
model = CTGAN(epochs=30)
model.fit(df)

# Step 4: Generate synthetic data
synthetic_data = model.sample(500)
print(synthetic_data.head())
