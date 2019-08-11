import cv2,sys,time,os
from Program.System_Check import system_compair,Dst_Check

class CCTV_VIEWER:

    def __init__(self):

        self.check_platform = system_compair()
        self.symbol = self.check_platform.check_system()

        self.ipv4 = ""
        self.usr = ""
        self.pas = ""

        print("\n\t Enter IP Address :")
        self.inPut()


    def inPut(self,Input = 1):
        if Input == 1:
            self.ipv4_start = input("\t\t\t {0} IP Viewer : ".format(self.symbol[2]))
            self.format_ip(self.ipv4_start)
        elif Input == 2:
            self.usr = input("\t\t\t {0} Username : ".format(self.symbol[2]))
            self.pas = input("\t\t\t {0} Password : ".format(self.symbol[2]))
            self.Viewer()

    def format_ip(self,ip):
        split_ip = ""
        try:
            split_ip = ip.split(".")
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
        self.ipv4 = ip
        self.inPut(2)


    def Viewer(self):
        check_dst = Dst_Check()
        check_ipv4 = check_dst.Ip_Check(self.ipv4)
        if check_ipv4 == "Opened":
                port = "554"
                url = "rtsp://{0}:{1}@{2}:{3}".format(self.usr,self.pas,self.ipv4,port)
                vcap = cv2.VideoCapture(url)
                if not vcap.isOpened():
                    os.system("cls")
                    print("[!] Wrong User&Password")

                else:

                    while (True):
                        data,frame = vcap.read()
                        cv2.imshow("VIEWER",frame)
                        key = cv2.waitKey(1)
                        if key == 27:
                            sys.exit(1)
                    cv2.release()
                    cv2.destroyWindow("VIEWER")

        else:
            print("[!] Wrong IP Desination")




"""
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
"""
