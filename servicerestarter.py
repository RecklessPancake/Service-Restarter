import tkinter as tk
import win32gui, win32con

#Hide console
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

root= tk.Tk()

#Create window
canvas1 = tk.Canvas(root, width = 350, height = 550)
canvas1.pack()


#Defines what services need to be restarted 
def service1 ():
    os.system('cmd /c "net stop [service] & net start [service] & net stop [service] & net start [service]"')

def service2 ():
    os.system('cmd /c "net stop [service] & net start [service]"')

def service3 ():
    os.system('cmd /c "net stop [service] & net start [service]"')

def service4 ():
    os.system('cmd /c "net stop [service] & net start [service] & net stop [service] & net start [service] & net stop [service] & net start [service]"')

def service5 ():
    os.system('cmd /c "net stop [service] & net start [service]"')

################# New Service Command Template ######################
#                                                                   #
#def service ():                                                    #
#    os.system('cmd /c "net stop [service] & net start [service]"') #
#                                                                   #
#####################################################################


#When button is clicked, the service defined in command will restart
button1 = tk.Button(text='      Serivce1      ', command=service1, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button1)


button2 = tk.Button(text='      Serivce2      ', command=service2, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button2)


button3 = tk.Button(text='      Serivce3      ', command=service3, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button3)


button4 = tk.Button(text='      Serivce4      ', command=service4, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button4)


button5 = tk.Button(text='      Serivce5      ', command=service5, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button5)

####################################################### New Button Template ###########################################################
#                                                                                                                                     #
#button = tk.Button(text='          Service           ', command=service, bg='green', fg='white', font=('helvetica', 12, 'bold'))     #
#canvas1.create_window(175, 400, window=button)                                                                                       #
#                                                                                                                                     #
#######################################################################################################################################


root.mainloop()
