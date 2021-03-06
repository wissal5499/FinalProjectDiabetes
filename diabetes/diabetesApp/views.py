from django.shortcuts import render
from django.template import context
from django.template.context import ContextDict
import pandas as pd
from matplotlib import pyplot as plt
plt.switch_backend('AGG')
import seaborn as sns
from io import StringIO
import sqlite3
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from django.http.response import JsonResponse

#  pie chart shows Percentage of diabetics relative to genetic         
def genetic():  
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1", con)
        # 0== none 1==mom 2==dad both==3
        none=df['parents'].value_counts()['0']        
        mom=df['parents'].value_counts()['1']
        dad=df['parents'].value_counts()['2']
        both=df['parents'].value_counts()['3']
        data = [none,mom,dad,both]
        labels = ['none','mom','dad', 'both']
        colors = ['#99CC33','#00CC66','#99FF66','#00FF00']
        plt.figure(0)
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%',  textprops={'fontsize': 14})
        plt.title("Pie chart genetic",fontsize=16)
        plt.legend(labels=["none","mom","dad","both"])
        imgdata = StringIO()
        plt.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data

#  pie chart shows Percentage of diabetics relative to gender         
def gender():  
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1", con)   
        # 0== male 1==female 
        maleNum=df['gender'].value_counts()['0']
        femaleNum=df['gender'].value_counts()['1']
        data = [maleNum, femaleNum]
        labels = ['Male', 'Female']
        colors = ['#009999','#00FFCC']
        plt.figure(1)               
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%', textprops={'fontsize': 14})
        plt.title("Pie chart Gender",fontsize=16)
        plt.legend(labels=["Male","Female"])
        imgdata = StringIO()
        plt.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data

#  pie chart shows Percentage of diabetics relative to areas         
def area():
        con2 = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1", con2) 
        north=df['area'].value_counts()['north']
        south=df['area'].value_counts()['south']
        center=df['area'].value_counts()['center']
        data = [north, south, center]
        labels = ['North', 'South','Center']
        colors = ['#CC6666','#CC9999','#CCCCCC']
        plt.figure(2)               
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%', textprops={'fontsize': 14})
        plt.title("Pie chart Area",fontsize=16)
        plt.legend(labels=["north","south","center"])
        imgdata = StringIO()
        plt.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data  

#  pie chart shows Percentage of diabetics relative to age         
def age():
        con2 = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1", con2) 
        count1=0
        count2=0
        count3=0
        for ind in df['age']:
                if(ind>19 and ind<41):
                        count1=count1+1
                elif(ind>40 and ind<61):
                        count2=count2+1
                else:
                        count3=count3+1 

        data = [count1, count2, count3]
        labels = ["20 to 40", "41 to 60", "60 up"]
        colors = ['#FFCC33','#FF9966','#FFCC99']
        plt.figure(3)               
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%', textprops={'fontsize': 14})
        plt.title("Pie chart Age",fontsize=16)
        plt.legend(labels=["20 to 40", "41 to 60", "60 up"])
        imgdata = StringIO()
        plt.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data     

#  pie chart shows Percentage of diabetics relative to BMI         
def BMI():
        plt.style.use('ggplot')
        con2 = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='0'", con2)
        dfemale = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='1'", con2)
        count0=0
        count1=0
        count2=0
        count3=0
        count3_2=0
        count4=0
        count5=0
        count6=0
        count7=0
        count8=0
        for x in df['BMI']:
                
                if(18.5 <= x < 25):
                        count4=count4+1
                elif(25 <= x < 30):
                        count5=count5+1
                elif(30 <= x < 35):
                        count6=count6+1
                elif(35 <= x <= 40):
                        count7=count7+1
                else:
                        count8=count8+1

        for y in dfemale['BMI']:
                
                if(18.5 <= y < 25):
                        count0=count0+1
                elif(25 <= y < 30):
                        count1=count1+1
                elif(30 <= y < 35):
                        count2=count2+1
                elif(35 <= y <= 40):
                        count3=count3+1
                else:
                        count3_2=count3_2+1
        fig, ax = plt.subplots(figsize=(8,4))
        x = ["18.5 - 25","25 - 30","30 - 35","35 - 40","> 40"]
        desc = ["Normal","Overweight","Obese Class I","Obese Class II","Obese Class III"]
        xlabels = [f"{x1}\n{x2}" for x1 ,x2 in zip(x,desc)]
        numDiabeticM=( count4+ count5 +count6 +count7+ count8)
        numDiabeticF=( count0+ count1 +count2 +count3+ count3_2)

        count4= (count4/numDiabeticM)*100
        count5= (count5/numDiabeticM)*100
        count6= (count6/numDiabeticM)*100
        count7= (count7/numDiabeticM)*100
        count8= (count8/numDiabeticM)*100

        count0= (count0/numDiabeticF)*100
        count1= (count1/numDiabeticF)*100
        count2= (count2/numDiabeticF)*100
        count3= (count3/numDiabeticF)*100
        count3_2= (count3_2/numDiabeticF)*100

        amountM = [count4,count5,count6,count7,count8]
        amountF = [count0,count1,count2,count3,count3_2]
        index = np.arange(5)
        bar_width = 0.35
        opacity = 0.9
        bar1=ax.bar(index, amountM, bar_width, alpha=opacity, color='green', label='Male')
        bar2=ax.bar(index+bar_width, amountF, bar_width, alpha=opacity, color='pink',label='Female')
        ax.bar_label(bar1, fmt='%.2f')
        ax.bar_label(bar2, fmt='%.2f')
        ax.set_title("bar chart BMI",fontsize=16)
        ax.set_ylabel('Percentage of diabetic (%)',fontsize=14)
        ax.set_xlabel('BMI',fontsize=14)
        ax.set_xticks(index + bar_width / 2)
        ax.set(xticklabels=xlabels)
        ax.legend(loc='center left', bbox_to_anchor=(0.95, 1))
        imgdata = StringIO()
        plt.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data 

#  pie chart shows Percentage of diabetics relative to smoking         
def smoking():
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='0'", con2)
         dfemale = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='1'", con2)
         count1=0
         count2=0
         count3=0
         count4=0
         count5=0
         count6=0
         count7=0
         count8=0
         count9=0
         count10=0
         # 0==never 1==little 2==middle 3==much
         for ob in df['smoking']:
                if(ob=='0'):
                        count1=count1+1
                elif(ob=='1'):
                        count2=count2+1
                elif(ob=='2'):
                        count3=count3+1
                elif(ob=='3'):
                        count4=count4+1
                else:
                        count5=count5+1

         for o in dfemale['smoking']:
                if(o=='0'):
                        count6=count6+1
                elif(o=='1'):
                        count7=count7+1
                elif(o=='2'):
                        count8=count8+1
                elif(o=='3'):
                        count9=count9+1
                else:
                        count10=count10+1
         fig, ax = plt.subplots(figsize=(8,4))
         #plt.figure(11)
         numDiabeticM=( count1+ count2 +count3 +count4+ count5)
         numDiabeticF=( count10 +count6 +count7+count8 +count9)
         count1= (count1/numDiabeticM)*100
         count2= (count2/numDiabeticM)*100
         count3= (count3/numDiabeticM)*100
         count4= (count4/numDiabeticM)*100
         count5= (count5/numDiabeticM)*100
         count6= (count6/numDiabeticF)*100
         count7= (count7/numDiabeticF)*100
         count8= (count8/numDiabeticF)*100
         count9= (count9/numDiabeticF)*100
         count10= (count10/numDiabeticF)*100
         numsM = [count5,count1,count2,count3,count4]
         numsF = [count10,count6,count7,count9,count10]

         index = np.arange(5)
         bar_width = 0.35
         opacity = 0.9
         bar1=ax.bar(index, numsM, bar_width, alpha=opacity, color='green', label='Male')
         bar2=ax.bar(index+bar_width, numsF, bar_width, alpha=opacity, color='pink',label='Female')
         ax.bar_label(bar1, fmt='%.2f')
         ax.bar_label(bar2, fmt='%.2f')
         ax.set_title("The cause of smoking",fontsize=16)
         ax.set_ylabel('Percentage of diabetic (%)',fontsize=14)
         ax.set_xlabel('smoking',fontsize=12)
         ax.set_xticks(index + bar_width / 2)
         ax.set_xticklabels(("in the past","never", "little","average","profusely"))
         ax.legend(loc='center left', bbox_to_anchor=(0.95, 1))
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data

#  pie chart shows Percentage of diabetics relative to genetic         
def parents():
         plt.style.use('ggplot')
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='0'", con2)
         dfemale = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='1'", con2)
         count1=0
         count2=0
         count3=0
         count4=0
        # 0==none 1==mom 2==dad
         for ob in df['parents']:
                if(ob=='0'):
                        count1=count1+1
                elif(ob=='1'):
                        count2=count2+1
                elif(ob=='2'):
                        count3=count3+1
                else:
                        count4=count4+1
         count5=0
         count6=0
         count7=0
         count8=0
         for ob in dfemale['parents']:
                if(ob=='0'):
                        count5=count5+1
                elif(ob=='1'):
                        count6=count6+1
                elif(ob=='2'):
                        count7=count7+1
                else:
                        count8=count8+1
         fig, ax = plt.subplots(figsize=(8,4))
         #plt.figure(8)
         langs = ["none", "dad", "mom","both"]
         numDiabeticMale=( count1+ count2 +count3 +count4)
         numDiabeticFemale=( count5+ count6 +count7 +count8)

         count1= (count1/numDiabeticMale)*100
         count2= (count2/numDiabeticMale)*100
         count3= (count3/numDiabeticMale)*100
         count4= (count4/numDiabeticMale)*100
         count5= (count5/numDiabeticFemale)*100
         count6= (count6/numDiabeticFemale)*100
         count7= (count7/numDiabeticFemale)*100
         count8= (count8/numDiabeticFemale)*100

         numsMale = [count1,count2,count3,count4]
         numsFemale = [count5,count6,count7,count8]
         index = np.arange(4)
         bar_width = 0.35
         opacity = 0.9
         bar1=ax.bar(index, numsMale, bar_width, alpha=opacity, color='green', label='Male')
         bar2=ax.bar(index+bar_width, numsFemale, bar_width, alpha=opacity, color='pink',label='Female')
         ax.bar_label(bar1, fmt='%.2f')
         ax.bar_label(bar2, fmt='%.2f')
         ax.set_title("The cause of genetic",fontsize=16)
         ax.set_ylabel('Percentage of diabetic (%)',fontsize=14)
         ax.set_xlabel('inherit from',fontsize=12)
         ax.set_xticks(index + bar_width / 2)
         ax.set_xticklabels(("none", "dad", "mom","both"))
         ax.legend(loc='center left', bbox_to_anchor=(0.95, 1))
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data

#  pie chart shows Percentage of diabetics relative to sweet         
def sweet():
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='0'", con2)
         dfemale = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='1'", con2)
         count1=0
         count2=0
         count3=0
         count4=0
         count5=0
         count6=0
         count7=0
         count8=0
        # 0==never 1==little 2==middle
         for ob in df['sweet']:
                if(ob=='0'):
                        count1=count1+1
                elif(ob=='1'):
                        count2=count2+1
                elif(ob=='2'):
                        count3=count3+1
                else:
                        count4=count4+1
         for ob in dfemale['sweet']:
                if(ob=='0'):
                        count5=count5+1
                elif(ob=='1'):
                        count6=count6+1
                elif(ob=='2'):
                        count7=count7+1
                else:
                        count8=count8+1
         fig, ax = plt.subplots(figsize=(8,4))
         #plt.figure(10)
         numDiabeticMale=( count1+ count2 +count3 +count4)
         numDiabeticFemale=( count5+ count6 +count7 +count8)

         count1= (count1/numDiabeticMale)*100
         count2= (count2/numDiabeticMale)*100
         count3= (count3/numDiabeticMale)*100
         count4= (count4/numDiabeticMale)*100
         count5= (count5/numDiabeticFemale)*100
         count6= (count6/numDiabeticFemale)*100
         count7= (count7/numDiabeticFemale)*100
         count8= (count8/numDiabeticFemale)*100

         numsMale = [count1,count2,count3,count4]
         numsFemale = [count5,count6,count7,count8]
         index = np.arange(4)
         bar_width = 0.35
         opacity = 0.9
         bar1=ax.bar(index, numsMale, bar_width, alpha=opacity, color='green', label='Male')
         bar2=ax.bar(index+bar_width, numsFemale, bar_width, alpha=opacity, color='pink',label='Female')
         ax.bar_label(bar1, fmt='%.2f')
         ax.bar_label(bar2, fmt='%.2f')
         ax.set_title("The cause of sweets",fontsize=16)
         ax.set_ylabel('Percentage of diabetic (%)',fontsize=14)
         ax.set_xlabel('eating sweet',fontsize=12)
         ax.set_xticks(index + bar_width / 2)
         ax.set_xticklabels(("never", "little","average","profusely"))
         ax.legend(loc='center left', bbox_to_anchor=(0.95, 1))
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data

#  pie chart shows Percentage of diabetics relative to fast food         
def ageGraph():
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='0'", con2)
         dfemale = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='1'", con2)
         count1=0
         count2=0
         count3=0
         count4=0
         count5=0
         count6=0

         for ind in df['age']:
                if(ind>19 and ind<41):
                        count1=count1+1
                elif(ind>40 and ind<61):
                        count2=count2+1
                else:
                        count3=count3+1 
         for ind in dfemale['age']:
                if(ind>19 and ind<41):
                        count4=count4+1
                elif(ind>40 and ind<61):
                        count5=count5+1
                else:
                        count6=count6+1 

         fig, ax = plt.subplots(figsize=(8,4))
         numDiabeticMale=(count1+ count2+count3 )
         numDiabeticFemale=(count4 +count5+count6)

         count1= (count1/numDiabeticMale)*100
         count2= (count2/numDiabeticMale)*100
         count3= (count3/numDiabeticMale)*100
         count4= (count4/numDiabeticFemale)*100
         count5= (count5/numDiabeticFemale)*100
         count6= (count6/numDiabeticFemale)*100
         numsMale = [count1,count2,count3]
         numsFemale = [count4,count5,count6]
         index = np.arange(3)
         bar_width = 0.35
         opacity = 0.9
         bar1=ax.bar(index, numsMale, bar_width, alpha=opacity, color='green', label='Male')
         bar2=ax.bar(index+bar_width, numsFemale, bar_width, alpha=opacity, color='pink',label='Female')
         ax.bar_label(bar1, fmt='%.2f')
         ax.bar_label(bar2, fmt='%.2f')
         ax.set_title("Age",fontsize=16)
         ax.set_ylabel('Percentage of diabetic (%)',fontsize=14)
         ax.set_xlabel('age',fontsize=12)
         ax.set_xticks(index + bar_width / 2)
         ax.set_xticklabels(("20 to 40", "41 to 60", "60 up"))
         ax.legend(loc='center left', bbox_to_anchor=(0.95, 1))
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data

#  pie chart shows Percentage of diabetics relative to sport         
def sport():
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='0'", con2)
         dfemale = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1 and gender='1'", con2)
         count1=0
         count2=0
         count3=0
         count4=0
         count5=0
         count6=0
         count7=0
         count8=0
        # 0==never 1==little 2==middle 
         for ob in df['sport']:
                if(ob=='0'):
                        count1=count1+1
                elif(ob=='1'):
                        count2=count2+1
                elif(ob=='2'):
                        count3=count3+1
                else:
                        count4=count4+1

         for ob in dfemale['sport']:
                if(ob=='0'):
                        count5=count5+1
                elif(ob=='1'):
                        count6=count6+1
                elif(ob=='2'):
                        count7=count7+1
                else:
                        count8=count8+1
         fig, ax = plt.subplots(figsize=(8,4))

         numDiabeticMale=(count1+ count2 +count3 +count4)
         numDiabeticFemale=( count5+ count6 +count7 +count8)

         count1= (count1/numDiabeticMale)*100
         count2= (count2/numDiabeticMale)*100
         count3= (count3/numDiabeticMale)*100
         count4= (count4/numDiabeticMale)*100
         count5= (count5/numDiabeticFemale)*100
         count6= (count6/numDiabeticFemale)*100
         count7= (count7/numDiabeticFemale)*100
         count8= (count8/numDiabeticFemale)*100
         numsMale = [count1,count2,count3,count4]
         numsFemale = [count5,count6,count7,count8]

         index = np.arange(4)
         bar_width = 0.35
         opacity = 0.9
         bar1=ax.bar(index, numsMale, bar_width, alpha=opacity, color='green', label='Male')
         bar2=ax.bar(index+bar_width, numsFemale, bar_width, alpha=opacity, color='pink',label='Female')
         ax.bar_label(bar1, fmt='%.2f')
         ax.bar_label(bar2, fmt='%.2f')
         ax.set_title("The cause of sport",fontsize=16)
         ax.set_ylabel('Percentage of diabetic (%)',fontsize=14)
         ax.set_xlabel('doing sport',fontsize=12)
         ax.set_xticks(index + bar_width / 2)
         ax.set_xticklabels(("never", "little","average","profusely"))
         ax.legend(loc='center left', bbox_to_anchor=(0.95, 1))
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data


#  pie chart shows Percentage of diabetics relative to hypertension         
def hypertension():
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1", con2)
         count1=0
         count2=0
        # 0==no 1==yes
         for ob in df['hypertension']:
                if(ob=='1'):
                        count1=count1+1
                else:
                        count2=count2+1
         numDiabetic=(count1+ count2)
         count1= (count1/numDiabetic)*100
         count2= (count2/numDiabetic)*100
         fig, ax = plt.subplots()
         #plt.figure(4)
         langs = ["YES", "NO"]
         nums = [count1,count2]
         bar=ax.bar(langs,nums,color='brown')
         ax.bar_label(bar, fmt='%.2f')
         ax.set_title("bar chart hypertension",fontsize=16)
         ax.set_ylabel('Percentage of diabetic (%)',fontsize=16)
         ax.set_xlabel('suffering from Hypertension',fontsize=14)
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data

#  pie chart shows Percentage of diabetics relative to delayed healing wounds         
def delayed_healing_wounds():
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic=1", con2)
         count1=0
         count2=0
        # 0==no 1==yes
         for ob in df['delayed_healing_wounds']:
                if(ob=='1'):
                        count1=count1+1
                else:
                        count2=count2+1
         numDiabetic=(count1+ count2)
         count1= (count1/numDiabetic)*100
         count2= (count2/numDiabetic)*100
         fig, ax = plt.subplots()
         #plt.figure(5)
         langs = ["YES", "NO"]
         nums = [count1,count2]
         bar=ax.bar(langs,nums,color='grey')
         ax.bar_label(bar, fmt='%.2f')
         ax.set_title("bar chart delayed healing wounds",fontsize=16)
         ax.set_ylabel('Percentage of diabetic (%)',fontsize=16)
         ax.set_xlabel('delayed healing wounds',fontsize=14)
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data

# predict the result (diabetic or not) AND adding user data to database table (diabetesApp_survey)
import sqlite3 
def result(request):
    if request.POST.get('action') == 'post':
        con = sqlite3.connect("db.sqlite3")
        data = pd.read_sql_query("SELECT * from diabetesApp_survey ", con)
        # Receive data from client
        gender= str(request.POST.get('gender'))
        area= str(request.POST.get('area'))        
        age= float(request.POST.get('age'))
        genetic= str(request.POST.get('genetic'))
        Siblings= str(request.POST.get('Siblings'))
        fast_food= str(request.POST.get('fast_food'))
        sweet= str(request.POST.get('sweet'))
        Hypertension= str(request.POST.get('Hypertension'))
        stress= str(request.POST.get('stress'))
        wounds= str(request.POST.get('wounds'))
        bruises= str(request.POST.get('bruises'))
        thirst= str(request.POST.get('thirst'))
        urination= str(request.POST.get('urination'))
        tired= str(request.POST.get('tired'))
        vision= str(request.POST.get('vision'))
        numbness= str(request.POST.get('numbness'))
        smoking= str(request.POST.get('smoking'))
        Sport= str(request.POST.get('Sport'))
        bmi=float(request.POST.get('bmi'))
        
        rf = RandomForestClassifier(n_estimators = 1000, random_state = 1)
        x = data.iloc[:, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
        y = data['diabetic']
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=0)
        # Make prediction
        rf.fit(x_train, y_train)

        result = rf.predict([[gender,age,genetic,Siblings,fast_food,sweet,Hypertension,stress,wounds,bruises,thirst,urination,tired,vision,numbness,smoking,Sport,bmi]])
        accuracy=""
        acc = rf.score(x_test,y_test)*100
        acc = "{:.2f}".format(acc)
        if result[0]=='1':
                classification = "positive"
                cursor  =  con.cursor ()
                query="INSERT INTO diabetesApp_survey(diabetic,gender, age,parents,siblings,fast_food_in_night,sweet,hypertension,stress,delayed_healing_wounds,delayed_bruise_recovery,thirst,urination,tired,blurred_vision,numbness,smoking,sport,BMI,area) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                data=("1",gender,age,genetic,Siblings,fast_food,sweet,Hypertension,stress,wounds,bruises,thirst,urination,tired,vision,numbness,smoking,Sport,bmi,area)
                cursor.execute(query,data)
                con.commit ()
                test2=""
                if (cursor.execute(query,data)):
                        test2="Data entered successfully"
                else:
                        test2="Data not entered"

                cursor.close()
        else:
                classification="negative"
                cursor  =  con.cursor ()
                query="INSERT INTO diabetesApp_survey(diabetic,gender,age,parents,siblings,fast_food_in_night,sweet,hypertension,stress,delayed_healing_wounds,delayed_bruise_recovery,thirst,urination,tired,blurred_vision,numbness,smoking,sport,BMI,area) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                data=("0",gender,age,genetic,Siblings,fast_food,sweet,Hypertension,stress,wounds,bruises,thirst,urination,tired,vision,numbness,smoking,Sport,bmi,area)
                cursor.execute(query,data)
                con.commit ()
                test2=""
                if (cursor.execute(query,data)):
                        test2="Data entered successfully"
                else:
                        test2="Data not entered"

                cursor.close()
        accuracy=acc
        return JsonResponse({'result': classification,'accuracy':accuracy},safe=False)


# bar chart showing the percentage of diabetic in arab society relative to factors
import imageio
def causes():
         con2 = sqlite3.connect("db.sqlite3")
         df = pd.read_sql_query("SELECT * from diabetesApp_survey where diabetic='1'", con2)
         parents=0
         sweet=0
         hypertension=0
         smoking=0
         sport=0
         weight=0
         age=0
         height = 0.9

        # 1==dad 2==mom 3==both
         for ob in df['parents']:
                 if(ob=='1' or ob=='2' or ob=='3' ):
                         parents=parents+1
        # 1==little 2==much 3==middle
         for ob in df['sweet']:  
                 if(ob=='3' or ob=='2' or ob=='1'):
                         sweet=sweet+1
        # 1=YES
         for ob in df['hypertension']:  
                 if(ob=='1'):
                         hypertension=hypertension+1 
        # 1==little 2==middle 3==much 4==in the past                      
         for ob in df['smoking']:  
                 if(ob=='1'or ob=='2' or ob=='3' or ob=='4'):
                         smoking=smoking+1
        # 0==never 	
         for ob in df['sport']:  
                 if(ob=='0'):
                         sport=sport+1
         for ob in df['age']:  
                 if(ob>39):
                         age=age+1                         
         for ob in df['BMI']:  
                 if(ob>24):
                         weight=weight+1 

         numofdiabetic=df['diabetic'].value_counts()['1']        
         parents=(parents/numofdiabetic)*100
         sweet=(sweet/numofdiabetic)*100
         hypertension=(hypertension/numofdiabetic)*100
         smoking=(smoking/numofdiabetic)*100
         sport=(sport/numofdiabetic)*100
         weight=(weight/numofdiabetic)*100
         age=(age/numofdiabetic)*100

         data = [age,weight,smoking,parents,sweet,hypertension,sport]
         age_img = imageio.imread('static/diabetes/images/age.png').swapaxes(0, 1)
         obisety_img = imageio.imread('static/diabetes/images/ob_img.jpg').swapaxes(0, 1)
         genetic_img = imageio.imread('static/diabetes/images/genetic.jpg').swapaxes(0, 1)
         smoking_img = imageio.imread('static/diabetes/images/smoke_img.jpg').swapaxes(0, 1)
         sport_img = imageio.imread('static/diabetes/images/sport_img.jpg').swapaxes(0, 1)
         sweet_img = imageio.imread('static/diabetes/images/sweet_img.png').swapaxes(0, 1)
         hypertension_img = imageio.imread('static/diabetes/images/hyper.png').swapaxes(0, 1)

         pic = [age_img,obisety_img, smoking_img, genetic_img,sweet_img, hypertension_img,sport_img]
         fig, ax = plt.subplots(figsize=(8,4))
         for i, (height, img) in enumerate(zip(data, pic)):
                 AR = 3
                 width = 36
                 left = width*i + 0.7*i
                 right = left + width
                 ax.imshow(img, extent=[left, right, 0, height])
                 ax.set_title("Percentage of diabetic (%) in Arab society",fontsize=17)
                 ax.set_ylabel('Percentage of diabetic (%)',fontsize=13)
                 ax.set_xlabel('factors',fontsize=13)
                 #figsize=(6,3)
         plt.xlim(0, right)
         plt.ylim(0, max(data)*1.2)
         plt.xticks(np.arange(0), (""))
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data


from sklearn.preprocessing import MinMaxScaler
def fac2():
         con2 = sqlite3.connect("db.sqlite3")
         data = pd.read_sql_query("SELECT * from diabetesApp_survey", con2)
         label = data["diabetic"]
         data.drop(['diabetic'], axis = 1,inplace=True)
         data.drop(['id'], axis = 1,inplace=True)
         data.drop(['area'], axis = 1,inplace=True)

         categorical_features = ["gender", "parents", "siblings","fast_food_in_night","sweet", "hypertension",
          "stress", "delayed_healing_wounds", "delayed_bruise_recovery", "thirst","urination",  "tired",
          "blurred_vision", "numbness", "smoking",  "sport"]

         data[categorical_features] = data[categorical_features].astype("category")

         continuous_features = set(data.columns) - set(categorical_features)
         scaler = MinMaxScaler()
         df_norm = data.copy()
         df_norm[list(continuous_features)] = scaler.fit_transform(data[list(continuous_features)])

         clf = RandomForestClassifier()
         clf.fit(df_norm, label)
         # create a figure to plot a bar, where x axis is features, and Y indicating the importance of each feature
         plt.figure(figsize=(8,4))
         feat_importances = pd.Series(clf.feature_importances_, index=df_norm.columns)
         feat_importances.nlargest(6).plot(kind='bar')
         plt.xticks(rotation='horizontal')
         plt.title('The most influential factors in diabetes',fontsize=17)
         plt.xlabel('factors',fontsize=13)
         plt.ylabel('the importance of a feature (scores)',fontsize=13)
         imgdata = StringIO()
         plt.savefig(imgdata, format='svg')
         imgdata.seek(0)
         data = imgdata.getvalue()
         return data

# sending charts to html pages 
def tr(request):
        db0=genetic()
        db2=area()
        db3=gender()
        db=age()
        db4=BMI()
        db5=parents()
        db6=hypertension()
        db8=smoking()
        db9=sport()
        db10=delayed_healing_wounds()
        db12=causes()
        db13=sweet()
        db14=ageGraph()
        db15=fac2()

        return render(request,'homepage.html',{'db0':db0,'db2':db2,'db3':db3,'db':db,'db4':db4,'db5':db5,'db6':db6,'db8':db8,'db9':db9,'db10':db10,'db12':db12,'db13':db13,'db14':db14,'db15':db15})
