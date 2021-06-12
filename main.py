import art

def ceaser(message,shifts,direction):
  encrypted = ""
  if direction == "decode":
    shifts *= -1
  for i in message:
    if i in alphabet:
      pos = alphabet.index(i)
      newpos = pos + shifts
      if (newpos>25): 
        newpos = newpos - 26
      encrypted += alphabet[newpos]
    else :
      encrypted += i
  print(f"The {direction}d message is: \n{encrypted}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo+"\n")

game = 'y'
while(game =='y'):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction =="encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift =shift % 26

    ceaser(text,shift,direction)

    game = input("Do you want to continue 'Y' or 'N':\n").lower()

    if game == 'n':
      print("Goodbye")
  else:
    print("Error, the options are limited to encode and decode")
