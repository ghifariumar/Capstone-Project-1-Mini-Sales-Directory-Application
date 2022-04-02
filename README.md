# Capstone Project-1: Mini-Sales-Directory-Application

In this project I have to make a mini application for directory in sales which can operating to "CRUD" Data(Create, Remove, Update, Delete) and handling errors

## 1. Def Function
```python
def function mainly use in this project. def is the keyword for the function and follow by the function name, parentheses '()' 
and colon ':' at the end. The function body start below the function name marked with identation. After function complete
you can call the function name with parentheses'()'.
Example:
```

<img width="358" alt="image" src="https://user-images.githubusercontent.com/99155979/161367387-491d9408-3f20-4daf-a71a-5a5b175c6aed.png">
==========================================================================

```python
I make all the function for every menu and at the end of lines I only need to call the menu_utama funtion.
```
<img width="343" alt="image" src="https://user-images.githubusercontent.com/99155979/161376839-5ddb8c13-c27b-4e08-8a87-264160d59300.png">

## 2. Create
```python
Create or add new data one at a time. First we need to input the primary key, in this project the primary key is the item's code.
If the primary key is already exist in the sales dictionary then the application will print "sales data is already exist".
If the primary key is new then user have to insert item's name, price, the amount item's sold, and the person responsible.
After that, there will be a question to make sure user wants to add a new data or not. If user answer yes than the new sales data 
will be saved and added to the directory, if user answer no then the data will not be saved.
```
<img width="623" alt="image" src="https://user-images.githubusercontent.com/99155979/161379039-f9448d4e-f2b1-4e71-9196-37f42e23bb09.png">

## 3. Read
```python
User can read all the data sales list or the exact sales data user needed by inputing the item's code user wants to see.
When user wants to see all the data. If there is no data sales at all at the dictionary then the application will print out
"No Data Sales". If there is data sales in the dictionary, application will print all the data list. That's also applies
when user wants to read the exact data by inputing item's code.
All sales data:
```
<img width="698" alt="image" src="https://user-images.githubusercontent.com/99155979/161379754-39ded675-751e-4535-9000-f5596b9953ca.png">

```python
Sales data based on item's code:
```
<img width="710" alt="image" src="https://user-images.githubusercontent.com/99155979/161379819-db2115a8-19f9-4fe1-a439-3052b44dd976.png">

## 4. Update
```python
User can change or update sales data by changing the detail's description on at a time.
First, user insert the item's code if the sales data of the item's code is in the dictionary then user need to insert 
the description user wants to change if user inserts the wrong description, application will print out 
"the description doesn't exist" and the application will be looping to ask the correct description. After user inserts
the exact descrption, user insert the details for the description. There will be another yes or no question if user
answers yes then the sales data will be updated if unser answers no the the sales data will be not updated.
```
<img width="713" alt="image" src="https://user-images.githubusercontent.com/99155979/161382954-0d73e046-b877-4772-8cb6-a4738ebabcd0.png">

```python
Update data's detail on data description based on item's code or primary key:
```
<img width="568" alt="image" src="https://user-images.githubusercontent.com/99155979/161383045-756398a8-fb16-4b57-9b25-114aab262886.png">

## 5. Delete
```python
User can remove or delete the sales data one at a time if user inserts the item's code that is in the directory. 
If the item's code is not in the directory then the application will print "No Sales Data". But if the item's code is in
the directory the sales data will be removed if user asnwesr yes in the confirmation request, while the sales data 
will not be removed if the user answers no.
```

<img width="604" alt="image" src="https://user-images.githubusercontent.com/99155979/161386651-b8e4d82a-82f2-4f0d-8bd0-8d56d4c93f5c.png">


