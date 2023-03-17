import tkinter as tk

#create the login window
root = tk.Tk()

#set the size of the login screen
root.wm_geometry("400x200")

#change the title
root.title("Space Defender")

#create an empty frame within the root window
frame_login = tk.Frame(root)
#call the grid
frame_login.grid(row=0, column=0, sticky="news")

#create a label so that player knows where to input their player name
lbl_playerName = tk.Label(frame_login, text="Username:", font="courier")
lbl_playerName.pack(pady=5, padx=100)

#adding an input box for the player name
ent_playerName = tk.Entry(frame_login, bd=3)
ent_playerName.pack(pady=5, padx=100)

#add a function to start the game when the play button is pressed
def startGame():
    import mGame as gm
    gm.game()
    playerName = ent_playerName.get()
    print(playerName)
    return playerName

#add a play button
play = tk.Button(frame_login, text="Play", font="courier", command=startGame)
play.pack(pady=5, padx=100)

root.mainloop()
