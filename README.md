# Capstone Project-1: Sales-Directory-Application

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
I make all the function for every menu and at the end of lines I only need to call the menu_utama function.
```
<img width="343" alt="image" src="https://user-images.githubusercontent.com/99155979/161376839-5ddb8c13-c27b-4e08-8a87-264160d59300.png">

```
Output result for main menu's application:
```
<img width="245" alt="image" src="https://user-images.githubusercontent.com/99155979/161672238-94d34233-f328-44ab-961e-416b0f466dcc.png">



## 2. Create
```python
Create or add new data one at a time. First we need to input the primary key. In this project the primary key is the item's code.
If the primary key is already exist in the sales dictionary then the application will print "sales data is already exist".
If the primary key is new then user have to insert item's name, price, the amount item's sold, and the person responsible.
After that, there will be a question to make sure user wants to add a new data or not. If user answer yes than the new sales data 
will be saved and added to the directory, if user answer no then the data will not be saved.
```
<img width="185" alt="1" src="https://user-images.githubusercontent.com/99155979/161680902-948762ad-d030-4966-b416-cb893bc7eee1.png">
==========================================================================
<img width="175" alt="2" src="https://user-images.githubusercontent.com/99155979/161680924-7f288a33-1711-4a6a-b6c7-e7d798b4fe9e.png">
==========================================================================
<img width="149" alt="3" src="https://user-images.githubusercontent.com/99155979/161680945-d417479e-f3dd-44a4-960c-85039de62bc0.png">
==========================================================================
<img width="184" alt="4" src="https://user-images.githubusercontent.com/99155979/161680970-dd745d91-ef69-417f-b029-c36bc6e17103.png">
==========================================================================
<img width="461" alt="5" src="https://user-images.githubusercontent.com/99155979/161680997-3b1d1a58-9922-4d4d-9088-17457b6759ee.png">
==========================================================================
<img width="250" alt="6" src="https://user-images.githubusercontent.com/99155979/161681011-0476f3cb-3628-44f7-9764-dd6f1868cc35.png">

## 3. Read
```python
User can read all the data sales list or the exact sales data user needed by inputing the item's code user wants to see.
When user wants to see all the data. If there is no data sales at all at the dictionary then the application will print out
"No Data Sales". If there is data sales in the dictionary, application will print all the data list. That's also applies
when user wants to read the exact data by inputing item's code.
All sales data:
```
<img width="540" alt="2" src="https://user-images.githubusercontent.com/99155979/161683306-3cd28c09-afbf-45cb-b720-2dc74b6edb9a.png">

```python
Sales data based on item's code:
```
<img width="529" alt="3" src="https://user-images.githubusercontent.com/99155979/161683331-ef766237-4a9a-43bc-97c1-b2d8a7a26036.png">

## 4. Update
```python
User can change or update sales data by changing the detail's description on at a time.
First, user insert the item's code if the sales data of the item's code is in the dictionary then user need to insert 
the description user wants to change if user inserts the wrong description, application will print out 
"the description doesn't exist" and the application will be looping to ask the correct description. After user inserts
the exact descrption, user insert the details for the description. There will be another yes or no question if user
answers yes then the sales data will be updated if unser answers no the the sales data will be not updated.
```
<img width="500" alt="2" src="https://user-images.githubusercontent.com/99155979/161697129-351d945e-e7c9-41f3-af9d-ecd90f377e51.png">
==========================================================================
<img width="275" alt="3" src="https://user-images.githubusercontent.com/99155979/161697176-da2a2f66-4db0-4216-b6f2-bddb5f665a7e.png">
==========================================================================
<img width="529" alt="4" src="https://user-images.githubusercontent.com/99155979/161697205-8d054a2b-a428-4a2e-996e-884c85257a9e.png">
==========================================================================

## 5. Delete
```python
User can remove or delete the sales data one at a time if user inserts the item's code that is in the directory. 
If the item's code is not in the directory then the application will print "No Sales Data". But if the item's code is in
the directory the sales data will be removed if user asnwesr yes in the confirmation request, while the sales data 
will not be removed if the user answers no.
```
<img width="264" alt="1" src="https://user-images.githubusercontent.com/99155979/161699412-40c03faa-586b-4c6b-a153-c79b731272f1.png">



