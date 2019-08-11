import platform
import socket

class system_compair:

    def __init__(self):
        super().__init__()
        self.symbol = ()
        self.unknow = ()
        self.plat_form = ""

        self.check_system()

    def check_system(self):
        self.plat_form = platform.system()
        if self.plat_form == "Windows":
            self.symbol = ("\u2B5D","\u2B9A","\u21B3")
            return self.symbol
        elif self.plat_form == "Linux":
            pass
        elif self.plat_form == "Darwin":
            self.symbol = ("\u21B4","\u21A3","\u21B3")
            return self.symbol
        else:
            pass

class Dst_Check():

    def __init__(self):
        super().__init__()

    def Ip_Check(self,ipv4):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ipv4,554))
        if result == 0:
            return "Opened"
        else:
            return "Closed"
