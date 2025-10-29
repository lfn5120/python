import mido

def load_song(source) -> mido.MidiFile:
    global song 
    while True: # until the user uploads a valid file
        try:
            song = mido.MidiFile(source)
            break # file was rendered sucessfully
        except:
            source = input(""""
            I'm sorry, but I wasn't able to understand this document, please try again with a valid file."
            """"")

print("""
      Welcome to Piano Master!
      I can play any song on the piano, just upload a .mid file with your song choice and listen to my melody!
      """)
source = input("Enter the path to your MIDI file: ")
               
load_song(source)
print(song.ticks_per_beat, len(song.tracks))
