import random

print("FB'nin attığı gol sayısı")
FB=(random.randint(0, 6))

print("GS'nin attığı gol sayısı")
GS=(random.randint(0, 6))

if  FB>GS :
    print("FB maçı kazandı.")
if FB==GS:
    print("maç berabere.")
else:
    print("GS maçı kazandı.")
