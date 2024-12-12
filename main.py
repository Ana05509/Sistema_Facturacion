from crear_cliente_form import CrearClienteForm
import crear_factura_form
import wx # type: ignore
from crear_form import CrearProducto, CrearProductoForm
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

class MainMenu(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Sistema de Facturación", size=(400, 300))
        panel = wx.Panel(self)
        
        registrar_producto_btn = wx.Button(panel, label="Registrar Producto", pos=(100, 50))
        registrar_producto_btn.Bind(wx.EVT_BUTTON, self.abrir_registrar_producto)
        
        registrar_cliente_btn = wx.Button(panel, label="Registrar Cliente", pos=(100, 100))
        registrar_cliente_btn.Bind(wx.EVT_BUTTON, self.abrir_registrar_cliente)
        
        generar_factura_btn = wx.Button(panel, label="Generar Factura", pos=(100, 150))
        generar_factura_btn.Bind(wx.EVT_BUTTON, self.abrir_generar_factura)
    
    def abrir_registrar_producto(self, event):
        CrearProductoForm(self).Show()
    
    def abrir_registrar_cliente(self, event):
        CrearClienteForm(self).Show()
    
    def abrir_generar_factura(self, event):
        crear_factura_form(self).Show()

if __name__ == "__main__":
    app = wx.App()
    MainMenu().Show()
    app.MainLoop()
