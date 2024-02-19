import customtkinter as Ctk
import winsound as ws

def play_sound():
    frequency = int(entryFrequency.get())               # ............................. #
    duration = (int(entryDuration.get())  * 1000  )     #     Sound player function     #                                     
    ws.Beep(frequency, duration)                         #...............................#

# Interface  ............................................................................................#
    
root = Ctk.CTk()
root.title("Sound Frequency")
root.geometry("750x450")

# Frequency input
labelFrequency = Ctk.CTkLabel(root, text="Frequency (Hz):", )
labelFrequency.pack(pady=(130,0))
entryFrequency = Ctk.CTkEntry(root)
entryFrequency.pack()

# Duration input
labelDuration = Ctk.CTkLabel(root, text="Duration (s):", )
labelDuration.pack()
entryDuration = Ctk.CTkEntry(root)
entryDuration.pack()

# Play 
playButton = Ctk.CTkButton(root, text="Play Sound",fg_color=("#5fb8ab"),hover_color=("#5fe1b4"),text_color=("#000000"), command=play_sound)
playButton.pack( pady=(20, 10))

# Run loop
root.mainloop()