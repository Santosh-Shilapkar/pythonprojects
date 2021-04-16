def sliceemail(email):
    for i in range(len(email)):
        if email[i]=="@":
            index=i
            break
    username=email[:index]
    domain=email[index+1:]
    print(f" Your username is {username} and domain is {domain}")


###driver code
print("Helo")
email=input("Enter your email address:").strip()
print(email)  
sliceemail(email)  


