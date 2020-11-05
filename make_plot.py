#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:08:33 2020

@author: kento
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Confirm source files
files = os.listdir('source/')

source = []
filename_without_ext = []

# For scatter plot using all source files
fig_all= plt.figure(figsize=(10,6),dpi=400)
ax_all = fig_all.add_subplot(1,1,1)
ax_all.set_xlabel('Temp(℃)')
ax_all.set_ylabel('Heart Flow(mW/mg)')
ax_all.axhline(c='k')    


for current_file in files:
    #Extract file name except extension(.xlsx)
    filename_without_ext.append(os.path.splitext(os.path.basename(current_file))[0])

    # Read source file
    source.append(pd.read_excel('source/' + current_file, header = None))
    
    # Remove unnecessary rows and columns
    df_plot = source[-1].drop(index=range(39),columns=range(5,10))

    # Plot scatter
    fig = plt.figure(figsize=(10,6),dpi=400)
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x=df_plot.iloc[:,1],y=df_plot.iloc[:,4],s=1)
    ax.set_xlabel('Temp(℃)')
    ax.set_ylabel('Heart Flow(mW/mg)')
    ax.axhline(c='k')

    # Save fig
    fig.savefig('fig/' + filename_without_ext[-1] + '.png')
    plt.close(fig)
    
    # Plot scatter using all source files
    ax_all.scatter(x=df_plot.iloc[:,1],y=df_plot.iloc[:,4],s=1,label=filename_without_ext[-1])



# Save fig_all
ax_all.legend(loc='lower right')
fig_all.savefig('fig/fig_all.png')
plt.close(fig_all)