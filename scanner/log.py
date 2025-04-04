import variaveis
import datetime
def box_text(texto):
    now = datetime.datetime.now()
    variaveis.BOX_TEXT += f"{now.strftime("%H:%M:%S")}: {texto}"
    variaveis.READ.set()
