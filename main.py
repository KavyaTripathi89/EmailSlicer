import re   
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

def check():  
    email = input("Enter a valid Email ID: ")
    if(re.search(regex,email)): 
        print("Valid Email") 
        email.strip()
        user_name=email[:email.index("@")]
        doamin_name=email[email.index("@")+1:]
        result = "Your username is '{}' and your domain name is '{}' :".format(user_name,doamin_name)
        print(result)
    else:   
        print("Invalid Email") 
        
check()
while input("\n Do you want to Check again 'yes' or 'no': ").lower()=='yes':
    check()


