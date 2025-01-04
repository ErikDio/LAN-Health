import openpyxl
from openpyxl.chart import BarChart, Reference, LineChart
import openpyxl.workbook
from copy import deepcopy
class Grafico:
    DEBUG = False
    LOG = False
    arquivo_planilha = None
    def setup(self, dbg, log, lcl):
        self.DEBUG = dbg
        self.LOG = log
        self.arquivo_planilha = lcl
    def GerarGrafico(self):
        wb = openpyxl.load_workbook(self.arquivo_planilha)
        
        wbgrafico = wb["Grafico"]
        wbdados = wb["Dados"]
        
        dados_uso_hoje = Reference(wbdados, min_col=2, max_col=3, min_row=1, max_row=25)
        dados_uso_ontem = Reference(wbdados, min_col=4, max_col=5, min_row=1, max_row=25)
        dados_conflito = Reference(wbdados, min_col=6, max_col=6,min_row=1, max_row=25)
        dados_estimativa = Reference(wbdados, min_col=7, max_col=7,min_row=1, max_row=25)
        dados_estimativa_ontem = Reference(wbdados, min_col=8, max_col=8,min_row=1, max_row=25)

        cats = Reference(wbdados, min_col=1, max_col=1, min_row=2, max_row=25)
        
        uso_grafico = BarChart()
        uso_grafico.type = "col"
        uso_grafico.style = 13
        uso_grafico.grouping = "stacked"
        uso_grafico.overlap = 100
        uso_grafico.y_axis.title = "Dispositivos Online (Hoje)"
        uso_grafico.x_axis.title = "Horário"    
        uso_grafico.width = 30
        uso_grafico.height = 12
        uso_grafico.y_axis.scaling.max = 255
        uso_grafico.y_axis.scaling.min = 0

        uso_grafico_ontem = deepcopy(uso_grafico)
        uso_grafico_ontem.y_axis.title = "Dispositivos Online (Ontem)"

        conflito_grafico = LineChart()
        conflito_grafico.title = "IPs Conflituosos Ativos"
        conflito_grafico.style = 13
        conflito_grafico.x_axis.title = 'Horário'
        conflito_grafico.y_axis.title = 'Conflitos'
        conflito_grafico.width = 30
        conflito_grafico.height = 12
        conflito_grafico.y_axis.scaling.min = 0
        
        estimativa_grafico = deepcopy(conflito_grafico)
        estimativa_grafico.title = "Velocidade de download (Hoje)"

        estimativa_grafico_ontem = deepcopy(conflito_grafico)
        estimativa_grafico_ontem.title = "Velocidade de download (ontem)"
        
        uso_grafico.add_data(dados_uso_hoje, titles_from_data=True)
        uso_grafico.set_categories(cats)

        uso_grafico_ontem.add_data(dados_uso_ontem, titles_from_data=True)
        uso_grafico_ontem.set_categories(cats)

        conflito_grafico.add_data(dados_conflito, titles_from_data=True)
        conflito_grafico.set_categories(cats)

        estimativa_grafico.add_data(dados_estimativa, titles_from_data=True)
        estimativa_grafico_ontem.add_data(dados_estimativa_ontem, titles_from_data=True)

        wbgrafico.add_chart(uso_grafico, f"A{1}")
        wbgrafico.add_chart(uso_grafico_ontem, f"A{1+26}")
        wbgrafico.add_chart(conflito_grafico, f"A{1+26*2}")
        wbgrafico.add_chart(estimativa_grafico, f"A{1+26*3}")
        wbgrafico.add_chart(estimativa_grafico_ontem, f"A{1+26*4}")
        wb.save(self.arquivo_planilha)