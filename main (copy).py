# [===] THE LIBRARIES [===] #
from flask import Flask, redirect, url_for, render_template, request, session  # IMPORTING ALL NECESSARY LIBRARIES TO BE USED
from datetime import timedelta
import sqlite3
import re
import smtplib

gmail_user = 'REDACTED'
gmail_password = 'REDACTED'
  
# [===] [===] #

#with sqlite3.connect("NewRiceCookerDatabase.db") as db:
#  cursor=db.cursor()

# [===] THE DATABASE [===] #
db = sqlite3.connect("NewRiceCookerDatabase.db", check_same_thread=False)
cursor = db.cursor()  # CONNECTING THE DATABASE AND CREATING A CURSOR TO PERFORM SQL WITH SQLITE
# [===] [===] #

# [===] FLASK SERVER [===] #
app = Flask(__name__)                                # CREATING THE APP FLASK
app.secret_key = "secretkey"                         # CREATING THE SECRET KEY
app.permanent_session_lifetime = timedelta(days=2)   # ALL SESSION DATA WILL LAST UP TO 2 DAYS UNLESS STATED OTHERWISE
# [===] [===] #

# [===] HOME PAGE [===] #
@app.route("/", methods=["POST", "GET"])            # ENABLES POST AND GET REQUESTS
def HomePage():                                     # SUBROUTINE FOR THE HOMEPAGE

  # THE FOLLOWING CODE IS TO GO THROUGH THE TABLE WITH ALL OF THE PRODUCT INFORMATION TO BE ABLE TO PUT IT ON THE FRONTEND

  cursor.execute("SELECT ProductName, ProductPrice, ProductShipping FROM tblProducts WHERE ProductID=1")
  # USING SQL, IT'S POSSIBLE TO GET THE PRODUCT NAME, PRICE AND THE COST OF SHIPPING FOR WHEN PRODUCT ID IS 1
  for x in cursor.fetchall():
    Product1Details = x
  # CONSEQUENTLY, USING A FOR LOOP, WE'RE ABLE TO PUT ALL OF THIS INFORMATION TO VARIABLE PRODUCT1DETAILS FOR THE TIME BEING, AS AN ARRAY

  cursor.execute("SELECT ProductName, ProductPrice, ProductShipping FROM tblProducts WHERE ProductID=2")
  # SQL SELECT STATEMENT ONCE AGAIN TO GET THE PRODUCT NAME, PRICE AND COST OF SHIPPING FOR PRODUCT ID 2
  for x in cursor.fetchall():
    Product2Details = x
  # USING A FOR LOOP TO GO THROUGH ALL OF THE DETAILS OF PRODUCT ID 2 AND PUT IT INTO THE ARRAY PRODUCT2DETAILS

  cursor.execute("SELECT ProductName, ProductPrice, ProductShipping FROM tblProducts WHERE ProductID=3")
  # SQL SELECT STATEMENT TO GET THE PRODUCT NAME, PRICE AND COST OF SHIPPING FOR WHEN PRODUCT ID IS 3
  for x in cursor.fetchall():
    Product3Details = x
  # USING A FOR LOOP TO GO THROUGH ALL OF THE INFORMATION SELECTED AND APPEND IT INTO THE ARRAY PRODUCT3DETAILS

  cursor.execute("SELECT ProductName, ProductPrice, ProductShipping FROM tblProducts WHERE ProductID=4")
  # SQL SELECT STATEMENT TO GET THE PRODUCT NAME, PRICE AND COST OF SHIPPING FOR PRODUCT ID 4
  for x in cursor.fetchall():
    Product4Details = x
  # USING A FOR LOOP TO GO THROUGH ALL OF THE INFORMATION OF PRODUCT ID 4 AND APPEND IT TO THE ARRAY PRODUCT4DETAILS

  cursor.execute("SELECT ProductName, ProductPrice, ProductShipping FROM tblProducts WHERE ProductID=5")
  # SQL SELECT STATEMENT TO GO GET PRODUCT ID 5 NAME, PRICE AND COST OF SHIPPING FROM THE TABLE PRODUCTS
  for x in cursor.fetchall():
    Product5Details = x
  # USING A FOR LOOP TO GO THROUGH ALL OF THE INFORMATION OF PRODUCT ID 5 AND PUT IT INTO THE ARRAY PRODUCT 5 DETAILS FOR LATER USE

  cursor.execute("SELECT ProductName, ProductPrice, ProductShipping FROM tblProducts WHERE ProductID=6")
  # SQL SELECT STATEMENT FOR PRODUCT ID 6 TO GET THEIR NAME, PRICE AND COST OF SHIPPING
  for x in cursor.fetchall():
    Product6Details = x
  # AND THEN USING THE FOR LOOP TO GO THROUGH ALL OF THE INFORMATION OF PRODUCT 6 AND PUT IT INTO THE ARRAY PRODUCT 6 DETAILS

  # CONSEQUENTLY, THE FOLLOWING CODE IS TO GET THE INFORMATION OUT OF THEIR ARRAY FORM, INTO NAME, PRICE AND SHIPPING FOR THE FRONTEND

  ProductName1 = Product1Details[0] # PRODUCT 1 GET IT'S NAME BY GOING THROUGH THE ARRAY AND IT'S FIRST ELEMENT AKA 0
  ProductPrice1 = Product1Details[1] # PRODUCT 1 GET IT'S PRICE BY GOING THROUGH THE ARRAY AND THE 2ND ELEMENT, AKA 1
  if Product1Details[2] == 0: # THIS USING A IF STATEMENT GO THROUGH PRODUCT 1 COST OF SHIPPING, IF IT'S 0, IT'S ASSIGNED AS FREE INSTEAD OF A NUMBER
    ProductShipping1 = "Free"
  else: # ELSE, THAN PRODUCT 1 COST OF SHIPPING SHALL BE ASSIGNED TO IT'S RIGHTFUL INTEGER
    ProductShipping1 = Product1Details[2]
    ProductShipping1 = str(ProductShipping1)
    ProductShipping1 = ("£" + ProductShipping1)

  ProductName2 = Product2Details[0] # THIS IS PRODUCT 2 GETTING ITS NAME FROM THE ARRAY THROUGH INDEXING THE 1ST ELEMENT WHICH IS 0
  ProductPrice2 = Product2Details[1] # THIS IS PRODUCT 2 GETTING ITS PRICE FROM THE ARRAY THROUGH INDEXING THE 2ND ELEMENT WHICH IS 1
  if Product2Details[2] == 0: # THIS IS PRODUCT 2 GETTING IT'S COST OF SHIPPING, IF IT'S EQUAL TO 0 THAN IT'S ASSIGNED AS FREE
    ProductShipping2 = "Free"
  else: # ELSE THAN WE GIVE PRODUCT 2 IT'S RIGHTFUL COST OF SHIPPING NUMBER
    ProductShipping2 = Product2Details[2]
    ProductShipping2 = str(ProductShipping2)
    ProductShipping2 = ("£" + ProductShipping2)

  ProductName3 = Product3Details[0] # THIS IS PRODUCT 3 GETTING ITS NAME FROM THE ARRAY THROUGH INDEXING THE 1ST ELEMENT WHICH IS 0
  ProductPrice3 = Product3Details[1] # THIS IS PRODUCT 3 GETTING ITS PRICE FROM THE ARRAY THROUGH INDEXING THE 2ND ELEMENT WHICH IS 1
  if Product3Details[2] == 0: # THIS IS PRODUCT 3 GETTING ITS COST OF SHIPPING, IF ITS EQUAL TO 0, THAN WE CAN ASSUME IT'S FREE
    ProductShipping3 = "Free"
  else: # ELSE THAN WE GO THROUGH THE ARRAY USING INDEX NUMBER 2 WHICH IS THE 3RD ELEMENT, WHICH IS THE PRODUCT'S COST OF SHIPPING
    ProductShipping3 = Product3Details[2]
    ProductShipping3 = str(ProductShipping3)
    ProductShipping3 = ("£" + ProductShipping3)

  ProductName4 = Product4Details[0] # THIS IS PRODUCT 4 GETTING ITS NAME FROM THE ARRAY THROUGH INDEXING THE 1ST ELEMENT WHICH IS 0
  ProductPrice4 = Product4Details[1] # THIS IS PRODUCT 4 GETTING ITS PRICE FROM THE ARRAY THROUGH INDEXING THE 2ND ELEMENT WHICH IS 1
  if Product4Details[2] == 0: # THIS IS PRODUCT 4 GETTING ITS COST OF SHIPPING, IF THE COST OF SHIPPING IS 0 THAN WE CAN ASSUME ITS FREE
    ProductShipping4 = "Free"
  else: # ELSE THAN THE COST OF SHIPPING FOR PRODUCT 4 IS ASSIGNED THROUGH THE ARRAY BY INDEX 2
    ProductShipping4 = Product4Details[2]
    ProductShipping4 = str(ProductShipping4)
    ProductShipping4 = ("£" + ProductShipping4)

  ProductName5 = Product5Details[0] # THIS IS PRODUCT 5 GETTING ITS NAME FROM THE ARRAY THROUGH INDEXING THE 1ST ELEMENT WHICH IS 0
  ProductPrice5 = Product5Details[1] # THIS IS PRODUCT 5 GETTING ITS PRICE FROM THE ARRAY THROUGH INDEXING THE 2ND ELEMENT WHICH IS 1
  if Product5Details[2] == 0: # THIS IS PRODUCT 5 GETTING ITS COST OF SHIPPING FROM THE ARRAY, IF ITS EQUAL TO 0, WE CAN ASSUME ITS FREE
    ProductShipping5 = "Free"
  else: # ELSE THAN THE COST OF SHIPPING FOR PRODUCT 5 IS ASSIGNED THROUGH THE ARRAY 3RD ELEMENT, WHICH IS INDEX 2
    ProductShipping5 = Product5Details[2]
    ProductShipping5 = str(ProductShipping5)
    ProductShipping5 = ("£" + ProductShipping5)

  ProductName6 = Product6Details[0] # THIS IS PRODUCT 6 GETTING ITS NAME FROM THE ARRAY THROUGH INDEXING THE 1ST ELEMENT WHICH IS 0
  ProductPrice6 = Product6Details[1] # THIS IS PRODUCT 6 GETTING ITS PRICE FROM THE ARRAY THROUGH INDEXING THE 2ND ELEMENT WHICH IS 1
  if Product6Details[2] == 0: # THIS IS PRODUCT 6 COST OF SHIPPING, IF ITS EQUAL TO 0 THAN WE CAN ASSUME ITS FREE
    ProductShipping6 = "Free"
  else: # ELSE THAN THE COST OF SHIPPING FOR PRODUCT 6 IS THE 3RD ELEMENT OF THE ARRAY, WHICH IS INDEX 2
    ProductShipping6 = Product6Details[2]
    ProductShipping6 = str(ProductShipping6)
    ProductShipping6 = ("£" + ProductShipping6)

  # TO BE ABLE TO PUT THE PRODUCT PRICE OF EACH PRODUCTS ONTO THE FRONTEND, WE DATA CAST CONVERT THEIR TYPE INTO A STRING, WHICH SHALL ALLOW US TO HTTP REQUEST THE HOMEPAGE TO THE FRONTEND, WITH THE PRICES OF THE PRODUCTS
  ProductPrice1 = str(ProductPrice1)
  ProductPrice1 = ("£" + ProductPrice1)
  ProductPrice2 = str(ProductPrice2)
  ProductPrice2 = ("£" + ProductPrice2)
  ProductPrice3 = str(ProductPrice3)
  ProductPrice3 = ("£" + ProductPrice3)
  ProductPrice4 = str(ProductPrice4)
  ProductPrice4 = ("£" + ProductPrice4)
  ProductPrice5 = str(ProductPrice5)
  ProductPrice5 = ("£" + ProductPrice5)
  ProductPrice6 = str(ProductPrice6) 
  ProductPrice6 = ("£" + ProductPrice6)

  # AFTER GETTING ALL OF THE DATA NECESSARY FOR THE HOME PAGE, WHICH IS THE PRODUCTS PRICE, COST OF SHIPPING AND THEIR NAME, WE'RE ABLE TO HTTP RESPOND BACK THE HOME PAGE TO THE FRONTEND FOR THE USER, USING HTML VARIABLES TO BE ABLE TO SHOW THE USER THE 3 KEY PIECES OF INFORMATION OF EACH PRODUCT TO THE FRONTEND

  return render_template("HomePage.html", ProductPrice1=ProductPrice1, ProductPrice2=ProductPrice2, ProductPrice3=ProductPrice3, ProductPrice4=ProductPrice4, ProductPrice5=ProductPrice5, ProductPrice6=ProductPrice6, ProductName1=ProductName1, ProductName2=ProductName2, ProductName3=ProductName3, ProductName4=ProductName4, ProductName5=ProductName5, ProductName6=ProductName6, ProductShipping1=ProductShipping1, ProductShipping2=ProductShipping2, ProductShipping3=ProductShipping3, ProductShipping4=ProductShipping4, ProductShipping5=ProductShipping5, ProductShipping6=ProductShipping6)           # BACKEND SENDS THE HOMEPAGE
# [===] [===] #

# [===] ABOUT US PAGE [===] #
@app.route("/AboutUs", methods=["POST", "GET"])    # ENABLES POST AND GET REQUESTS
def AboutUs():                                     # SUBROUTINE FOR THE ABOUT US PAGE
  return render_template("AboutUs.html")           # BACKEND SENDS THE ABOUT US PAGE
# [===] [===] #

# [===] SIGN UP PAGE [===] #
@app.route("/Account", methods=["POST", "GET"])    # ENABLES POST AND GET REQUESTS
def Account():                                     # SUBROUTINE FOR THE ACCOUNT PAGE
  if "Username" in session and "Password" in session and "Email" in session: # IN CASE USER IS ALREADY LOGGED IN
    return redirect(url_for("LogOut"))                                       # GET SENT TO THE LOGOUT PAGE INSTEAD
    
  elif request.method == "POST":             # IF USER IS TRYING TO SEND DATA TO THE SERVER
    Username = request.form["USERNAME"]      # WE RECEIVE THE USERNAME, EMAIL AND PASSWORD FROM THE FRONTEND 
    Email = request.form["EMAIL"]
    Password = request.form["PASSWORD"]
    
    PasswordVerify = False                   # USED AS A LOCAL VARIABLE TO CHANGE WHEN VERIFYING THE USER'S PASSWORD
    
    try:                                     # TRY AND EXCEPT CLAUSE IN CASE THINGS DOESN'T WORK OUT
      for x in Username:                     # FOR LOOP THROUGHOUT THE USERNAME TO FIND SPACES OR EMPTINESS AND REMOVE IT
        if x == "" or x == " ":
          Username.remove(x)
    
    except:
      pass                                   # ELSE PASS
  
    UsernameCount = len(Username)            # KEEP A COUNT OF HOW LONG THE USERNAME IS WITHOUT SPACES
    
    pattern = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'  # PATTERN TO VERIFY THE USER'S EMAIL
    
    if (re.search(pattern, Email)):  # IF THEIR EMAIL IS CORRECT ACCORDING TO THE PATTERN, THEY CAN CONTINUE
      pass
    else: # ELSE THE ACCOUNT PAGE IS SENT FROM THE BACKEND WITH AN ERROR MESSAGE REGARDING THEIR EMAIL
      return render_template("Account.html", ErrorMessage="You need to input a legitimate email.")   
    
    try: # TRY AND EXCEPT CLAUSE IN CASE ANYTHING GOES WRONG
      for x in Password: # GOES THROUGH ALL OF THE CHARACTERS IN THE PASSWORD AND IF THERE'S ANY SPACES/NULL ELEMENTS, PASSWORD VERIFY IS TRUE
        if x == "" or x == " ":
          PasswordVerify = True
    
    except: # ELSE IT SHALL STAY AS FALSE
      PasswordVerify = False
    
    if UsernameCount < 8:      # AFTER REMOVING ANY POSSIBLE SPACES WITHIN THE USERNAME, THIS IS TO CHECK THAT THE USERNAME IS LESS THAN 8 CHARACTERS LONG OR NOT
      Needed = 8 - UsernameCount # CONSEQUENTLY, WE CAN FIND THEIR ACTUAL COUNT AND TAKE IT AWAY FROM 8
      Needed = str(Needed) # TO THEN MAKE THE CHARACTERS THEY ARE SHORT OF, INTO A STRING
      return render_template("Account.html", ErrorMessage="Your username is " + Needed + " characters short.")
      # TO BE ABLE TO RETURN THE HTML PAGE WITH THE ERROR MESSAGE, NOTIFYING THAT THE USER'S USERNAME IS X AMOUNT OF CHARACTERS SHORT
    
    elif PasswordVerify == True: # ELSE, IF THE USERNAME IS MORE THAN 8 CHARACTERS LONG
      return render_template("Account.html", ErrorMessage="Spaces aren't allowed within the password.")
      # IT'LL HTTP RESPOND BACK THE ACCOUNT HTML PAGE NOTIFYING THE USER THAT SPACES AREN'T ALLOWED WITHIN THE PASSWORD
    
    else:   # AFTER CHECKING IF THE PASSWORD AND USERNAME FITS THE REQUIREMENTS, THIS ALGORITHM IS THEN USED TO CHECK THEIR EMAIL
      EmailCount = 0 # AN COUNT OF HOW MANY TIMES THE EMAIL HAS BEEN USED FOR AN ACCOUNT IS A CONSTANT OF 0
    
      cursor.execute("SELECT Email FROM tblUsers WHERE Email = ?", (Email,))
      # IT GOES THROUGH THE USER TABLE TO SEE IF THE EMAIL HAS BEEN USED BEFORE OR NOT
      for x in cursor.fetchall():
        EmailCount += 1

        # IF IT HAS BEEN USED BEFORE, THAN WE KNOW THAT THE USER CANNOT MAKE/SIGN UP ANOTHER ACCOUNT AGAIN, AS THE EMAIL IS BEING USED
        # SO EMAIL COUNT IS INCREMENTED
    
      if EmailCount == 0: # IF THE EMAIL WASN'T USED, THAN EMAIL COUNT STAYS AS 0
        cursor.execute("INSERT INTO tblUsers (Username, Email, Password) VALUES (?, ?, ?)", (Username, Email, Password))
        # THIS ENSURES THAT THE EMAIL HASN'T BEEN USED BEFORE TO CREATE AN ACCOUNT, AND THUS, WILL UPDATE THE USER TABLE ABOUT THE NEW ACCOUNT CREATED
        db.commit()
        # WITH THE COMMIT COMMAND TO ENSURE TO SAVE THE UPDATE OF DATA INTO THE TABLE

        session.permanent = True
        session["Username"] = Username
        session["Email"] = Email
        session["Password"] = Password

        # AS THE USER HAS NOW SUCCESSFULLY SIGNED UP AND MADE AN ACCOUNT, ALL SESSION DATA IS NOW TURNED ON
        # THIS IS SO WHEN THEY NAVIGATE THROUGHOUT THE WEBSITE, THEY WON'T BE REQUIRED TO LOGIN INTO THEIR ACCOUNT, THAT THEY JUST MADE
        
        return redirect(url_for("HomePage"))
        # WITH IT SENDING THEM BACK TO THE HOME PAGE, AFTER THEY'VE FINISHED CREATING AN ACCOUNT
    
      elif EmailCount > 0:
        return render_template("Account.html", ErrorMessage="This email has already been used.")
        # ELSE IF THE EMAIL HAS BEEN USED BEFORE, THAN WE SEND BACK THE ACCOUNT HTML PAGE, NOTIFYING THEM THAT THE EMAIL HAS BEEN USED
        # AND THEIR SIGN UP PROCESS HAS FAILED

  else:
    return render_template("Account.html")
    # ELSE, IF NO DATA WAS SENT TO THE SERVER, THAN IT'LL JUST SEND THE ACCOUNT/SIGN UP PAGE, FOR THE USER TO UTILISE
# [===] [===] #

# [===] LOGIN PAGE [===] #
@app.route("/Login", methods=["POST", "GET"]) # THIS IS TO MAKE THE LOGIN PAGE TO BE ABLE TO ACCEPT BOTH POST AND GET REQUESTS
def Login():
  if "Username" in session and "Password" in session and "Email" in session: # INCASE THE USER IS ALREADY LOGGED IN USING SESSION DATA, 
    return redirect(url_for("LogOut")) # WE'LL JUST SEND THEM TO THE LOGOUT PAGE AS THEY'RE ALREADY LOGGED IN
    
  elif request.method == "POST": # ELSE, THAN WE'LL USE THE POST REQUEST METHOD TO TAKE IN THEIR LOGIN DETAILS
    Username = request.form["USERNAME"] # THESE LINES OF CODE WILL BE ABLE TO TAKE THE HTML VARIABLE INTO A PYTHON VARIABLE AND GO THROUGH A VERIFICATION PROCESS
    Email = request.form["EMAIL"]
    Password = request.form["PASSWORD"]

    PasswordVerify = False # THIS IS A CONSTANT TO USE LATER ON WHEN CHECKING FOR THE AUTHENTICATION OF THE USER PASSWORD

    try: # TRY AND EXCEPT CLAUSE IN CASE ANYTHING DOESN'T WORK
      for x in Username: # WE'LL GO THROUGH THE USERNAME AND REMOVE ANY SPACES OR NULL ELEMENTS INSIDE OF IT
        if x == "" or x == " ": # UTILISING THE IF AND REMOVE STATEMENTS
          Username.remove(x)

    except: # IF THE USERNAME HAS NO SPACES OR NULL ELEMENT, THAN WE'LL PASS
      pass

    UsernameCount = len(Username) # WE THEN CHECK THE LENGTH OF THE USERNAME, JUST TO ENSURE THAT THE USER TYPED IN AN USERNAME

    pattern = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$' # FOR REGULAR EXPRESSIONS, THIS PATTERN IS USED TO ENSURE THE EMAIL ADDRESS IS LEGIT

    if (re.search(pattern, Email)): # WE'LL CHECK IF THE EMAIL ADDRESS IS LEGIT, IF IT IS, THAN PASS
      pass
    else: # ELSE, THAN HTTP RESPOND BACK THE LOGIN PAGE WITH THE ERROR MESSAGE THAT THEY NEED A LEGIT EMAIL
      return render_template("Login.html", ErrorMessage="You need to input a legitimate email.")   

    try: # TRY AND EXCEPT CLAUSE IN CASE ANYTHING BREAKS
      for x in Password: # GOING THROUGH THE PASSWORD AND FINDING FOR ANY SPACES/NULL ELEMENTS TO REMOVE, TO ENSURE THEY PUT IN A PASSWORD
        if x == "" or x == " ":
          PasswordVerify = True # IF THERE ARE NULL/SPACE ELEMENTS, WE CAN TELL THEY DIDN'T PUT A PROPER PASSWORD IN AS IT DOESN'T ALLOW SPACES/NULL ELEMENTS
            # CONSEQUENTLY THE CONSTANT IS SET TO TRUE, TO BE USED IN LATER USAGE
    except:
      PasswordVerify = False # ELSE, THE CONSTANT STAYS AS FALSE AND THE VERIFICATION PROCESS CONTINUES

    if UsernameCount < 8: # IF IT DOES TURNS OUT THAT THE USERNAME IS SHORTER THAN 8 CHARACTERS, WE FIND OUT THE NUMBER OF CHARACTERS THEY'RE SHORT OF
      Needed = 8 - UsernameCount
      Needed = str(Needed) # DATA CAST TYPE CONVERT IT INTO A STRING TO HTTP RESPOND BACK THE LOGIN PAGE, WITH ERROR MESSAGE SAYING THEY'RE X SHORT CHARACTERS
      return render_template("Login.html", ErrorMessage="Your username is " + Needed + " characters short.")

    elif PasswordVerify == True: # ELSE IF PASSWORD CONSTANT IS TRUE, THAN IT'LL HTTP RESPOND BACK THE LOGIN PAGE, STATING SPACES AREN'T ALLOWED IN THE PASSWORD
      # AS AN ERROR MESSAGE
      return render_template("Login.html", ErrorMessage="Spaces aren't allowed within the password.")

    else: # AS ALL OF THE DATA INPUTS ARE CORRECT, IT'S NOW CHECKING TO SEE IF THEIR DETAILS ARE CORRECT FOR THE USER ACCOUNT
      CorrectCount = 0 # THIS IS A CONSTANT TO SEE IF THERE'S AN ACCOUNT
      cursor.execute("SELECT * FROM tblUsers WHERE Email = ? AND Username = ? AND Password = ?", (Email, Username, Password,))
      for x in cursor.fetchall(): # SQL STATEMENT TO CHECK THE USER TABLE IF THE DETAILS MATCHES ANY ACCOUNTS
        CorrectCount += 1 # IF THE DETAILS DID MATCH, THAN CORRECT COUNT WOULD ONLY INCREMENT ONCE, ELSE SOMETHING IS WRONG

      if CorrectCount == 1: # IF CORRECT COUNT IS 1, THAN SESSION DATA IS TURNED ON WITH THE SPECIFIC AND RELEVANT LOGIN DETAILS

        session.permanent = True
        session["Username"] = Username
        session["Email"] = Email
        session["Password"] = Password
        
        return redirect(url_for("HomePage")) # USER IS NOW LOGGED IN, IN SESSION DATA AND IS HTTP RESPONDED BACK TO THE HOME PAGE

      else: # IF NOT, THAN THE USER HAS TYPED IN THE WRONG LOGIN DETAILS, AND WILL BE HTTP RESPONDED BACK THE LOGIN PAGE WITH ERROR MESSAGE ACCOUNT DETAILS ARE WRONG
        return render_template("Login.html", ErrorMessage="Account details are wrong.")
  
  else:
    return render_template("Login.html") # IF THE USER DOESN'T TRY TO LOG IN OR ISN'T IN SESSION DATA, THEY'LL JUST BE HTTP RESPONDED THE LOGIN PAGE
# [===] [===] #

# [===] LOGOUT PAGE [===] #
@app.route("/LogOut", methods=["POST", "GET"])  # THIS IS THE LOGOUT PAGE, WHICH ALLOWS BOTH POST AND GET REQUESTS FROM THE USER
def LogOut(): # THIS IS THE SUBROUTINE ESTABLISHING THE LOGOUT PAGE
  Username = session.get("Username") # IF THE USER IS IN SESSION DATA, THAN WE'LL GET THEIR USERNAME AND HTTP SEND BACK THE LOGOUT PAGE WITH THEIR NAME
  return render_template("LogOut.html", USERNAME=Username)
# [===] [===] #

# [===] LOGGING OUT [===] #  
@app.route("/ActuallyLoggedOut", methods=["POST", "GET"]) # THIS IS THE PROCESS OF THE USER LOGGING OUT THROUGH A GET REQUEST
def ActuallyLoggedOut(): # USING THIS SUBROUTINE TO BE ABLE TO FORWARD THE PROCESSES OF LOGGING OUT
  session.pop("Username", None) # THIS IS BY REMOVING ALL SESSION DATA SO THE USER IS FULLY LOGGED OUT
  session.pop("Email", None)
  session.pop("Password", None)

  return redirect(url_for("Account")) # THAN THEY'LL BE HTTP RESPONDED BACK THE SIGN UP PAGE
# [===] [===] #

# [===] INSIGHTS AND RECIPES [===] #
@app.route("/InsightsAndRecipes", methods=["POST", "GET"]) # THIS IS THE INSIGHTS AND RECIPES PAGE, WITH POST AND GET REQUESTS ENABLED
def InsightsAndRecipes():

  cursor.execute("SELECT PostID FROM tblInsightsAndRecipes") # FIRST, IT'LL GET THE POST ID, IT'LL GO THROUGH EVERYTHING SO THE FINAL POSTID IS THE RECENT POST
  for x in cursor.fetchall():
    PostNumber = x # WITH THE RECENT POST NUMBER BEING ASSIGNED TO THIS VARIABLE

  cursor.execute("SELECT Title FROM tblInsightsAndRecipes WHERE PostID=?", (PostNumber))
  for x in cursor.fetchall(): # CONSEQUENTLY, WE CAN USE THIS POST ID TO FIND THE RECENT POST TITLE BY SQL SELECT STATEMENTS
    Title = x # ASSIGNING THE TITLE TO THIS VARIABLE TO USED ON LATER

  cursor.execute("SELECT Content FROM tblInsightsAndRecipes WHERE PostID=?", (PostNumber))
  for x in cursor.fetchall(): # USING SQL SELECT STATEMENTS, WE CAN FIND THE RECENT POST CONTENT AS WELL
    Paragraph = x # ASSIGNING THE CONTENT TO THIS VARIABLE TO USED ON LATER

  # THE FOLLOWING CODE IS TO REMOVE THE BRACKETS, COMMAS AND QUOTATION MARKS THAT THE VARIABLES ARE IN DUE TO BEING IN A SQL TABLE
  TitleArray = [] # FIRST CREATING AN ARRAY TO STORE THE TITLE IN
  for i in Title: # WE GO THROUGH EVERYTHING IN THE TITLE TO REMOVE THE FOLLOWING ELEMENTS INSIDE OF IT
    if i == "(" or i == ")" or i == "," or i == "'":
      pass # BY SIMPLY PREVENTING IT BEING ADDED TO THE TITLE ARRAY

    else: # AND THE ACTUAL TITLE IS THEN PUT IN TITLE ARRAY, TO USE AS A TEMPORARY MEMORY LOCATION, THROUGH THE APPEND COMMAND
      TitleArray.append(i)
        
  Title = ("".join(TitleArray)) # AS A RESULT, EVERYTHING IN THE ARRAY IS JOINED TOGETHER, TO GET THE TITLE WHILST REMOVING THE SQL FORMAT IT WAS IN

  ParagraphArray = [] # A SIMILAR PROCESS FOR THE ACTUAL CONTENT, WHERE AN ARRAY IS SET UP AS A TEMPORARY MEMORY LOCATION
  for i in Paragraph: # GOING THROUGH EVERYTHING IN THE CONTENT TO AVOID APPENDING THESE ELEMENTS INTO THE ARRAY, TO REMOVE THE SQL FORMAT
    if i == "(" or i == ")" or i == "," or i == "'":
      pass

    else: # WITH THE ACTUAL CONTENT BEING APPENDED TO THIS TEMPORARY MEMORY LOCATION
      ParagraphArray.append(i)

  Paragraph = ("".join(ParagraphArray)) # THAN JOINING ALL OF THE ELEMENTS TOGETHER TO BRING BACK THE CONTENT IN IT'S ORIGINAL STATE WITHOUT THE SQL FORMAT

  PostNumber = str(PostNumber) # THIS IS DATA TYPE CONVERTING THE POST NUMBER TO A STRING TO SHOW IT ON THE FRONTEND, AND TO REMOVE IT'S SQL FORMAT
  
  PostNumberArray = [] # AN ARRAY IS ESTABLISHED AS A TEMPORARY MEMORY LOCATION
  for i in PostNumber: # ANYTHING IN THE POST ID THAT IS PART OF THE SQL FORMAT IS PREVENTED TO BE ADDED IN TO THE ARRAY
    if i == "(" or i == ")" or i == "," or i == "'":
      pass

    else: # THE ACTUAL POST ID CONTENT IS APPENDED TO THE ARRAY
      PostNumberArray.append(i)

  PostNumber = ("".join(PostNumberArray)) # CONTENT OF THE ARRAY IS JOINED TOGETHER TO CONVEY THE ACTUAL POSTID
  global CurrentPostCount # GLOBALISING THIS VARIABLE SINCE WE'RE CHANGING IT
  CurrentPostCount = int(PostNumber) # CURRENT POST IS THE POST NUMBER, SO WHEN MOVING TO OLDER/RECENT POSTS, WE KNOW THIS IS WHERE WE ARE IN THE ORDER
  global MaxPosts # THIS IS ALSO TO GLOBALISE THE VARIABLE OF HOW MANY POSTS THERE ARE, SO THE WEBSITE CAN'T GET ANYTHING OLDER THAN X POST
  MaxPosts = int(PostNumber) # ENSURING THAT IT'S AN INTEGER

  return render_template("InsightsAndRecipes.html", TITLE=Title, PARAGRAPH=Paragraph, POSTNUMBER=PostNumber)
  # AFTER THAT IS DONE, IT HTTP RESPONDS BACK THE INSIGHTS AND RECIPES PAGE WITH THE TITLE, PARAGRAPH AND POSTNUMBER OF THE CURRENT LATEST POST
# [===] [===] #

# [===] INSIGHTS AND RECIPES OLD [===] #
@app.route("/InsightsAndRecipesOld", methods=["POST", "GET"]) # THIS IS WHERE THE USER IS SENT WHEN THEY TRY TO GET TO AN OLDER POST
def InsightsAndRecipesOld(): # WITH THE SUBROUTINE BEING THE CODE TO MOVE TO THE OLDEST POST (DECREMENTING)
  global CurrentPostCount # FIRST GLOBALISING THE CURRENT POST COUNT AS WE'RE NOW ON A NEW POST

  if CurrentPostCount == 1: # IF CURRENT POST COUNT IS 1, MEANS THAT WE'RE ALREADY ON THE OLDEST POST AND DON'T NEED TO MOVE
    pass # SO JUST PAST

  else: # IF WE'RE NOT ALREADY ON THE OLDEST POST, THAN WE JUST DECREMENT IT TO GET TO THE NEXT OLDEST POST
    CurrentPostCount -= 1
  
  CurrentPostCount = str(CurrentPostCount) # AS SUCH THE NEW CURRENT POST NUMBER IS A STRING FOR LATER USE
  PostNumber = CurrentPostCount # THE POST NUMBER IS THE CURRENT POST COUNT, AKA THE NEXT OLD POST WE'RE ON
  CurrentPostCount = int(CurrentPostCount) # WHICH IS THEN BACK TO AN INTEGER FOR LATER USE

  cursor.execute("SELECT Title FROM tblInsightsAndRecipes WHERE PostID=?", (PostNumber))
  for x in cursor.fetchall(): # AS A RESULT, WE USE THE POST NUMBER TO FIND THE TITLE OF THE OLDER POST, THROUGH SQL SELECT STATEMENT
    Title = x # THIS IS THE OLDER POST TITLE

  cursor.execute("SELECT Content FROM tblInsightsAndRecipes WHERE PostID=?", (PostNumber))
  for x in cursor.fetchall(): # USING HTE POST NUMBER TO FIND THE CONTENT OF THE OLDER POST, THROUGH SQL SELECT STATEMENT
    Paragraph = x # WITH THE OLDER POST CONTENT BEING STORED TO THIS VARIABLE

  TitleArray = [] # THIS IS A TEMPORARY MEMORY LOCATION TO STORE THE TITLE IN WHEN TRYING TO REMOVE IT FROM IT'S SQL FORMAT
  for i in Title: # GOING THROUGH ALL OF THE ELEMENTS IN THE TITLE TO PREVENT THE SQL FORMAT BEING ADDED INTO THE TEMPORARY MEMORY LOCATION
    if i == "(" or i == ")" or i == "," or i == "'":
      pass # ACCOMPLISHING IT WITH A PASS

    else: # HOWEVER, IF IT IS PART OF THE TITLE, IT'S APPENDED TO THE TEMPORAY MEMORY LOCATION
      TitleArray.append(i)
        
  Title = ("".join(TitleArray)) # WITH ALL OF THE ARRAY'S ELEMENTS BEING JOINED TOGETHER TO FORM AS A THE TITLE

  ParagraphArray = [] # TEMPORARY MEMORY LOCATION TO STORE THE PARAGRAPH IN WHEN TRYING TO REMOVE IT FROM IT'S SQL FORMAT
  for i in Paragraph: # GOING THROUGH ALL OF THE ELEMENTS IN THE PARAGRAPH TO PREVENT THE SQL FORMAT BEING PART OF THE TEMPORARY MEMORY LOCATION
    if i == "(" or i == ")" or i == "," or i == "'":
      pass # DONE WITH A PASS AND AN IF STATEMENT

    else: # ELSE, ALL OF THE PARAGRAPH CONTENT IS APPENDED TO THIS MEMORY LOCATION TO BE USED LATER ON
      ParagraphArray.append(i)

  Paragraph = ("".join(ParagraphArray)) # USING THE JOIN COMMAND SO THE PARAGRAPH IS TAKEN FROM THE ARRAY INTO AN ACTUAL PARAGRAPH

  return render_template("InsightsAndRecipes.html", TITLE=Title, PARAGRAPH=Paragraph, POSTNUMBER=PostNumber)
  # THIS THEN HTTP RESPONDS BACK THE POST HTML PAGE, WITH THE TITLE, PARAGRAPH AND THE OLDER POST NUMBER
  
# [===] [===] #

# [===] INSIGHTS AND RECIPES RECENT [===] #
@app.route("/InsightsAndRecipesRecent") # IN CASE THE USER WANTS A MORE RECENT POST, THAN WE USE THIS BLOCK OF CODE
def InsightsAndRecipesRecent(): # SUBROUTINE ESTABLISHING THE CODE FOR THE RECEPT POST OF THE INSIGHTS AND RECIPES PAGE
  global CurrentPostCount # GLOBALISING THESE VARIABLES TO SEE WHAT'S THE CURRENT POST WE'RE ON, AND WHAT'S THE MAX NUMBER OF POSTS AVAILABLE
  global MaxPosts

  if CurrentPostCount == MaxPosts: # IF THE CURRENT POST WE'RE ON IS THE MAX, THAN WE PASS AS WE CANNOT GO ANY MORE RECENT THAN THIS
    pass

  else: # ELSE WE INCREMENT TO THE CURRENT POST COUNT, TO BE ABLE TO GO TO THE NEXT AVAILABLE RECENT POST
    CurrentPostCount += 1

  CurrentPostCount = str(CurrentPostCount) # AS SUCH THE CURRENT POST COUNT IS TEMPORARILY CONVERTED TO A STRING
  PostNumber = CurrentPostCount # SO WE CAN GET THE POST NUMBER TO USE FOR SQL SELECTING STATEMENTS
  CurrentPostCount = int(CurrentPostCount) # AND TURNING BACK THE CURRENT POST COUNT TO AN INTEGER

  cursor.execute("SELECT Title FROM tblInsightsAndRecipes WHERE PostID=?", (PostNumber))
  for x in cursor.fetchall(): # THIS IS USED TO FIND THE TITLE OF THE NEXT RECENT POST THROUGH A SQL SELECT STATEMENT
    Title = x # THAN STORING THE TITLE OF THE NEXT RECENT POST TO THIS VARIABLE

  cursor.execute("SELECT Content FROM tblInsightsAndRecipes WHERE PostID=?", (PostNumber))
  for x in cursor.fetchall(): # THIS IS USED TO FIND THE PARAGRAPH OF THE NEXT RECENT POST THROUGH A SQL STATEMENT
    Paragraph = x # THAN STORING THE PARAGRAPH OF THE NEXT RECENT POST TO THIS VARIABLE

  TitleArray = [] # THIS IS A TEMPORARY ARRAY TO STORE THE NEXT RECENT POST TITLE IN, TO REMOVE IT'S SQL FORMAT
  for i in Title: # GOING THROUGH THE TITLE TO REMOVE ANY PRESENCE OF THE SQL FORMAT
    if i == "(" or i == ")" or i == "," or i == "'":
      pass # THIS IS DONE THROUGH PASS AND PREVENTING IT TO BE PART OF THE TITLE ARRAY MEMORY LOCATION

    else: # ELSE, THE ACTUAL CONTENT OF THE NEXT RECENT POST TITLE, IS APPENDED TO THIS ARRAY
      TitleArray.append(i)
        
  Title = ("".join(TitleArray)) # WITH ALL OF THE ELEMENTS BEING JOINED TOGETHER TO FORM THE NEXT RECENT POST TITLE WITHOUT THE SQL FORMAT

  ParagraphArray = [] # THIS IS AN ARRAY TO TEMPORARILY STORE THE NEXT RECENT POST PARAGRAPH CONTENT
  for i in Paragraph: # THIS IS BY GOING THROUGH THE PARAGRAPH AND PREVENTING TO APPEND ANY OF THE SQL FORMAT INTO THE PARAGRAPH
    if i == "(" or i == ")" or i == "," or i == "'":
      pass # ACCOMPLISHED BY AN IF STATEMENT AND THROUGH PASS

    else: # ELSE, ALL OF THE CONTENT OF THE PARAGRAPH ARRAY IS APPENDED TO THIS ARRAY TEMPORARILY WHILST THIS PROCESS IS BEING FINISHED
      ParagraphArray.append(i)

  Paragraph = ("".join(ParagraphArray)) # AFTER GETTING ALL OF THE CONTENT OF THE PARAGRAPH, IT'S JOINED TOGETHER TO TAKE IT OUT OF THE ARRAY

  return render_template("InsightsAndRecipes.html", TITLE=Title, PARAGRAPH=Paragraph, POSTNUMBER=PostNumber)
  # TO CONCLUDE, THE INSIGHTS AND RECIPES PAGE IS HTTP RESPONDED BACK, WITH THE NEXT RECENT POST TITLE, PARAGRAPH AND POST NUMBER OF THIS POST
# [===] [===] #

# [===] CONTACT US PAGE [===] #
@app.route("/ContactUs", methods=["POST", "GET"]) # THIS IS THE HTML PAGE FOR THE CONTACT US, ACCEPTING BOTH POST AND GET REQUESTS
def ContactUs(): # THIS IS THE SUBROUTINE THAT SHALL HOLD THE CODE FOR THE PROCESSING OF THE CONTACT US PAGE 
  if request.method == "POST": # THIS IS CHECKING IF THE USER IS SENDING A POST REQUEST OR NOT FIRST
    FirstName = request.form["FIRSTNAME"] # AS IT IS, IT'S RECEIVING ALL OF THE INPUTS THE USER TYPED IN, INTO THESE VARIABLES
    LastName = request.form["LASTNAME"]
    EnquiryEmail = request.form["EMAIL"]
    Country = request.form["COUNTRY"]
    Enquiry = request.form["ENQUIRY"]
    EmailMessage  = request.form["EMAILMESSAGE"]

    # THE FOLLOWING CODE ENSURES THAT THE DATA THEY PUT IN, EXISTS OR NOT
    try: # TRY AND EXCEPT CLAUSE TO ENSURE THAT THE FIRST NAME EXISTS
      for x in FirstName: # GOING THROUGH EVERYTHING OF THE FIRST NAME, IF IT FINDS ANY NULL/SPACE ELEMENTS, IT'S REMOVED
        if x == " " or x == "":
          FirstName.remove(x) # ACHIEVED BY AN IF STATEMENT AND REMOVE COMMAND

    except: # ELSE IF THE FIRSTNAME THAT THE USER TYPED IN DOES EXIST, THAN WE CAN JUST PASS THROUGH THIS PROCESS
      pass

    if len(FirstName) == 0: # THIS IS THEN CHECKING HOW LONG THE FIRST NAME IS
      return render_template("ContactUs.html", ERRORMESSAGE="Please enter something for the first name slot.")
      # IF IT'S 0, WE CAN ASSUME THAT THE USER TYPED IN NOTHING OR JUST SPACES, SO WE SEND BACK THE CONTACT US PAGE WITH THE ERROR MESSAGE TO TYPE A FIRSTNAME

    try: # ELSE IT PROCEEDS TO CHECK IF THE LAST NAME HAS BEEN ENTERED IN OR NOT
      for x in LastName: # THIS GOES THROUGH THE ENTIRETY OF THE LASTNAME
        if x == " " or x == "": # IF THERE'S ANY SPACE OR NULL ELEMENTS, IT SHALL BE REMOVED 
          LastName.remove(x)

    except: # IF THE USER DID PUT IN SOMETHING, THAN PASS
      pass

    if len(LastName) == 0: # THIS IS CHECKING IF THE LAST NAME DOESN'T EXIST OR NOT
      return render_template("ContactUs.html", ERRORMESSAGE="Please enter something for the last name slot.")
      # IF THE LAST NAME LENGTH IS EQUAL TO 0, IT'S ASSUMED THAT THEY DIDN'T TYPED IN ANYTHING, SO IT HTTP RESPOND BACK THE CONTACT US PAGE, WITH ERROR MESSAGE TO TYPE SOMETHING IN FOR THE LAST NAME INPUT BOX

    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # THIS IS THE REGULAR EXPRESSIONS PATTERN TO VERIFY THE EMAIL

    if (re.search(pattern, EnquiryEmail)):
      pass # IF THE EMAIL TYPED FOLLOWS THE PATTERN, THAN IT'LL PASS AND CONTINUE WITH THE PROCESS

    else: # ELSE, IT'LL HTTP RESPOND BACK THE CONTACT US PAGE, WITH THE ERROR MESSAGE THAT THE EMAIL IS WRONG
      return render_template("ContactUs.html", ERRORMESSAGE="You need to input a legitimate email.")

    try: # TRY AND EXCEPT CLAUSE IN CASE ANYTHING FAILS, THIS IS CHECKING IF THE USER PROVIDED THEIR COUNTRY
      for x in Country: # GOING THROUGH EACH CHARACTERS OF THE COUNTRY THEY INPUT, CHECKING FOR ANY NULL OR SPACE ELEMENTS
        if x == " " or x == "":
          Country.remove(x) # ANY OF THOSE ELEMENTS ARE REMOVED FROM THE COUNTRY THEY PROVIDED

    except: # OTHERWISE, IF THE COUNTRY THEY PROVIDED IS JUST CHRACTERS, THAN IT'LL PASS
      pass

    if len(Country) == 0: # CHECKING THE LENGTH OF THE COUNTRY AFTER REMOVING ANY UNWANTED CHARACTERS TO SUGGEST THERE'S NO INPUT
      return render_template("ContactUs.html", ERRORMESSAGE="Please put down the country you're from.")
      # IF IT IS 0, THAN THEY DIDN'T PUT IN A COUNTRY, HTTP RESPOND BACK THE CONTACT US PAGE WITH AN ERROR MESSAGE

    try: # TRY AND EXCEPT CLAUSE IN CASE ANYTHING GOES WRONG, THIS IS VERIFYING THAT THEY TYPED IN THEIR ENQUIRY
      for x in Enquiry: # GOING THROUGH ALL OF THE CHARACTERS IN THE ENQUIRY TO REMOVE ANY NULL OR SPACE ELEMENTS
        if x == " " or x == "":
          Enquiry.remove(x) # WHICH IS ACHIEVED BY AN IF STAEMENT AND REMOVE 

    except: # IF THE ENQUIRY IS JUST CHARACTERS, IT PASSES AND CONTINUES TO PROCEEDS ON
      pass

    if len(Enquiry) == 0: # THIS IS THEN CHECKING THE LENGTH OF THE ENQUIRY, IF THERE ARE NO CHARACTERS WE CAN ASSUME THAT THEY DIDN'T TYPED IN ANYTHING, AS SUCH, THE CONTACT US PAGE IS HTTP RESPONDED BACK TO THE USER WITH AN ERROR MESSAGE
      return render_template("ContactUs.html", ERRORMESSAGE="Please enter something for the enquiry slot.")

    try: # THIS IS AN TRY AND EXCEPT CLAUSE TO ENSURE THAT THEY TYPE IN AN MESSAGE FOR THEIR EMAIL
      for x in EmailMessage: # THIS IS BY GOING THROUGH THE CONTENTS OF THE EMAIL MESSAGE, REMOVING ANY SPACE OR NULL CHARACTERS, SO WHAT'S LEFT IS SUPPOSEDLY THE EMAIL MESSAGE, IF IT'S JUST ALL CHARACTERS, THAN IT PASSES
        if x == " " or x == "":
          EmailMessage.remove(x)

    except:
      pass

    if len(EmailMessage) == 0: # AS SUCH, IT LENS THE EMAIL MESSAGE, IF IT IS 0, WE CAN ASSUME ALL THEY TYPED IN WAS NULL OR SPACE ELEMENTS, AS SUCH NOTHING, THEN PROCEEDING TO HTTP RESPOND BACK THE CONTACT US PAGE WITH AN ERROR MESSAGE, UNLESS THEY DID PUT IN AN INPUT FOR THE EMAIL MESSAGE
      return render_template("ContactUs.html", ERRORMESSAGE="Please write an email message.")


    # THIS ENTIRE PIECE OF CODE IS TO FORMAT ALL OF THE INFORMATION THAT THE USER PROVIDED TO USE INTO A VARIABLE, AS A FORMAT, SO WHEN SENDING IT TO THE BUSINESS EMAIL, IT WON'T BE MULTIPLE EMAILS, BUT INSTEAD, 1 EMAIL WITH ALL OF THE CONTENT
    Message = ("""
    Consumer First Name = """ + FirstName + """
    Consumer Last Name = """ + LastName + """
    Consumer's Country = """ + Country + """
    Consumer's Email = """ + EnquiryEmail + """

    Email's Enquiry:
    """ + Enquiry + """

    Email's Content:
    """ + EmailMessage + """
               """)
    # THIS IS ACHIEVED THROUGH CONCATENACTION ALL OF THE INFORMATION AS VARIABLES IN THIS FORMAT TO BE USED LATER ON

    gmail_user = 'REDACTED'
    gmail_password = 'REDACTED'
    # THIS IS ESTABLISHING THE USERNAME AND PASSWORD OF THE GMAIL ACCOUNT THAT THE BUSINESS USE, FOLLOWING THE SMTP SERVER BUILTIN FUNCTION

    FROM = EnquiryEmail
    TO = gmail_user
    SUBJECT = Enquiry
    TEXT = Message
    # THIS IS ACCORDANCE TO THE SMTP SERVER BUILTIN FUNCTION SYNTAX, WHERE IT MUST STATES WHERE THE EMAIL IS FROM (WHATEVER THE CONSUMER TYPED IN), WHO IT'S FOR (THE BUSINESS GMAIL USER ACCOUNT), ALONGSIDE THE SUBJECT WHICH IS THE ENQUIRY THAT THE CONSUMER INPUTTED AND THE ACTUAL TEXT WHICH IS THE MESSAGE FORMATTED ABOVE

    emailmessage = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # CONSEQUENTLY, ONCE AGAIN, FOLLOWING THE SMTP SERVER BUILTIN FEATURE, WE CONCATENACT EVERYTHING INTO THIS EMAIL MESSAGE VARIABLE

    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(FROM, TO, emailmessage)
    server.close
    # FOLLOWING THE SMTP SERVER SYNTAX, THE SERVER IS ESTABLISHED AS A GMAIL SERVER, USING PORT 587. WITH THE FOLLOWING CODE EHLO TO ESTABLISH THE SERVER AND STARTTLS TO MAKE IT MORE SECURE, USING LOGIN TO AUTHENTICATE THE BUSINESS EMAIL AND BE ABLE TO RECEIVE AN EMAIL, WITH THE SEND MAIL AS THE FINAL PIECE OF THE SYNTAX CODE OF THE SMTP SERVER, TO BE ABLE TO SEND THIS ENQUIRY TOWARDS THE BUSINESS EMAIL, AND THEN CLOSING THE SMTP SERVER

    return render_template("ContactUs.html", ERRORMESSAGE="Email sent successfully.")
      # CONSEQUENTLY, AFTER ALL OF THAT, THE USER IS HTTP RESPONDED BACK THE CONTACT US PAGE, STATING THAT THE EMAIL HAS BEEN SENT SUCCESSFULLY, THROUGH THE HTML VARIABLE ERRORMESSAGE

  else:
    return render_template("ContactUs.html")
    # ELSE IF THE USER DIDN'T SENT IN A POST REQUEST, BUT THIS IS A GET REQUEST, WE JUST HTTP RESPOND BACK THE USER WITH THE CONTACT US HTML PAGE
# [===] [===] #

# [===] WEB PAGES FOR EACH PRODUCT FROM THE PRODUCT PORTFOLIO [===] #
# [===] THE RICE MACHINE [===] #
@app.route("/TheRiceMachine", methods=["POST", "GET"])
def TheRiceMachine():
  cursor.execute("SELECT ProductPrice, ProductStock, ProductShipping, ProductCapacity, ProductColour, ProductVersion, ProductDescription FROM tblProducts WHERE ProductID=1")
  for x in cursor.fetchall():
    Product1Information = x

  cursor.execute("SELECT * FROM tblAddToCart")
  for x in cursor.fetchall():
    print(x)

  global ProductPrice
  global ProductStock
  global ProductShipping
  global ProductCapacity
  global ProductColour
  global ProductVersion
  global ProductDescription
  
  ProductPrice = Product1Information[0]
  ProductStock = Product1Information[1]
  if Product1Information[2] == 0:
    ProductShipping = "Free"
  else:
    ProductShipping = Product1Information[2]
    ProductShipping = str(ProductShipping)
    ProductShipping = ("£" + ProductShipping)
  ProductCapacity = Product1Information[3]
  ProductColour = Product1Information[4]
  ProductVersion = Product1Information[5]
  ProductDescription = Product1Information[6]
  
  ProductPrice = str(ProductPrice)
  ProductPrice = ("£" + ProductPrice)
  ProductCapacity = str(ProductCapacity)

  if request.method == "POST" and "NewReview" in request.form:
    print("SUBMIT BUTTON WORKS")
    NewReview = request.form["NewReview"]
  
    cursor.execute("INSERT INTO tblReviews (Review, ProductID) VALUES (?, 1)", [NewReview])
    db.commit()
    
  elif request.method == "POST":
    cursor.execute("SELECT * FROM tblAddToCart")
    for x in cursor.fetchall():
      print(x)

    cursor.execute("SELECT Email FROM tblAddToCart")
    for x in cursor.fetchall():
      print(x)
      
    if "Username" in session and "Password" in session and "Email" in session:
          
      Count = 0

      Email = session["Email"]
      print(Email)

      cursor.execute("SELECT * FROM tblAddToCart WHERE Email = Email")
      for x in cursor.fetchall():
        Count += 1

      if Count == 1:
        cursor.execute("SELECT TheRiceMachine FROM tblAddToCart WHERE Email = Email")
        for x in cursor.fetchall():
          RiceMachineOrders = x

        RiceMachineOrdersNumber = RiceMachineOrders[0]
        RiceMachineOrdersNumber = int(RiceMachineOrdersNumber)
        RiceMachineOrdersNumber += 1
        RiceMachineOrdersNumber = str(RiceMachineOrdersNumber)

        cursor.execute("UPDATE tblAddToCart SET TheRiceMachine = ? WHERE Email=Email", (RiceMachineOrdersNumber))
        db.commit()

      else:
        cursor.execute("INSERT INTO tblAddToCart (Email, TheRiceMachine) VALUES (?, ?)", (Email, 1))
        db.commit()

    else:
      ErrorMessage = "Please log in to your account to be able to order products."
      
      return render_template("TheRiceMachine.html", ProductPrice=ProductPrice, ProductStock=ProductStock, ProductShipping=ProductShipping, ProductCapacity=ProductCapacity, ProductColour=ProductColour, ProductVersion=ProductVersion, DescriptionBox=ProductDescription, Error=ErrorMessage)

    # this is for the code to be able to add items to a shopping cart for the add to cart button
  
  else:
    pass
  
  # FOR THE PRODUCT I'LL NEED TO PROVIDE HTE PRODUCT DESCRIPTION, THEIR PRICE, STOCK, SHIPPING, CAPACITY, COLOUR AND VERSION
  # THE HTML VARIABLES FOR THESE ARE ProductPrice, ProductStock, ProductShipping, ProductCapacity, ProductColour, ProductVersion, DescriptionBox


  Product1Reviews = []

  cursor.execute("SELECT Review FROM tblReviews, tblProducts WHERE tblProducts.ProductID = tblReviews.ProductID")
  for x in cursor.fetchall():
    Product1Reviews.append(x)

  print(Product1Reviews)

  ProductReviewsArray1 = []
  for x in Product1Reviews:
    for i in x:
      if i == "(" or i == ")" or i == "," or i == "'":
        pass

      else:
        ProductReviewsArray1.append(i)

  print(ProductReviewsArray1)

  #ProductReviews1 = ("".join(ProductReviewsArray1))

  
  
  return render_template("TheRiceMachine.html", ProductPrice=ProductPrice, ProductStock=ProductStock, ProductShipping=ProductShipping, ProductCapacity=ProductCapacity, ProductColour=ProductColour, ProductVersion=ProductVersion, DescriptionBox=ProductDescription)
# [===] [===] #

# [===] THE BUFFALO [===] #
@app.route("/TheBuffalo")
def TheBuffalo():
  cursor.execute("SELECT ProductPrice, ProductStock, ProductShipping, ProductCapacity, ProductColour, ProductVersion, ProductDescription FROM tblProducts WHERE ProductID=2")
  for x in cursor.fetchall():
    Product2Information = x

  ProductPrice = Product2Information[0]
  ProductStock = Product2Information[1]
  if Product2Information[2] == 0:
    ProductShipping = "Free"
  else:
    ProductShipping = Product2Information[2]
    ProductShipping = str(ProductShipping)
    ProductShipping = ("£" + ProductShipping)
  ProductCapacity = Product2Information[3]
  ProductColour = Product2Information[4]
  ProductVersion = Product2Information[5]
  ProductDescription = Product2Information[6]

  ProductPrice = str(ProductPrice)
  ProductPrice = ("£" + ProductPrice)
  ProductCapacity = str(ProductCapacity)
  
  return render_template("TheBuffalo.html", ProductPrice=ProductPrice, ProductStock=ProductStock, ProductShipping=ProductShipping, ProductCapacity=ProductCapacity, ProductColour=ProductColour, ProductVersion=ProductVersion, DescriptionBox=ProductDescription)
# [===] [===]#

# [===] THE UNCLE JOHN [===] #
@app.route("/TheUncleJohn")
def TheUncleJohn():
  cursor.execute("SELECT ProductPrice, ProductStock, ProductShipping, ProductCapacity, ProductColour, ProductVersion, ProductDescription FROM tblProducts WHERE ProductID=3")
  for x in cursor.fetchall():
    Product3Information = x

  ProductPrice = Product3Information[0]
  ProductStock = Product3Information[1]
  if Product3Information[2] == 0:
    ProductShipping = "Free"
  else:
    ProductShipping = Product3Information[2]
    ProductShipping = str(ProductShipping)
    ProductShipping = ("£" + ProductShipping)
  ProductCapacity = Product3Information[3]
  ProductColour = Product3Information[4]
  ProductVersion = Product3Information[5]
  ProductDescription = Product3Information[6]

  ProductPrice = str(ProductPrice)
  ProductPrice = ("£" + ProductPrice)
  ProductCapacity = str(ProductCapacity)
  
  return render_template("TheUncleJohn.html", ProductPrice=ProductPrice, ProductStock=ProductStock, ProductShipping=ProductShipping, ProductCapacity=ProductCapacity, ProductColour=ProductColour, ProductVersion=ProductVersion, DescriptionBox=ProductDescription)
# [===] [===] #

# [===] RICE AND DICE [===] #
@app.route("/RiceAndDice")
def RiceAndDice():
  cursor.execute("SELECT ProductPrice, ProductStock, ProductShipping, ProductCapacity, ProductColour, ProductVersion, ProductDescription FROM tblProducts WHERE ProductID=4")
  for x in cursor.fetchall():
    Product4Information = x

  ProductPrice = Product4Information[0]
  ProductStock = Product4Information[1]
  if Product4Information[2] == 0:
    ProductShipping = "Free"
  else:
    ProductShipping = Product4Information[2]
    ProductShipping = str(ProductShipping)
    ProductShipping = ("£" + ProductShipping)
  ProductCapacity = Product4Information[3]
  ProductColour = Product4Information[4]
  ProductVersion = Product4Information[5]
  ProductDescription = Product4Information[6]

  ProductPrice = str(ProductPrice)
  ProductPrice = ("£" + ProductPrice)
  ProductCapacity = str(ProductCapacity)
  
  return render_template("RiceAndDice.html", ProductPrice=ProductPrice, ProductStock=ProductStock, ProductShipping=ProductShipping, ProductCapacity=ProductCapacity, ProductColour=ProductColour, ProductVersion=ProductVersion, DescriptionBox=ProductDescription)
# [===] [===] #

# [===] THE BASMATI BOILER [===] #
@app.route("/TheBasmatiBoiler")
def TheBasmatiBoiler():
  cursor.execute("SELECT ProductPrice, ProductStock, ProductShipping, ProductCapacity, ProductColour, ProductVersion, ProductDescription FROM tblProducts WHERE ProductID=5")
  for x in cursor.fetchall():
    Product5Information = x

  ProductPrice = Product5Information[0]
  ProductStock = Product5Information[1]
  if Product5Information[2] == 0:
    ProductShipping = "Free"
  else:
    ProductShipping = Product5Information[2]
    ProductShipping = str(ProductShipping)
    ProductShipping = ("£" + ProductShipping)
  ProductCapacity = Product5Information[3]
  ProductColour = Product5Information[4]
  ProductVersion = Product5Information[5]
  ProductDescription = Product5Information[6]

  ProductPrice = str(ProductPrice)
  ProductPrice = ("£" + ProductPrice)
  ProductCapacity = str(ProductCapacity)
  
  return render_template("TheBasmatiBoiler.html", ProductPrice=ProductPrice, ProductStock=ProductStock, ProductShipping=ProductShipping, ProductCapacity=ProductCapacity, ProductColour=ProductColour, ProductVersion=ProductVersion, DescriptionBox=ProductDescription)
# [===] [===] #

# [===] RICE COOKER 3000 [===] #
@app.route("/RiceCooker3000")
def RiceCooker3000():
  cursor.execute("SELECT ProductPrice, ProductStock, ProductShipping, ProductCapacity, ProductColour, ProductVersion, ProductDescription FROM tblProducts WHERE ProductID=6")
  for x in cursor.fetchall():
    Product6Information = x

  ProductPrice = Product6Information[0]
  ProductStock = Product6Information[1]
  if Product6Information[2] == 0:
    ProductShipping = "Free"
  else:
    ProductShipping = Product6Information[2]
    ProductShipping = str(ProductShipping)
    ProductShipping = ("£" + ProductShipping)
  ProductCapacity = Product6Information[3]
  ProductColour = Product6Information[4]
  ProductVersion = Product6Information[5]
  ProductDescription = Product6Information[6]

  ProductPrice = str(ProductPrice)
  ProductPrice = ("£" + ProductPrice)
  ProductCapacity = str(ProductCapacity)
  
  return render_template("RiceCooker3000.html", ProductPrice=ProductPrice, ProductStock=ProductStock, ProductShipping=ProductShipping, ProductCapacity=ProductCapacity, ProductColour=ProductColour, ProductVersion=ProductVersion, DescriptionBox=ProductDescription)
# [===] [===] #

# [===] THE SERVER [===] #
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="8080")
# [===] [===] #
