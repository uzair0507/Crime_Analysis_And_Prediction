#............................................prediction................................................#
import os
import time
import joblib
import numpy as np
import pandas as pd

load_predict = joblib.load('BestModel.pkl')

def crime_test(file):
    test =pd.read_csv(file)
    testing_feature_col_names = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','Poverty rate','Literacy rate','gender ratio(Female/1000 Males)','Dacoity (Section 395-398 IPC) - Number of cases registered','Robbery(Section 392-394, 397, 398 IPC) - Number of cases registered',
    'Burglary(Section 449-452, 454, 455, 457-460 IPC) - Number of cases registered',
    'Theft (Section 379-382 IPC) - Number of cases registered',
    'MURDERED ADULT TOTAL (TOTAL)',
    'MURDERED TOTAL (MALE)',
    'MURDERED TOTAL (FEMALE)',
    'MURDERED TOTAL (TOTAL)']
    test_x=test[testing_feature_col_names].values
    label = load_predict.predict(test_x)
    print('label',label)
    new_prob = load_predict.predict_proba(test_x)
    test_confidence = 100*np.max(new_prob)
    acc = "{:.0f}".format(test_confidence)
    accuracy = "{:2f}%".format(test_confidence)
    print("Test_Accuracy:",accuracy)
    cs = 'confidence score:',accuracy
        
    if int(label[0]) == 0:
        out = 'You live in an area with LOW CRIME RATE.'
        print(out)
    else:
        out = 'Your area has a HIGH CRIME RATE'
        print(out)
    return out,cs


