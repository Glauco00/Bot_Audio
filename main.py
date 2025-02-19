#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

# Inicializa o reconhecedor de fala
recognizer = sr.Recognizer()

# Usando o microfone do sistema como fonte de áudio
with sr.Microphone() as source:
    print("Ajustando para o ruído ambiente... aguarde.")
    recognizer.adjust_for_ambient_noise(source)
    print("Por favor, fale agora!")
    
    # Captura o áudio do microfone
    audio = recognizer.listen(source)

# Usando o serviço do Google para reconhecer o áudio
try:
    print("Reconhecendo áudio...")
    text = recognizer.recognize_google(audio, language="pt-BR")
    print(f"Você disse: {text}")
except sr.UnknownValueError:
    print("Não consegui entender o áudio.")
except sr.RequestError as e:
    print(f"Erro na requisição do serviço de reconhecimento: {e}")
