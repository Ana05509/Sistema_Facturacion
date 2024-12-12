import wx 
from db import obtener_conexion

class CrearClienteForm(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Registrar Cliente", size=(400, 300))
        panel = wx.Panel(self)
        
        wx.StaticText(panel, label="Nombre:", pos=(20, 20))
        self.nombre_input = wx.TextCtrl(panel, pos=(100, 20), size=(200, -1))
        
        wx.StaticText(panel, label="Dirección:", pos=(20, 60))
        self.direccion_input = wx.TextCtrl(panel, pos=(100, 60), size=(200, -1))
        
        wx.StaticText(panel, label="Contacto:", pos=(20, 100))
        self.contacto_input = wx.TextCtrl(panel, pos=(100, 100), size=(200, -1))
        
        guardar_btn = wx.Button(panel, label="Guardar", pos=(150, 150))
        guardar_btn.Bind(wx.EVT_BUTTON, self.guardar_cliente)
    
    def guardar_cliente(self, event):
        nombre = self.nombre_input.GetValue()
        direccion = self.direccion_input.GetValue()
        contacto = self.contacto_input.GetValue()
        
        if not nombre:
            wx.MessageBox("El nombre es obligatorio.", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO clientes (nombre, direccion, contacto) VALUES (?, ?, ?)",
                           (nombre, direccion, contacto))
            conexion.commit()
            conexion.close()
            wx.MessageBox("Cliente guardado correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        except Exception as e:
            wx.MessageBox(f"Error: {e}", "Error", wx.OK | wx.ICON_ERROR)
