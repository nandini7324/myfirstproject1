dict={"1.hero":"50 RS",
      "2.honda":"70 RS",
      "3.yamaha":"90 RS"}
hero=50
zero=70
yamaha=90
available_bike=10 
while True:
   print("------BIKE RENTRAL SERVICE------")
   print("1. show available bikes")
   print("2. Rent a bike")
   print("3. show rented bikes")
   print("4. exit")
   x=int(input("Enter your choice"))
   if x==1 :
      print("Available bike :",available_bike)
   elif x<0 :
      print("NOT valid")
   elif x==2 :
      a=str(input("Enter your name : "))
      print("Which bike would you like\n",dict)
      b=int(input("Enter bike number:"))
      c=int(input("How many hours :"))
      if b==1 :
         total=b*hero*c
         print(f"{a} , rented hero for {c} hours. total : {total}" )
      if b==2 :
         total=b*zero*c
         print(f"{a} , rented honda for {c} hours. total : {total} "  )
      if b==3 :
         total=b*yamaha*c
         print( f"{a} , rented yamaha for {c} hours. total :{total} " )
   elif x==3 :
      print("Rented bike information :\n")
   elif x==4 :
      print("thank you for using the services")   
      break
   else :
      print("not valid")
      break
      

      
   
       

     
     
         

       

      
