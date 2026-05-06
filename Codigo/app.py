# Importar bibliotecas
import streamlit as st
import pickle
import numpy as np

# Carregar modelo
with open('Codigo/modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Criar página Streamlit
# Titulo e descrição
st.title("📊 Previsão de Risco de Defasagem")

st.write("Insira os dados do aluno para prever o risco de defasagem.")

# Formulário
IDA = st.number_input("Desempenho acadêmico (IDA)", 0.0, 10.0, 5.0)
IEG = st.number_input("Engajamento (IEG)", 0.0, 10.0, 5.0)
IAA = st.number_input("Autoavaliação (IAA)", 0.0, 10.0, 5.0)
IPS = st.number_input("Aspectos psicossociais (IPS)", 0.0, 10.0, 5.0)
IPP = st.number_input("Aspectos psicopedagógicos (IPP)", 0.0, 10.0, 5.0)
IPV = st.number_input("Ponto de virada (IPV)", 0.0, 10.0, 5.0)

# Botão de previsão
if st.button("Prever risco"):

    entrada = np.array([[IDA, IEG, IAA, IPS, IPP, IPV]])

    pred = modelo.predict(entrada)
    prob = modelo.predict_proba(entrada)[0][1]

    if pred[0] == 1:
        st.error(f"⚠️ Aluno em risco ({prob*100:.1f}%)")
    else:
        st.success(f"✅ Aluno sem risco ({prob*100:.1f}%)")