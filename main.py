from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.boxlayout import BoxLayout


class App_main(MDApp):

    def build(self):
        screen = Screen()

        # A képernyő téma beállítása
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        # Fő elrendezés (BoxLayout) a képernyő tartalmához
        main_layout = BoxLayout(orientation='vertical')

        # BoxLayout az alsó gombok számára (vízszintes elrendezés)
        bottom_buttons = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=10, padding=[5, 5])

        # Bal alsó gomb (Receptek)
        btn_flat_recept = MDRectangleFlatIconButton(text="Receptek", icon="food", size_hint_x=1)

        # Jobb alsó gomb (Vonalkód)
        btn_flat_vonalkod = MDRectangleFlatIconButton(text="Vonalkód", icon="barcode", size_hint_x=1)

        # Gombok hozzáadása az alsó BoxLayout-hoz
        bottom_buttons.add_widget(btn_flat_recept)
        bottom_buttons.add_widget(btn_flat_vonalkod)

        # Fő layouthoz hozzáadjuk az alsó gombokat
        main_layout.add_widget(bottom_buttons)

        # Hozzáadjuk a fő layoutot a képernyőhöz
        screen.add_widget(main_layout)

        return screen


App_main().run()
