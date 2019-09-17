# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:19:29 2019

@author: Prashun
"""
import pandas as pd
from sklearn import linear_model
import tkinter as tk
import statsmodels.api as sm
glacier = pd.read_csv('gmbal_glaciers.csv')
df = pd.DataFrame(glacier, columns= ['AccNum','Xtnd','Lon','Lat','Zmin','Zmax','NmnlArea','TermType'])
print(df)
X = df[['Lon','Lat','Zmax','NmnlArea']] # here we have 2 input variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['Zmin'] # output variable (what we are trying to predict)

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
# with statsmodels
X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 

# tkinter GUI
root= tk.Tk() 

canvas1 = tk.Canvas(root, width = 1200, height = 450)
canvas1.pack()

# with sklearn
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)

# with sklearn
Coefficients_result = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)

# with statsmodels
print_model = model.summary()
label_model = tk.Label(root, text=print_model, justify = 'center', relief = 'solid', bg='LightSkyBlue1')
canvas1.create_window(800, 220, window=label_model)



# New_Lon label and input box
label1 = tk.Label(root, text=' Type Lon:')
canvas1.create_window(120, 120, window=label1)

entry1 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry1)

# New_Lat label and input box
label2 = tk.Label(root, text=' Type Lat:')
canvas1.create_window(120, 120, window=label2)

entry2= tk.Entry (root) # create 3rd entry box
canvas1.create_window(270, 120, window=entry2)

# New_I label and input box
label3 = tk.Label(root, text=' Type Zmax:')
canvas1.create_window(120, 120, window=label3)

entry3 = tk.Entry (root) # create 4th entry box
canvas1.create_window(270, 120, window=entry3)

# New_NormalArea label and input box
label4 = tk.Label(root, text=' Type NmnlArea:')
canvas1.create_window(120, 120, window=label4)

entry4 = tk.Entry (root) # create 5th entry box
canvas1.create_window(270, 120, window=entry4)

def values(): 

    global New_Lon 
    New_Lon = float(entry1.get()) 
    
    global New_Lat 
    New_Lat = float(entry2.get()) 
    
    global New_Zmax 
    New_Zmax = float(entry3.get()) 
    
    global New_NmnlArea 
    New_NmnlArea = float(entry4.get()) 

Prediction_result  = ('Predicted Zmin: ',regr.predict([[New_Lon,New_Lat,New_Zmax,New_NmnlArea]]))
label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
canvas1.create_window(260, 280, window=label_Prediction)
button1 = tk.Button (root, text='Predict Zmin',command=values(), bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)

root.mainloop()

