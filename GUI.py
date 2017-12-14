"""
Stephen Zupan
INST326
December 2nd, 2017
Python version 3.6
Thanks for a great semester
"""

from tkinter import *
import pymysql
db = pymysql.connect(host="localhost", port=3306, user="me", passwd="me", db="AIRLINE_SCHEMA")
class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cleveland Hopkins International Airport")

        self.bgphoto = PhotoImage(file="/Users/Zupan/Desktop/Zupan_Stephen_Final/cleveland-hopkins.gif")
        self.bgphotoLabel = Label(image=self.bgphoto)
        self.bgphotoLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = Label(master, text="Welcome to Cleveland Hopkins International Airport! How may we help you?")
        self.label.grid(row=1, column=0)

        self.airlineMaker = Button(master, text="Introduce new airline", command=self.airlineWindow)
        self.airlineMaker.grid(row=2, column=0, sticky=W)

        self.flightSchedule = Button(master, text="schedule a flight", command=self.flightWindow)
        self.flightSchedule.grid(row=3, column=0, sticky=W)

        self.flightSchedule = Button(master, text="change an existing flight", command=self.flightChangeWindow)
        self.flightSchedule.grid(row=4, column=0, sticky=W)

        self.planeMaker = Button(master, text="introduce new plane", command=self.planeWindow)
        self.planeMaker.grid(row=5, column=0, sticky=W)

        self.ticketMaker = Button(master, text="get your ticket", command=self.ticketWindow)
        self.ticketMaker.grid(row=6, column=0, sticky=W)

        self.ticketMaker = Button(master, text="change your ticket", command=self.changeTicketWindow)
        self.ticketMaker.grid(row=7, column=0, sticky=W)

        self.ticketKiller = Button(master, text="delete your ticket", command=self.deleteTicketWindow)
        self.ticketKiller.grid(row=8, column=0, sticky=W)

        self.endGreet = Label(master, text="For assistance, call (216) 265-6000")
        self.endGreet.grid(row=9, column=0, sticky=W)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=12, column=0, sticky=W)

    def airlineWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = AddAirlineWindow(self.newWindow)

    def flightWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = AddFlightsWindow(self.newWindow)

    def flightChangeWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = ChangeFlightsWindow(self.newWindow)

    def planeWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = PlaneWindow(self.newWindow)

    def ticketWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = TicketWindow(self.newWindow)

    def changeTicketWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = changeTicketWindow(self.newWindow)

    def deleteTicketWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = deleteTicketWindow(self.newWindow)

class AddAirlineWindow:
    def __init__(self, master):
        self.master = master
        master.title("Expand Airline")

        self.greetlabel = Label(master, text="Thanks for bringing a new airline to Cleveland Hopkins International Airport!")
        self.greetlabel.grid(row=0, column=0, columnspan=2)

        self.idAirlineEntry = Entry(master)
        self.idAirlineEntry.grid(row=1, column=1)
        self.idAirlinePrompt = Label(master, text="(3 digit) Airline ID#:")
        self.idAirlinePrompt.grid(row=1, column=0)


        self.nameAirlineEntry = Entry(master)
        self.nameAirlineEntry.grid(row=2, column=1)
        self.nameAirlinePrompt = Label(master, text="Airline Name:")
        self.nameAirlinePrompt.grid(row=2, column=0)

        self.hubStatusEntry = Entry(master)
        self.hubStatusEntry.grid(row=3, column=1)
        self.hubStatusPrompt = Label(master, text="will you be opening a hub? enter 0 for no, 1 for yes:")
        self.hubStatusPrompt.grid(row=3, column=0)

        self.planeNumEntry = Entry(master)
        self.planeNumEntry.grid(row=4, column=1)
        self.planeNumPrompt = Label(master, text="Number of planes on rotation:")
        self.planeNumPrompt.grid(row=4, column=0)


        self.submitButton = Button(master, text="Submit", command=self.insertInfo2DB)
        self.submitButton.grid(row=6, column=3)

        # clear entered text
        self.clear_button = Button(master, text="Clear text", command=self.clear_text)
        self.clear_button.grid(row=6, column=2)

    def clear_text(self):
        self.idAirlineEntry.delete(0, 'end')
        self.nameAirlineEntry.delete(0, 'end')
        self.hubStatusEntry.delete(0, 'end')
        self.planeNumEntry.delete(0, 'end')

    def insertInfo2DB(self):
        #QUERY TIME SONNNNNNN
        cursor = db.cursor()
        cursor.execute("""INSERT INTO airline(idairline,
           airlineName, hubBool, planeNum)
           VALUES (%s, %s, %s, %s)""", (int(self.idAirlineEntry.get()), str(self.nameAirlineEntry.get()),
                                        int(self.hubStatusEntry.get()), int(self.planeNumEntry.get())))
        db.commit()

class AddFlightsWindow:
    def __init__(self, master):
        self.master = master
        master.title("Schedule a Flight")

        self.greetlabel = Label(master, text="Thanks for scheduling a new flight at Cleveland Hopkins International Airport!")
        self.greetlabel.grid(row=0, column=0, columnspan=2)

        self.flightNumEntry = Entry(master)
        self.flightNumEntry.grid(row=1, column=1)
        self.flightNumPrompt = Label(master, text="(4 digit) Flight Number:")
        self.flightNumPrompt.grid(row=1, column=0)

        self.pilotIDEntry = Entry(master)
        self.pilotIDEntry.grid(row=2, column=1)
        self.pilotIDPrompt = Label(master, text="Pilot ID#:")
        self.pilotIDPrompt.grid(row=2, column=0)

        self.depTimeEntry = Entry(master)
        self.depTimeEntry.grid(row=3, column=1)
        self.depTimePrompt = Label(master, text="when does this flight depart (eg. '10:35AM'):")
        self.depTimePrompt.grid(row=3, column=0)

        self.arrTimeEntry = Entry(master)
        self.arrTimeEntry.grid(row=4, column=1)
        self.arrTimePrompt = Label(master, text="when does this flight arrive at it's destination (eg. '4:05AM'):")
        self.arrTimePrompt.grid(row=4, column=0)

        #The famed query button, tell your friends
        self.submitButton = Button(master, text="Submit", command=self.insertInfo2DB)
        self.submitButton.grid(row=6, column=3)

        # clear entered text
        self.clear_button = Button(master, text="Clear text", command=self.clear_text)
        self.clear_button.grid(row=6, column=2)

    def clear_text(self):
        self.flightNumEntry.delete(0, 'end')
        self.pilotIDEntry.delete(0, 'end')
        self.depTimeEntry.delete(0, 'end')
        self.arrTimeEntry.delete(0, 'end')
        self.destroy()

    def insertInfo2DB(self):
        #QUERY TIME SONNNNNNN
        cursor = db.cursor()
        cursor.execute("""INSERT INTO Flights(flightNums,
           pilotID, depTime, arrTime)
           VALUES (%s, %s, %s, %s)""", (int(self.flightNumEntry.get()), float(self.pilotIDEntry.get()),
                                        str(self.depTimeEntry.get()), str(self.arrTimeEntry.get())))
        db.commit()


class ChangeFlightsWindow:
    def __init__(self, master):
        self.master = master
        master.title("Change a Flight")
        self.greetlabel = Label(master, text="Thanks for changing a flight at Cleveland Hopkins International Airport!")
        self.greetlabel.grid(row=0, column=0, columnspan=2)

        self.flightNumEntry = Entry(master)
        self.flightNumEntry.grid(row=1, column=1)
        self.flightNumPrompt = Label(master, text="(4 digit) Flight Number:")
        self.flightNumPrompt.grid(row=1, column=0)

        self.pilotIDEntry = Entry(master)
        self.pilotIDEntry.grid(row=2, column=1)
        self.pilotIDPrompt = Label(master, text="Pilot ID#:")
        self.pilotIDPrompt.grid(row=2, column=0)

        self.depTimeEntry = Entry(master)
        self.depTimeEntry.grid(row=3, column=1)
        self.depTimePrompt = Label(master, text="when does this flight depart (eg. '10:35AM'):")
        self.depTimePrompt.grid(row=3, column=0)

        self.arrTimeEntry = Entry(master)
        self.arrTimeEntry.grid(row=4, column=1)
        self.arrTimePrompt = Label(master, text="when does this flight arrive at it's destination (eg. '4:05AM'):")
        self.arrTimePrompt.grid(row=4, column=0)

        # The famed query button, tell your friends
        self.submitButton = Button(master, text="Submit", command=self.changeFromDB)
        self.submitButton.grid(row=6, column=3)

        #clear entered text
        self.clear_button = Button(master, text="Clear text", command=self.clear_text)
        self.clear_button.grid(row=6, column=2)

    def clear_text(self):
        self.flightNumEntry.delete(0, 'end')
        self.pilotIDEntry.delete(0, 'end')
        self.depTimeEntry.delete(0, 'end')
        self.arrTimeEntry.delete(0, 'end')

    def changeFromDB(self):
        cursor = db.cursor()
        cursor.execute("""UPDATE Flights
        SET flightNums=%s, pilotID=%s, depTime=%s, arrTime=%s WHERE flightNums=%s""",
                       (int(self.flightNumEntry.get()), float(self.pilotIDEntry.get()),
                        str(self.depTimeEntry.get()), str(self.arrTimeEntry.get()), int(self.flightNumEntry.get())))
        db.commit()

class PlaneWindow:
    def __init__(self, master):
        self.master = master
        master.title("Introduce a Plane")

        self.greetlabel = Label(master, text="Thanks for introducing a new plane to Cleveland Hopkins International Airport!")
        self.greetlabel.grid(row=0, column=0, columnspan=2)

        self.modelNumEntry = Entry(master)
        self.modelNumEntry.grid(row=1, column=1)
        self.modelNumPrompt = Label(master, text="(7 digit) Model Number:")
        self.modelNumPrompt.grid(row=1, column=0)

        self.modelNameEntry = Entry(master)
        self.modelNameEntry.grid(row=2, column=1)
        self.modelNamePrompt = Label(master, text="What is the name of this model:")
        self.modelNamePrompt.grid(row=2, column=0)

        self.readyEntry = Entry(master)
        self.readyEntry.grid(row=3, column=1)
        self.readyPrompt = Label(master, text="is this plane ready to fly (y/n):")
        self.readyPrompt.grid(row=3, column=0)

        self.fuelLevelEntry = Entry(master)
        self.fuelLevelEntry.grid(row=4, column=1)
        self.fuelLevelPrompt = Label(master, text="what numerical percent fuel is the plane at (eg. '67'):")
        self.fuelLevelPrompt.grid(row=4, column=0)

        #Create button to submit info
        self.submitButton = Button(master, text="Submit", command=self.insertInfo2DB)
        self.submitButton.grid(row=6, column=3)

        # clear entered text
        self.clear_button = Button(master, text="Clear text", command=self.clear_text)
        self.clear_button.grid(row=6, column=2)

    def clear_text(self):
        self.modelNumEntry.delete(0, 'end')
        self.modelNameEntry.delete(0, 'end')
        self.readyEntry.delete(0, 'end')
        self.fuelLevelEntry.delete(0, 'end')

    def insertInfo2DB(self):
        # QUERY TIME SONNNNNNN
        cursor = db.cursor()
        cursor.execute("""INSERT INTO planes(model,
            modelName, ready, fuelLevel)
            VALUES (%s, %s, %s, %s)""", (int(self.modelNumEntry.get()), str(self.modelNameEntry.get()),
                                            str(self.readyEntry.get()), float(self.fuelLevelEntry.get())))
        db.commit()

class TicketWindow:
    def __init__(self, master):
        self.master = master
        master.title("Get your ticket")

        self.greetlabel = Label(master, text="Thanks for getting your ticket from Cleveland Hopkins International Airport!")
        self.greetlabel.grid(row=0, column=0, columnspan=2)

        self.confirmationNumEntry = Entry(master)
        self.confirmationNumEntry.grid(row=1, column=1)
        self.confirmationNumPrompt = Label(master, text="Enter your six-digit confirmation number:")
        self.confirmationNumPrompt.grid(row=1, column=0)

        self.seatEntry = Entry(master)
        self.seatEntry.grid(row=2, column=1)
        self.seatPrompt = Label(master, text="Which seat would you like (eg. 'A14'):")
        self.seatPrompt.grid(row=2, column=0)

        self.tickTypeEntry = Entry(master)
        self.tickTypeEntry.grid(row=3, column=1)
        self.tickTypePrompt = Label(master, text="Would you prefer a paper ticket or email PDF (PAP/PDF):")
        self.tickTypePrompt.grid(row=3, column=0)

        self.submitButton = Button(master, text="Submit", command=self.insertInfo2DB)
        self.submitButton.grid(row=5, column=3)

        # clear entered text
        self.clear_button = Button(master, text="Clear text", command=self.clear_text)
        self.clear_button.grid(row=6, column=2)

    def clear_text(self):
        self.confirmationNumEntry.delete(0, 'end')
        self.seatEntry.delete(0, 'end')
        self.tickTypeEntry.delete(0, 'end')

    def insertInfo2DB(self):
        #QUERY TIME SONNNNNNN
        cursor = db.cursor()
        cursor.execute("""INSERT INTO tickets(confirmationNum,
           seat, tickType)
           VALUES (%s, %s, %s)""", (int(self.confirmationNumEntry.get()), str(self.seatEntry.get()), str(self.tickTypeEntry.get())))
        db.commit()

class changeTicketWindow:
    def __init__(self, master):
        self.master = master
        master.title("Change your ticket")

        self.greetlabel = Label(master,
                                text="Thanks for getting your ticket from Cleveland Hopkins International Airport!")
        self.greetlabel.grid(row=0, column=0, columnspan=2)

        self.confirmationNumEntry = Entry(master)
        self.confirmationNumEntry.grid(row=1, column=1)
        self.confirmationNumPrompt = Label(master, text="Enter your six-digit confirmation number:")
        self.confirmationNumPrompt.grid(row=1, column=0)

        self.seatEntry = Entry(master)
        self.seatEntry.grid(row=2, column=1)
        self.seatPrompt = Label(master, text="Which seat would you like (eg. 'A14'):")
        self.seatPrompt.grid(row=2, column=0)

        self.tickTypeEntry = Entry(master)
        self.tickTypeEntry.grid(row=3, column=1)
        self.tickTypePrompt = Label(master, text="Would you prefer a paper ticket or email PDF (PAP/PDF):")
        self.tickTypePrompt.grid(row=3, column=0)

        self.submitButton = Button(master, text="Submit", command=self.changeFromDB)
        self.submitButton.grid(row=5, column=3)

        #clear entered text
        self.clear_button = Button(master, text="Clear text", command=self.clear_text)
        self.clear_button.grid(row=6, column=2)

    def clear_text(self):
        self.confirmationNumEntry.delete(0, 'end')
        self.seatEntry.delete(0, 'end')
        self.tickTypeEntry.delete(0, 'end')

    def changeFromDB(self):
        cursor = db.cursor()
        cursor.execute("""UPDATE tickets
        SET confirmationNum=%s, seat=%s, tickType=%s WHERE confirmationNum=%s""",
                       (int(self.confirmationNumEntry.get()), str(self.seatEntry.get()),
                        str(self.tickTypeEntry.get()), int(self.confirmationNumEntry.get())))
        db.commit()

class deleteTicketWindow:
    def __init__(self, master):
        self.master = master
        master.title("Delete your ticket")

        self.greetlabel = Label(master, text="We're sorry to see you go!")
        self.greetlabel.grid(row=0, column=0, columnspan=2)

        self.confirmationNumEntry = Entry(master)
        self.confirmationNumEntry.grid(row=1, column=1)
        self.confirmationNumPrompt = Label(master, text="Enter your six-digit confirmation number:")
        self.confirmationNumPrompt.grid(row=1, column=0)

        self.seatEntry = Entry(master)
        self.seatEntry.grid(row=2, column=1)
        self.seatPrompt = Label(master, text="Which seat did you have (eg. 'A14'):")
        self.seatPrompt.grid(row=2, column=0)

        self.tickTypeEntry = Entry(master)
        self.tickTypeEntry.grid(row=3, column=1)
        self.tickTypePrompt = Label(master, text="How was your ticket delivered (PAP/PDF):")
        self.tickTypePrompt.grid(row=3, column=0)

        self.submitButton = Button(master, text="Remove", command=self.removeFromDB)
        self.submitButton.grid(row=5, column=3)

        #clear entered text
        self.clear_button = Button(master, text="Clear text", command=self.clear_text)
        self.clear_button.grid(row=6, column=2)

    def clear_text(self):
        self.confirmationNumEntry.delete(0, 'end')
        self.seatEntry.delete(0, 'end')
        self.tickTypeEntry.delete(0, 'end')

    def removeFromDB(self):
        cursor = db.cursor()
        cursor.execute("""DELETE FROM tickets WHERE confirmationNum=%s""",
                       (int(self.confirmationNumEntry.get())))
        db.commit()

root = Tk()
my_gui = MainGUI(root)
root.geometry('{}x{}'.format(1400, 850))
root.mainloop()

