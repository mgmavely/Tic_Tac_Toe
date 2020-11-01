import random
import twilVar

#Uses for loop to generate random 8-digit verification code and returns
def otpGenerator():
    retVal = 0;
    for i in range(8):
        randVal = random.randint(0,9)
        retVal += randVal
        retVal *= 10
    return retVal

#Function that sends message given user inputted number and random password
def messageSend(inpNum, password):
    message = twilVar.client.messages.create(
        body="Your verification password is: " + str(password),
        from_=twilVar.twilNum,
        to='+' + str(inpNum)
        )

#Function that validates proper phone number entry
def phoneNumValidate():
    retVal = input('Enter your phone number (with area code i.e Canada [1])\n+')
    return retVal

#Function that verifies the user has entered the random generated password
#received via SMS
def authValidate():
    while True:
        inp = input('Enter the verification code: \n')
        if inp == str(password):
            print('Success!\n')
            break
        else:
            print('Invalid password, try again!\n')
                

password = otpGenerator()
inputNumber = phoneNumValidate()
messageSend(inputNumber, password)
authValidate()


        
            
