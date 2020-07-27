#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

#from .models import *

def login(request):
    url='login.html'
    msg=''
    if request.method== 'POST':
        user= request.POST['name']
        pas= request.POST['pass']

        if(user=="admin"):
            if(pas=="pass"):
                url='info.html'
            else:
                url='login.html'
                msg='Error!! Login again'
        else:
            url='login.html'
            msg='Error!! Login again'
    return render(request,url,{'result':msg})

def perinfo(request):
    return render(request,'perinfo.html')
    
def index(request):
    return render(request,'index.html')

def page2(request):

    return render(request,'info.html')


def check(request):
    #check=[]
    #list_of_input_ids=-1
    l=[]
    p=''
    import requests
    if request.method == 'POST':
        #gives list of id of inputs 
        some_var = request.POST.getlist('check')
        print(some_var[:])
        #print(some_var[0])


        
        import os
        import numpy as np 
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import train_test_split
        from sklearn import metrics
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.tree import DecisionTreeClassifier

        df=pd.read_csv('media/Training (1).csv')
        df2=pd.read_csv('media/Testing.csv')
        
        X=df2.iloc[:,:-1].values
        Y=df2['prognosis'].values
        x=df.iloc[:,:-1].values
        y=df['prognosis'].values
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15,random_state=2)
        sc_x=StandardScaler()
        x_train=sc_x.fit_transform(x_train)
        x_test=sc_x.transform(x_test)
        from sklearn.ensemble import RandomForestClassifier
        accuracies={}
        rf = RandomForestClassifier(n_estimators=50,random_state=0)
        rf.fit(x,y)

        acc = rf.score(X,Y)*100
        accuracies['Random Forest'] = acc
        print("Random Forest Algorithm Accuracy Score : {:.2f}%".format(acc))

        import pickle
        pickle.dump(rf,open('minor.pkl','wb'))

        x1=df.iloc[:,:-1]
        symptoms_dict={}
        for index,symptom in enumerate(x1):
            symptoms_dict[symptom]=index
        input_vector=np.zeros(len(symptoms_dict))


        input_vector
        #print(input_vector)
        input_vector=np.zeros(len(symptoms_dict))

        #Arr=[]
        #cnt=0
        #print("fsvsfjhbvskjvbsfkvs")
        #print(input_vector[[symptoms_dict['receiving_blood_transfusion']]]+1)
        #while True:
        #    if (cnt==0):
        #        print("Enter Symptom")
        #        cnt+=1
        #    else:
        #        ("Enter more Symptom or NO to exit")
        #
        #    input_var=input()
            #print(input_var,"asdfghjk")
       #     if(input_var=="No"or input_var=="NO"or input_var=="nO" or input_var=="no"):
       #         break;
       #     else:
        #a=some_var[0]
        #print(a)
        print("testing")
        some_var[:]
        for i in some_var: 
            print(i)
            a=int(i)
            print(a)
            input_vector[[a]]=1

        
        arr=rf.predict_proba([input_vector])
        i=int(np.argmax(arr))
        print(input_vector)
        p=arr[0][i]*100
        print(p)
        l=rf.classes_[i]
        print(l)
    return render(request,'check.html',{'result':l,'prediction':p})
    #return render(request,'upload_OD.html')


    #return render(request,'upload_classify.html',{'result':result,'f5':img_des})





def error_404_view(request, exception):
    return render(request,'404.html')

def index(request):
    try:
        return render(request, 'index.html')
    except:
        return render(request, '404.html')

