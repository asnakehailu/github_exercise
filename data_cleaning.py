# Import necessary libraries
from sklearn.datasets import make_multilabel_classification
import pandas as pd
import matplotlib.pyplot as plt

# Generate 2d classification dataset
X, y = make_multilabel_classification(n_samples=500, n_features=2,
									n_classes=2, n_labels=2,
									allow_unlabeled=True,
									random_state=23)
# create pandas dataframe from generated dataset
df = pd.concat([pd.DataFrame(X, columns=['X1', 'X2']),
				pd.DataFrame(y, columns=['Label1', 'Label2'])],
			axis=1)
display(df.head())

# Plot the generated datasets
plt.scatter(df['X1'], df['X2'], c=df['Label1'])
plt.show()