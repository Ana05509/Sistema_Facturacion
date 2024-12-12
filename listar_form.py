import wx
from db import obtener_datos

class ListarProductos(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Listar Productos", size=(400, 300))
        panel = wx.Panel(self)

        productos = obtener_datos("SELECT id, nombre, precio, cantidad FROM productos")
        lista = wx.TextCtrl(panel, pos=(10, 10), size=(360, 240), style=wx.TE_MULTILINE | wx.TE_READONLY)

        for producto in productos:
            lista.AppendText(f"ID: {producto[0]} | Nombre: {producto[1]} | Precio: ${producto[2]:.2f} | Cantidad: {producto[3]}\n")
