
## Descripción

Este script permite automatizar la busqueda de posibles Local File Inclusion's 

(con los payloads proporcionados por hacktricks)

## Uso

El script puede usarse de dos maneras:
1. **Proporcionando un parámetro específico**: Si conoces el parámetro que quieres probar, puedes usar la opción `-p` para especificarlo.

```bash
python3 incluseek.py http://example.com -p parametro
```

2. **Iterando sobre un diccionario de palabras**: Si no conoces el parámetro, puedes usar la opción `-w` para proporcionar un archivo de diccionario que contenga posibles nombres de parámetros.
```bash
python3 incluseek.py http://example.com -w diccionario.txt
```

### Requisitos

Asegúrate de tener instaladas las dependencias necesarias. Puedes instalarlas usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
### Recomiendo añadir el binario a una ruta relativa al $PATH
