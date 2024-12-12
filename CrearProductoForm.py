import wx # type: ignore
from db import obtener_conexion

class CrearProductoForm(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Registrar Producto", size=(400, 300))
        panel = wx.Panel(self)
        
        # Campos del formulario
        wx.StaticText(panel, label="Nombre:", pos=(20, 20))
        self.nombre_input = wx.TextCtrl(panel, pos=(100, 20), size=(200, -1))
        
        wx.StaticText(panel, label="Precio:", pos=(20, 60))
        self.precio_input = wx.TextCtrl(panel, pos=(100, 60), size=(200, -1))
        
        wx.StaticText(panel, label="Stock:", pos=(20, 100))
        self.stock_input = wx.TextCtrl(panel, pos=(100, 100), size=(200, -1))
        
        guardar_btn = wx.Button(panel, label="Guardar", pos=(150, 150))
        guardar_btn.Bind(wx.EVT_BUTTON, self.guardar_producto)
    
    def guardar_producto(self, event):
        nombre = self.nombre_input.GetValue()
        precio = self.precio_input.GetValue()
        stock = self.stock_input.GetValue()
        
        if not nombre or not precio or not stock:
            wx.MessageBox("Por favor completa todos los campos.", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", 
                           (nombre, float(precio), int(stock)))
            conexion.commit()
            conexion.close()
            wx.MessageBox("Producto guardado correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        except Exception as e:
            wx.MessageBox(f"Error: {e}", "Error", wx.OK | wx.ICON_ERROR)
