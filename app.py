import streamlit as st
from kasir import kasir_app
from database import database_app
from menu_makanan import makanan
from menu_minuman import minuman


page = st.sidebar.radio("Pilih Halaman", ("Kasir", "Database","Menu Makanan","Menu Minuman"))

if page == "Kasir":
    kasir_app()
elif page == "Database":
    database_app()
elif page == "Menu Makanan":
    makanan()
elif page == "Menu Minuman":
    minuman()