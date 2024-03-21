# Creating users table

cursor.execute("""                                          
CREATE TABLE IF NOT EXISTS tblUsers(                       # CREATING THE TABLE FOR TBL USERS
UserID INTEGER PRIMARY KEY,                                # CREATING USER ID AS AN INTEGER AS PRIMARY KEY                         
Username VARCHAR(100) NOT NULL,                            # CREATING USERNAME AS 100 VARIABLE CHARACTERS, NOT NULL
Email VARCHAR(100) NOT NULL,                               # CREATING EMAIL AS 100 VARIABLE CHARACTERS, NOT NULL
Password VARCHAR(100) NOT NULL                             # CREATING PASSWORD AS 100 VARIABLE CHARACTERS, NOT NULL                         
);""") 
db.commit()                                                # COMMITING IT TO THE DATABASE


# Creating insights and recipes table

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblInsightsAndRecipes(          # CREATING THE TABLE FOR TBLINSIGHTSANDRECIPES
PostID INTEGER PRIMARY KEY,                                # CREATING POST ID AS INTEGER WITH A PRIMARY KEY
Title VARCHAR(1000) NOT NULL,                              # CREATING TITLE WITH 1000 VARIABLE CHARACTERS AS NOT NULL
Content VARCHAR(4000) NOT NULL                             # CREATING CONTENT (THE POST PARAGRAPH) WITH 4000 VARIABLE CHARACTERS NOT NULL
);""")
db.commit()                                                # COMMITTING IT TO THE DATABASE


# Creating the product table

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblProducts(                    # CREATING THE TABLE FOR PRODUCTS
ProductID INTEGER PRIMARY KEY,                             # CREATING THE TABLE'S PRODUCT ID AS A PRIMARY KEY
ProductName VARCHAR(300) NOT NULL,                         # ATTRIBUTE PRODUCT NAME, AS 300 VARIABLE CHARACTERS NOT NULL
ProductPrice FLOAT NOT NULL,                               # ATTRIBUTE PRODUCT PRICE AS FLOAT, NOT NULL
ProductShipping FLOAT NOT NULL,                            # ATTRIBUTE PRODUCT SHIPPING AS FLOAT, NOT NULL
ProductStock VARCHAR(100) NOT NULL,                        # ATTRIBUTE PRODUCT'S STOCK 100 VARIABLE CHARACTERS NOT NULL
ProductCapacity INTEGER NOT NULL,                          # ATTRIBUTE PRODUCT CAPACITY AS DATA TYPE INTEGER NOT NULL
ProductColour VARCHAR(300) NOT NULL,                       # ATTRIBUTE PRODUCT COLOUR AS 300 VARIABLE CHARACTERS NOT NULL
ProductVersion VARCHAR(300) NOT NULL,                      # ATTRIBUTE PRODUCT VERSION AS 300 VARIABLE CHARACTERS NOT NULL
ProductDescription VARCHAR(1000) NOT NULL                  # ATTRIBUTE PRODUCT DESCRIPTION AS 1000 VARIABLE CHARACTERS NOT NULL
);""")
db.commit()                                                # COMMITTING IT TO THE DATABASE


# Creating the reviews table

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblReviews(                        # CREATING THE TABLE FOR REVIEWS
ReviewID INTEGER PRIMARY KEY,                                 # ATTRIBUTE REVIEW ID, DATA TYPE AS AN INTEGER, PRIMARY KEY
Review VARCHAR(10000) NOT NULL,                               # ATTRIBUTE REVIEW, DATA TYPE AS 10000 VARIABLE CHARACTERS NOT NULL
ProductID INTEGER,                                            # ATTRIBUTE PRODUCT ID AS DATA TYPE INTEGER
FOREIGN KEY (ProductID) REFERENCES tblProducts(ProductID)     # FOREIGN KEY REFERENCING TO TBLPRODUCTS WITH PRODUCTID, SO REVIEWS ARE LINKED TO THE RIGHT PRODUCT
);
               """)
db.commit()                                                   # COMMITTING IT TO THE DATABASE



# Creating the add to cart table

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblAddToCart(                      # CREATING THE TABLE FOR ADD TO CART
CartID INTEGER PRIMARY KEY,                                   # ATTRIBUTE CART ID DATA TYPE AS AN INTEGER, PRIMARY KEY
Email VARCHAR(100) NOT NULL,                                  # ATTRIBUTE EMAIL, DATA TYPE AS 100 VARIABLE CHARACTERS, NOT NULL
TheRiceMachine INT,                                           # ATTRIBUTE THE RICE MACHINE, DATA TYPE AS INTEGER
TheBuffalo INT,                                               # ATTRIBUTE THE BUFFALO, DATA TYPE AS INTEGER
TheUncleJohn INT,                                             # ATTRIBUTE THE UNCLE JOHN, DATA TYPE AS INTEGER
RiceAndDice INT,                                              # ATTRIBUTE RICE AND DICE, DATA TYPE AS INTEGER
TheBasmatiBoiler INT,                                         # ATTRIBUTE THE BASMATI BOILER, DATA TYPE AS INTEGER
RiceCooker3000 INT,                                           # ATTRIBUTE THE RICE COOKER 3000, DATA TYPE AS INTEGER
FOREIGN KEY (Email) REFERENCES tblUsers(Email)                # FOREIGN KEY REFERENCING TO TBLUSERS WITH EMAIL, SO THE SHOPPING CART IS LINKED TO THE RIGHT CONSUMER
);""")
db.commit()                                                   # COMMITTING IT TO THE DATABASE



# Creating the discount table

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblDiscounts(                      # CREATING THE TABLE FOR DISCOUNTS
DiscountID INTEGER PRIMARY KEY,                               # ATTRIBUTE DISCOUNT ID, DATA TYPE INTEGER, PRIMARY KEY
DiscountName VARCHAR(100) NOT NULL,                           # ATTRIBUTE DISCOUNT NAME, DATA TYPE AS 100 VARIABLE CHARACTERS, NOT NULL
DiscountPercentage INTEGER NOT NULL                           # ATTRIBUTE DISCOUNT PERCENTAGE, DATA TYPE AS AN INTEGER, NOT NULL
);              
               """)
db.commit()                                                   # COMMITTING IT TO THE DATABASE



# Table with payment details

cursor.execute("""                                            
CREATE TABLE IF NOT EXISTS tblPaymentDetails(                  # CREATING THE TABLE FOR TBL PAYMENT DETAILS
PaymentDetailsID INTEGER PRIMARY KEY,                          # ATTRIBUTE PAYMENT DETAILS ID AS DATA TYPE INTEGER AS A PRIMARY KEY
PaymentChoice VARCHAR(100) NOT NULL,                           # ATTRIBUTE PAYMENT CHOICE IS DATA TYPE 100 VARIABLE CHARACTERS, NOT NULL
CardNumber INTEGER NOT NULL,                                   # ATTRIBUTE CARD NUMBER, DATA TYPE AS INTEGER, NOT NULL
PostCode VARCHAR(100) NOT NULL,                                # ATTRIBUTE POST CODE, DATA TYPE AS 100 VARIABLE CHARACTERS, NOT NULL
ExpirationDate VARCHAR(100) NOT NULL                           # ATTRIBUTE EXPIRATION DATE, DATA TYPE AS 100 VARIABLE CHARACTERS, NOT NULL
);               
               """)
db.commit()                                                    # COMMITTING IT TO THE DATABASE



# Table with financial information

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblFinancialDetails(                                  # CREATING THE TABLE FOR TBL FINANCIAL DETAILS
PurchaseID INTEGER PRIMARY KEY,                                                  # PURCHASE ID AS AN ATTRIBUTE, DATA TYPE IS AN INTEGER, PRIMARY KEY
PaymentDetailsID INTEGER AUTO_INCREMENT,                                         # PAYMENT DETAILS ID AS AN INTEGER FOR THEIR DATA TYPE, AUTO INCREMENT ENABLED
TotalRevenue FLOAT NOT NULL,                                                     # ATTRIBUTE TOTAL REVENUE, DATA TYPE AS A FLOAT, NOT NULL
VAT FLOAT NOT NULL,                                                              # ATTRIBUTE VAT, DATA TYPE AS FLOAT, NOT NULL
ShippingCosts FLOAT NOT NULL,                                                    # ATTRIBUTE SHIPPING COSTS, DATA TYPE AS FLOAT, NOT NULL
SalesCosts FLOAT NOT NULL,                                                       # ATTRIBUTE SALES COSTS, DATA TYPE AS FLOAT, NOT NULL
UnitsSold INT NOT NULL,                                                          # ATTRIBUTE UNITS SOLD, DATA TYPE AS AN INTEGER, NOT NULL
TheRiceMachine INT,                                                              # ATTRIBUTE THE RICE MACHINE, DATA TYPE AS AN INTEGER
TheBuffalo INT,                                                                  # ATTRIBUTE THE BUFFALO, DATA TYPE AS AN INTEGER
TheUncleJohn INT,                                                                # ATTRIBUTE THE UNCLE JOHN, DATA TYPE AS AN INTEGER
RiceAndDice INT,                                                                 # ATTRIBUTE RICE AND DICE, DATA TYPE AS AN INTEGER
TheBasmatiBoiler INT,                                                            # ATTRIBUTE THE BASMATI BOILER, DATA TYPE AS AN INTEGER
RiceCooker3000 INT,                                                              # ATTRIBUTE RICE COOKER 3000, DATA TYPE AS AN INTEGER
FOREIGN KEY (PaymentDetailsID) REFERENCES tblPaymentDetails(PaymentDetailsID)    # FOREIGN KEY REFERENCES TO TBL PAYMENT DETAILS WITH PAYMENTDETAILSID, SO THE 
);                                                                               # INFORMATION ABOUT THE USER AND THE PAYMENT USED IS LINKED TO THE ACTUAL COSTS
               """)
db.commit()                                                                      # COMMITTING IT TO THE DATABASE


