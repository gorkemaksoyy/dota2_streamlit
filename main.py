#pip install streamlit
import pandas as pd
import streamlit as st
from openpyxl import Workbook
rec_list = pd.read_excel("tavsiye_listesi.xlsx")
rec_list.index = rec_list["Item_Names"]
rec_list.drop("Item_Names", axis=1, inplace=True)
hero_list = list(rec_list.columns)
item_list = list(rec_list.index)
hero_chosen = st.selectbox("Hero seçiniz", hero_list) #sidebar.selectbox ile yan tarafta kutucuk açılabilir
#st.columns sayfayı bölüyor, col1, col2 = st.columns(2) sonrada with col1: diye başlıyoruz

if hero_chosen:
    item_list_suggestions = []
    for index in range(0, len(rec_list.index)):
        if rec_list["Anti-Mage"][index] == rec_list["Anti-Mage"][index]:
            item_list_suggestions.append(item_list[index])
    len(item_list_suggestions)
    item_chosen = st.selectbox("Eşya seçiniz", item_list_suggestions)

if item_chosen:
    recommendation = list(rec_list[hero_chosen][item_chosen])
    for item in recommendation:
        st.write(item)
