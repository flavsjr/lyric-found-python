from lyricsgenius import Genius
from fpdf import FPDF
import webbrowser
import requests
client_acess_token = 'fGa7UxUsUmSsMmj_D8pxErI87AfhY_WjYjBnoWMGq8GXjjZIGTCjfCvQX-MnvF0x'
genius = Genius(client_acess_token)
artista = input("Digite o nome do artista: ")
nome_musica = input("Digite o nome da música: ")
song = genius.search_song(nome_musica, artista)
print(song.lyrics)

text2 = song.lyrics.encode('latin-1', 'replace').decode('latin-1')
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="", ln=1, align="L")
pdf.write(5, text2)
pdf.output('letra.pdf')
path = 'letra.pdf'
webbrowser.open_new(path)