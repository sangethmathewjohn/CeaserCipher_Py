# CeaserCipher

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence

## Example

    Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
    Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
   
## Program

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
      print(f"The {direction}d of {message} is: \n{encrypted}")

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
        print("Error")

## Output


     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           


    Type 'encode' to encrypt, type 'decode' to decrypt:
    encode
    Type your message:
    hwllo world
    Type the shift number:
    8
    The encoded message is: 
    pettw ewztl
    Do you want to continue 'Y' or 'N':
    y
    Type 'encode' to encrypt, type 'decode' to decrypt:
    decode
    Type your message:
    pettw ewztl
    Type the shift number:
    8
    The decoded message is: 
    hwllo world
    Do you want to continue 'Y' or 'N':
    y
    Type 'encode' to encrypt, type 'decode' to decrypt:
    waht
    Error
    Type 'encode' to encrypt, type 'decode' to decrypt:
    encode
    Type your message:
    zuly
    Type the shift number:
    7
    The encoded message is: 
    gbsf
    Do you want to continue 'Y' or 'N':
    n
    Goodbye

