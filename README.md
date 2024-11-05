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

Example Data:
![New Project](https://github.com/user-attachments/assets/5c2d3afb-bdb9-4737-b2a2-a5a8c708eadf)


Example Graph (K=4.0)
![k1](https://github.com/user-attachments/assets/c4c01f21-f7f9-43d5-acef-fc8086082d4c)


Graph of all permutations:
![Conglomerate graph](https://github.com/user-attachments/assets/57d0d3dc-e6cc-4a3e-9c4b-016fd24e8ad5)
