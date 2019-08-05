from Program.Check_Rtsp_Status import IPCam_Check_Status
import sys

class Menu:

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
            Menu \u2B5D

                [1] \u2B9A IPCam Scan
                [2] \u2B9A IPCam Viewer
                [3] \u2B9A IPCam Capture

                [4] - Exit
                    """

        self.Footer = """

                                    Create By Telnetz
            *****************************************************************
               """

        print(self.Logo+"\n"+self.Menu_List+"\n"+self.Footer)

    def Choosed_Menu(self):
        self.Menu_Input = input("\t \u21B3 Please select choice : ")
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
            pass
        elif choice == "3":
            pass
        else:
            sys.exit(0)

if __name__=="__main__":
    menu = Menu()
    menu.Screen_Menu()
    menu.Choosed_Menu()
