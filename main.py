# Taking user email id input
email=input("Enter a valid email ID: ").strip()
#Extracting user name
user_name=email[:email.index("@")]
#Extracting domain name
doamin_name=email[email.index("@")+1:]
#printing result
result = "Your username is '{}' and your domain name is '{}' :".format(user_name,doamin_name)

print(result)