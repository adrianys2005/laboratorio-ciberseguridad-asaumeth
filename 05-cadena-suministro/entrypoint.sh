#!/bin/sh

echo "=== INICIANDO SERVICIO COMPROMETIDO EN LA CADENA DE SUMINISTRO ==="
echo "Verificando integridad del contenedor..."

if [ -f "/app/malicious_dependency.sh" ]; then
  echo "[ALERTA DE SEGURIDAD] Se ha detectado una dependencia no autorizada inyectada durante la construcción del artefacto."
  sh /app/malicious_dependency.sh
else
  echo "[OK] Artefacto limpio."
fi

python3 -m http.server 8080
