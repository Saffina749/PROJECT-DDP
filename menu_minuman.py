import streamlit as st

def minuman():
        st.subheader("Menu Minuman")
        menu_minuman = {
            1: ("es jeruk", 5000, "img/ES-JERUK.jpg"),  
            2: ("sop durian", 15000, "img/SOP-DURIAN.jpg"),  
            3: ("es campur", 10000, "img/ES-CAMPUR.jpg"),  
            4: ("matcha latte", 15000, "img/MATCHA-LATTE.jpg"),  
            5: ("cappuccino", 20000, "img/CAPPUCINO.jpg")  
        }

        pilihan_minuman = st.selectbox("Pilih minuman:", options=["es jeruk", "sop durian", "es campur", "matcha latte", "cappuccino"])
        gelas = st.number_input("Berapa gelas?", min_value=1, value=1)

        for key, value in menu_minuman.items():
            if value[0] == pilihan_minuman:
                st.image(value[2], caption=value[0], use_container_width=True)  
                total_minuman = gelas * value[1]
                st.write(f"{gelas} {pilihan_minuman} = Rp.{total_minuman}")
                return total_minuman, pilihan_minuman, gelas

        return 0, "", 0