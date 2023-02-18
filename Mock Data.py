import numpy 
import datetime
import pandas as pd
import random
from randomtimestamp import randomtimestamp, random_date, random_time
import calendar
import names
from random_address import real_random_address


# defining the fields of each table
order_fields = ['order_id', 'date','created_at', 'customer_id(fk)','dlvry_adrs','total_price']
customer_fields=['customer_id','firstname','lastname']
customerAddresses_fields=['customer_id(fk)','address','address_number','addressType']
Item_fields=['item_id','item_name','size','price', 'category']
OrderItem_fields=['order_id(fk)', 'item_id(fk)']
Ingredient_fields=['ing_id','ing_name','unit(gm)','price_per_unit']
ItemIngredient_fileds=['item_id(fk)','ing_id(fk)','quantity']
Inventory_fields=['inv_id','ing_id(fk)','available_qty(kg)','qty_needed_per_month(kg)','qty_to_restock(kg)']
shift_fields=['shift_id','weekday','start_time','end_time']
staff_fields=['staff_id','firstanme','lastname','position','hrly_rate']
rota_fields=['rota_id','staff_id(fk)','shift_id(fk)','date']



# creating a dataframe for each table
order_df                = pd.DataFrame(columns=order_fields)
customer_df             = pd.DataFrame(columns=customer_fields)
customerAddresses_df    = pd.DataFrame(columns=customerAddresses_fields)
Item_df                 = pd.DataFrame(columns=Item_fields)
OrderItem_df            = pd.DataFrame(columns=OrderItem_fields)
Ingredient_df           = pd.DataFrame(columns=Ingredient_fields)
ItemIngredient_df       = pd.DataFrame(columns=ItemIngredient_fileds)
Inventory_df            = pd.DataFrame(columns=Inventory_fields)
shift_df                = pd.DataFrame(columns=shift_fields)
staff_df                = pd.DataFrame(columns=staff_fields)
rota_df                 = pd.DataFrame(columns=rota_fields)




# filling customer data
for i in range(1,482):
    firstname= names.get_first_name()
    lastname=names.get_last_name()
    customer_df.loc[i]= [f"CUS00{i}", firstname, lastname]



#fillingg customer addresses data
idx=0
for i in range(1,482):
    number_of_addresses = random.randint(1,2)
    for j in range(0,number_of_addresses):
        address=real_random_address()['address1']
        type=random.randint(0,2)
        
        if type ==0:
            addressType='home'
        elif type==1:
            addressType='work'
        elif type==2:
            addressType='other'

        idx=idx+1
        customerAddresses_df.loc[idx]= [f"CUS00{i}", address,j+1, addressType]
        







# fill out staff data
for i in range(1,17):
    firstname= names.get_first_name()
    lastname=names.get_last_name()
    staff_df.loc[i]= [f"STF00{i}", firstname, lastname,'Null', 'Null']

staff_df.loc[[1], ['position','hrly_rate']]=['Headchef',21.25]
staff_df.loc[[2], ['position', 'hrly_rate']]=['Souschef',19.8]
staff_df.loc[[3], ['position', 'hrly_rate']]=['Chef',17.5]
staff_df.loc[[4], ['position', 'hrly_rate']]=['Chef',17.5]
staff_df.loc[[5], ['position', 'hrly_rate']]=['Chef',17.5]
staff_df.loc[[6], ['position', 'hrly_rate']]=['Chef',17.5]
staff_df.loc[[7], ['position', 'hrly_rate']]=['Order Manager',18.0]
staff_df.loc[[8], ['position', 'hrly_rate']]=['Order Manager',18.0]
staff_df.loc[[9], ['position', 'hrly_rate']]=['Delivery Boy',15.75]
staff_df.loc[[10], ['position', 'hrly_rate']]=['Delivery Boy',15.75]
staff_df.loc[[11], ['position', 'hrly_rate']]=['Delivery Boy',15.75]
staff_df.loc[[12], ['position', 'hrly_rate']]=['Delivery Boy',15.75]
staff_df.loc[[13], ['position', 'hrly_rate']]=['Delivery Boy',15.75]
staff_df.loc[[14], ['position', 'hrly_rate']]=['Delivery Boy',15.75]
staff_df.loc[[15], ['position', 'hrly_rate']]=['Delivery Boy',15.75]
staff_df.loc[[16], ['position', 'hrly_rate']]=['Delivery Boy',15.75]















# fill out shift data 
shift_df.loc[1]=  ["SHF001", 'Monday', '10:00', '15:30']
shift_df.loc[2]=  ["SHF002", 'Monday', '15:30', '21:00']
shift_df.loc[3]=  ["SHF003", 'Tuesday', '10:00', '15:30']
shift_df.loc[4]=  ["SHF004", 'Tuesday', '15:30', '21:00']
shift_df.loc[5]=  ["SHF005", 'Wednesday', '10:00', '15:30']
shift_df.loc[6]=  ["SHF006", 'Wednesday', '15:30', '21:00']
shift_df.loc[7]=  ["SHF007", 'Thursday', '10:00', '15:30']
shift_df.loc[8]=  ["SHF008", 'Thursday', '15:30', '21:00']
shift_df.loc[9]=  ["SHF009", 'Friday', '10:00', '15:30']
shift_df.loc[10]= ["SHF0010", 'Friday', '15:30', '21:00']
shift_df.loc[11]= ["SHF0011", 'Saturday', '10:00', '15:30']
shift_df.loc[12]= ["SHF0012", 'Saturday', '15:30', '21:00']
shift_df.loc[13]= ["SHF0013", 'Sunday', '10:00', '15:30']
shift_df.loc[14]= ["SHF0014", 'Sunday', '15:30', '21:00']










# fillout rota data
dates = pd.date_range(start="01/01/2023" , end="02/01/2023", freq='D')
numOfDays= len(dates)
numOfRotas= numOfDays*18

hc_counter=2
c_counter=2+4
om_counter=2+4+3
d_counter=2+4+3+8

for i in range(numOfRotas):
    dateIDX=int(i/18)
    shiftIDX=int(i/9)
    date=str(dates[dateIDX]).split(' ')[0]

    if hc_counter>0:
        staffIDX=hc_counter
        hc_counter=hc_counter-1
    elif c_counter>2:
        staffIDX=c_counter
        c_counter=c_counter-1
    
    elif om_counter>2+4:
        staffIDX=om_counter
        om_counter=om_counter-1

    elif d_counter>2+4+3:
        staffIDX=d_counter
        if d_counter==2+4+3+1:
            hc_counter=2
            c_counter=2+4
            om_counter=2+4+3
            d_counter=2+4+3+8
        else: d_counter=d_counter-1


    rota_df.loc[i]= [f"ROT00{i}", f"STF00{staffIDX}",f"SHF00{staffIDX}",date]





# fill in item data
Item_df.loc[1]=  ["ITM001", 'Margherita', 'M',13,'Special Pizza']
Item_df.loc[2]=  ["ITM002", 'Margherita', 'L',15,'Special Pizza']
Item_df.loc[3]=  ["ITM003", 'Diavola', 'M',16,'Special Pizza']
Item_df.loc[4]=  ["ITM004", 'Diavola', 'L',19,'Special Pizza']
Item_df.loc[5]=  ["ITM005", 'Parmigiana', 'M',15,'Special Pizza']
Item_df.loc[6]=  ["ITM006", 'Parmigiana', 'L',18,'Special Pizza']
Item_df.loc[7]=  ["ITM007", 'Quattro Formagi', 'M',16,'Special Pizza']
Item_df.loc[8]=  ["ITM008", 'Quattro Formagi', 'L',19,'Special Pizza']
Item_df.loc[9]=  ["ITM009", 'Napolitana', 'M',16,'Special Pizza']
Item_df.loc[10]=  ["ITM0010", 'Napolitana', 'L',18,'Special Pizza']
Item_df.loc[11]=  ["ITM0011", 'Pepperoni', 'M',15,'Special Pizza']
Item_df.loc[12]=  ["ITM0012", 'Pepperoni', 'L',17,'Special Pizza']
Item_df.loc[13]=  ["ITM0013", 'Seafood', 'M',17,'Special Pizza']
Item_df.loc[14]=  ["ITM0014", 'Seafood', 'L',20,'Special Pizza']
Item_df.loc[15]=  ["ITM0015", 'Hawaiian', 'M',15,'Special Pizza']
Item_df.loc[16]=  ["ITM0016", 'Hawaiian', 'L',17,'Special Pizza']







#fill in ingredient data
Ingredient_df.loc[1]=   ["ING001", 'Pizza Dough', 300, 0.6]
Ingredient_df.loc[2]=   ["ING002", 'Tomato Sauce', 200 ,0.57]
Ingredient_df.loc[3]=   ["ING003", 'Mozzarella Cheese', 100, 1.25]
Ingredient_df.loc[4]=   ["ING004", 'Dried Orgenao', 10 ,0.2]
Ingredient_df.loc[5]=   ["ING005", 'Spicy Salami', 200, 2.9]
Ingredient_df.loc[6]=   ["ING006", 'Chilli Pepper', 10 ,0.24]
Ingredient_df.loc[7]=   ["ING007", 'Eggplant', 100, 0.3]
Ingredient_df.loc[8]=   ["ING008", 'Parmesan Cheese', 100 ,1.6]
Ingredient_df.loc[9]=   ["ING009", 'Cheddar Cheese', 100 ,1.12]
Ingredient_df.loc[10]=  ["ING0010", 'Ricotta Cheese', 100 ,1.32]
Ingredient_df.loc[11]=  ["ING0011", 'Anchovies', 200 ,2.7]
Ingredient_df.loc[12]=  ["ING0012", 'Capers', 50 ,0.28]
Ingredient_df.loc[13]=  ["ING0013", 'Pepperoni', 200,3.0]
Ingredient_df.loc[14]=  ["ING0014", 'Shrimp', 200 ,3.4]
Ingredient_df.loc[15]=  ["ING0015", 'Tuna', 200 ,3.45]
Ingredient_df.loc[16]=  ["ING0016", 'Calamari', 200 ,3.50]
Ingredient_df.loc[17]=  ["ING0017", 'Beef Bacon', 200 ,3]
Ingredient_df.loc[18]=  ["ING0018", 'Pineapple', 100 ,1.45]




# fill in itemingredient data

# Margherita Medium
ItemIngredient_df.loc[1]=   ["ITM001", "ING001", 1]
ItemIngredient_df.loc[2]=   ["ITM001", "ING002",1]
ItemIngredient_df.loc[3]=   ["ITM001", "ING003", 1]
ItemIngredient_df.loc[4]=   ["ITM001", "ING004", 1]
ItemIngredient_df.loc[5]=   ["ITM002", "ING001", 1.5]
ItemIngredient_df.loc[6]=   ["ITM002", "ING002",1.5]
ItemIngredient_df.loc[7]=   ["ITM002", "ING003", 1.5]
ItemIngredient_df.loc[8]=   ["ITM002", "ING004", 1.5]
ItemIngredient_df.loc[9]=   ["ITM003", "ING001", 1]
ItemIngredient_df.loc[10]=   ["ITM003", "ING003",1]
ItemIngredient_df.loc[11]=   ["ITM003", "ING005", 1]
ItemIngredient_df.loc[12]=   ["ITM003", "ING006", 1]
ItemIngredient_df.loc[13]=   ["ITM004", "ING001", 1.5]
ItemIngredient_df.loc[14]=   ["ITM004", "ING003",1.5]
ItemIngredient_df.loc[15]=   ["ITM004", "ING005", 1.5]
ItemIngredient_df.loc[16]=   ["ITM004", "ING006", 1.5]
ItemIngredient_df.loc[17]=   ["ITM005", "ING001", 1]
ItemIngredient_df.loc[18]=   ["ITM005", "ING003",1]
ItemIngredient_df.loc[19]=   ["ITM005", "ING007", 1]
ItemIngredient_df.loc[20]=   ["ITM005", "ING008", 1]
ItemIngredient_df.loc[21]=   ["ITM006", "ING001", 1.5]
ItemIngredient_df.loc[22]=   ["ITM006", "ING003",1.5]
ItemIngredient_df.loc[23]=   ["ITM006", "ING007", 1.5]
ItemIngredient_df.loc[24]=   ["ITM006", "ING008", 1.5]
ItemIngredient_df.loc[25]=   ["ITM007", "ING001", 1]
ItemIngredient_df.loc[26]=   ["ITM007", "ING008",1]
ItemIngredient_df.loc[27]=   ["ITM007", "ING009", 1]
ItemIngredient_df.loc[28]=   ["ITM007", "ING0010", 1]
ItemIngredient_df.loc[29]=   ["ITM008", "ING001", 1.5]
ItemIngredient_df.loc[30]=   ["ITM008", "ING008",1.5]
ItemIngredient_df.loc[31]=   ["ITM008", "ING009", 1.5]
ItemIngredient_df.loc[32]=   ["ITM008", "ING0010", 1.5]
ItemIngredient_df.loc[33]=   ["ITM009", "ING001", 1]
ItemIngredient_df.loc[34]=   ["ITM009", "ING003",1]
ItemIngredient_df.loc[35]=   ["ITM009", "ING0011", 1]
ItemIngredient_df.loc[36]=   ["ITM009", "ING002", 1]
ItemIngredient_df.loc[37]=   ["ITM0010", "ING001", 1.5]
ItemIngredient_df.loc[38]=   ["ITM0010", "ING003",1.5]
ItemIngredient_df.loc[39]=   ["ITM0010", "ING0011", 1.5]
ItemIngredient_df.loc[40]=   ["ITM0010", "ING0012", 1.5]
ItemIngredient_df.loc[41]=   ["ITM0011", "ING001", 1]
ItemIngredient_df.loc[42]=   ["ITM0011", "ING003",1]
ItemIngredient_df.loc[43]=   ["ITM0011", "ING0013", 1]
ItemIngredient_df.loc[44]=   ["ITM0012", "ING001", 1.5]
ItemIngredient_df.loc[45]=   ["ITM0012", "ING003",1.5]
ItemIngredient_df.loc[46]=   ["ITM0012", "ING0013", 1.5]
ItemIngredient_df.loc[47]=   ["ITM0013", "ING001", 1]
ItemIngredient_df.loc[48]=   ["ITM0013", "ING003",1]
ItemIngredient_df.loc[49]=   ["ITM0013", "ING0014", 1]
ItemIngredient_df.loc[50]=   ["ITM0013", "ING0015", 1]
ItemIngredient_df.loc[51]=   ["ITM0013", "ING0016", 1]
ItemIngredient_df.loc[52]=   ["ITM0014", "ING001", 1.5]
ItemIngredient_df.loc[53]=   ["ITM0014", "ING003",1.5]
ItemIngredient_df.loc[54]=   ["ITM0014", "ING0014", 1.5]
ItemIngredient_df.loc[55]=   ["ITM0014", "ING0015", 1.5]
ItemIngredient_df.loc[56]=   ["ITM0014", "ING0016", 1.5]
ItemIngredient_df.loc[57]=   ["ITM0015", "ING001", 1]
ItemIngredient_df.loc[58]=   ["ITM0015", "ING003",1]
ItemIngredient_df.loc[59]=   ["ITM0015", "ING0017", 1]
ItemIngredient_df.loc[60]=   ["ITM0015", "ING0018", 1]
ItemIngredient_df.loc[61]=   ["ITM0016", "ING001", 1.5]
ItemIngredient_df.loc[62]=   ["ITM0016", "ING003",1.5]
ItemIngredient_df.loc[63]=   ["ITM0016", "ING0017", 1.5]
ItemIngredient_df.loc[64]=   ["ITM0016", "ING0018", 1.5]






# fill in inventory data


for i in range(1,18):
    qty_needed_per_month=0
    for j in range(len(ItemIngredient_df)):
        if ItemIngredient_df.iat[j,1]==f"ING00{i}":
            qty_needed_per_month = qty_needed_per_month + ItemIngredient_df.iat[j,2]
    qty_needed_per_month=qty_needed_per_month*int(Ingredient_df.iat[i,2])*4*30/1000
    Inventory_df.loc[i]=[f"INV00{i}",f"ING00{i}",'NA',qty_needed_per_month,'NA']    


avl_qty=random.randrange(480)
needed_qty=int(Inventory_df.loc[1,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[1,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(30)
needed_qty=int(Inventory_df.loc[2,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[2,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(21)
needed_qty=int(Inventory_df.loc[3,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[3,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[4,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[4,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(3)
needed_qty=int(Inventory_df.loc[5,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[5,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(30)
needed_qty=int(Inventory_df.loc[6,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[6,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(30)
needed_qty=int(Inventory_df.loc[7,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[7,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[8,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[8,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(30)
needed_qty=int(Inventory_df.loc[9,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[9,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[10,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[10,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(15)
needed_qty=int(Inventory_df.loc[11,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[11,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[12,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[12,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[13,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[13,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[14,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[14,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[15,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[15,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[16,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[16,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]
avl_qty=random.randrange(60)
needed_qty=int(Inventory_df.loc[17,'qty_needed_per_month(kg)'])-avl_qty
Inventory_df.loc[17,['available_qty(kg)','qty_to_restock(kg)']]=[avl_qty,needed_qty]




# fill in order data
dates = pd.date_range(start="01/01/2023" , end="02/01/2023", freq='D')

idx=1

for i in range(len(dates)):
    num_of_orders=random.randint(10,40)
    date=str(dates[i]).split(' ')[0]
    start_time=datetime.time(10,0,0)
    end_time=datetime.time(21,0,0)
    for j in range(num_of_orders):
        customer=f"CUS00{random.randint(1,len(customer_df))}"
        time=random_time(start_time,end_time)
        address_no=random.randint(1,2)
        for k in range(len(customerAddresses_df)):
            if customer==customerAddresses_df.iloc[k, 0]:
                if address_no==1 and customerAddresses_df.iloc[k, 2]==1:
                     address=customerAddresses_df.iloc[k, 1]
                elif address_no==1 and customerAddresses_df.iloc[k, 2]==2:
                    x=0
                elif k+1 > len(customerAddresses_df):
                    x=0
                elif address_no==2 and customerAddresses_df.iloc[k, 2]==1 and customerAddresses_df.iloc[k+1, 2]!=2:
                    address=customerAddresses_df.iloc[k, 1]
                elif address_no==2 and customerAddresses_df.iloc[k, 2]==1 and customerAddresses_df.iloc[k+1, 2]==2:
                    x=0
                elif address_no==2 and customerAddresses_df.iloc[k, 2]==2 :
                    address=customerAddresses_df.iloc[k, 1]
                
                    
        order_df.loc[idx]= [f"ORD00{idx}", date, time,customer,address,"NA"]
        idx=idx+1




# fill OrderItem data
idx=0
for i in range(1,len(order_df)):
    num_of_items=random.randint(1,4)
    for j in range(1,num_of_items+1):
        itm_no=random.randint(1,len(Item_df))
        OrderItem_df.loc[idx]=[f"ORD00{i}", f"ITM00{itm_no}"]
        idx=idx+1









# adding total price for orders
ttl_price=0
for i in range(1,len(order_df)):
    for j in range(1,len(OrderItem_df)):
        if order_df.iloc[i, 0]== OrderItem_df.iloc[j,0]:
            for k in range(1,len(Item_df)):
                if OrderItem_df.iloc[j,1]==Item_df.iloc[k,0]:
                    ttl_price=ttl_price+Item_df.iloc[k,3]
    
    order_df.iloc[i, 5]=ttl_price
    ttl_price=0







#exporting dataframes to excel file
with pd.ExcelWriter('RestaurantData.xlsx') as writer:
    order_df.to_excel(writer, sheet_name='order', index=False)
    customer_df.to_excel(writer, sheet_name='customer', index=False)
    customerAddresses_df.to_excel(writer, sheet_name='customerAddresses', index=False)
    Item_df.to_excel(writer, sheet_name='Item', index=False)
    OrderItem_df.to_excel(writer, sheet_name='OrderItem', index=False)
    Ingredient_df.to_excel(writer, sheet_name='Ingredient', index=False)
    ItemIngredient_df.to_excel(writer, sheet_name='ItemIngredient', index=False)
    Inventory_df.to_excel(writer, sheet_name='Inventory', index=False)
    shift_df.to_excel(writer, sheet_name='shift', index=False)
    staff_df.to_excel(writer, sheet_name='staff', index=False)
    rota_df.to_excel(writer, sheet_name='rota', index=False)






