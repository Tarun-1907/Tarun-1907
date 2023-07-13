def validemail():
  email=input("Enter an Email: \n")
  j=0,
  l=0,
  m=0
  if len(email)>=6:                 
    if email[0].isalpha():         
        if (email[-4]==".") ^ (email[-3]=="."):        
            if "@" in email and email.count("@")==1:    
                for i in email:
                    if i==i.isspace():      
                       j=1
                    elif i.isdigit():                              
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    elif i.isalpha():        
                        if i==i.upper():     
                            l=1
                    else:
                        m=1
                print("\n All conditions are satisfied. This is an valid email.")
                if j==1 or l==1 or m==1:
                    print("\n Wrong email !!")
                    print("Condition 5 is not satisfied.")
            else:
                print("\n Wrong email !!")
                print("Condition 4 is not satisfied.")
        else:
            print("\n Wrong email !!")
            print("Condition 3 is not satisfied.")
    else:
        print("\n Wrong email !!")    
        print("Condition 2 is not satisfied.")
  else:
    print("\n wrong email !!")
    print("Condition 1 is not satisfied.")
    
print("Conditions for a valid email !!\n")
def conditions():
  print("C1. Email must contains 6 or more than 6 strings")
  print("C2. Email must starts with alphabet")
  print("C3."'.'"must be at the fourth last or third last position")
  print("C4. Email must and only have one '@'")
  print("C5. Email must not contain any space or any upper letter and only contain this three( _ . @ ) special characters\n")  
conditions()
validemail()    