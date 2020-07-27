import os
import numpy as np 
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('Training1.csv');

//convert target into integers
def convert_to_int(word):
    
    word_dict={'Fungal infection':1,'Allergy':2,'GERD':3,'Chronic cholestasis':4,'Drug Reaction':5,'Peptic ulcer diseae':6,'AIDS','Diabetes':7,'Gastroenteritis':8,'Bronchial Asthma':9,
                    'Hypertension':10,'Migraine':11,'Cervical spondylosis':12,'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,'hepatitis B':20,
                    'Hepatitis B':21,'Hepatitis C':22,'Hepatitis D':23,'Hepatitis E':24,'Alcoholic hepatitis':25,'Tuberculosis':26,'Common Cold':27,'Pneumonia':28,'Dimorphic hemmorhoids(piles)':29,'Heart attack':30,
                    'Varicose veins':31,'Hypothyroidism':32,'Hyperthyroidism':33,'Hypoglycemia':34,'Osteoarthristis':35,'Arthritis':36,'(vertigo) Paroymsal  Positional Vertigo':37,'Acne':38,'Urinary tract infection':39,
                    'Psoriasis':40,'Impetigo':41}
    return word_dict[word]
X['prognosis']=X['prognosis'].apply(lambda x: convert_to_int(x))


rf = RandomForestClassifier(n_estimators=2000,random_state=0)
rf.fit(x,y)

acc = rf.score(X,Y)*100
accuracies['Random Forest'] = acc
print("Random Forest Algorithm Accuracy Score : {:.2f}%".format(acc))