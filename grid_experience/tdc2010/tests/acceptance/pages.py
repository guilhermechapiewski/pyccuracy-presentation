from pyccuracy import Page

class PaginaRapida(Page):
    url = '/'

class PaginaLenta(Page):
    url = '/slow'

class PaginaMaisLenta(Page):
    url = '/slower'