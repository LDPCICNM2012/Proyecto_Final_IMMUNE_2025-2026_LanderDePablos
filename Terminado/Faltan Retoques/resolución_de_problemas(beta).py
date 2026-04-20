#Resolución de problemas.py
#Imports
import ollama
from docx import Document
import subprocess
import time

conversacion = []
run_conversacion = True

print("Bienvenido al Ayudador ayudadoso que ayuda a los necesitados a ayudar sus problemas ayudandose.")
while run_conversacion == True:
    pregunta = input("¿Cuál es tu problema? (Escribe 'FIN' para terminar): ")
    if pregunta.upper() == "FIN":
        run_conversacion = False
        break
    conversacion.append({'role': 'user', 'content': pregunta})
    
    instrucciones = (
        "Eres un Solucionador de Problemas de alto rendimiento. "
        "Tu enfoque es: Analizar el problema -> Identificar la causa -> Dar solución técnica/práctica aunque puedes poner comentarios para ser mas resolutivo. "
        "Analiza por qué y da un plan de acción real para la ocasion. "
        "Responde siempre con estructura: 1. Diagnóstico, 2. Solución, 3. Primer paso."
    )
    
    response = ollama.chat(
        model="qwen2.5-coder:1.5b",
        messages=[
            {'role': 'system', 'content': instrucciones},
            *conversacion
        ],
        options={
            "temperature": 0.2,
            "num_predict": 1000
        }
    )
    
    respuesta_ia = response['message']['content']
    print(f"[IA] {respuesta_ia}")
    conversacion.append({'role': 'assistant', 'content': respuesta_ia})