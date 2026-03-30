import locale
import time

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %Y, %H:%M:%S", tempo_em_struct)
print(f"Tempo formatado: {tempo_formatado}")