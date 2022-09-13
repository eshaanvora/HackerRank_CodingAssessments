#HackerRank Technical Assessment
#Associate Data Scientist

## Import Packages
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import KFold, cross_val_score

### GET TRAINING VARIABLES
## Get X Variables
x_train = train[['feat_0','feat_1', 'feat_2', 'feat3',
                 'feat_4', 'feat5']]

## Get Y Variable
y_train = train['label']

### GET TESTING VARIABLES
## Get X
x_test = test[['feat_0','feat_1', 'feat_2', 'feat3',
                 'feat_4', 'feat5']]

## Do K Fold CV
kf = KF(n_splits = 10)

## Initialize and Fit Model to Dataset
## Tune Hyperparamters
rf = RandomForestClassifier(n_estimators = 100).fit(x_train, y_train)

## Evaluate Model
rf_scores = cross_val_score(rf, x_train, y_train, cv = kf)
print("Average Cross Validation Score: ", np.mean(rf_scores))

## Get Predictions
y_pred = rf.predict(x_test)

## Create a Dataframe with Test Labels
submission_df = pd.Dataframe(y_pred)

## Export to CSV?
submission_df.to_csv('submission.csv')
