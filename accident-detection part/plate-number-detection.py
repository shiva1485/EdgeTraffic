import pytesseract as tess
from PIL import Image
import time
import datetime
import colorama
from colorama import Fore, Back, Style
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
import time

serialInst = serial.Serial()

portslist = []

for onePort in ports:
 portslist.append(str (onePort))
 print (str(onePort))

val = "5"

for x in range(0, len(portslist)):
 if portslist[x].startswith("COM" + str(val)):
  portVar = "COM" + str(val)
  print (portVar)


def sendcmd(cmd):
    time.sleep(2)
    command = cmd
    serialInst.write(command.encode('utf-8'))


serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

def sendcmd(cmd):
    time.sleep(2)
    command = cmd
    serialInst.write(command.encode('utf-8'))

tess.pytesseract.tesseract_cmd = r'C:\Users\SUPERUSER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
time.sleep(4)

print("\nAccident Detected!!!\n")
sendcmd("buzzerOn")

# Load the image
img = Image.open('acc1.png')

text = tess.image_to_string(img)

store =''
for x in range(11):
    store += text[x]

if store == 'UP85 AL2270':
    print(Fore.RED+"plate number is: ",store)
    
    print(Fore.RED+"\nplease wait")
    print(Fore.RED+"\nfetching the car owner details",end='')
    for i in range(6):
        print(Fore.GREEN+'.',end='')
        time.sleep(1)
        
    print(Fore.RED+"\n \nfetching data successful")
    print(Fore.RED+"\ndisplaying data:")

print(Fore.GREEN+'''\nVehicle Details Showing in Registering Authority

1. Registering Authority: Ghaziabad, Uttar Pradesh
                
Registration No: UP85AL2270
Chassis No: ME4JFSOAFKWO
Registration Date: 20-4-2019
Engine No: JFSDEWOO*****
Owner Name: DALIP KUMAR
Vehicle Class: (-M) www Cycle/Scooter(2WN)
Fuel: PETROL
Maker: HONDA MOTORCYCLE AND SCOOTER INDIA (P) LTD/ACTIVA SG
Fitness/Regn Upto: 19-Jul-2034 
Insurance Upto: 30-Jun-2024
MV Tax upte: LTT
Phone Number: +9184251681646
Father Number: +91898264664''')

print(Fore.RED+"\nextracting relative number",end='')
for i in range(6):
    print(Fore.GREEN+'.',end='')
    time.sleep(1)

print(Fore.BLUE+"\ninforming the accident to relative")
print("\nsending accident details to traffic police")
print("\nlocating nearest hospital",end='')
for i in range(6):
    print(Fore.GREEN+'.',end='')
    time.sleep(1)
print("\n \nsending message to hospital")
print("\nprinting accident details:")
print(Fore.WHITE+"\naccident location: Dawson St, Uttar Pradesh, India")
print(Fore.BLUE+"\nlive location: https://www.google.com/maps/d/viewer?ie=UTF8&t=h&oe=UTF8&msa=0&mid=1QSDHFff59t5WxziPBBisLBGW9Kc&ll=53.3412506183315%2C-6.2581974252673245&z=21")
current_time = datetime.datetime.now().time()
print(Fore.YELLOW+"\ntime of accident: ",current_time)

print(Style.RESET_ALL)