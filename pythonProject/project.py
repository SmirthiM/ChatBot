import time
import os
from twilio.rest import Client

print("WELCOME TO CHATBOT")
a = input()
b=["jupiter 125","zest 110","apache rtr","starcity+".upper()]
if a=="hai" or a=="Hai" or a=="HAI" or a=="HELLO" or a=="hello" or a=="Hello":
    print("\t Hello,***WELCOME TO TVS MOTORS***")
time.sleep(1)
print("\n VEHICLE LISTS:\n",b)
time.sleep(1)
n=input("\nPlease select your vehicle:")
if n=="jupiter 125":
    print("\t VEHICLE COLORS:")
    c=["Black","White","Grey","Brown","Red"]
    print(c)
    time.sleep(1)
    n = input("\nChoose your vehicle color:").capitalize()
    if n=="Black":
        time.sleep(1)
        print("DETAILS:\n\tCOLORS:Black\n\tPRICE:88,500\n\tMILEAGE:50 to 60km/l\n\tFUEL CAPACITY:5.8litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 8083\nFor 2 years:Monthly due is 4395\nFor 3 years:Monthly due is 3166 ")
    if n=="White":
        time.sleep(1)
        print("DETAILS:\n\tCOLORS:White\n\tPRICE:88,000\n\tMILEAGE:50 to 60km/l\n\tFUEL CAPACITY:5.8litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 8037\nFor 2 years:Monthly due is 4370\nFor 3 years:Monthly due is 3148 ")
    if n=="Grey":
        time.sleep(1)
        print("DETAILS:\n\tCOLORS:Grey\n\tPRICE:87,500\n\tMILEAGE:50 to 60km/l\n\tFUEL CAPACITY:5.8litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7991\nFor 2 years:Monthly due is 4345\nFor 3 years:Monthly due is 3130 ")
    if n=="Brown":
        time.sleep(1)
        print("DETAILS:\n\tCOLORS:Brown\n\tPRICE:87,000\n\tMILEAGE:50 to 60km/l\n\tFUEL CAPACITY:5.8litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7946\nFor 2 years:Monthly due is 4321\nFor 3 years:Monthly due is 3112 ")
    if n=="Red":
        time.sleep(1)
        print("DETAILS:\n\tCOLORS:Red\n\tPRICE:86,500\n\tMILEAGE:50 to 60km/l\n\tFUEL CAPACITY:5.8litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7900\nFor 2 years:Monthly due is 4296\nFor 3 years:Monthly due is 3094 ")
elif n=="zest 110":
    print("\nVEHICLE COLORS:")
    c = ["Blue","Black","Purple","Pink","Yellow"]
    print(c)
    time.sleep(1)
    n = input("\nChoose your vehicle color:").capitalize()
    if n=="Blue":
        print("DETAILS:\n\tCOLORS:Blue\n\tPRICE:90,000\n\tMILEAGE:48km/l\n\tFUEL CAPACITY:5litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 8220\nFor 2 years:Monthly due is 4470\nFor 3 years:Monthly due is 3220 ")
    if n=="Black":
        print("DETAILS:\n\tCOLORS:Black\n\tPRICE:93,000\n\tMILEAGE:48km/l\n\tFUEL CAPACITY:5litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 8494\nFor 2 years:Monthly due is 4619\nFor 3 years:Monthly due is 3327 ")
    if n=="Purple":
        print("DETAILS:\n\tCOLORS:Purple\n\tPRICE:92,000\n\tMILEAGE:48km/l\n\tFUEL CAPACITY:5litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 8402\nFor 2 years:Monthly due is 4569\nFor 3 years:Monthly due is 3291 ")
    if n=="Pink":
         print("DETAILS:\n\tCOLORS:Pink\n\tPRICE:91000\n\tMILEAGE:48km/l\n\tFUEL CAPACITY:5litre")
         print("RATE OF INTEREST FOR EMI IS 9.6%")
         print("For 1 year:Monthly due is 8311\nFor 2 years:Monthly due is 4519\nFor 3 years:Monthly due is 3225 ")
    if n=="Yellow":
        print("DETAILS:\n\tCOLORS:Yellow\n\tPRICE:90000\n\tMILEAGE:48km/l\n\tFUEL CAPACITY:5litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 8220\nFor 2 years:Monthly due is 4470\nFor 3 years:Monthly due is 3220")
elif n=="apache rtr":
    print("\nVEHICLE COLORS:")
    c = ["White","Black","Grey","Red","Blue"]
    print(c)
    time.sleep(1)
    n = input("\nChoose your vehicle color:").capitalize()
    if n=="White":
        print("DETAILS:\n\tCOLORS:White\n\tPRICE:1,36,000\n\tMILEAGE:45 to 60km/l\n\tFUEL CAPACITY:12litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 12421\nFor 2 years:Monthly due is 6755\nFor 3 years:Monthly due is 4865 ")
    if n=="Black":
        print("DETAILS:\n\tCOLORS:Black\n\tPRICE:1,38,000\n\tMILEAGE:45 to 60km/l\n\tFUEL CAPACITY:12litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 12604\nFor 2 years:Monthly due is 6854\nFor 3 years:Monthly due is 4937 ")
    if n=="Grey":
        print("DETAILS:\n\tCOLORS:Grey\n\tPRICE:1,36,500\n\tMILEAGE:45 to 60km/l\n\tFUEL CAPACITY:12litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 12467\nFor 2 years:Monthly due is 6780\nFor 3 years:Monthly due is 4883 ")
    if n=="Red":
        print("DETAILS:\n\tCOLORS:Red\n\tPRICE:1,37,500\n\tMILEAGE:45 to 60km/l\n\tFUEL CAPACITY:12litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 12558\nFor 2 years:Monthly due is 6829\nFor 3 years:Monthly due is 4919 ")
    if n=="Blue":
        print("DETAILS:\n\tCOLORS:Blue\n\tPRICE:1,37,000\n\tMILEAGE:45 to 60km/l\n\tFUEL CAPACITY:12litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 12554\n For2 years:Monthly due is 6804\n For3 years:Monthly due is 4901 ")
elif n=="starcity+":
    print("\nVEHICLE COLORS:")
    c = ["Red","Black","Blue","Grey","Blue silver"]
    print(c)
    time.sleep(1)
    n = input("\nChoose your vehicle color:").capitalize()
    if n=="Red":
        print("DETAILS:\n\tCOLORS:Red\n\tPRICE:80,000\n\tMILEAGE:68km/l\n\tFUEL CAPACITY:10litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7306\nFor 2 years:Monthly due is 3973\nFor 3 years:Monthly due is 2862 ")
    if n=="Black":
        print("DETAILS:\n\tCOLORS:Black\n\tPRICE:82,000\n\tMILEAGE:68km/l\n\tFUEL CAPACITY:10litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7489\nFor 2 years:Monthly due is 4072\nFor 3 years:Monthly due is 2933 ")
    if n=="Blue":
        print("DETAILS:\n\tCOLORS:Blue\n\tPRICE:80,500\n\tMILEAGE:68km/l\n\tFUEL CAPACITY:10litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7352\nFor 2 years:Monthly due is 3998\nFor 3 years:Monthly due is 2880 ")
    if n=="Grey":
        print("DETAILS:\n\tCOLORS:Grey\n\tPRICE:81,000\n\tMILEAGE:68km/l\n\tFUEL CAPACITY:10litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7398\nFor2 years:Monthly due is 4023\nFor3 years:Monthly due is 2898 ")
    if n=="Blue silver":
        print("DETAILS:\n\tCOLORS:Blue silver\n\tPRICE:82,500\n\tMILEAGE:68km/l\n\tFUEL CAPACITY:10litre")
        print("RATE OF INTEREST FOR EMI IS 9.6%")
        print("For 1 year:Monthly due is 7535\nFor 2 years:Monthly due is 4097\nFor 3 years:Monthly due is 2951 ")
time.sleep(1)
x=input("\n ARE YOU WILLING TO PROCEED:").lower()
if x=="yes":
    print("Choose your payment mode:\t* By full cash\n\t\t\t\t\t\t\t* By EMI ")
    m=input("SELECT:").upper()
    if m=="BY FULL CASH":
        print("OK,We will proceed with your reports")
    elif m=="EMI":
        print("Once your vehicle purchase is complete,you will need to repay the loan through monthly EMI's")
        print("EMI DETAILS:\n\t 1 year\n\t 2 year\n\t 3 year")
        y=input("Select your EMI year:")
    else:
        print("\n\tOK,THANK YOU")
v=int(input("Enter the phone number:"))
account_sid = " ACCOUNT ID"
auth_token = "AUTH TOKEN"
verify_sid = "VERIFY ID"
verified_number = "PHONE NUMBER"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print("otp verified ")
print("Yor booking was done successfully")
time.sleep(1)
print("\n\tOK,THANK YOU")
print("\n\t FOR FURTHER DETAILS:\n Please contact us:##########")









