from kivymd.uix.menu.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen

class CidadaoScreen(MDScreen):
    """
    Example Screen.
    """
    
    def abrir(self):
        menu_items = [
            {
                'text': 'nome'
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button,
            items= menu_items
        )
        self.menu.open()
