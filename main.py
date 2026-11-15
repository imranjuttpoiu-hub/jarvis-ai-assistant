# My Jarvis - Tareeka 2 - Version 1
# Dost jaisa assistant

import time

print("--- Jarvis Online Hai Boss ---")
print("Jarvis: Yes Boss, bolo kya kaam hai?")

# Ye pehla version hai
# Agla version me isme Awaz (Vosk) + Dimagh (Gemini API) add karenge

while True:
    command = input("\nAap Bolo: ")
    
    if "jarvis" in command.lower():
        print("Jarvis: Ji Boss, sun raha hu, hukam karo!")
    
    elif "kya haal" in command.lower():
        print("Jarvis: Ek dum mast Boss, aap sunao!")
    
    elif "band" in command.lower() or "exit" in command.lower():
        print("Jarvis: Ok Boss, milte hain!")
        break
    
    elif command.strip() == "":
        continue
        
    else:
        print(f"Jarvis ne suna: '{command}' - (Agla version iska jawab dega)")
        print("Jarvis: Samajh gaya Boss, ispe kaam karunga!")
