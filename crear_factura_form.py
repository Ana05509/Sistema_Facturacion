from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_factura_pdf(factura_id, cliente, productos, total):
    c = canvas.Canvas(f"factura_{factura_id}.pdf", pagesize=letter)
    c.drawString(100, 750, f"Factura ID: {factura_id}")
    c.drawString(100, 730, f"Cliente: {cliente['nombre']}")
    c.drawString(100, 710, f"Dirección: {cliente['direccion']}")
    
    y = 680
    for producto in productos:
        c.drawString(100, y, f"{producto['nombre']} - Cantidad: {producto['cantidad']} - Subtotal: {producto['subtotal']}")
        y -= 20
    
    c.drawString(100, y, f"Total: {total}")
    c.save()
