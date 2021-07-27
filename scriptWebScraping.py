from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

distribuidora=5707 #CEEE
anos=list(range(2010,2021))
meses=list(range(1,13))

for ano in anos:
	col1, col2, col3, col4, col5, col6, col7, col8, col9 = [], [], [], [], [], [], [], [], []
	col10, col11, col12, col13, col14, col15, col16, col17, col18 = [], [], [], [], [], [], [], [], []
	col19, col20, col21, col22, col23, col24, col25, col26, col27 = [], [], [], [], [], [], [], [], []
	#col19, col20, col21, col22, col23, col24, col25, col26, col27 = [], [], [], [], [], [], [], [], []	
	for mes in meses:

		#html = urlopen("https://www2.aneel.gov.br")
		html = urlopen("https://www2.aneel.gov.br/aplicacoes/indicadores_de_qualidade/decFecSegMensal.cfm?mes="+str(mes)+"&ano="+str(ano)+"&regiao=SU&distribuidora="+str(distribuidora)+"&tipo=d")
		# https://www2.aneel.gov.br/aplicacoes/indicadores_de_qualidade/decFecSegMensal.cfm?mes=5&ano=2021&regiao=SU&distribuidora=5707&tipo=d
		bs = BeautifulSoup(html, 'html.parser')
		linhas = bs.find_all('tr')

		## Imprime todo texto contido em cada linha ##
		#for i in linhas:
		#    print(i.text)## Imprime o texto de cada uma das tags filhas ##



		for i in linhas:
			filhas = i.findChildren("td")
			if len(filhas)>10 and filhas[0].text!="CONJUNTO":
				col1.append(filhas[0].text.rstrip())
				col2.append(filhas[1].text.rstrip())
				col3.append(filhas[2].text.rstrip())
				col4.append(filhas[3].text.rstrip())
				col5.append(filhas[4].text.rstrip())
				col6.append(filhas[5].text.rstrip())
				col7.append(filhas[6].text.rstrip())
				col8.append(filhas[7].text.rstrip())
				col9.append(filhas[8].text.rstrip())
				col10.append(filhas[9].text.rstrip())
				col11.append(filhas[10].text.rstrip())
				col12.append(filhas[11].text.rstrip())
				col13.append(filhas[12].text.rstrip())
				col14.append(filhas[13].text.rstrip())
				col15.append(filhas[14].text.rstrip())
				col16.append(filhas[15].text.rstrip())
				col17.append(filhas[16].text.rstrip())
				col18.append(filhas[17].text.rstrip())
				col19.append(filhas[18].text.rstrip())
				col20.append(filhas[19].text.rstrip())
				col21.append(filhas[20].text.rstrip())
				col22.append(filhas[21].text.rstrip())
				col23.append(filhas[22].text.rstrip())
				col24.append(filhas[23].text.rstrip())
				col25.append(filhas[24].text.rstrip())
				col26.append(ano)
				col27.append(mes)
				#for j in filhas:
					#print(j.text.rstrip()+"|",end='')
			#print()


	df = pd.DataFrame(columns=None,index=None,data={'Col1': col1, 'Col2': col2, 'Col3': col3, 'Col4': col4, 'Col5': col5, 'Col6': col6, 'Col7': col7, 'Col8': col8, 
	'Col9': col9, 'Col10': col10,'Col11': col11, 'Col12': col12, 'Col13': col13, 'Col14': col14, 'Col15': col15, 'Col16': col16, 
	'Col17': col17, 'Col18': col18, 'Col19': col19, 'Col20': col20,'Col21': col21, 'Col22': col22, 'Col23': col23, 'Col24': col24, 'Col25': col25, 'Ano': col26, 'Mes': col27})
	df.head()

	df.to_csv('dist'+str(distribuidora)+'_'+str(ano)+'_indicadoresDetalhados'+'.csv')
	#df.to_csv('dist'+str(distribuidora)+'_'+str(ano)+'_'+str(mes)+'_indicadoresDetalhados'+'.csv')

#print(linhas.prettify())
print("Script de Web Scraping do Clodoaldo!")
