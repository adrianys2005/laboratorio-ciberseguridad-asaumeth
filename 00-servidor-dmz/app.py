from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Nombre de la estudiante personalizado
        estudiante = os.getenv("ESTUDIANTE_NOMBRE", "Adrianys Maria Saumeth Padilla")
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Servidor Web DMZ</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }}
                .container {{ background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }}
                h1 {{ color: #1e3a8a; border-bottom: 2px solid #3b82f6; padding-bottom: 10px; }}
                .status {{ color: #16a34a; font-weight: bold; background: #dcfce7; padding: 4px 8px; border-radius: 4px; }}
                .info {{ background: #eff6ff; padding: 12px; border-left: 4px solid #2563eb; margin-top: 15px; border-radius: 4px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🛡️ Servidor Objetivo DMZ</h1>
                <p>Estado del servicio: <span class="status">ONLINE / ACTIVO</span></p>
                <div class="info">
                    <p><strong>Laboratorio de Ciberseguridad:</strong> {estudiante}</p>
                    <p><strong>Institución:</strong> IU Digital de Antioquia</p>
                </div>
                <p>Este nodo actúa como objetivo central para las pruebas de tráfico, auditoría perimetral y análisis de logs en Render.</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Servidor DMZ iniciado y escuchando en el puerto 8080...")
    httpd.serve_forever()
