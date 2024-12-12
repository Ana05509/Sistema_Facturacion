import wx
from db import ejecutar_consulta, obtener_datos

class ActualizarProducto(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Actualizar Producto", size=(300, 250))
        panel = wx.Panel(self)

        wx.StaticText(panel, label="ID Producto:", pos=(10, 10))
        wx.StaticText(panel, label="Nuevo Precio:", pos=(10, 50))
        wx.StaticText(panel, label="Nueva Cantidad:", pos=(10, 90))

        self.producto_id = wx.TextCtrl(panel, pos=(100, 10))
        self.nuevo_precio = wx.TextCtrl(panel, pos=(100, 50))
        self.nueva_cantidad = wx.TextCtrl(panel, pos=(100, 90))

        btn_actualizar = wx.Button(panel, label="Actualizar", pos=(10, 130))
        btn_actualizar.Bind(wx.EVT_BUTTON, self.actualizar_producto)

    def actualizar_producto(self, event):
        producto_id = int(self.producto_id.GetValue())
        nuevo_precio = float(self.nuevo_precio.GetValue())
        nueva_cantidad = int(self.nueva_cantidad.GetValue())

        query = "UPDATE productos SET precio = ?, cantidad = ? WHERE id = ?"
        ejecutar_consulta(query, (nuevo_precio, nueva_cantidad, producto_id))

        wx.MessageBox("Producto actualizado con éxito", "Información", wx.OK | wx.ICON_INFORMATION)
        self.producto_id.SetValue("")
        self.nuevo_precio.SetValue("")
        self.nueva_cantidad.SetValue("")
