#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:50:09 2018

@author: rburcon
"""

from iapws import IAPWS97
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(rc={"figure.figsize": (12, 6)})

T_ini=25 #C
T_final=75 #C
PCI_glp=46128.6 #kJ/kg
PCI_lenha_umid=10041.6 #kJ/kg com 40% de umidade
PCI_lenha_seca=15899.2 #kJ/kg com 12% de umidade
efic_caldeira=0.75 #varia entre 65% a 75%, podedo chegar ate 87%
               
#cp agua (kJ/kg.K)
T_ini=T_ini+273.15 #K
T_final=T_final+273.15 #K
agua_sat_inic=IAPWS97(T=T_ini, x=0) 
agua_sat_final=IAPWS97(T=T_final, x=0)   

#massa inicial de agua em kg
m=2000                   

Q=m*((agua_sat_inic.cp+agua_sat_final.cp)/2)*(T_final-T_ini)
m_gas=(Q/PCI_glp)/efic_caldeira
m_lenha_umid=(Q/PCI_lenha_umid)/efic_caldeira
m_lenha_seca=(Q/PCI_lenha_seca)/efic_caldeira

print("\n\nConsiderando somente o aquecimento da agua")             
print ("\nO calor consumido por hora-->>", round(Q,2), "kJ ou", round(Q*0.239006,2),"kcal" )
print ("\nA massa de combustivel consumida por hora-->>", round(m_gas,2), "kg de GLP")
print ("\nA massa de combustivel consumida por hora-->>", round(m_lenha_umid,2), "kg de lenha 40% umidade")
print ("\nA massa de combustivel consumida por hora-->>", round(m_lenha_seca,2), "kg de lenha 12% umidade\n\n")

efic_caldeira=x=np.linspace(0.65,0.87,100)

m_gas=(Q/PCI_glp)/efic_caldeira
m_lenha_umid=(Q/PCI_lenha_umid)/efic_caldeira
m_lenha_seca=(Q/PCI_lenha_seca)/efic_caldeira

fig, ax = plt.subplots()
ax.plot(efic_caldeira, m_gas, color="blue", label="m_gas")
ax.plot(efic_caldeira, m_lenha_umid, color="red", label="m_lenha_umid")
ax.plot(efic_caldeira, m_lenha_seca, color="green", label="m_lenha_seca")
ax.set_title("Consumo de combustível x eficiência da caldeira")
ax.set_xlabel("eficiência da caldeira")
ax.set_ylabel("massa de combustível[kg]")
ax.legend()