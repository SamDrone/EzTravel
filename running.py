#Program for Sales
#---------------------------------------------------H & General OTC SALE:------------------------------------------
import pickle
import os
class chemist():
    def __init__(self):
        self.Name=""
        self.Price=0.0
        self.BNo=""                 #BNo-Batch Number
        self.MFD=""                 #MFD-Manufactured Date
        self.EXP=""                 #EXP-Expiry Date
        self.Quantity=0
        self.Bcode=""               #Bcode-Bar code
        self.Schedule=""
        self.Netprice=0
    def checkschedule(self):
        if len(self.Bcode)>4:
            print "Schedule=H1"
            print "Please switch to H1 Sales:"
            H1Menu()
        if len(self.Bcode)==4:
            print "Schedule=H"
        if len(self.Bcode)==3:
            print "Schedule=Plain"
    def inputdata(self):
        self.Name=raw_input("Enter Drug Name ")
        self.Price=input("Enter Price ")
        self.BNo=raw_input("Enter BNo ")
        self.MFD=raw_input("Enter MFD ")
        self.EXP=raw_input("Enter EXP ")
        self.Bcode=raw_input("Enter Bcode ")
        self.schedule=self.checkschedule()
        self.Quantity=input("Enter Quantity ")
        self.Netprice=self.Quantity*self.Price
    def Display(self):
        print self.Name,"Name of Drug"
        print self.Price,"Price"
        print self.BNo,"Batch No"
        print self.MFD,"Manufacture Date"
        print self.EXP,"Expiry Date"
        print self.Bcode,"Barcode"
        print self.Quantity,"Quatity "
        print self.Netprice,"Netprice "
    def getBcode(self):
        return self.Bcode
    def moddata(self,bc) :
            print("Enter New Details: ")
            print
            print 
            self.bcode=bc
            self.Price=input("Enter Price ")
            self.BNo=raw_input("Enter BNo ")
            self.MFD=raw_input("Enter MFD ")
            self.EXP=raw_input("Enter EXP ")
            self.Quantity=input("Enter Quantity ")
            self.Netprice=self.Quantity*self.Price
A=chemist()
A.checkschedule()
def checkBcode(Bcode) :
     flag=False
     fin=open("chemist1.log","rb")
     try :
          while True :
               A=pickle.load(fin)
               
               if A.getBcode()==Bcode :
                    flag=True
               else :
                    flag=False
     except EOFError :
          #print "End of file encountered"
          fin.close()          

     return flag
         
            
def indata() :
    ans='y'
    print("Drug Details")
    fout=open("chemist1.log",'ab')
    if not fout :
         print "File doesn't exists"
    else :     
         while ans=='y' or ans=='Y' :
              A.inputdata()
              Bcode=A.getBcode()
              res=checkBcode(Bcode)
              #print res
              if res :
                  print "Record already exists" 
              else :
                  pickle.dump(A,fout)
                  print "Record Saved "
              
              ans=raw_input("Do you wish to add more records (y/n)")     
    fout.close()
    
def srch() :
     fin=open("chemist1.log","rb")
     print "Searching of a record "
     bc=raw_input("Enter the Bcode to be searched ")
     try :
          while True :
              A=pickle.load(fin)
              A.Display() 
              
              if A.getBcode()==bc :
                  print "Record found "
                  A.Display()
                  fd='y'
                  break
              else:
                  fd='n'
           
         
     except EOFError :
          fin.close()
     if fd=='n' :
            print "Record not found"
            
def dele():
    print "DELETION OF RECORD"
    fin=open("chemist1.log", "rb")
    fout=open("temp.log","wb")
    Bcode=raw_input("Enter the item Bcode whose record is to be deleted ") 
    try :
         while True :
            A=pickle.load(fin)
            r=A.getBcode()
            if r==Bcode :
                 print "Record found"
                 A.Display()
                 fd='y'
                 confirm=raw_input("Do you wish to keep the record (y/n)")
                 if confirm=='n' :
                      pickle.dump(A,fout)
                                      
            else :
                 pickle.dump(A,fout)
                 fd='n' 
           
    except EOFError :
        fin.close()
        fout.close()
    os.remove("chemist1.log")
    os.rename("temp.log","chemist1.log")
    
    if fd=='n' :
        print "Record not found"
      
def modi():
    print "MODIFICATION OF RECORD"
    fin=open("chemist1.log", "rb")
    fout=open("temp.log","wb")
    
    bc=raw_input("Enter the item Bcode whose record is to be modified ") 
    try :
        while True :
            A=pickle.load(fin)
            r=A.getBcode()
            if r==bc :
                print "Record found"
                A.Display()
                fd='y'
                pos=fin.tell()
                #print "position =",pos
                nm=A.Bcode
                A.moddata(bc)
                fin.seek(pos)
                pickle.dump(A,fout)
                 
            else :
                pickle.dump(A,fout)
                fd='n' 

    except EOFError :
        fin.close()
        fout.close()
    os.remove("chemist1.log")
    os.rename("temp.log","chemist1.log")
    if fd=='n' :
        print "Record not found"


#-----------------------------------------------------H1sales-----------------------------------------------------------
import pickle
import os
class H1Sales():
    def __init__(self):
        self.Date=0
        self.CName=""
        self.PhNo=0
        self.Dname=""
        self.RegNo=0
        self.Quantity=0
        self.Name=""
        self.BNO=""
        self.EXP=0
        self.Price=0.0
        self.Bcode=""   
        self.Netprice=0
        self.CMNO=0
    def Readdata(self):
        self.Date=input("Enter Date Of Purchase:")
        self.CName=raw_input("Enter Customer Name:")
        self.PhNo=input("Enter Phone Number Of Customer:")
        self.Dname=raw_input("Enter Doctor Name:")
        self.RegNo=input("Enter DMC/IMC Registered Number:")
        self.Bcode=raw_input("Enter Bcode:")
        self.Quantity=input("Enter Quantity:")
        self.Name=raw_input("Enter Drug Name:")
        self.BNO=raw_input("Enter BNo:")
        self.EXP=raw_input("Enter EXP:")
        self.Price=input("Enter Price:")
        self.Netprice=self.Quantity*self.Price
        self.CMNO=input("Enter Cash Memo Number")
    def Display(self):
        print "H1 Details:"
        print self.Date,"Date of Purchase"
        print self.CName,"Customer Name"
        print self.PhNo,"Customer phone Number"
        print self.Dname,"Doctor Name"
        print self.RegNo,"DMC/IMC"
        print self.Bcode,"Barcode of Drug"
        print self.Quantity,"Quantity"
        print self.Name,"Name of Drug"
        print self.BNO,"Batch Number"
        print self.EXP,"Expiry Date"
        print self.Price,"Price of Drug"
        print self.Netprice,"Total Price of Drug "
        print self.CMNO,"Cashmeno Number"
    def getBcode(self):
        return self.Bcode
    def moddata(self,bc) :
        print("Enter New Data of Sale:")
        self.bcode=bc
        self.BNO=raw_input("Enter BNo:")
        self.EXP=raw_input("Enter EXP:")
        self.Price=input("Enter Price:")
        self.Netprice=self.Quantity*self.Price
        self.CMNO=input("Enter Cash Memo Number:")


B=H1Sales()

def checkBcode1(Bcode) :
    flag=False
    fin=open("H1sales1.log","rb")
    try :
        while True :
            B=pickle.load(fin)
            if B.getBcode()==Bcode :
                flag=True
            else :
                flag=False
    except EOFError :
         #print "End of file encountered"
         fin.close()          
    return flag
         
            
def indata1() :
    ans='y'
    print("Drug Details")
    fout=open("H1sales1.log",'ab')
    if not fout :
         print "File doesn't exists"
    else :     
         while ans=='y' or ans=='Y' :
             B.Readdata()
             Bcode=B.getBcode()
             res=checkBcode1(Bcode)
              #print res
             if res :
                 print "Record already exists" 
             else :
                 pickle.dump(B,fout)
                 print "Record Saved "
              
             ans=raw_input("Do you wish to add more records (y/n)")     
    fout.close()
    
     
def srch1() :
     fin=open("H1sales1.log","rb")
     print "Searching of a record "
     bc=raw_input("Enter the Bcode to be searched ")
     try :
          while True :
              B=pickle.load(fin)           
              if B.getBcode()==bc :
                  print "Record found "
                  B.Display()
                  fd='y'
                  break
              else:
                  fd='n'
           
         
     except EOFError :
          fin.close()
     if fd=='n' :
            print "Record not found"
            
def dele1():
    print "DELETION OF RECORD"
    fin=open("H1sales1.log", "rb")
    fout=open("temp.log","wb")
    Bcode=raw_input("Enter the item Bcode whose record is to be deleted ") 
    try :
         while True :
             B=pickle.load(fin)
             r=B.getBcode()
             if r==Bcode :
                 print "Record found"
                 B.Display()
                 fd='y'
                 confirm=raw_input("Do you wish to delete the record (y/n)")
                 if confirm=='y' :
                     pickle.dump(B,fout)                    
             else :
                 pickle.dump(B,fout)
                 fd='n' 
           
    except EOFError :
        fin.close()
        fout.close()
    os.remove("H1sales1.log")
    os.rename("temp.log","H1sales1.log")    
    if fd=='n' :
        print "Record not found"
      
def modi1():
    print "MODIFICATION OF RECORD"
    fin=open("H1sales1.log", "rb")
    fout=open("temp.log","wb")
    bc=raw_input("Enter the item Bcode whose record is to be modified ") 
    try :
         while True :
             B=pickle.load(fin)
             r=B.getBcode()
             if r==bc :
                 print "Record found"
                 B.Display()
                 fd='y'
                 pos=fin.tell()
                 #print "position =",pos
                 nm=B.Bcode
                 B.moddata(bc)
                 fin.seek(pos)
                 pickle.dump(B,fout)
             else :
                 pickle.dump(B,fout)
                 fd='n' 
    except EOFError :
        fin.close()
        fout.close()
    os.remove("H1sales1.log")
    os.rename("temp.log","H1sales1.log")
    if fd=='n' :
        print "Record not found"


#Program for Purchases
#------------------------------Purchase-------------------------------
import pickle
def Purchase():
    class purchase():
        def __init__(self):
            self.Stockist=""
            self.Name=""
            self.EXP=""
            self.BNo=""
            self.schedule=""
            self.WSPrice=0                      #WSPrice-WholesalePrice
            self.RPrice=0                      #RPrice=RetailPrice
            self.Quantity=0
            self.Total=0
        def Inputdata(self):
            self.Stockist=raw_input("Enter Name Of Supplier ")
            self.Name=raw_input("Enter Name Of Drug ")
            self.EXP=raw_input("Enter EXP ")
            self.BNo=raw_input("Enter BNo ")
            self.schedule=raw_input("Enter Schedule ")
            self.WSPrice=input("Enter Whole Sale Price ")
            self.RPrice=input("Enter Retail Price ")
            self.Quantity=input("Enter Quatity ")
            self.Total=self.Quantity*self.WSPrice
        def Display(self):
            print self.Stockist,"Supplier of Drug"
            print self.Name,"Drug Name"
            print self.EXP,"Expiry Date"
            print self.BNo,"Batch Number"
            print self.schedule,"Schedule of Drug"
            print self.WSPrice,"WholeSale Price"                     
            print self.RPrice,"Retail Price"                     
            print self.Quantity,"Quantity"
            print self.Total,"Total amount"
        def listdata2(self) :
            print "-"*92
            print '{0:^2}{1:^15}{2:^10}{3:^10}{4:^7}{5:^7}{6:^10}{7:^10}{8:^10}{9:^10}'.format(Sno,self.Stockist,self.Name,self.EXP,self.BNo,self.schedule,self.WSPrice,self.RPrice,self.Quantity,self.Total)  
    A=purchase()
    A.Inputdata()
    F1=open("Purchases.log","ab")
    pickle.dump(A,F1)
    F1.close()
   
#Program for Details
#-------------------------------Details--------------------------------
def Details1():
    n=input("Enter number of items")
    for i in range(n):
        if n<=10:
            Bcode=input("Enter The Barcode")
            if Bcode==89041:
                print "Name-Vintor4000"
                print "Drug-H1"
                print "Quantity-6"
                print "BNo-061323V24"
                print "MFD-JUL-2016"
                print "EXP-JUN-2018"
                print "Price-1318.80"
            if Bcode==17904:
                print "Name-CRESAR-H"
                print "Drug-H1"
                print "Quantity-4"
                print "BNo-A32266"
                print "MFD-OCT-2016"
                print "EXP-MAR-2018"
                print "Price-76.00"
            if Bcode==14911:
                print "Name-MAHACEF XL 200"
                print "Drug-H1"
                print "Quantity-4"
                print "BNo-A1DRN017"
                print "MFD-JAN-2016"
                print "EXP-DEC-2018"
                print "Price-125.00"
            if Bcode==1110:
                print "Name-FLORA Zn"
                print "Drug-H"
                print "Quantity-3"
                print "BNo-A0CTN018"
                print "MFD-MAR-2016"
                print "EXP-AUG-2018"
                print "Price-10.00"
            if Bcode==1201:
                print "Name-BUDECORT-0.5mg"
                print "Drug-H"
                print "Quantity-3"
                print "BNo-G31051"
                print "MFD-DEC-2016"
                print "EXP-NOV-2018"
                print "Price-137.50"
            if Bcode==1202:
                print "Name-BUDECORT-1mg"
                print "Drug-H"
                print "Quantity-3"
                print "BNo-A04835"
                print "MFD-APR-2016"
                print "EXP-MAR-2018"
                print "Price-150.00"
            if Bcode==1971:
                print "Name-ASTHALIN"
                print "Drug-H"
                print "Quantity-3"
                print "BNo-A40865"
                print "MFD-APR-2016"
                print "EXP-MAR-2019"
                print "Price-18.40"
            if Bcode==111:
                print "Name-FLORA-BC"
                print "Drug-P"
                print "Quantity-3"
                print "BNo-E7AHN004"
                print "MFD-JAN-2017"
                print "EXP-JUN-2018"
                print "Price-21.90"
            if Bcode==152:
                print "Name-D'COLD TOTAL"
                print "Drug-P"
                print "Quantity-3"
                print "BNo-B0428"
                print "MFD-OCT-2013"
                print "EXP-SEP-2016"
                print "Price-26.60"
            if Bcode==780:
                print "Name-DEXORANGE 100ml"
                print "Drug-P"
                print "Quantity-6"
                print "BNo-K13375"
                print "MFD-JUL-2015"
                print "EXP-DEC-2017"
                print "Price-89.00"
        else:
            print "Enter Valid Barcode"
def Details2():
    print "Medicinal Company Are:"
    print "1.Cipla"
    print "2.Mankind"
    print "3.General Drug" 
    ch=input("Enter Your Choice:")
    if ch==1:
        F=open("Cipla.txt","r")
        A=F.read()
        print A
        F.close()
    elif ch==2:
        F1=open("Mankind.txt","r")
        B=F1.read()
        print B
        F1.close()
    elif ch==3:
        F3=open("General(OTC).txt","r")
        C=F3.read()
        print C
        F3.close()

#Program for Reports
#------------------------------drug Inspection--------------------------
class chemist():
    def __init__(self):
        self.Name=""
        self.Price=0.0
        self.BNo=""                 #BNo-Batch Number
        self.MFD=""                 #MFD-Manufactured Date
        self.EXP=""                 #EXP-Expiry Date
        self.Quantity=0
        self.Bcode=""               #Bcode-Bar code
        self.Schedule=""
        self.Netprice=0
    def read(self):
        self.BNo=raw_input("Enter BNo ")
    def getBcode(self):
        return self.Bcode  
    def Display(self):
        print self.Name,"Name of Drug"
        print self.Price,"Price"
        print self.BNo,"Batch No"
        print self.MFD,"Manufacture Date"
        print self.EXP,"Expiry Date"
        print self.Bcode,"Barcode"
        print self.Quantity,"Quatity "
        print self.Netprice,"Netprice "
    def listdata(self) :
            print '\n'
            print "-"*90
            print '{0:^15}{1:^10}{2:^10}{3:^10}{4:^10}{5:^10}{6:^10}{7:^10}'.format(self.Name,self.Price,self.BNo,self.MFD,self.EXP,self.Bcode,self.Quantity,self.Netprice)
    def moddata(self,bc) :
            print("Enter New Details: ")
            print
            print 
            self.bcode=bc
            self.Price=input("Enter Price ")
            self.BNo=raw_input("Enter BNo ")
            self.MFD=raw_input("Enter MFD ")
            self.EXP=raw_input("Enter EXP ")
            self.Quantity=input("Enter Quantity ")
            self.Netprice=self.Quantity*self.Price
def repH() :
    F=open("Chemist1.log","rb")
    print "\nList of records are as follows......"
    print    '{0:^15}{1:^10}{2:^10}{3:^10}{4:^10}{5:^10}{6:^10}{7:^10}'.format("Name","Price","BNo","MFD","EXP","Bcode","Quantity","Netprice")
    try :
        while True :
            C=pickle.load(F)
            C.listdata()
            
    except EOFError :    
        F.close()

class H1Sales():
    def __init__(self):
        self.Date=0
        self.CName=""
        self.PhNo=0
        self.Dname=""
        self.RegNo=0
        self.Bcode=""
        self.Quantity=0
        self.Name=""
        self.BNO=""
        self.EXP=0
        self.price=0.0
        self.Netprice=0.0
        self.CMNO=0
    def read(self):
        self.BNo=raw_input("Enter BNo ")
    def getBcode(self):
        return self.Bcode   
    def Display(self):
        print "H1 Details:"
        print self.Date,"Date of Purchase"
        print self.CName,"Customer Name"
        print self.PhNo,"Customer phone Number"
        print self.Dname,"Doctor Name"
        print self.RegNo,"DMC/IMC"
        print self.Bcode,"Barcode of Drug"
        print self.Quantity,"Quantity"
        print self.Name,"Name of Drug"
        print self.BNO,"Batch Number"
        print self.EXP,"Expiry Date"
        print self.Price,"Price of Drug"
        print self.Netprice,"Total Price of Drug "
        print self.CMNO,"Cashmeno Number"
    def listdata1(self):
        print '\n'
        print "-"*125
        print '{0:^7}{1:^10}{2:^5}{3:^10}{4:^7}{5:^8}{6:^10}{7:^10}{8:^10}{9:^10}{10:^10}{11:^10}'.format(self.Date,self.CName,self.PhNo,self.Dname,self.RegNo,self.Bcode,self.Quantity,self.Name,self.BNO,self.EXP,self.Price,self.Netprice,self.CMNO)

def repH1():
    F3=open("H1Sales1.log","rb")
    print "\nList of records are as follows......"
    print  '{0:^7}{1:^10}{2:^5}{3:^10}{4:^7}{5:^8}{6:^10}{7:^10}{8:^10}{9:^10}{10:^10}{11:^10}'.format("Date","CName","PhNo","Dname","RegNo","Bcode","Quant","Name","BNo","EXP","Price","Netprice","CMNO")
    try:
        while True:
            C=pickle.load(F3)
            C.listdata1()
          
    except EOFError:
            F3.close()

class purchase():
    def __init__(self):
        self.Stockist=""
        self.Name=""
        self.EXP=""
        self.BNo=""
        self.schedule=""
        self.WSPrice=0                      #WSPrice-WholesalePrice
        self.RPrice=0                      #RPrice=RetailPrice
        self.Quantity=0
        self.Total=0
    
    def Display(self):
            print self.Stockist,"Supplier of Drug"
            print self.Name,"Drug Name"
            print self.EXP,"Expiry Date"
            print self.BNo,"Batch Number"
            print self.schedule,"Schedule of Drug"
            print self.WSPrice,"WholeSale Price"                     
            print self.RPrice,"Retail Price"                     
            print self.Quantity,"Quantity"
            print self.Total,"Total amount"
    def listdata2(self) :
        print "-"*92
        print '{0:^15}{1:^10}{2:^10}{3:^7}{4:^7}{5:^10}{6:^10}{7:^10}{8:^10}'.format(self.Stockist,self.Name,self.EXP,self.BNo,self.schedule,self.WSPrice,self.RPrice,self.Quantity,self.Total)
def repP():
    F3=open("Purchases.log","rb")
    print  '{0:^15}{1:^10}{2:^10}{3:^7}{4:^7}{5:^10}{6:^10}{7:^10}{8:^10}'.format("Stockist","Name","EXP","BNO","Schedule","WSPrice","RPrice","Quantity","Totall")
    
    try:
        while True:
            D=pickle.load(F3)
            D.listdata2()
            
    except EOFError:
            F3.close()

#Program for Main Menu
#-------------------------------main-----------------------------------
def Mainmenu():
    print "\t\t\tEnter your choice:"
    print "\t\t\t1.Sales"
    print "\t\t\t2.Purchses"
    print "\t\t\t3.Details"
    print "\t\t\t4.Drug Inspections"
    print "\t\t\t5.Exit"
    choice=input("Enter Your Choice")
    if choice==1:
        print "\t\t\t1.H & General(OTC) Sale"
        print "\t\t\t2.H1 Sales"
        n=input("\t\t\tEnter your choice")
        if n==1:
            HMenu()
        if n==2:
            H1Menu()
        Mainmenu()
    elif choice==2:
        Purchase()
        Mainmenu()
    elif choice==3:
        print "\t\t\tDetails Section:"
        print "\t\t\t1.Details-Red Strip Medicine"
        print "\t\t\t2.Company-Medicines"
        a=input("\t\t\tEnter Your Choice:")
        if a==1:
            Details1()
        if a==2:
            Details2()
        Mainmenu()
    elif choice==4:
        print "\t\t\tDrug Inspections:"
        print "\t\t\t1.DisplayChemist"
        print "\t\t\t2.DisplayH1salses"
        print "\t\t\t3.Displaypurchase"
        c=input("\t\t\tEnter Your choice:")
        if c==1:
            repH()
        if c==2:
            repH1()
        if c==3:
            repP()
        Mainmenu()
    else:
        print "\t\t\tCounter is closed"
def HMenu():
    print "\t\t\tH & General OTC SALE:"
    print "\t\t\t1.Insertion"
    print "\t\t\t2.Searching"
    print "\t\t\t3.Modification"
    print "\t\t\t4.Deletion"
    print "\t\t\t5.Main Menu"
    choice=input("\t\t\tEnter the number")
    if choice==1:
        indata()
        HMenu()
    elif choice==2:
        srch()
        HMenu()
    elif choice==3:
        modi()
        HMenu()
    elif choice==4:
        dele()
        HMenu()
    else:
        Mainmenu()
        
def H1Menu():
    print "\t\t\tH1 SALE:"
    print "\t\t\t1.Insertion"
    print "\t\t\t2.Searching"
    print "\t\t\t3.Modification"
    print "\t\t\t4.Deletion"
    print "\t\t\t5.Main Menu"
    choice=input("\t\t\tEnter the number")
    if choice==1:
        indata1()
        H1Menu()
    elif choice==2:
        srch1()
        H1Menu()
    elif choice==3:
        modi1()
        H1Menu()
    elif choice==4:
        dele1()
        H1Menu()
    elif choice==5:
        Mainmenu()
Mainmenu()
