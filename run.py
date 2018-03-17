
"""Main script for generating output.csv."""

import os
import pandas as pd
fd = pd.read_csv('./baseball.csv');

def avg_OBP_SLG_OPS(R, Id):

##############AVG###############

    myset = set(fd[Id]);
    max=0;
    for i in fd[Id]:
        if (max<=i):
            max=i;
    AVG=[[0 for i in range(len(myset))] for j in range(3)];
    array=[[0 for i in range(max+2)] for j in range(2)];
    for i in range(len(fd[Id])):
       if (fd[Id][i] in myset and fd['PitcherSide'][i]==R): 
           index = int(fd[Id][i]); 
           array[0][index]+=int (fd['AB'][i]);
           array[1][index]+=int (fd['H'][i]);
    count=0;
    for i in myset:
        index=int(i);
        if(float(array[0][index]) != 0 ):
            AVG[0][count] = index;
            AVG[1][count] = float(array[1][index])/float(array[0][index]); 
            count+=1;
        else:
            AVG[0][count]=index;
            AVG[1][count]=0;
            count+=1;
##########OPB######################


   
    OBP=[[0 for i in range(len(myset))] for j in range(3)];
    array=[[0 for i in range(max+1)] for j in range(2)];
    for i in range(len(fd[Id])):
       if (fd[Id][i] in myset and fd['PitcherSide'][i]==R): 
           index = int(fd[Id][i]); 
           array[0][index]+=int (fd['AB'][i])+ int(fd['BB'][i])+ int(fd['SF'][i]);
           array[1][index]+=int (fd['H'][i])+ int(fd['BB'][i]);
    count=0;
    for i in myset:
        index=int(i);
        if(float(array[0][index]) != 0 ):
            OBP[0][count]=index;
            OBP[1][count]=float(array[1][index])/float(array[0][index]);
            count+=1;
        else:
            OBP[0][count]=index;
            OBP[1][count]=0;
            count+=1;

################SLG###################


    SLG=[[0 for i in range(len(myset))] for j in range(3)];
    array=[[0 for i in range(max+1)] for j in range(2)];
    for i in range(len(fd[Id])):
       if (fd[Id][i] in myset and fd['PitcherSide'][i]==R): 
           index = int(fd[Id][i]); 
           array[0][index]+=int (fd['AB'][i])+ int(fd['BB'][i])+ int(fd['SF'][i]);
           array[1][index]+=2*int(fd['2B'][i])+ 3*(int(fd['3B'][i]))+ 4*(int(fd['HR'][i]));
           if(int(fd['2B'][i])==0 and int(fd['3B'][i])==0 and int(fd['HR'][i])==0 and int(fd['H'][i])==1):
               array[1][index]+=1;
    count=0;       
    for i in myset:
        index=int(i);
        if(float(array[0][index]) != 0 ):
            SLG[0][count] = i,
            SLG[1][count] = float(array[1][index])/float(array[0][index]);
            count+=1;
        else:
            SLG[0][count]=index;
            SLG[1][count]=0;
            count+=1;

#############OPS###############
    count=0;
    OPS=[[0 for i in range(len(myset))] for j in range(3)];
    for i in range(len(myset)):
        OPS[0][i] = AVG[0][i],
        OPS[1][i] = SLG[1][i] + OBP[1][i];
        count+=1;

##########write back###########
    if(Id =='HitterId' and R=='R'):
        split = 'RHP';
    elif(Id =='PitcherId' and R=='R'):
        split = 'RHH';
    elif(Id =='HitterId' and R=='L'):
        split = 'LHP';
    elif(Id =='PitcherId' and R=='L'):
        split = 'LHH';
    if(Id =='HitterTeamId' and R=='R'):
        split = 'RHP';
    elif(Id =='PitcherTeamId' and R=='R'):
        split = 'RHH';
    elif(Id =='HitterTeamId' and R=='L'):
        split = 'LHP';
    elif(Id =='PitcherTeamId' and R=='L'):
        split = 'LHH';
    
    if (os.path.isfile('./output.csv')):
        da0 = pd.read_csv('./output.csv');
    da1 = pd.DataFrame({'SubjectId':AVG[0], 'Stat':'AVG',  'Split':split  , 'Subject':Id , 'Value':AVG[1]});
    da2 = pd.DataFrame({'SubjectId':AVG[0], 'Stat':'OBP',  'Split':split  , 'Subject':Id , 'Value':OBP[1]});
    da3 = pd.DataFrame({'SubjectId':AVG[0], 'Stat':'SLG',  'Split':split  , 'Subject':Id , 'Value':SLG[1]});
    da4 = pd.DataFrame({'SubjectId':AVG[0], 'Stat':'OPS',  'Split':split  , 'Subject':Id , 'Value':OPS[1]});
    if (os.path.isfile('./output.csv')):
        da5 = pd.concat([da0,da1,da2,da3,da4]);
    else:
        da5 = pd.concat([da1,da2,da3,da4]);
    da5.to_csv("./output.csv",index=False,sep=',',columns= ['SubjectId', 'Stat', 'Split', 'Subject', 'Value']);

    pass


def main():
    if(os.path.isfile('./output.csv')):
        os.remove('./output.csv');
    avg_OBP_SLG_OPS('R', 'HitterId');
    avg_OBP_SLG_OPS('L', 'HitterId');
    avg_OBP_SLG_OPS('R', 'HitterTeamId');
    avg_OBP_SLG_OPS('L', 'HitterTeamId');
    avg_OBP_SLG_OPS('R', 'PitcherId');
    avg_OBP_SLG_OPS('L', 'PitcherId');
    avg_OBP_SLG_OPS('R', 'PitcherTeamId');
    avg_OBP_SLG_OPS('L', 'PitcherTeamId');
    pass


if __name__ == '__main__':
    main()
