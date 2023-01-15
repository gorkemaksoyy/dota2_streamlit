import pandas as pd
import streamlit as st
rec_list = pd.read_csv("tavsiyeler.csv")
rec_list.drop("Unnamed: 0", axis=1, inplace=True)
rec_list.index = rec_list["Item_Names"]
rec_list.drop("Item_Names", axis=1, inplace=True)
hero_list = list(rec_list.columns)
item_list = list(rec_list.index)
hero_chosen = st.selectbox("Hero seçiniz", hero_list) #sidebar.selectbox ile yan tarafta kutucuk açılabilir
#st.columns sayfayı bölüyor, col1, col2 = st.columns(2) sonrada with col1: diye başlıyoruz

if hero_chosen:
    item_list_suggestions = []
    for index in range(0, len(rec_list.index)):
        if rec_list[hero_chosen][index] == rec_list[hero_chosen][index]:
            item_list_suggestions.append(item_list[index])
    len(item_list_suggestions)
    item_chosen = st.selectbox("Eşya seçiniz", item_list_suggestions)

if item_chosen:
    recommendation = rec_list.loc[rec_list.index == item_chosen,hero_chosen][0][1:-1]
    new_list = recommendation.split(",")
    fin_list = []
    for index, elem in enumerate(new_list):
        if index == 0:
            new_elem = elem[1:-1]
            fin_list.append(new_elem)
        else:
            new_elem = elem[2:-1]
            fin_list.append(new_elem)
    for elem in fin_list:
        st.write(elem)
