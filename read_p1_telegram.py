# DSMR P1 uitlezen
# (c) 10-2012 - GJ - gratis te kopieren en te plakken
# update Arne Kaas 10-08-2017

versie = "2.0"
import sys
import serial

##############################################################################
#Main program
##############################################################################
print "USB DSMR P1 telegram reader, version "+  versie
print "Control-C to exit"

#Set COM port config
ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize=serial.SEVENBITS
ser.parity=serial.PARITY_EVEN
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyUSB0"

#Open COM port
try:
    ser.open()
except:
    try:
        print ("Increased baudrate to 19200, retrying serial")
        ser.baudrate = 19200
        ser.open()
    except:
        sys.exit ("Fout bij het openen van %s. Aaaaarch."  % ser.name)

#print(ser.name)         # check which port was really used

#Initialize
#p1_teller is mijn tellertje voor van 0 tot 20 te tellen
telegram = ''

while True:
    p1_raw = ser.readline()
    p1_str=str(p1_raw)
    p1_line=p1_str.strip()
# als je alles wil zien moet je de volgende line uncommenten
    print (p1_line)
    telegram += str(p1_line) + '\n'
    if p1_line == '!':
	#Close port and show status
	try:
	     ser.close()
	except:	
	     sys.exit ("Oops %s. Programma afgebroken. Kon de seriele poort niet sluiten." % ser.name )
	break

text_file = open("logs/lastP1read.txt", "w")
text_file.write(telegram)
text_file.close()
