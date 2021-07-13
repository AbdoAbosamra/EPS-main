import pandas as pd
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
Z = np.arange(61, 121)

def Normal_dis():
    x = np.arange(40, 121)
    xU, xL = x + 1, x - 1
    prob = ss.norm.cdf(xU, scale = 60) - ss.norm.cdf(xL, scale = 60)
    prob = prob / prob.sum() # normalize the probabilities so their sum is 1
    nums = np.random.choice(x, size = 1400, p = prob)


    return list(nums)
dict = {
    'ID': range(1,1401),
    'Calculus':Normal_dis(),
    'DataBase':Normal_dis(),
    'LinerAlgebra':Normal_dis(),
    'IntroToCs':Normal_dis(),
    'IntroToIS':Normal_dis(),
    'DiscreteMath':Normal_dis(),
    'ObjectOriented':Normal_dis(),
    'Statistics':Normal_dis(),
    'IntoToPrograming':Normal_dis(),
    'DifferentialEquations':Normal_dis(),
    'OperationsResearch':Normal_dis(),
    'DataStructure':Normal_dis(),
    'FileProcessing':Normal_dis(),
    'AdvancedMathematics':Normal_dis(),
    'Physics':Normal_dis(),
    'Stochastic':Normal_dis(),
    'Multimedia':Normal_dis(),
    'InformationTheory':Normal_dis(),
    'SystemAnalysisAndDesign':Normal_dis(),
}
Data = pd.DataFrame(dict)

Data = Data[Data>60]
Data = Data.dropna(Data)




Data.to_csv('D:\EPS\Data\Data3.csv', index= False)
#Data = pd.read_csv('D:\EPS\Data\Data3.csv' )
#Data1 = Data.drop('ID' , axis= 'columns')




##columns =['Calculus'	,'DataBase'	,'LinerAlgebra'	,'IntroToCs' , 'IntroToIS' , 	'DiscreteMath'	,'ObjectOriented','Statistics'	,'IntoToPrograming'	,'DifferentialEquations',	'OperationsResearch	' , 'DataStructure'	,'FileProcessing'	,'AdvancedMathematics'	,'Physics'	,'Stochastic'	,'Multimedia'	,'InformationTheory'	,'SystemAnalysisAndDesign'] )
(unique, counts) = np.unique(Normal_dis(), return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies[: , 1])


