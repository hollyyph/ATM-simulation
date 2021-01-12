# import Tkinter # for GUI
from time import time, ctime
from getpass import getpass
from PIL import Image, ImageDraw, ImageFont

# Dictionary
cards = list()
blocked = False
# valid = True
powerOn = True
chances = 3

cardNumber = "8888-1234-9876"
cardPIN = "012345"
cardName = "Hollyana PH"
cardBalance = 50000000

electricalBill = "983725497308"
electricalBillName = "Hollyana PH"
electricalBillAmount = 520000
electricalBillPeriod = "December 2021"

educationBill_1 = "7000118218013"
educationBillName_1 = "Hollyana PH"
educationBillAmount_1 = 12500000
educationBillPeriod_1 = "December 2021"

educationBill_2 = "31461315"
educationBillName_2 = "Hollyana PH"
educationBillAmount_2 = 1890000
educationBillPeriod_2 = "January 2021"

taxBill = "3674054612990005"
taxBillName = "Hollyana PH"
taxBillAmount = 12400000
taxBillPeriod = "2021"

t = time()
newPic = Image.new('RGB', (2000,4000), color = (255, 255, 255))
fnt = ImageFont.truetype('fake-receipt.ttf', 75)
resi = ImageDraw.Draw(newPic)
name = "AAAAAA"
resi.text((500,2000), name, fill=(0,0,0), font=fnt)
resi.text((500,2400), name, fill=(0,0,0), font=fnt)
resi.text((500,2800), name, fill=(0,0,0), font=fnt)
resi.text((500,3200), ctime(t), fill=(0,0,0), font=fnt)
newPic.show()

class Card :

    def __init__(self, number, PIN, name, balance):
        self.number = number
        self.PIN = PIN
        self.name = name
        self.balance = balance

    def getCardNumber():
        return self.number

    def getCardName():
        return self.name

    def getCardBalance():
        return self.balance

    def printCardInfo():
        print('''
        CardNumber: {}
        CardOwner: {}
        Balance: {}
        ''').format(self.number, self.name, self.balance) 

    def setCardNumber(a):
        self.number = a

    def setCardName(a):
        self.name = a

    def setCardBalance(a):
        self.balance = a

    def minBalance(angka):
        self.balance = self.balance - angka
        
    # def transaction()


cards.append(Card("8888-1234-9876", "012345", "Hollyana PH", 50000000))
cards.append(Card("8080-4168-9076", "012345", "Gloryana DH", 5000000))
cards.append(Card("8999-7272-4343", "012345", "Someone Outhere", 3550000))
cards.append(Card("8111-0332-2330", "012345", "Talking Todemoon", 8000000))
cards.append(Card("8777-4567-2654", "012345", "Happy Everafter", 15000000))

def isCardNumberValid(inputNumb):
    i= 0
    while i < len(cards):
        if (cards[i] == inputNumb):
            return True
        elif (i < len(cards)):
            i+=1
        else:
            return False
        
# main program
cards[0].printCardInfo

while (powerOn):
    print(" ")
    print("Welcome to Bank Grizzly")
    time.sleep(1.5)
    # while (valid):
    while (chances > 0):
        time.sleep(0.5)
        inputPIN = str(getpass('''Input your PIN (6 digit): 
>>>'''))
        if (inputPIN != cardPIN):
            print("Your PIN is wrong, try again!")
            chances = chances - 1
            print("Chances = " , chances)
        else :
            transaction = True
            while (transaction):
                time.sleep(2)
                print(" ")
                print("Welcome to Bank Grizzly, " + cardName)
                time.sleep(0.5)
                print("ATM Menu")
                time.sleep(0.5)
                print("1. Account Information ")
                time.sleep(0.5)
                print("2. Transfer")
                time.sleep(0.5)
                print("3. Payment")            
                time.sleep(0.5)
                print("4. Withdraw Cash")
                time.sleep(0.5)
                inputMenu = int(input('''Input your Menu choice (by number) : 
    '''))           
                if (inputMenu == 1):
                    # Account Information
                    print(" ")
                    time.sleep(0.5)
                    stringPrint = '''
                    Information Menu
                    Owner Name: {}
                    Card Number: {}
                    Balance: {}
                    '''.format(cardName, cardNumber, cardBalance)
                    print("Information Menu")
                    print("Owner Name: ", cardName)
                    print("Card Number: ", cardNumber)
                    print("Balance: ", cardBalance)

                    newPic = Image.new('RGB', (2000,4000), color = (255, 255, 255))
                    fnt = ImageFont.truetype('fake-receipt.ttf', 75)
                    resi = ImageDraw.Draw(newPic)
                    name = "AAAAAA"
                    resi.text((500,1600), "Bank Grizzly", fill=(0,0,0), font=fnt)
                    resi.text((500,2000), stringPrint, fill=(0,0,0), font=fnt)
                    resi.text((500,3200), ctime(t), fill=(0,0,0), font=fnt)
                    newPic.show()

                elif (inputMenu == 2):
                    # Transfer
                    print(" ")
                    inputTransferNum = str(input('''Transfer Number :
    '''))
                    inputTransferAmount = int(input('''Amount :
    '''))
                    if (inputTransferAmount > cardBalance):
                        print(" ")
                        time.sleep(1)
                        print ("Balance not enough")
                    else: 
                        print(" ")
                        time.sleep(2)
                        cardBalance = cardBalance - inputTransferAmount
                        print ('''Success Transfer 
    To Account Number: {}
    Rp {}
                        '''.format(inputTransferNum, inputTransferAmount))
                        time.sleep(0.5)
                        print ("Card Balance: ", cardBalance)

                elif (inputMenu == 3):
                    # Payment
                    print(" ")
                    time.sleep(0.5)
                    print("Payment Menu")
                    time.sleep(0.5)
                    print("1. Electrical Bill ")
                    time.sleep(0.5)
                    print("2. Education")
                    time.sleep(0.5)
                    print("3. Tax")            
                    time.sleep(0.5)
                    print("4. E-commerce")
                    time.sleep(0.5)

                    inputPayment = int(input('''Input your Menu choice (by number) : 
    '''))
                    print(" ")
                    if (inputPayment == 1):
                        print ('''Electrical Payment 
    Payment Number: {}
    Company: PLN
    Name: {}
    Amount: Rp {}
    Period: {}
    
                        '''.format(electricalBill, electricalBillName, electricalBillAmount, electricalBillPeriod))
                        confirm = str(input("Are you sure to pay now? (Y or N) "))
                        print(" ")
                        if (confirm == "Y" or confirm == "y"):
                            cardBalance = cardBalance - electricalBillAmount
                            time.sleep(1)
                            print ("Your electrical payment succeed" )
                            time.sleep(0.5)
                            print ("Your card balance: ", cardBalance )
                        elif (confirm == "N" or confirm == "n"):
                            time.sleep(1)
                            print ("Your electrical payment has been canceled" )


                    elif (inputPayment == 2):
                        time.sleep(0.5)
                        print("Education Payment")
                        time.sleep(0.5)
                        print("1. College ")
                        time.sleep(0.5)
                        print("2. School")

                        inputEducation = int(input('''Input your Menu choice (by number) : 
    '''))
                        print(" ")
                        if (inputEducation == 1):
                            print ('''Collage Education Payment 
    Payment Number: {}
    Company: ITB
    Name: {}
    Amount: Rp {}
    Period: {}
    
                        '''.format(educationBill_1, educationBillName_1, educationBillAmount_1, educationBillPeriod_1))
                        
                            confirm = str(input("Are you sure to pay now? (Y or N) "))
                            print(" ")
                            if (confirm == "Y" or confirm == "y"):
                                cardBalance = cardBalance - educationBillAmount_1
                                time.sleep(1)
                                print ("Your education payment succeed" )
                                time.sleep(0.5)
                                print ("Your card balance: ", cardBalance )
                            elif (confirm == "N" or confirm == "n"):
                                time.sleep(1)
                                print ("Your education payment has been canceled" )

                        elif (inputEducation == 2):
                            print ('''School Education Payment 
    Payment Number: {}
    Company: SMAK PENABUR Bintaro Jaya
    Name: {}
    Amount: Rp {}
    Period: {}

                        '''.format(educationBill_2, educationBillName_2, educationBillAmount_2, educationBillPeriod_2))
                        
                            confirm = str(input("Are you sure to pay now? (Y or N) "))
                            print(" ")
                            if (confirm == "Y" or confirm == "y"):
                                cardBalance = cardBalance - educationBillAmount_2
                                time.sleep(1)
                                print ("Your education payment succeed" )
                                time.sleep(0.5)
                                print ("Your card balance: ", cardBalance )
                            elif (confirm == "N" or confirm == "n"):
                                time.sleep(1)
                                print ("Your education payment has been canceled" )
                        else:
                            print("Wrong Input!")

                    elif (inputPayment == 3):
                        print ('''Tax Payment 
    Payment Number: {}
    Name: {}
    Amount: Rp {}
    Period: {}
    
                        '''.format(taxBill, taxBillName, taxBillAmount, taxBillPeriod))

                        confirm = str(input("Are you sure to pay now? (Y or N) "))
                        print(" ")
                        if (confirm == "Y" or confirm == "y"):
                            cardBalance = cardBalance - taxBillAmount
                            time.sleep(1)
                            print ("Your tax payment succeed" )
                            time.sleep(0.5)
                            print ("Your card balance: ", cardBalance )
                        elif (confirm == "N" or confirm == "n"):
                            time.sleep(1)
                            print ("Your tax payment has been canceled" )
                    else:
                        print("Wrong input!")                                                    
                elif (inputMenu == 4):
                    # Withdraw
                    print("Choose Nominal ")
                    time.sleep(0.5)
                    inputWithdraw = int(input('''Amount :
    '''))
                    print(" ")
                    if (inputWithdraw < cardBalance):
                        cardBalance = cardBalance - inputWithdraw
                        time.sleep(1)
                        print ("Success withdraw Rp", inputWithdraw)
                        time.sleep(0.5)
                        print ("Card Balance: ", cardBalance)

                    # print("1. Rp100.000 ")
                    # time.sleep(0.5)
                    # print("2. Rp500.000")
                    # time.sleep(0.5)
                    # print("3. Rp1.000.000")            
                    # time.sleep(0.5)
                    # print("4. Rp100.000")
                    # time.sleep(0.5)

                else:
                    print("Wrong Input!")
    
    print("Your card is blocked")

print("Quit")
quit()

    # inputNumb = str(input("Enter cardNumber: "))
    # if (not(isCardNumberValid(inputNumb))):        
    #     valid = False
    #     print("Fallllse")
    # else:
    #     time.sleep(3)
    #     inputPIN = str(input('''Input your PIN (6 digit): 
    #     '''))


            

