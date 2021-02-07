import wave
import tkinter
from tkinter import *
from tkinter import ttk
from pyaudio import PyAudio
chunk=2014

class player():
    def play(self):
        wf = wave.open(r"1_1.wav",'rb')
        p =PyAudio()
        stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
        wf.getnchannels(),rate=wf.getframerate(),output=True) 
        while True:
            data = wf.readframes(chunk)
            if data == "":break
            stream.write(data)
        stream.close()
        p.terminate()

def played():
    rec = player()
    rec.play()

root=Tk()
Button4=tkinter.Button(root, text ="播放录音", command = played)

Button4.grid(row=0,column=3,padx=20,pady=20)
root.mainloop()