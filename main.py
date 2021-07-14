import tkinter as tk
import random, string

def randomPasswort():
    random.seed()
    inhalt = ''

    w = str(wunschzeichen.get())
    z = str(anzahlzeichen.get())
    if(z.isdigit()):
        z1 = int(anzahlzeichen.get())
    else:
        z1 = 0

    laenge = z1
    klein = "ja"
    gross = "ja"
    zahl = "ja"
    zeichen = "ja"

    if klein == 'ja':
        inhalt += string.ascii_lowercase
    if gross == 'ja':
        inhalt += string.ascii_uppercase
    if zahl == 'ja':
        inhalt += '0123456789'
    if zeichen == 'ja':
        inhalt += '''`~!@#$%^&*()_+-=][';}{":/.,<>?"}'''

    pw = ''.join(random.choice(inhalt) for i in range(laenge))

    return(pw+w+"\n")





def generatePasswort():
    e = str(emailzeichen.get())
    b = str(benutzerzeichen.get())
    passwort= randomPasswort()
    f= open("Passwort.txt","a")
    f.write("Email: "+e + " | Benutzername: " + b + " | Passwort: " + passwort)
    f.close()

    infozeichen.set("Passwort gespeichert!")



if __name__ == '__main__':

    window = tk.Tk()
    anzahlzeichen = tk.IntVar()
    wunschzeichen = tk.StringVar()
    emailzeichen = tk.StringVar()
    benutzerzeichen = tk.StringVar()
    infozeichen = tk.StringVar()

    window.geometry("600x400")

    label = tk.Label(window,text="Passwortgenerator").grid(row=0)

    emaillabel = tk.Label(window, text="Email: ").grid(row=1)
    benutzerlabel = tk.Label(window, text="Benutzername: ").grid(row=2)
    zeichenlabel = tk.Label(window,text= "Anzahl zeichen:").grid(row = 3)
    wunschlabel = tk.Label(window,text="wunsch Anhang:").grid(row=4)

    emailinput = tk.Entry(window, textvariable=emailzeichen).grid(row=1, column=1)
    benutzerinput = tk.Entry(window, textvariable=benutzerzeichen).grid(row=2, column=1)
    zeicheninput = tk.Entry(window,textvariable=anzahlzeichen).grid(row=3,column =1)
    wunsch = tk.Entry(window,textvariable=wunschzeichen).grid(row=4,column =1)


    generate = tk.Button(window,text= "Generate Passwort",command=lambda:generatePasswort()).grid(row=5)

    info= tk.Label(window,text="",textvariable=infozeichen).grid(row=6)


    window.mainloop()




