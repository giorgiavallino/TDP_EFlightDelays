import flet as ft

class View(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        # Page stuff
        self._page = page
        self._page.title = "TDP 2025 Flights Manager"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # Graphical elements
        self._title = None
        self._txtCompMinime = None
        self._btnAnalizza = None
        self._ddAeroportoP = None
        self._btnConnessi = None
        self._ddAeroportoA = None
        self._txtTratteMax = None
        self._btnCerca = None

    def load_interface(self):
        # Title
        self._title = ft.Text("Welcome to the TDP 2025 Flights Manager",
                              color="blue",
                              size=24)
        self._page.controls.append(self._title)

        # Rows with some controls
        self._txtCompMinime = ft.TextField(label="Numero compagnie minime")
        self._btnAnalizza = ft.ElevatedButton(text="Analizza aeroporti",
                                              on_click=self._controller.handleAnalizza)
        row_01 = ft.Row([ft.Container(None, width=250),
                         ft.Container(self._txtCompMinime, width=250),
                         ft.Container(self._btnAnalizza, width=250)],
                        alignment=ft.MainAxisAlignment.CENTER)
        self._ddAeroportoP =ft.Dropdown(label="Aeroporto di partenza")
        self._btnConnessi = ft.ElevatedButton(text="Aeroporti connessi",
                                              on_click=self._controller.handleConnessi)
        row_02 = ft.Row([ft.Container(None, width=250),
                         ft.Container(self._ddAeroportoP, width=250),
                         ft.Container(self._btnConnessi, width=250)],
                        alignment=ft.MainAxisAlignment.CENTER)
        self._ddAeroportoA = ft.Dropdown(label="Aeroporto di arrivo")
        self._txtTratteMax = ft.TextField(label="Numero tratte massimo")
        self._btnCerca = ft.ElevatedButton(text="Cerca itinerario",
                                           on_click=self._controller.handleCerca)
        row_03 = ft.Row([ft.Container(self._ddAeroportoA, width=250),
                         ft.Container(self._txtTratteMax, width=250),
                         ft.Container(self._btnCerca, width=250)],
                        alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row_01, row_02, row_03)

        # List view where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
