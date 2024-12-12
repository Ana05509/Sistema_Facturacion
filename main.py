import wx
from crear_form import CrearProducto
from listar_form import ListarProductos
from actualizar_form import ActualizarProducto
from db import inicializar_base_datos

class SistemaVentas(wx.Frame):
    def __init__(self, *args, **kw):
        super(SistemaVentas, self).__init__(*args, **kw)
        self.init_ui()

    def init_ui(self):
        self.SetTitle("Sistema de Ventas")
        self.SetSize((400, 300))

        panel = wx.Panel(self)

        btn_crear = wx.Button(panel, label="Crear Producto", pos=(10, 50))
        btn_listar = wx.Button(panel, label="Listar Productos", pos=(10, 100))
        btn_actualizar = wx.Button(panel, label="Actualizar Producto", pos=(10, 150))

        btn_crear.Bind(wx.EVT_BUTTON, self.crear_producto)
        btn_listar.Bind(wx.EVT_BUTTON, self.listar_productos)
        btn_actualizar.Bind(wx.EVT_BUTTON, self.actualizar_producto)

    def crear_producto(self, event):
        CrearProducto(self).Show()

    def listar_productos(self, event):
        ListarProductos(self).Show()

    def actualizar_producto(self, event):
        ActualizarProducto(self).Show()

if __name__ == "__main__":
    inicializar_base_datos()
    app = wx.App()
    frame = SistemaVentas(None)
    frame.Show()
    app.MainLoop()
