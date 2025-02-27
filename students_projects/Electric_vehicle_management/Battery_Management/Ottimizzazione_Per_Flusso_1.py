from gekko import GEKKO

m=GEKKO()

m.options.SOLVER=1

x1 = m.Var(value=0, lb=0, ub=1, integer=True)
x2 = m.Var(value=0, lb=0, ub=1, integer=True)
x3 = m.Var(value=0, lb=0, ub=1, integer=True)
x4 = m.Var(value=0, lb=0, ub=1, integer=True)
x5 = m.Var(value=0, lb=0, ub=1, integer=True)
x6 = m.Var(value=0, lb=0, ub=1, integer=True)
x7 = m.Var(value=0, lb=0, ub=1, integer=True)
x8 = m.Var(value=0, lb=0, ub=1, integer=True)
x9 = m.Var(value=0, lb=0, ub=1, integer=True)
x10 = m.Var(value=0, lb=0, ub=1, integer=True)
x11 = m.Var(value=0, lb=0, ub=1, integer=True)
x12 = m.Var(value=0, lb=0, ub=1, integer=True)
x13 = m.Var(value=0, lb=0, ub=1, integer=True)
x14 = m.Var(value=0, lb=0, ub=1, integer=True)
x15 = m.Var(value=0, lb=0, ub=1, integer=True)
x16 = m.Var(value=0, lb=0, ub=1, integer=True)
x17 = m.Var(value=0, lb=0, ub=1, integer=True)

# Equations
#m.Equation(230*x1 + 178*x2 + 157*x3 + 68*x4 + 54*x5 + 277*x6 + 70*x7 + 79*x8 + 22*x9 + 9*x10 + 27*x11 + 38*x12 + 714*x13 + 192*x14 <= 1200)
#m.Equation(230*x1 + 178*x2 + 157*x3 + 68*x4 + 54*x5 + 277*x6 + 42*x15 + 60*x16 + 78*x17 + 9*x10 + 27*x11 + 38*x12 + 714*x13 + 192*x14 <= 1200)
m.Equation(100-(230/150*10*x1)-(178/150*10*x2)-(157/150*10*x3) - (68/150*x4*10) - (54/150*10*x5) - (277/150*10*x6) - (70/150*10*x7) - (79/150*10*x8) - (22/150*x9*10) - (9/150*x10*10) - (27/150*x11*10) - (38/150*x12*10) - (714/150*x13*10) - (192/150*x14*10) >= 35)
m.Equation(100-(230/150*10*x1)-(178/150*10*x2)-(157/150*10*x3) - (68/150*x4*10) - (54/150*10*x5) - (277/150*10*x6) - (42/150*10*x15) - (60/150*10*x16) - (79/150*x17*10) - (9/150*x10*10) - (27/150*x11*10) - (38/150*x12*10) - (714/150*x13*10) - (192/150*x14*10) >= 35)
#Objective
m.Obj(-(1/2*(0.1*230*x1 + 0.1*178*x2 + 0.1*157*x3 + 0.3*68*x4 + 0.4*54*x5 + 0.5*277*x6 + 0.7*42*x15 + 0.9*60*x16 + 78*x17 + 9*x10 + 27*x11 + 38*x12 + 0.3*714*x13 + 0.1*192*x14) + 1/2*(0.1*230*x1 + 0.1*178*x2 + 0.1*157*x3 + 0.3*68*x4 + 0.4*54*x5 + 0.5*277*x6 + 0.9*70*x7 + 79*x8 + 22*x9 + 9*x10 + 27*x11 + 38*x12 + 0.3*714*x13 + 0.1*192*x14))) # Objective
m.solve() # Solve
print("x1: " + str(x1.value))
print("x2: " + str(x2.value))
print("x3: " + str(x3.value))
print("x4: " + str(x4.value))
print("x5: " + str(x5.value))
print("x6: " + str(x6.value))
print("x7: " + str(x7.value))
print("x8: " + str(x8.value))
print("x9: " + str(x9.value))
print("x10: " + str(x10.value))
print("x11: " + str(x11.value))
print("x12: " + str(x12.value))
print("x13: " + str(x13.value))
print("x14: " + str(x14.value))
print("x15: " + str(x15.value))
print("x16: " + str(x16.value))
print("x17: " + str(x17.value))
print("Objective: " + str(m.options.objfcnval))
Variabili=(x1.value,x2.value,x3.value,x4.value,x5.value,x6.value,x7.value,x8.value,x9.value,x10.value,x11.value,x12.value,x13.value,x14.value,)
