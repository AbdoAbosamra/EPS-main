import pandas as pd
import numpy as np
#from Create_data import IDs
Data= pd.read_csv('D:\EPS\Data\Data3.csv' ,index_col=0 )

CS_Mat = np.array([
    Data['Calculus'][:] > 90,
    Data['DataBase'][:] < 99 ,
    Data['LinerAlgebra'][:] > 99 ,
    Data['IntroToCs'][:] > 99 ,
    Data['IntroToIS'][:] < 99 ,#IS
    Data['DiscreteMath'][:] > 95 ,#CS,IS
    Data['ObjectOriented'][:] > 90 ,#IS,Cs
    Data['Statistics'][:] > 95 , #IS,CS
    Data['IntoToPrograming'][:] > 99 ,#IS,CS
    Data['DifferentialEquations'][:] > 90 ,
    Data['OperationsResearch'][:] > 90 ,#CS
    Data['DataStructure'][:] > 99 ,
    Data['FileProcessing'][:] < 102 ,
    Data['AdvancedMathematics'][:] > 99 ,
    Data['Physics'][:] > 90 ,
    Data['Stochastic'][:] > 90 ,
    Data['Multimedia'][:] < 102 ,# IS
    Data['InformationTheory'][:] < 102 , #IS
    Data['SystemAnalysisAndDesign'][:] < 102 , #IS
    ])
IS_Mat = np.array([
    Data['Calculus'][:] < 99,
    Data['DataBase'][:] > 99 ,
    Data['LinerAlgebra'][:] < 99 ,
    Data['IntroToCs'][:] < 99 ,
    Data['IntroToIS'][:] > 99 ,
    Data['DiscreteMath'][:] > 99 ,
    Data['ObjectOriented'][:] < 99 ,
    Data['Statistics'][:] < 90 ,
    Data['IntoToPrograming'][:] < 99 ,
    Data['DifferentialEquations'][:] < 99 ,
    Data['OperationsResearch'][:] > 102 ,
    Data['DataStructure'][:] < 99 ,
    Data['FileProcessing'][:] > 102 ,
    Data['AdvancedMathematics'][:] < 99 ,
    Data['Physics'][:] < 95 ,
    Data['Stochastic'][:] < 95 ,
    Data['Multimedia'][:] > 102 ,
    Data['InformationTheory'][:] > 102 ,
    Data['SystemAnalysisAndDesign'][:] > 102 ,
])

CS_Pre = sum(CS_Mat.astype(int))
CS_Pre = list(CS_Pre)
CS_Chance = []
for sample in CS_Pre:    
    CS_Chance.append(round(sample / 19 ,2))

c = 0 
for n in range(len(CS_Chance)):
    if round(CS_Chance[n]) >= 0.50:
        c += 1
    
IS_Pre = sum(IS_Mat.astype(int))
IS_Pre = list(IS_Pre)

IS_Chance = []
for sample in IS_Pre:    
    IS_Chance.append(round(sample / 19 ,2))
    
z = 0 
for n in range(len(IS_Chance)):
    if IS_Chance[n] > 0.50:
        z += 1
Data['CS_Chance'] = CS_Chance
Data['IS_Chance'] = IS_Chance

Check_Dep = np.array([
    Data['CS_Chance'][:] >= Data['IS_Chance']
])
Check_Dep= Check_Dep.T
Dep = []
for i in range(len(Check_Dep)):
    if Check_Dep[i]:
        Dep.append('CS')
    else:
        Dep.append('IS')
from collections import Counter
freq = Counter(Dep)
Data['Department'] = Dep

Department = []
for i in range(len(CS_Pre)):
    if(CS_Pre[i] == max(CS_Pre[i] , IS_Pre[i])):
        Department.append('CS')
    else :
        Department.append('IS')

Data.to_csv('D:\EPS\Data\Data-V1.0.csv') #Export Final version of data.
