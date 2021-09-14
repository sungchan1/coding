from matplotlib.gridspec import GridSpec
import numpy as np; import matplotlib.pyplot as plt; from matplotlib.widgets import Cursor; from tkinter.constants import END
import pandas as pd; import openpyxl; from openpyxl import load_workbook; from openpyxl import Workbook
import os; from tkinter import filedialog; from tkinter import messagebox; import pyautogui; import math; import functools
from matplotlib import font_manager, rc; import matplotlib; from matplotlib.widgets import CheckButtons

list_file = []                                                                                      # 파일 목록 담을 리스트 생성
files = filedialog.askopenfilenames(initialdir="/",\
                 title = "파일을 선택 해 주세요",\
                    filetypes = (("*.csv","*csv"),("*.xls","*xls"),("*.xlsx","*xlsx")))             # files 변수에 선택 파일 경로 넣기

                                                            # 파일 리스트의 길이

result    = pd.DataFrame()

# -------------------------------------------------------------------------- #
### 변수명 지정
# File Open
for file in files :
    df = pd.read_csv(file)


    # Time
    for column in df:
        dfc = list(df)
        a= 'Rel. Time (s)'
        b= ''

        if a in dfc :
            time = df[a]

        elif b in dfc :
            time = df[b]
        else :
            time = []

     # sequence
    for column in df:
        dfc = list(df)
        a= 'sequence'
        b= ''

        if a in dfc :
            sequence = df[a]

        elif b in dfc :
            sequence = df[b]
        else :
            sequence = []

    # Acc - x
    for column in df:
        dfc = list(df)
        a= 'Acc-x'
        b= ''
        c= ''
        d= ''

        if a in dfc :
            accx = df[a]

        elif b in dfc :
            accx = df[b]

        elif c in dfc :
            accx = df[c]
        elif d in dfc :
            accx = df[d]
        else :
            accx = []


    #  Acc - y
    for column in df:
        dfc = list(df)
        a= 'Acc-y'
        b= ''

        if a in dfc :
            accy = df[a]

        elif b in dfc :
            accy = df[b]
        else :
            accy = []

    #  Acc - z
    for column in df:
        dfc = list(df)
        a= 'Acc-z'
        b= ''

        if a in dfc :
            accz = df[a]

        elif b in dfc :
            accz= df[b]
        else :
            accz= []

    # Gyro-x
    for column in df:
        dfc = list(df)
        a= 'Gyro-x'
        b= ''

        if a in dfc :
            gyrox  = df[a]

        elif b in dfc :
            gyrox  = df[b]
        else :
            gyrox = []

    # Gyro-y
    for column in df:
        dfc = list(df)
        a= 'Gyro-y'
        b = ''
        d = ''
        c = ''

        if a in dfc :
            gyroy = df[a]
        elif b in dfc :
            gyroy = df[b]
        elif c in dfc :
            gyroy = df[c]
        elif d in dfc :
            gyroy = df[d]

        else :
            gyroy= [5 for i in range(10000)]


    # Gyro-z
    for column in df:
        dfc = list(df)
        a= 'Gyro-z'
        b=  ''
        c = ''
        d = ''

        if a in dfc :
            gyroz = df[a]
        elif b in dfc :
            gyroz = df[b]
        elif c in dfc :
            gyroz = df[c]
        elif d in dfc :
            gyroz = df[d]
        else :
            gyroz = [5 for i in range(10000)]

    # Meg-x
    for column in df:
        dfc = list(df)
        a= 'Meg-x'
        b= ''

        if a in dfc :
            megx = df[a]

        elif b in dfc :
            megx = df[b]
        else :
            megx = [0 for i in range(10000)]

    # Meg-y
    for column in df:
        dfc = list(df)
        a= 'Meg-y'
        b= ''

        if a in dfc :
            megy = df[a]

        elif b in dfc :
            megy = df[b]
        else :
            megy = [0 for i in range(10000)]

    # Meg-z
    for column in df:
        dfc = list(df)
        a= 'Meg-z'
        b= ''

        if a in dfc :
            megz = df[a]

        elif b in dfc :
            megz = df[b]
        else :
            megz = [0 for i in range(10000)]

# -------------------------------------------------------------------------- #



### Angle 범위 지정

fig = plt.figure()
ax = fig.subplots()
ax.plot(time,sequence, color = 'k')


cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                color = "#13EAC9", linewidth = 1)


plt.title('Choose Range', fontweight ="bold", color = "#13EAC9")
plt.xticks(fontsize = 8); plt.yticks(fontsize = 8)
plt.ylabel('Sequence', fontweight='bold', fontsize = 10, color = 'k')
plt.xlabel('Time [s]', fontweight='bold', fontsize = 10, color = 'k')


[x1, x2] = plt.ginput(2)
plt.close()

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

array = time
value = x1[0]
t1 = find_nearest(array, value)
value = x2[0]
t2 = find_nearest(array, value)


index1 = np.where(time == t1); index2 = np.where(time == t2)

t  =   time[int(index1[0]):int(index2[0])]
ax  =   accx[int(index1[0]):int(index2[0])]
ay =   accy[int(index1[0]):int(index2[0])]
az  =   accz[int(index1[0]):int(index2[0])]
gx  =  gyrox[int(index1[0]):int(index2[0])]
gy  =  gyroy[int(index1[0]):int(index2[0])]
gz  =  gyroz[int(index1[0]):int(index2[0])]
mx =   megx[int(index1[0]):int(index2[0])]
my =   megy[int(index1[0]):int(index2[0])]
mz =   megz[int(index1[0]):int(index2[0])]

# -------------------------------------------------------------------------- #


### 그래프 표출

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
matplotlib.rcParams['axes.unicode_minus'] = False



plt.figure(1)
p_ax, = plt.plot(t,ax, color = 'r', linewidth=0.3, label='Acc-x')
p_ay, = plt.plot(t,ay, color = 'g', linewidth=0.3, label='Acc-y')
p_az, = plt.plot(t,az, color = 'b', linewidth=0.3, label='Acc-z')
plt.legend(('Acc-x','Acc-y','Acc-z'), loc = 8, ncol=3, prop={'size': 10})
plt.xlabel('time [s]', fontweight='bold', fontsize = 10, color = 'k')
plt.ylabel('진동강도 [g]', fontweight='bold', fontsize = 10, color = 'k')
plt.title('진동감지 결과(가속센서)', fontweight='bold', fontsize = 14, color = 'k')
plt.gca().set_facecolor('#FFFFFF')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.grid(axis = 'y')
plt.xticks(fontsize = 8); plt.yticks(fontsize = 8)


lines = [p_ax, p_ay, p_az]
rax = plt.axes([0.8, 0.13, 0.08, 0.12])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)

def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()

check.on_clicked(func)
plt.show()



plt.figure(2)
p_gx, = plt.plot(t,gx, color = 'r', linewidth=0.3, label='Gyro-x')
p_gy, = plt.plot(t,gy, color = 'g', linewidth=0.3, label='Gyro-y')
p_gz, = plt.plot(t,gz, color = 'b', linewidth=0.3, label='Gyro-z')
plt.legend(('Gyro-x','Gyro-y','Gyro-z'), loc = 8, ncol=3, prop={'size': 10})
plt.xlabel('time [s]', fontweight='bold', fontsize = 10, color = 'k')
plt.ylabel('회전각도 [deg/s]', fontweight='bold', fontsize = 10, color = 'k')
plt.title('뒤틀림 감지(자이로 센서)', fontweight='bold', fontsize = 14, color = 'k')
plt.gca().set_facecolor('#FFFFFF')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.grid(axis = 'y')
plt.xticks(fontsize = 8); plt.yticks(fontsize = 8)

lines = [p_gx, p_gy, p_gz]
rax = plt.axes([0.8, 0.13, 0.08, 0.12])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)

check.on_clicked(func)
plt.show()



plt.figure(3)
p_mx, = plt.plot(t,mx, color = 'r', linewidth=0.3, label='Meg-x')
p_my, = plt.plot(t,my, color = 'g', linewidth=0.3, label='Meg-y')
p_mz, = plt.plot(t,mz, color = 'b', linewidth=0.3, label='Meg-z')
plt.legend(('Meg-x','Meg-y','Meg-z'), loc = 8, ncol=3, prop={'size': 10})
plt.xlabel('time [s]', fontweight='bold', fontsize = 10, color = 'k')
plt.ylabel('지자계 강도 [μT]', fontweight='bold', fontsize = 10, color = 'k')
plt.title('방위감지 결과(지자계 감지 센서)', fontweight='bold', fontsize = 14, color = 'k')
plt.gca().set_facecolor('#FFFFFF')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.grid(axis = 'y')
plt.xticks(fontsize = 8); plt.yticks(fontsize = 8)

lines = [p_mx, p_my, p_mz]
rax = plt.axes([0.8, 0.13, 0.08, 0.12])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)
check.on_clicked(func)

plt.show()