from Program.CCTV_SCAN import IPCam_Check_Status
from Program.CCTV_VIEWER import CCTV_VIEWER
from Program.System_Check import system_compair
import sys

class Menu:

    def __init__(self):
        self.check_platform = system_compair()
        self.symbol = self.check_platform.check_system()

    def Screen_Menu(self):
        self.Logo = """
             _______   _            _         _______          _ _    _ _
            |__   __| | |          | |       |__   __|        | | |  (_) |
               | | ___| |_ __   ___| |_ ____    | | ___   ___ | | | ___| |_
               | |/ _ \ | '_ \ / _ \ __|_  /    | |/ _ \ / _ \| | |/ / | __|
               | |  __/ | | | |  __/ |_ / /     | | (_) | (_) | |   <| | |_
               |_|\___|_|_| |_|\___|\__/___|    |_|\___/ \___/|_|_|\_\_|\__|

            *****************************************************************
               """
        self.Menu_List = """
            Menu {0}

                [1] {1} IPCam Scan
                [2] {1} IPCam Viewer
                [3] {1} IPCam Capture

                [4] - Exit
                    """.format(self.symbol[0],self.symbol[1])

        self.Footer = """

                                    Create By Telnetz
            *****************************************************************
               """

        print(self.Logo+"\n"+self.Menu_List+"\n"+self.Footer)

    def Choosed_Menu(self):
        self.Menu_Input = input("\t {0} Please select choice : ".format(self.symbol[2]))
        self.Check_Input()

    def Check_Input(self):

        try:
            int(self.Menu_Input)
        except:
            print("\t\t[ Error ] : Please input numeric")
            self.Choosed_Menu()

        if len(self.Menu_Input) == 0:
            print("\t\t[ Error ] : Null")
            self.Choosed_Menu()
        elif int(self.Menu_Input) >= 5:
            print("\t\t[ Error ] : Out of Range")
            self.Choosed_Menu()
        else:
            self.Your_Choose(self.Menu_Input)

    def Your_Choose(self,choice):
        if choice == "1":
            ipcam_scan = IPCam_Check_Status()
        elif choice == "2":
            cctv_viewer = CCTV_VIEWER()
        elif choice == "3":
            pass
        else:
            sys.exit(0)

if __name__=="__main__":
    menu = Menu()
    menu.Screen_Menu()
    menu.Choosed_Menu()
