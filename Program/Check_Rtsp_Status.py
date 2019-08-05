import socket,sys
from prettytable import PrettyTable

class IPCam_Check_Status:

    def __init__(self):

        self.x = PrettyTable()
        self.x.field_names = ["No","IP_Address","Port_Status"]


        print("\n\t Enter IP Address :")
        self.inPut()


    def inPut(self,Input = 1):
        if Input == 1:
            self.ipv4_start = input("\t\t\t \u21B3 From IPv4 : ")
            self.format_ip_start(self.ipv4_start)
        elif Input == 2:
            self.ipv4_end = input("\t\t\t \u21B3 To IPv4   : ")
            self.format_ip_end(self.ipv4_end)
            self.Check_Stats()

    def format_ip_start(self,ip_start):
        split_ip = ""
        try:
            split_ip = ip_start.split(".")
        except:
            self.inPut()
        if len(split_ip) != 4:
            self.inPut()
        for ip_digit in split_ip:
            if not ip_digit.isdigit():
                self.inPut()
            try:
                if int(ip_digit)< 0 or int(ip_digit) > 255:
                    self.inPut()
            except:
                self.inPut()
        self.start = split_ip[3]
        self.inPut(2)

    def format_ip_end(self,ip_end):
        split_ip = ""

        try:
            split_ip = ip_end.split(".")
        except:
            self.inPut(2)

        if len(split_ip) != 4:
            self.inPut(2)
        for ip_digit in split_ip:
            if not ip_digit.isdigit():
                self.inPut(2)
            try:
                if int(ip_digit)< 0 or int(ip_digit) > 255:
                    self.inPut(2)
            except:
                pass
        self.end = split_ip[3]

    def Check_Stats(self):

        split_ip = ""
        sort_ip = ""
        if self.start < self.end:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for i in range(int(self.start), int(self.end)):

                split_ip = self.ipv4_start.split(".")
                sort_ip = "%s.%s.%s.%s" % (split_ip[0], split_ip[1], split_ip[2], i)
                self.sock.settimeout(1)
                self.result = self.sock.connect_ex((sort_ip, 554))
                if self.result == 0:
                    self.x.add_row(["*", sort_ip, "Opened"])
                else:
                    pass
            print("\n")
            print(self.x)

            self.sock.close()
            sys.exit(1)

        elif self.start > self.end:
            self.inPut(2)
        else:
            pass

