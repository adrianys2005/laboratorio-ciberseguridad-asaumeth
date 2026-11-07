#!/bin/sh

TARGET="${TARGET_URL:-https://servidor-web-dmz-adrianysmaria.onrender.com}"
RUTAS="/admin /config.php /login /secret /backup.zip /index.html"

echo "=== INICIANDO ENUMERACIÓN DE RUTAS EN LA DMZ ==="
echo "Probando peticiones HTTP a rutas conocidas sobre $TARGET..."

for ruta in $RUTAS; do
  CODE=$(curl -o /dev/null -s -w "%{http_code}" "$TARGET$ruta")
  echo "Ruta probada: $ruta -> Código de respuesta HTTP: $CODE"
done

echo "=== ENUMERACIÓN DE RUTAS FINALIZADA CON ÉXITO ==="

python3 -m http.server 8080
