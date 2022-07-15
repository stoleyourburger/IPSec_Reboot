import getpass
import telnetlib
import time
from datetime import datetime

def main():
    #tn.read_until(b"(config)> ")
    tn.write(b"show ipsec\n")
    time.sleep(3)
    line = tn.read_very_eager()  # Read one line
    print(line)
    if b'ESTABLISHED' in line:  # last line, no more read
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("The IPSec is running.")
        print("Current Time =", current_time)
        time.sleep(5)
        main()
    else:
        tn.write(b"crypto map IPSec\n")
        line = tn.read_until(b"\n")  # Read one line
        print(line)
        time.sleep(5)
        tn.write(b"no enable\n")
        line = tn.read_until(b"\n")  # Read one line
        print(line)
        time.sleep(5)
        tn.write(b"enable\n")
        line = tn.read_until(b"\n")  # Read one line
        print(line)
        time.sleep(5)
        tn.write(b"exit\n")
        line = tn.read_until(b"\n")  # Read one line
        print(line)
        time.sleep(60)
        main()

HOST = "10.10.10.1"
user = 'pi'
password = 'nijmIs-tynkip-3gonsa'

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Login: ")
tn.write(user.encode('ascii') + b"\n")

time.sleep(2)
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

print("Logged in\n")
time.sleep(2)


main()
