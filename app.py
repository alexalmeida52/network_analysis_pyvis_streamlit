import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
import source.got as got
import source.routes as routes
import source.histograma as histograma
import source.community as community

Network(notebook=True)
st.title('Network Analysis')

def net_repr_html(self):
 nodes, edges, height, width, options = self.get_network_data()
 html = self.template.render(height=height, width=width, nodes=nodes, edges=edges, options=options)
 return html

Network._repr_html_ = net_repr_html
st.sidebar.title('Selecione a página que deseja visualizar!')
option=st.sidebar.selectbox('Selecione',('ABOUT', 'FILTERED ROUTES', 'HISTOGRAM', 'COMMUNITY', 'GOT'))
physics=st.sidebar.checkbox('Adicionar interatividade?')

routes.routes_func(physics)

if option == 'ABOUT':
  st.markdown("### **Sobre o dataset:** O OpenFlights/Airline Route Mapper Route Database mapeou 59.036 rotas entre 3.209 aeroportos em 531 companhias aéreas em todo o mundo em janeiro de 2012. Segue aqui o link do dataset disponível no Kaggle: <https://www.kaggle.com/datasets/open-flights/flight-route-database>\n### Os nós são aeroportos nomeados com o código aeroportuário IATA que é uma sigla composta por três letras, utilizada para designar os aeroportos em todo o mundo. É definido pela Associação Internacional de Transportes Aéreos, que tem sede em Toronto, no Canadá. Já as arestas são as conexões entre um aeroporto e outro, representam as linhas aéreas conectando origem e destino de viagens.")
  st.image("assets/atvd2_routes.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
  
if option=='ROUTES':
  HtmlFile = open("./html/routes.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)

got.got_func(physics)

if option == 'HISTOGRAM':
  histograma.generate_histogram()

if option == 'COMMUNITY':
  community.draw_community()

if option=='GOT':
  HtmlFile = open("./html/gameofthrones.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)
