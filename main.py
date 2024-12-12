import wx
from crear_cliente_form import CrearClienteForm
from CrearProductoForm import CrearProductoForm
from crear_factura_form import CrearFacturaForm
from listar_form import ListarForm

class FacturacionApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Sistema de Facturación", size=(800, 600))
        panel = wx.Panel(self)

        # Botones principales
        btn_crear_cliente = wx.Button(panel, label="Crear Cliente", pos=(50, 50))
        btn_crear_producto = wx.Button(panel, label="Crear Producto", pos=(50, 100))
        btn_crear_factura = wx.Button(panel, label="Crear Factura", pos=(50, 150))
        btn_listar = wx.Button(panel, label="Listar Registros", pos=(50, 200))

        # Eventos
        btn_crear_cliente.Bind(wx.EVT_BUTTON, self.abrir_crear_cliente)
        btn_crear_producto.Bind(wx.EVT_BUTTON, self.abrir_crear_producto)
        btn_crear_factura.Bind(wx.EVT_BUTTON, self.abrir_crear_factura)
        btn_listar.Bind(wx.EVT_BUTTON, self.abrir_listar)

    def abrir_crear_cliente(self, event):
        form = CrearClienteForm(self)
        form.Show()

    def abrir_crear_producto(self, event):
        form = CrearProductoForm(self)
        form.Show()

    def abrir_crear_factura(self, event):
        form = CrearFacturaForm(self)
        form.Show()

    def abrir_listar(self, event):
        form = ListarForm(self)
        form.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = FacturacionApp()
    frame.Show()
    app.MainLoop()
