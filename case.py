from gurobipy import *
import pandas as pd

# 產品、月份、運送方法編號 i k t
ProductID = range(0, 10)  # 0-9
ShippingID = range(0, 3)  # 0-2
MonthID = range(0, 6)  # 0-5

df = pd.read_excel('OR109-1_case01_data.xlsx')
Demand = pd.read_excel('OR109-1_case01_data.xlsx', sheet_name='Demand')
del Demand['Product']
# for t in MonthID[3:]:
#     print(Demand.columns[t][:3])


# 初始存貨
Ini_inv_df = pd.read_excel('OR109-1_case01_data.xlsx', 'Initial inventory')
Initial_inventory = Ini_inv_df['Initial inventory']

# 運送費用
Shipping_Cost = pd.read_excel('OR109-1_case01_data.xlsx', 'Shipping cost')
Express_delivery = Shipping_Cost['Express delivery']
Air_freight = Shipping_Cost['Air freight']
Fixed_cost = [100, 80, 50]

# 在途存貨
Intransit_df = pd.read_excel('OR109-1_case01_data.xlsx', 'In-transit')
Intransit_Apr = Intransit_df['April']
Intransit_May = Intransit_df['May']

# 箱子大小(第二題)
Size = pd.read_excel('OR109-1_case01_data.xlsx', 'Size')
Cubic_meter = Size['Cubic meter']

# 售價、購買成本、期末持有成本
Price_info = pd.read_excel('OR109-1_case01_data.xlsx', 'Price and cost')
Sales = Price_info['Sales price']
Purchasing_cost = Price_info['Purchasing cost']
Holding_cost = Price_info['Holding']

eg1 = Model('eg1')

# Xikt 變數
x = []
for i in ProductID:
    x.append([])
    for k in ShippingID:
        x[i].append([])
        for t in MonthID:
            x[i][k].append(eg1.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x" + str(i + 1) + str(k + 1) + str(t + 3)))
            # x(1-10),(1-3),(3-8)
# Z binary 變數
z = []
for k in ShippingID:
    z.append([])
    for t in MonthID:
        z[k].append(eg1.addVar(lb=0, vtype=GRB.BINARY, name="z" + str(k + 1) + str(t + 3)))  # z(1-3),(3-8)

# y 期末存貨
y = []
for i in ProductID:
    y.append([])
    for t in MonthID:
        y[i].append(eg1.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y" + str(i + 1) + str(t + 3)))  # y(1-10),(3-8)

# setting the objective function
purchasing = quicksum(quicksum(Purchasing_cost[i] * x[i][k][t] for k in ShippingID for t in MonthID) for i in ProductID)
shipping_ex = quicksum(quicksum(Express_delivery[i] * x[i][0][t] for i in ProductID) for t in MonthID)
shipping_air = quicksum(quicksum(Air_freight[i] * x[i][1][t] for i in ProductID) for t in MonthID)
shipping_f = quicksum(quicksum(Fixed_cost[k] * z[k][t] for k in ShippingID) for t in MonthID)
holding = quicksum(Holding_cost[i] * y[i][t] for i in ProductID for t in MonthID)
eg1.setObjective(purchasing + shipping_f + shipping_ex + shipping_air + holding, GRB.MINIMIZE)

# add constraints of ending inv
eg1.addConstrs((y[i][0] == (Initial_inventory[i] - Demand.iloc[i, 0]) for i in ProductID), 'Ending_inv_Mar')
eg1.addConstrs((y[i][1] == (y[i][0] + x[i][1][0] - Demand.iloc[i, 1] + Intransit_Apr[i]) for i in ProductID),
               'Ending_inv_Apr')
eg1.addConstrs(
    (y[i][2] == (y[i][1] + x[i][2][0] + x[i][1][1] - Demand.iloc[i, 2] + Intransit_May[i]) for i in ProductID),
    'Ending_inv_May')

for t in MonthID[3:]:
    eg1.addConstrs((y[i][t] == (y[i][t - 1] + quicksum(x[i][k][t - k] for k in ShippingID) - Demand.iloc[i, t]) for i in
                    ProductID), 'Ending_inv_' + str(Demand.columns[t][:3]))

eg1.optimize()
