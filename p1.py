import pandas as pd
import numpy as np
import csv
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#importing the csv data 
data = pd.read_csv("C:\\Users\\cheta\\OneDrive\\Desktop\\3rdRecord\\PyProject\\apple.csv")

# heads prints
print(data.head())

# checking dataset contains any null values
print(data.isnull().sum())

#describe
print(data.describe())

# 1. top 10 highest-rated iPhones in India 
highest_rated = data.sort_values(by=["Star Rating"],ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])


# 2.overall ratings of the highest-rated iPhones 
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label,y = counts,title="Number of Reviews of Highest Rated iPhones")
figure.show()



# 3.creating new Discount column by using Mrp and Sale Price values
fc4=data
fc4['Discount']=fc4['Mrp'] - fc4['Sale Price']
print(fc4)


# 4. have a look at the relationship between the sale price of iPhones and there ratings
figure = px.scatter(data_frame = data, x="Number Of Ratings",y="Sale Price")
figure.show()


# 5.Discount percentage on iPhones on Flipkart and the number of ratings:
figure = px.scatter(data_frame = data, x="Number Of Ratings",y="Discount Percentage")
figure.show()



# 6. Finding unique values from each column
pd.DataFrame(data.nunique().sort_values(), columns= ['Number of unique values'])



# 7. Differencing in iphone sales interms of max sale price and Mrp values
d=data['Sale Price'].values
k=data['Mrp'].values
plt.hist(d,bins=50)
plt.xlabel("Sale price")
plt.ylabel("Mrp values")
plt.title('max sale price')
plt.show()


# 8. pie chat graphical view of Number of reviews on 10 Iphone brands
y = data['Number Of Reviews'].head(10)
x = data['Product Name'].head(10)
plt.pie(y,labels=x,autopct='%1.0f%%')
plt.title('Pie Chart')
plt.show()


# 9. Minimum And Maximum Mrp values and Sales Prices values 
data1 = data['Sale Price'].min()
print("The Min price of IPhone : ",data1)
data3 = data['Sale Price'].max()
print("The Max price of IPhone : ",data3)
data2 = data['Mrp'].max()
print("The Max price of IPhone : ",data2)
data2 = data['Mrp'].min()
print("The Min price of IPhone : ",data2)




#  10.Comparision betweeten sale price and Mrp price over all brand of Iphones
x = data['Sale Price']
y1 = data['Mrp']
y2 = data['Sale Price']
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='MRP', color='red',marker='o') 
plt.plot(x, y2, label='Sale', color='blue',marker='*') 
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Sale price VS MRP price') 
plt.legend() 
plt.show()