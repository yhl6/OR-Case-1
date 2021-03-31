from gurobipy import *
import pandas as pd

df = pd.read_excel('OR109-1_case01_data.xlsx')
Demand_info = pd.read_excel('OR109-1_case01_data.xlsx','Demand')
Demandlist = []
for i in Demand_info.index:
	Demandlist.append(list(Demand_info.loc[i]))
print(Demand_info)
print(Demandlist)
# #產品、月份、運送方法編號 i k t
# ProductID = range(len(Demand_info['Product']))
# Shipping_method = range(0,3)
# MonthID = range(3,9)
#
#
#
#
# #初始存貨
# Initial_Inv = pd.read_excel('OR109-1_case01_data.xlsx', 'Initial inventory')
# Initial_Inventory = Initial_Inv['Initial inventory']
#
# #運送費用
# Shipping_Cost = pd.read_excel('OR109-1_case01_data.xlsx','Shipping cost')
# Express_delivery = Shipping_Cost['Express delivery']
# Air_freight = Shipping_Cost = ['Air_freight']
# Fixed_cost = [100,80,50]
#
# #在途存貨
# In_transit = pd.read_excel('OR109-1_case01_data.xlsx','In-transit')
# April_intransit = In_transit['April']
# May_intransit = In_transit['May']
#
# #箱子大小(第二題)
# Size = pd.read_excel('OR109-1_case01_data.xlsx','Size')
# Cubic_meter = Size['Cubic meter']
#
# #售價、購買成本、期末持有成本
# Price_info = pd.read_excel('OR109-1_case01_data.xlsx','Price and cost')
# Sales = Price_info['Sales price']
# Purchasing_cost = Price_info['Purchasing cost']
# Holding_cost = Price_info['Holding']
#
# #第三四題 Shortage還沒輸進來
#
#
#
#
# eg1 = Model("eg1")
#
# # Xikt 變數
# x = []
# count = []
# for i in ProductID:
# 	x.append([])      #十個list
# 	#count.append([])
#
# 	for k in Shipping_method:
# 		x[i].append([])
# 		#count[i].append([])      #三個list
#
# 		for t in MonthID:
# 			x[i][k].append(eg1.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = "x" + str(i+1)+ str(k)+ str(t)))
# 			#count[i][k].append("x" + str(i+1)+ str(k+1)+ str(t))
#
#
# #Z binary 變數
# z = []
# for k in ProductID:
# 	z.append([])
# 	for t in MonthID:
# 		z[k].append(eg1.addVar(lb = 0, vtype = GRB.BINARY, name = "z" + str(k+1) + str(t)))
#
# # y 期末存貨
# y = []
# for i in ProductID:
# 	y.append([])
# 	for t in MonthID:
# 		y[i].append(eg1.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = "y" + str(i+1) + str(t)))
#
# #setting the objective function
# eg1.setObjective(
#     quicksum(quicksum(Express_delivery[i] * x[i][0][t] for i in ProductID) for t in MonthID)      #變動成本
#     +  quicksum(quicksum(Air_freight[i] * x[i][1][t] for i in ProductID) for t in MonthID)
#     +   quicksum(quicksum(Fixed_cost[k] * z[k][t] for k in Shipping_method) for t in MonthID)      #固定成本
#
#
#
# # add constraints and name them
#
# '''
# # add variables as a list
# # setting the objective function
# eg2.setObjective(
#     quicksum(operating_costs[j] * x[j] for j in cities)
#     +  quicksum(quicksum(shipping_costs[i][j] * y[i][j] for j in cities) for i in markets)
#     , GRB.MINIMIZE)
#
# # add constraints and name them
# eg2.addConstrs((quicksum(y[i][j] for i in markets) <= capacities[j] * x[j]
#                 for j in cities), "productCapacity")
#
# eg2.addConstrs((quicksum(y[i][j] for j in cities) >= demands[i]
#                 for i in markets), "demand_fulfillment")
#
# eg2.optimize()
# '''
#
#
