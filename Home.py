import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import sqlite3
from PIL import Image

def home():
    

def frame():
    global button_frame, login_frame,signup_frame
    button_frame = ctk.CTkFrame(welcome2_frame,width=50,fg_color='white')
    button_frame.grid(row=5,column=0)

    signup_frame = ctk.CTkFrame(welcome2_frame,fg_color='white')
    # signup_frame.grid(row=6,column=0)

    login_frame = ctk.CTkFrame(welcome2_frame,fg_color='white')
    # login_frame.grid(row=6,column=0)

    login_btn = ctk.CTkButton(button_frame,text='LOGIN',width=150,fg_color='black',command=login_page)
    login_btn.grid(row=0,column=0,pady=(15,30),padx=20)

    signup_btn = ctk.CTkButton(button_frame,text='SIGNUP',width=150,fg_color='green',command=signup_page)
    signup_btn.grid(row=1,column=0,pady=(0,15),padx=20)

def signup_page():
    global first_nameEntry,lastnameEntry,UsernameEntry,emailaddress_Entry,phoneNumber_Entry,password_Entry,confirmPassword_Entry,gender_comboBox
    button_frame.grid_remove()
    login_frame.grid_remove()
    message_frame.grid_remove()
    signup_frame.grid(row=0,column=0)

    #Creating a signup page
    title_label = ctk.CTkLabel(signup_frame, text = "Register", font=('Cooper Black', 20, 'bold'), fg_color='green')
    title_label.grid(row=0,column=0,pady=25,ipadx=10,ipady=10)

    firstname_Label = ctk.CTkLabel(signup_frame, text="FIRST NAME")
    firstname_Label.grid(row=1,column=0)
    
    first_nameEntry = ctk.CTkEntry(signup_frame, placeholder_text = 'First Name', width=350)
    first_nameEntry.grid(row=2,column=0)

    lastname_Label = ctk.CTkLabel(signup_frame, text = "LAST NAME")
    lastname_Label.grid(row=3,column=0)
    
    lastnameEntry = ctk.CTkEntry(signup_frame, placeholder_text = "Last Name", width=350)
    lastnameEntry.grid(row=4,column=0)

    Username_Label = ctk.CTkLabel(signup_frame, text = "USERNAME")
    Username_Label.grid(row=5,column=0)
    
    UsernameEntry = ctk.CTkEntry(signup_frame, placeholder_text = "Username", width=350)
    UsernameEntry.grid(row=6,column=0)

    gender_label = ctk.CTkLabel(signup_frame, text = "GENDER")
    gender_label.grid(row=7, column=0)
    gender_var = ctk.StringVar(value="Male")
    gender_comboBox = ctk.CTkComboBox(signup_frame,values=["Male","Female","Transgender","I rather not say"], width=350,variable=gender_var)
    gender_comboBox.grid(row=8,column=0)

    emailaddress_Label = ctk.CTkLabel(signup_frame, text = "EMAIL ADDRESS")
    emailaddress_Label.grid(row=9,column=0)
    
    emailaddress_Entry = ctk.CTkEntry(signup_frame, placeholder_text="example@gmail.com", width=350)
    emailaddress_Entry.grid(row=10,column=0,padx=30)
    
    phoneNumber_Label = ctk.CTkLabel(signup_frame, text = "PHONE NUMBER")
    phoneNumber_Label.grid(row=11,column=0, padx=(15,10))
    phoneNumber_Entry = ctk.CTkEntry(signup_frame, placeholder_text = "Phone Number", width=350)
    phoneNumber_Entry.grid(row=12,column=0, padx=(15,10))

    password_label = ctk.CTkLabel(signup_frame, text = "PASSWORD")
    password_label.grid(row=13,column=0)
    password_Entry = ctk.CTkEntry(signup_frame, placeholder_text = "Password", width=350, show = '*')
    password_Entry.grid(row=14,column=0,padx=5)

    confirmPassword_Label = ctk.CTkLabel(signup_frame, text = "CONFIRM PASSWORD")
    confirmPassword_Label.grid(row=15,column=0,pady=(0,0))
    confirmPassword_Entry = ctk.CTkEntry(signup_frame, placeholder_text = "Confirm Password", width=350, show ='*')
    confirmPassword_Entry.grid(row=16,column=0,padx=30)

    check_btn = ctk.CTkCheckBox(signup_frame, text = "I agree to the Terms & Conditions of this App")
    check_btn.grid(row=17,column=0,pady=(20,0))

    signup = ctk.CTkButton(signup_frame, text='Sign Up', command=signup_info_msg, fg_color='black')
    signup.grid(row=18,column=0,padx=30,pady=15)

    title = ctk.CTkLabel(signup_frame, text='Already have an account?')
    title.grid(row=19,column=0,padx=(0,20),pady = (20,0))

    login_btn = ctk.CTkButton(signup_frame,text='Login',fg_color='grey',command=login_page)
    login_btn.grid(row=19, column=0, padx = (300,0), pady = (20,0))
#login section
def login_page():
    global usersnameEntry2,password_Entry2
    button_frame.grid_remove()
    signup_frame.grid_remove()
    message_frame.grid_remove()
    login_frame.grid(row=0,column=0, padx=0)

    login_title = ctk.CTkLabel(login_frame, text='Login Section', font=('Cooper Black',18),fg_color='green')
    login_title.grid(row=0, column=0, pady=(130,25),ipadx=10,ipady=10)
    
    usersname = ctk.CTkLabel(login_frame, text= 'Username')
    usersname.grid(row=1, column=0)
    usersnameEntry2 = ctk.CTkEntry(login_frame,placeholder_text='Username', width=250)
    usersnameEntry2.grid(row=2,column=0, padx=30, pady=(0,15))

    password_label = ctk.CTkLabel(login_frame, text = "PASSWORD")
    password_label.grid(row=3,column=0)
    password_Entry2 = ctk.CTkEntry(login_frame,placeholder_text='Password', width=250, show = '*')
    password_Entry2.grid(row=4,column=0,padx=30,pady=(0,15))

    chekbtn = ctk.CTkButton(password_Entry2,text='SHOW',width=50,fg_color='grey')
    chekbtn.grid(row=0,column=0,padx=(200,0))

    login = ctk.CTkButton(login_frame, text = 'LOGIN', fg_color='black', command=login_get_info)
    login.grid(row=5,column=0,padx=30, pady=(15))

    add = ctk.CTkLabel(login_frame, text="---------------------------- OR ----------------------------------")
    add.grid(row=6,column=0,padx=(0,2),pady = (5,20))

    title = ctk.CTkLabel(login_frame, text="Don't have an account yet?")
    title.grid(row=7,column=0,padx=(0,20),pady = (20,200))

    signup_btn = ctk.CTkButton(login_frame,text='Sign Up',fg_color='grey',width=100,command=signup_page)
    signup_btn.grid(row=7, column=0, padx = (300,0), pady = (20,200))

def signup_info_msg():
    first_name = first_nameEntry.get()
    last_name = lastnameEntry.get()
    user_name = UsernameEntry.get()
    gend = gender_comboBox.get()
    phoneNumber = phoneNumber_Entry.get()
    email_address = emailaddress_Entry.get()
    password = password_Entry.get()
    confirm_password = confirmPassword_Entry.get()
    if first_name == '':
        CTkMessagebox(title='Signup Page ', message="Fill in your First Name")
    elif last_name == '':
        CTkMessagebox(title='Signup Page ', message="Fill in your Last Name")
    elif user_name == '':
        CTkMessagebox(title='Signup Page ', message="Fill in your UserName")
    elif gend == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Gender")
    elif phoneNumber == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Phone Number")
    elif email_address == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Email Address")
    elif password == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Password")
    elif confirm_password == '':
        CTkMessagebox(title='Signup Page ', message="Confirm Your Password")
    elif password != confirm_password:
        CTkMessagebox(title='Signup Page', message="Invalid Password.\nInput the correct password ")
    elif password == confirm_password:
        CTkMessagebox(title='Signup Page ', message="Correct Password")
        conn = sqlite3.connect('VotersDatabase.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS EntryTable
                (FirstName TEXT,LastName TEXT,Username TEXT,Gender TEXT,EmailAddress TEXT,Phone_Number INTEGER,Password TEXT)''')
        c.execute('''INSERT INTO EntryTable(FirstName,LastName,Username,Gender,EmailAddress,Phone_Number,Password)VALUES(?,?,?,?,?,?,?)
                ''',
                (first_name,last_name,user_name,gend,email_address,phoneNumber,password))
        conn.commit()     
        CTkMessagebox(title='Signup Page ', message="You have successfully signed in")

def login_get_info():
    email = usersnameEntry2.get()
    password = password_Entry2.get()

    con=sqlite3.connect('VotersDatabase.db')
    cur = con.cursor()
    statement = f"SELECT email from EntryTable WHERE Email='{email}' AND Password='{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        print('Invalid login details')

def intro():
    intro_frame = ctk.CTkFrame(window,fg_color='white')
    intro_frame.grid(row=0,column=0,sticky='nw')
    intro_frame.configure(width=1400,height=100)
    logo1_image = ctk.CTkImage(light_image=Image.open('coderslogo.png'), size=(200,150))
    logo1 = ctk.CTkLabel(intro_frame,image=logo1_image, bg_color='white',text='')
    logo1.grid(row=0, column=0, sticky='nw')

    home = ctk.CTkButton(intro_frame,text='Home',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    home.grid(row=0,column=0,padx=(200,6), pady=(60,0), sticky='nw')
    aboute_text = ctk.CTkButton(intro_frame,text='About',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    aboute_text.grid(row=0,column=0,padx=(300,6), pady=(60,0), sticky='nw')
    hep_text = ctk.CTkButton(intro_frame,text='Help',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    hep_text.grid(row=0,column=0,padx=(400,5), pady=(60,0), sticky='nw')
    methode_var = ctk.StringVar(value="Methods")
    methode_combobox = ctk.CTkComboBox(intro_frame,values=["single transferable vote", "Borda", "Instant runoff voting", "Condorcet", "Approval voting", "Plurality/FPTP"],width=100,variable=methode_var,fg_color='white',border_color='white',font=('Cooper Black',15))
    methode_combobox.grid(row=0,column=1,padx=(600,4),pady=(60,0),sticky='nw')
    helpe_btn = ctk.CTkButton(intro_frame,text="Who we help",text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    helpe_btn.grid(row=0,column=2,padx=(50,26), pady=(60,0),sticky='nw')


def vote():
    global cast_frame
    image_frame.grid_forget()
    intro()
    cast_frame = ctk.CTkFrame(window,fg_color='white')
    cast_frame.grid(row=1,column=0)
    field_label = ctk.CTkLabel(cast_frame,fg_color='white',text='Choose the field you want to use VoteStream for',font=('Arial Bold',30),text_color='Black')
    field_label.grid(row=0,column=0,padx=(350,0),pady=10,ipady=10,sticky='nw')

    gov_image = ctk.CTkImage(light_image=Image.open('vote.png'),size=(200,100))
    govimage_label = ctk.CTkLabel(cast_frame,image=gov_image,text='')
    govimage_label.grid(row=1,column=0,padx=15,pady=10,sticky='w')
    gov_label = ctk.CTkButton(cast_frame,text='Government related\n Election',font=('Cooper Black',25),text_color='black',fg_color='white',command=government)
    gov_label.grid(row=2,column=0,padx=15,pady=10,sticky='w')

    bus_image = ctk.CTkImage(light_image=Image.open('ballot box.webp'),size=(200,100))
    busimage_label = ctk.CTkLabel(cast_frame,image=bus_image,text='')
    busimage_label.grid(row=1,column=0,padx=550,pady=10,sticky='w')
    bus_label = ctk.CTkButton(cast_frame,text='Business related\n Election',font=('Cooper Black',25),text_color='black',fg_color='white',command=business)
    bus_label.grid(row=2,column=0,padx=550,pady=10,sticky='w')

    edu_image = ctk.CTkImage(light_image=Image.open('election.webp'),size=(200,100))
    eduimage_label = ctk.CTkLabel(cast_frame,image=edu_image,text='')
    eduimage_label.grid(row=1,column=0,padx=1050,pady=10,sticky='w')
    edu_label = ctk.CTkButton(cast_frame,text='Education related \n Election',font=('Cooper Black',25),text_color='black',fg_color='white',command=education)
    edu_label.grid(row=2,column=0,padx=1000,pady=10,sticky='w')

    celeb_image = ctk.CTkImage(light_image=Image.open('vs.webp'),size=(200,100))
    celebimage_label = ctk.CTkLabel(cast_frame,image=celeb_image,text='')
    celebimage_label.grid(row=3,column=0,padx=15,pady=30,sticky='w')
    celeb_label = ctk.CTkButton(cast_frame,text='Celebrity based \n Election',font=('Cooper Black',25),text_color='black',fg_color='white',command=celebrity)
    celeb_label.grid(row=4,column=0,padx=15,pady=10,sticky='w')

    food_image = ctk.CTkImage(light_image=Image.open('coderslogo(1).jpg'),size=(200,180))
    foodimage_label = ctk.CTkLabel(cast_frame,image=food_image,text='')
    foodimage_label.grid(row=3,column=0,padx=550,pady=10,sticky='w')
    food_label = ctk.CTkButton(cast_frame,text='Food Based\n Election',font=('Cooper Black',25),text_color='black',fg_color='white',command=food)
    food_label.grid(row=4,column=0,padx=590,pady=10,sticky='w')

    random_image = ctk.CTkImage(light_image=Image.open('election.webp'),size=(200,180))
    randomimage_label = ctk.CTkLabel(cast_frame,image=random_image,text='')
    randomimage_label.grid(row=3,column=0,padx=1050,pady=10,sticky='w')
    random_label = ctk.CTkButton(cast_frame,text='Random \n Election',font=('Cooper Black',25),text_color='black',fg_color='white',command=random)
    random_label.grid(row=4,column=0,padx=1080,pady=10,sticky='w')

def government():
    global gov_frame,add_candName
    cast_frame.grid_forget()
    text_label = ctk.CTkLabel(window,text='Create a Poll',font=('Times New Roman',30),text_color='black')
    text_label.grid(row=1,column=0,pady=10,sticky='ns') 
    text1_label = ctk.CTkLabel(window,text='Complete the below fields to create your polls',font=('Arial',20),text_color='grey')
    text1_label.grid(row=2,column=0,sticky='ns')   
    gov_frame = ctk.CTkFrame(window,fg_color='white',width=900,height=1400)
    gov_frame.grid(row=3,column=0,pady=50)
    gov_label = ctk.CTkLabel(gov_frame,text='Which post are you voting for: ',font=('Arial',20))
    gov_label.grid(row=0,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    post_var = ctk.StringVar(value="Post")
    post_combobox = ctk.CTkComboBox(gov_frame,values=['President', 'Vice - President','Governor','Deputy Governor', 'Senator','Others'],width=200,variable=post_var,fg_color='white',border_color='white',font=('Arial',15))
    post_combobox.grid(row=1,column=0,padx=(10,50))
    other_post =  ctk.CTkLabel(gov_frame,text="Other Post ",font=('Arial',20))
    other_post.grid(row=2,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    other_postEntry = ctk.CTkEntry(gov_frame,placeholder_text='Other post which are not included',width=200)
    other_postEntry.grid(row=3,column=0,padx=20,pady=15)
    vote_label = ctk.CTkLabel(gov_frame,text='Voting type',font=('Arial',20))
    vote_label.grid(row=4,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    voting_var = ctk.StringVar(value="Single choice")
    voting_type = ctk.CTkComboBox(gov_frame,values=['Multiple Choice', 'Ranking Poll','Single choice'],width=200,variable=voting_var,fg_color='white',border_color='white',font=('Arial',15))
    voting_type.grid(row=5,column=0,padx=(10,50))
    candidate_name =  ctk.CTkLabel(gov_frame,text="Candidate's name *",font=('Arial',20))
    candidate_name.grid(row=0,column=1,padx=2,pady=(20,0),sticky='nw')
    candidate_nameEntry = ctk.CTkEntry(gov_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=1,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(gov_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=2,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(gov_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=3,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(gov_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=4,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(gov_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=5,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(gov_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=6,column=1,padx=2)
    votingSec_label = ctk.CTkLabel(gov_frame,text="Voting Security",font=('Arial',20))
    votingSec_label.grid(row=0,column=2,padx=(10,50),pady=(20,0),sticky='nw') 
    voting_sec = ctk.StringVar(value="Security")
    voting_security = ctk.CTkComboBox(gov_frame,values=['Allow multiple votes per person','Allow one vote per votestream account'],width=300,variable=voting_sec,fg_color='white',border_color='white',font=('Arial',15))
    voting_security.grid(row=1,column=2,padx=(10,50))

def business():
    cast_frame.grid_forget()
    text_label = ctk.CTkLabel(window,text='Create a Poll',font=('Times New Roman',30),text_color='black')
    text_label.grid(row=1,column=0,pady=10,sticky='ns') 
    text1_label = ctk.CTkLabel(window,text='Complete the below fields to create your polls',font=('Arial',20),text_color='grey')
    text1_label.grid(row=2,column=0,sticky='ns')   
    bus_frame = ctk.CTkFrame(window,fg_color='white',width=900,height=1400)
    bus_frame.grid(row=3,column=0,pady=50)
    bus_label = ctk.CTkLabel(bus_frame,text='Which post are you voting for: ',font=('Arial',20))
    bus_label.grid(row=0,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    post_var = ctk.StringVar(value="Post")
    post_combobox = ctk.CTkComboBox(bus_frame,values=['Manager', 'Ass.Manager','Director','Ass.director', 'Secretary','Personal Assistant','Others'],width=200,variable=post_var,fg_color='white',border_color='white',font=('Arial',15))
    post_combobox.grid(row=1,column=0,padx=(10,50))
    other_post =  ctk.CTkLabel(bus_frame,text="Other Post ",font=('Arial',20))
    other_post.grid(row=2,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    other_postEntry = ctk.CTkEntry(bus_frame,placeholder_text='Other post which are not included',width=200)
    other_postEntry.grid(row=3,column=0,padx=20,pady=15)
    vote_label = ctk.CTkLabel(bus_frame,text='Voting type',font=('Arial',20))
    vote_label.grid(row=4,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    voting_var = ctk.StringVar(value="Single choice")
    voting_type = ctk.CTkComboBox(bus_frame,values=['Multiple Choice', 'Ranking Poll','Single choice'],width=200,variable=voting_var,fg_color='white',border_color='white',font=('Arial',15))
    voting_type.grid(row=5,column=0,padx=(10,50))
    candidate_name =  ctk.CTkLabel(bus_frame,text="Candidate's name *",font=('Arial',20))
    candidate_name.grid(row=0,column=1,padx=2,pady=(20,0),sticky='nw')
    candidate_nameEntry = ctk.CTkEntry(bus_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=1,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(bus_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=2,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(bus_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=3,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(bus_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=4,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(bus_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=5,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(bus_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=6,column=1,padx=2)
    votingSec_label = ctk.CTkLabel(bus_frame,text="Voting Security",font=('Arial',20))
    votingSec_label.grid(row=0,column=2,padx=(10,50),pady=(20,0),sticky='nw') 
    voting_sec = ctk.StringVar(value="Security")
    voting_security = ctk.CTkComboBox(bus_frame,values=['Allow multiple votes per person','Allow one vote per votestream account'],width=300,variable=voting_sec,fg_color='white',border_color='white',font=('Arial',15))
    voting_security.grid(row=1,column=2,padx=(10,50))

def education():
    cast_frame.grid_forget()
    text_label = ctk.CTkLabel(window,text='Create a Poll',font=('Times New Roman',30),text_color='black')
    text_label.grid(row=1,column=0,pady=10,sticky='ns') 
    text1_label = ctk.CTkLabel(window,text='Complete the below fields to create your polls',font=('Arial',20),text_color='grey')
    text1_label.grid(row=2,column=0,sticky='ns')   
    edu_frame = ctk.CTkFrame(window,fg_color='white',width=900,height=1400)
    edu_frame.grid(row=3,column=0,pady=50)
    edu_label = ctk.CTkLabel(edu_frame,text='Which post are you voting for: ',font=('Arial',20))
    edu_label.grid(row=0,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    post_var = ctk.StringVar(value="Post")
    post_combobox = ctk.CTkComboBox(edu_frame,values=['Teacher', 'Principal','Accountant','Lecturer', 'Senior lecturer','Professor','Head of Department','Chancellor','Vice Chancellor','Others'],width=200,variable=post_var,fg_color='white',border_color='white',font=('Arial',15))
    post_combobox.grid(row=1,column=0,padx=(10,50))
    other_post =  ctk.CTkLabel(edu_frame,text="Other Post ",font=('Arial',20))
    other_post.grid(row=2,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    other_postEntry = ctk.CTkEntry(edu_frame,placeholder_text='Other post which are not included',width=200)
    other_postEntry.grid(row=3,column=0,padx=20,pady=15)
    vote_label = ctk.CTkLabel(edu_frame,text='Voting type',font=('Arial',20))
    vote_label.grid(row=4,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    voting_var = ctk.StringVar(value="Single choice")
    voting_type = ctk.CTkComboBox(edu_frame,values=['Multiple Choice', 'Ranking Poll','Single choice'],width=200,variable=voting_var,fg_color='white',border_color='white',font=('Arial',15))
    voting_type.grid(row=5,column=0,padx=(10,50))
    candidate_name =  ctk.CTkLabel(edu_frame,text="Candidate's name *",font=('Arial',20))
    candidate_name.grid(row=0,column=1,padx=2,pady=(20,0),sticky='nw')
    candidate_nameEntry = ctk.CTkEntry(edu_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=1,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(edu_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=2,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(edu_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=3,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(edu_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=4,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(edu_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=5,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(edu_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=6,column=1,padx=2)
    votingSec_label = ctk.CTkLabel(edu_frame,text="Voting Security",font=('Arial',20))
    votingSec_label.grid(row=0,column=2,padx=(10,50),pady=(20,0),sticky='nw') 
    voting_sec = ctk.StringVar(value="Security")
    voting_security = ctk.CTkComboBox(edu_frame,values=['Allow multiple votes per person','Allow one vote per votestream account'],width=300,variable=voting_sec,fg_color='white',border_color='white',font=('Arial',15))
    voting_security.grid(row=1,column=2,padx=(10,50))

def celebrity():
    cast_frame.grid_forget()
    text_label = ctk.CTkLabel(window,text='Create a Poll',font=('Times New Roman',30),text_color='black')
    text_label.grid(row=1,column=0,pady=10,sticky='ns') 
    text1_label = ctk.CTkLabel(window,text='Complete the below fields to create your polls',font=('Arial',20),text_color='grey')
    text1_label.grid(row=2,column=0,sticky='ns')   
    celeb_frame = ctk.CTkFrame(window,fg_color='white',width=900,height=1400)
    celeb_frame.grid(row=3,column=0,pady=50)
    other_post =  ctk.CTkLabel(celeb_frame,text="Title",font=('Arial',20))
    other_post.grid(row=2,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    other_postEntry = ctk.CTkEntry(celeb_frame,placeholder_text='This field is required',width=200)
    other_postEntry.grid(row=3,column=0,padx=20,pady=15)
    vote_label = ctk.CTkLabel(celeb_frame,text='Voting type',font=('Arial',20))
    vote_label.grid(row=4,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    voting_var = ctk.StringVar(value="Single choice")
    voting_type = ctk.CTkComboBox(celeb_frame,values=['Multiple Choice', 'Ranking Poll','Single choice'],width=200,variable=voting_var,fg_color='white',border_color='white',font=('Arial',15))
    voting_type.grid(row=5,column=0,padx=(10,50))
    candidate_name =  ctk.CTkLabel(celeb_frame,text="Celebrity's name *",font=('Arial',20))
    candidate_name.grid(row=0,column=1,padx=2,pady=(20,0),sticky='nw')
    candidate_nameEntry = ctk.CTkEntry(celeb_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=1,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(celeb_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=2,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(celeb_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=3,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(celeb_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=4,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(celeb_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=5,column=1,padx=2)
    candidate_nameEntry = ctk.CTkEntry(celeb_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry.grid(row=6,column=1,padx=2)
    votingSec_label= ctk.CTkLabel(celeb_frame,text="Voting Security",font=('Arial',20))
    votingSec_label.grid(row=0,column=2,padx=(10,50),pady=(20,0),sticky='nw') 
    voting_sec = ctk.StringVar(value="Security")
    voting_security = ctk.CTkComboBox(celeb_frame,values=['Allow multiple votes per person','Allow one vote per votestream account'],width=300,variable=voting_sec,fg_color='white',border_color='white',font=('Arial',15))
    voting_security.grid(row=1,column=2,padx=(10,50))

def food():
    cast_frame.grid_forget()
    text_label = ctk.CTkLabel(window,text='Create a Poll',font=('Times New Roman',30),text_color='black')
    text_label.grid(row=1,column=0,pady=10,sticky='ns') 
    text1_label = ctk.CTkLabel(window,text='Complete the below fields to create your polls',font=('Arial',20),text_color='grey')
    text1_label.grid(row=2,column=0,sticky='ns')   
    food_frame = ctk.CTkFrame(window,fg_color='white',width=900,height=1400)
    food_frame.grid(row=3,column=0,pady=50)
    food_label = ctk.CTkLabel(food_frame,text='Title/Description',font=('Arial',20))
    food_label.grid(row=0,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    other_postEntry = ctk.CTkEntry(food_frame,placeholder_text='This field is required',width=200)
    other_postEntry.grid(row=3,column=0,padx=2)
    vote_label = ctk.CTkLabel(food_frame,text='Voting type',font=('Arial',20))
    vote_label.grid(row=4,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    voting_var = ctk.StringVar(value="Single choice")
    voting_type = ctk.CTkComboBox(food_frame,values=['Multiple Choice', 'Ranking Poll','Single choice'],width=200,variable=voting_var,fg_color='white',border_color='white',font=('Arial',15))
    voting_type.grid(row=5,column=0,padx=(10,50))
    food_name =  ctk.CTkLabel(food_frame,text="Food name *",font=('Arial',20))
    food_name.grid(row=0,column=1,padx=2,pady=(20,0),sticky='nw')
    food_nameEntry1 = ctk.CTkEntry(food_frame,placeholder_text='This field is required',width=300)
    food_nameEntry1.grid(row=1,column=1,padx=2)
    food_nameEntry2 = ctk.CTkEntry(food_frame,placeholder_text='This field is required',width=300)
    food_nameEntry2.grid(row=2,column=1,padx=2)
    food_nameEntry3 = ctk.CTkEntry(food_frame,placeholder_text='This field is required',width=300)
    food_nameEntry3.grid(row=3,column=1,padx=2)
    food_nameEntry4 = ctk.CTkEntry(food_frame,placeholder_text='This field is required',width=300)
    food_nameEntry4.grid(row=4,column=1,padx=2)
    food_nameEntry5 = ctk.CTkEntry(food_frame,placeholder_text='This field is required',width=300)
    food_nameEntry5.grid(row=5,column=1,padx=2)
    food_nameEntry6 = ctk.CTkEntry(food_frame,placeholder_text='This field is required',width=300)
    food_nameEntry6.grid(row=6,column=1,padx=2)
    votingSec_label = ctk.CTkLabel(food_frame,text="Voting Security",font=('Arial',20))
    votingSec_label.grid(row=0,column=2,padx=(10,50),pady=(20,0),sticky='nw') 
    voting_sec = ctk.StringVar(value="Security")
    voting_security = ctk.CTkComboBox(food_frame,values=['Allow multiple votes per person','Allow one vote per votestream account'],width=300,variable=voting_sec,fg_color='white',border_color='white',font=('Arial',15))
    voting_security.grid(row=1,column=2,padx=(10,50))

def random():
    cast_frame.grid_forget()
    text_label = ctk.CTkLabel(window,text='Create a Poll',font=('Times New Roman',30),text_color='black')
    text_label.grid(row=1,column=0,pady=10,sticky='ns') 
    text1_label = ctk.CTkLabel(window,text='Complete the below fields to create your polls',font=('Arial',20),text_color='grey')
    text1_label.grid(row=2,column=0,sticky='ns')   
    random_frame = ctk.CTkFrame(window,fg_color='white',width=900,height=1400)
    random_frame.grid(row=3,column=0,pady=50)
    title =  ctk.CTkLabel(random_frame,text="Title",font=('Arial',20))
    title.grid(row=1,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    titleEntry = ctk.CTkEntry(random_frame,placeholder_text='This field is required',width=300)
    titleEntry.grid(row=2,column=0,padx=2)
    vote_label = ctk.CTkLabel(random_frame,text='Voting type',font=('Arial',20))
    vote_label.grid(row=3,column=0,padx=(10,50),pady=(20,0),sticky='nw')
    voting_var = ctk.StringVar(value="Single choice")
    voting_type = ctk.CTkComboBox(random_frame,values=['Multiple Choice', 'Ranking Poll','Single choice'],width=200,variable=voting_var,fg_color='white',border_color='white',font=('Arial',15))
    voting_type.grid(row=4,column=0,padx=(10,50))
    candidate_name =  ctk.CTkLabel(random_frame,text="Candidate's name *",font=('Arial',20))
    candidate_name.grid(row=0,column=1,padx=2,pady=(20,0),sticky='nw')
    candidate_nameEntry1 = ctk.CTkEntry(random_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry1.grid(row=1,column=1,padx=2)
    candidate_nameEntry2 = ctk.CTkEntry(random_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry2.grid(row=2,column=1,padx=2)
    candidate_nameEntry3 = ctk.CTkEntry(random_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry3.grid(row=3,column=1,padx=2)
    candidate_nameEntry4 = ctk.CTkEntry(random_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry4.grid(row=4,column=1,padx=2)
    candidate_nameEntry5 = ctk.CTkEntry(random_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry5.grid(row=5,column=1,padx=2)
    candidate_nameEntry6 = ctk.CTkEntry(random_frame,placeholder_text='This field is required',width=300)
    candidate_nameEntry6.grid(row=6,column=1,padx=2)
    votingSec_label = ctk.CTkLabel(random_frame,text="Voting Security",font=('Arial',20))
    votingSec_label.grid(row=0,column=2,padx=(10,50),pady=(20,0),sticky='nw') 
    voting_sec = ctk.StringVar(value="Security")
    voting_security = ctk.CTkComboBox(random_frame,values=['Allow multiple votes per person','Allow one vote per votestream account'],width=300,variable=voting_sec,fg_color='white',border_color='white',font=('Arial',15))
    voting_security.grid(row=1,column=2,padx=(10,50))

if __name__ == "__main__":
    window = ctk.CTk()
    window.title("VoteStream")
    window.iconbitmap("votelogs.ico")
    window.geometry('1400x800+0+0')

    logo_frame = ctk.CTkFrame(window,bg_color='white',width=1200,height=600)
    logo_frame.grid()
    logo_frame.columnconfigure(0, weight=2)
    logo_frame.rowconfigure(0, weight=2)

    img = ctk.CTkImage(light_image=Image.open('coderslogo.png'),size=(920,600))
    lbl_img = ctk.CTkLabel(logo_frame,image=img,bg_color='white',text='')
    lbl_img.grid(row=0,column=0,ipadx=220,ipady=35,sticky='nw,sw,ne,se')

    logo_frame.after(6000, logo_frame.destroy)

    bg = ctk.CTkImage(light_image=Image.open('coderslogo.png'),size=(900,700))
    lbl_bg = ctk.CTkLabel(window,image=bg,bg_color='white',text='')
    lbl_bg.grid(row=0,column=0)

    welcome2_frame = ctk.CTkFrame(window,fg_color='white',width=600,height=600)
    welcome2_frame.grid(row=0,column=1)

    message_frame = ctk.CTkFrame(welcome2_frame, fg_color='white',width=600,height=600)
    message_frame.grid(row=0, column=0)

    lbel = ctk.CTkLabel(message_frame,text='Good Day',font=('Cooper Black',25))
    lbel.grid(row=0,column=1,pady=(50,50))
    lbel = ctk.CTkLabel(message_frame,text='Our Esteemed Voters',font=('Cooper Black',25))
    lbel.grid(row=1,column=1,pady=(0,50))
    labl = ctk.CTkLabel(message_frame,text='Welcome to',font=('Cooper Black',25))
    labl.grid(row=2,column=1,pady=(0,50))
    labl = ctk.CTkLabel(message_frame,text='Your Number 1 Voting System',font=('Cooper Black',25))
    labl.grid(row=3,column=1,pady=(0,50))
    labl = ctk.CTkLabel(message_frame,text='Powered by the Exceptional coders',font=('Cooper Black',25))
    labl.grid(row=4,column=1,pady=(0,50),ipadx=10)

    message_frame.after(5000,message_frame.destroy)

    first_frame = ctk.CTkFrame(master=welcome2_frame,fg_color='white')
    first_frame.grid(row=0,column=0)
    bg_label = ctk.CTkLabel(master=first_frame, text='')
    bg_label.grid(row=0, column=0)

    bkg_image = ctk.CTkImage(light_image=Image.open('voteimg1.png'), size=(1400,570))
    image_frame = ctk.CTkFrame(master=first_frame,fg_color='white')
    image_frame.grid(row=0,column=0)

    bg_label = ctk.CTkLabel(master=image_frame, image=bkg_image, text='')
    bg_label.grid(row=0, column=0)

    logo_image = ctk.CTkImage(light_image=Image.open('coderslogo.png'), size=(200,150))
    logo = ctk.CTkLabel(bg_label,image=logo_image, bg_color='white',text='')
    logo.grid(row=0, column=0, sticky='nw')
    home = ctk.CTkButton(bg_label,text='Home',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    home.grid(row=0,column=0,padx=(200,6), pady=(60,0), sticky='nw')
    aboute_text = ctk.CTkButton(bg_label,text='About',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    aboute_text.grid(row=0,column=0,padx=(300,6), pady=(60,0), sticky='nw')
    hep_text = ctk.CTkButton(bg_label,text='Help',text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    hep_text.grid(row=0,column=0,padx=(400,5), pady=(60,0), sticky='nw')
    methode_var = ctk.StringVar(value="Methods")
    methode_combobox = ctk.CTkComboBox(bg_label,values=["single transferable vote", "Borda", "Instant runoff voting", "Condorcet", "Approval voting", "Plurality/FPTP"],width=100,variable=methode_var,fg_color='white',border_color='white',font=('Cooper Black',15))
    methode_combobox.grid(row=0,column=0,padx=(1,400),pady=(60,0),sticky='ne')
    helpe_btn = ctk.CTkButton(bg_label,text="Who we help",text_color='Black',font=('Cooper Black',15),fg_color='white',width=50)
    helpe_btn.grid(row=0,column=0,padx=(1,250), pady=(60,0),sticky='ne')
    vote_btn = ctk.CTkButton(bg_label,text="+ Cast your vote ",text_color='Black',font=('Cooper Black',15),fg_color='white',width=70,border_color='green',command=vote)
    vote_btn.grid(row=0,column=0,padx=(1,100), pady=(60,0),sticky='ne')
    
    description_header = ctk.CTkLabel(bg_label,text='We Make Online Elections Thorough and Effortless',text_color='Black',font=('Arial Bold',30),fg_color='white')
    description_header.grid(row=1,column=0,padx=(100,0))

    description_text = ctk.CTkLabel(bg_label,text='''
                    VoteStream is a secure online voting platform that makes it easy to run elections at a fraction of
                        the usual cost. We're the leading provider of ranked choice elections, which helps achieve 
                            more democratic outcomes by better representing the will of your votes.''',
                                    text_color='Black',font=('Arial',20),fg_color='white')
    description_text.grid(row=3,column=0,padx=(5,0))

    

    


window.mainloop()

    # opts =ctk.StringVar()
    # Label(window, textvariable=opts)
    # method_combobox = ctk.CTkComboBox(window, widget_text=opts, width=30)
    # method_combobox['values'] = ["single transferable vote", "Borda", "Instant runoff voting", "Condorcet", "Approval voting", "Plurality/FPTP"]
    # method_combobox.grid(row=0,column=0,padx=(1,350),pady=(80,0),sticky='ne')

