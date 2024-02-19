import customtkinter as Ctk
import winsound as ws

def play_sound():
    frequency = int(entry_frequency.get())               # ............................. #
    duration = (int(entry_duration.get())  * 1000  )     #     Sound player function     #                                     
    ws.Beep(frequency, duration)                         #...............................#

# Interface  ............................................................................................#
    
root = Ctk.CTk()
root.title("Sound Frequency")
root.geometry("750x450")

# Frequency input
label_frequency = Ctk.CTkLabel(root, text="Frequency (Hz):", )
label_frequency.pack(pady=(130,0))
entry_frequency = Ctk.CTkEntry(root)
entry_frequency.pack()

# Duration input
label_duration = Ctk.CTkLabel(root, text="Duration (s):", )
label_duration.pack()
entry_duration = Ctk.CTkEntry(root)
entry_duration.pack()

# Play 
play_button = Ctk.CTkButton(root, text="Play Sound",fg_color=("#5fb8ab"),hover_color=("#5fe1b4"),text_color=("#000000"), command=play_sound)
play_button.pack( pady=(20, 10))

# Run loop
root.mainloop()