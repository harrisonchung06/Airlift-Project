# Airlift-Project

## A simple script that graphs all permutations of the preformance curve ![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7BV%7D%7B%5Csqrt%7B2gL%7D%7D) vs ![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7BQg%7D%7BQf%7D) of different configurations of airlift/mammoth pumps based on the Stenning-Martin Model.  

## Use Instructions:
1. Install requirements in requirements.txt 
2. Input ranges of values for K (Loss coefficient), s (Slip Ratio), ![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7BH%7D%7BL%7D) (Submergence Ratio) 
3. Keep the given range of ![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7BQg%7D%7BQf%7D) values 
4. Run the script

## Project Goals: 
* Graph the example data in the Stenning Martin study
* Graph theoretical values based on the Stenning Martin Model approximating the preformance of a custom airlift
* Determine which set of parameters to use for maximum flow. 

## Project Results: 
* Script was able to graph example data well 
* Preformance curves of all combinations of theoretical values plotted 
* The highest preforming curve was obtained by comparing the maximum preformance for each graph against one another 
* Parameters from the highest preforming curve were obtained 

Comparison With Study:
![New Project](https://github.com/user-attachments/assets/ee9569a1-6519-42f5-a875-5f04287c2376)
![New Project(1)](https://github.com/user-attachments/assets/804354ef-c92c-477b-bf56-29a5ef6be756)

Example Graph:

Graph of all permutations:
![Fixed Perm Graph](https://github.com/user-attachments/assets/6c637743-3e64-482f-9477-9f4016b79659)

