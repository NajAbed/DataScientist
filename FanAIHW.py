import numpy as np
import matplotlib.pyplot as plt
import csv

x=[];y=[];u=[]
with open('C:/Python27/TrendData.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        y.append(float(row[1]))
        u.append(str(row[0]))
    x=range(len(y))

# calculate polynomial
z = np.polyfit(x, y, 30)
f = np.poly1d(z)

#crit_points = x + [x1 for x1 in f.deriv().r if x1.imag == 0 and x[0] < x1.real < x[1]]
crit = f.deriv().r
r_crit = crit[crit.imag==0].real
test = f.deriv(2)(r_crit)
x_min = r_crit[test>0]
y_min = f(x_min)

with open('names1.csv', 'w') as csvfile:
    fieldnames = ['start_date', 'end_date', 'start_value', 'end_value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    sv1 = int(y[len(u)-1]); ev1 = int(y_min[0]);
    if (sv1 > ev1):
        temp = sv1
        sv1 = ev1
        ev1 = temp
    writer.writerow({'start_date': u[len(u)-1], 'end_date': u[int(x_min[0])],'start_value': sv1, 'end_value': ev1})
    for i in range(len(x_min)-1):
        temp1 = int(x_min[i]); temp2 = int(x_min[i+1]);
        sv2 =  int(y_min[i]); ev2 = int(y_min[i+1]);
        if (sv2 > ev2):
            temp = sv2
            sv2 = ev2
            ev2 = temp
        writer.writerow({'start_date': u[temp1], 'end_date': u[temp2],'start_value': sv2, 'end_value': ev2})
    sv3 =  int(y_min[len(y_min)-1]); ev3 = int(y[0])
    if (sv3 > ev3):
        temp = sv3
        sv3 = ev3
        ev3 = temp
    writer.writerow({'start_date': u[int(x_min[len(y_min)-1])], 'end_date': u[0],'start_value': sv3, 'end_value': ev3 })

            
# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
