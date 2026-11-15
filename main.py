# FINAL JARVIS - Imran Jutt Boss
import os, datetime, webbrowser
try:
    import google.generativeai as genai
    AI=True
except:
    AI=False

API_KEY="AQ.Ab8RN6LfTtHFQZhXWp1XAFnZF2WZjmpgjmNZ9Zu2Frwg7qC8Xg"

if AI and API_KEY!="YAHAN_APNI_GEMINI_API_KEY_DALO":
    genai.configure(api_key=API_KEY)
    model=genai.GenerativeModel('gemini-1.5-flash')
    print("Jarvis Brain: Connected ✅")
else:
    model=None
    print("Jarvis Brain: Offline Mode")

def jarvis_speak(text):
    print(f"\nJarvis: {text}")
    try:
        os.system(f'termux-tts-speak "{text}"')
    except:
        pass

def get_reply(prompt):
    if not model:
        return "Boss API Key dalo to main smart jawab dunga. Abhi time "+datetime.datetime.now().strftime("%I:%M %p")+" hua hai."
    try:
        full=f"Tum Jarvis ho, Imran ka dost AI. Roman Urdu me short funny jawab do. Q: {prompt}"
        return model.generate_content(full).text
    except Exception as e:
        return f"Error: {e}"

jarvis_speak("Yes Boss, Jarvis Ready hai. Bolo kya kaam hai?")

while True:
    user=input("\nAap Bolo: ")
    if not user.strip(): continue
    if "exit" in user.lower() or "band" in user.lower():
        jarvis_speak("Ok Boss, Allah Hafiz!")
        break
    clean=user.lower().replace("jarvis","").strip()
    if not clean:
        jarvis_speak("Ji Boss hukam karo?")
        continue
    print("Soch raha hu...")
    reply=get_reply(clean)
    jarvis_speak(reply)
