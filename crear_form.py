import wx
from db import obtener_conexion

class CrearProductoForm(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Crear Producto", size=(400, 300))
        panel = wx.Panel(self)
        
        # Campos del formulario
        wx.StaticText(panel, label="Nombre:", pos=(20, 20))
        self.nombre_input = wx.TextCtrl(panel, pos=(100, 20), size=(200, -1))
        
        wx.StaticText(panel, label="Precio:", pos=(20, 60))
        self.precio_input = wx.TextCtrl(panel, pos=(100, 60), size=(200, -1))
        
        wx.StaticText(panel, label="Stock:", pos=(20, 100))
        self.stock_input = wx.TextCtrl(panel, pos=(100, 100), size=(200, -1))
        
        # Botón para guardar
        guardar_btn = wx.Button(panel, label="Guardar Producto", pos=(100, 150))
        guardar_btn.Bind(wx.EVT_BUTTON, self.guardar_producto)
    
    def guardar_producto(self, event):
        nombre = self.nombre_input.GetValue()
        precio = self.precio_input.GetValue()
        stock = self.stock_input.GetValue()
        
        # Validar datos
        if not nombre or not precio or not stock:
            wx.MessageBox("Por favor, completa todos los campos.", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        # Guardar en la base de datos
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                           (nombre, float(precio), int(stock)))
            conexion.commit()
            conexion.close()
            wx.MessageBox("Producto guardado con éxito.", "Éxito", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        except Exception as e:
            wx.MessageBox(f"Error al guardar el producto: {e}", "Error", wx.OK | wx.ICON_ERROR)
class CrearUsuarioForm(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Crear Usuario", size=(400, 300))
        panel = wx.Panel(self)
        
        # Campos del formulario
        wx.StaticText(panel, label="Nombre:", pos=(20, 20))
        self.nombre_input = wx.TextCtrl(panel, pos=(100, 20), size=(200, -1))
        
        wx.StaticText(panel, label="Email:", pos=(20, 60))
        self.email_input = wx.TextCtrl(panel, pos=(100, 60), size=(200, -1))
        
        # Botón para guardar
        guardar_btn = wx.Button(panel, label="Guardar Usuario", pos=(100, 100))
        guardar_btn.Bind(wx.EVT_BUTTON, self.guardar_usuario)
    
    def guardar_usuario(self, event):
        nombre = self.nombre_input.GetValue()
        email = self.email_input.GetValue()
        
        # Validar datos
        if not nombre or not email:
            wx.MessageBox("Por favor, completa todos los campos.", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        # Guardar en la base de datos
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
            conexion.commit()
            conexion.close()
            wx.MessageBox("Usuario guardado con éxito.", "Éxito", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        except Exception as e:
            wx.MessageBox(f"Error al guardar el usuario: {e}", "Error", wx.OK | wx.ICON_ERROR)
