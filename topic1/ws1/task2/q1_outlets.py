outletSales = [4,50]

Outlet1Sales = [10, 12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]
 
totalSales=[0,0,0,0]

for i in range(0,4):
   totalSales[i]= (Outlet1Sales[i]+Outlet2Sales[i]+Outlet3Sales[i])*1000

for j in range(0,4):
   print("Total for quarter",str(j),totalSales[j])