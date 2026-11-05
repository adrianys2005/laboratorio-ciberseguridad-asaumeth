#!/bin/sh

TARGET="${TARGET_URL:-https://servidor-web-dmz-asaumeth.onrender.com}"

echo "=== SIMULACIÓN: GENERANDO TRÁFICO MASIVO HTTP ==="
echo "Enviando ráfaga de peticiones concurrentes a $TARGET..."

for i in $(seq 1 30); do
  curl -s -o /dev/null "$TARGET" &
done

wait
echo "=== PRUEBA FINALIZADA CON ÉXITO ==="

# Mantiene el servicio activo en Render
python3 -m http.server 8080
