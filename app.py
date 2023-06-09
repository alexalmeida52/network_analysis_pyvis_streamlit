import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
import source.got as got
import source.routes as routes

Network(notebook=True)
st.title('Hello Pyvis')
# make Network show itself with repr_html

def net_repr_html(self):
 nodes, edges, height, width, options = self.get_network_data()
 html = self.template.render(height=height, width=width, nodes=nodes, edges=edges, options=options)
 return html

Network._repr_html_ = net_repr_html
st.sidebar.title('Selecione o gráfico que deseja visualizar!')
option=st.sidebar.selectbox('Selecione',('ROUTES', 'GOT'))
physics=st.sidebar.checkbox('Adicionar interatividade?')

routes.routes_func(physics)

if option=='ROUTES':
  HtmlFile = open("./html/routes.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)



