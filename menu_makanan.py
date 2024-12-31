import streamlit as st

def makanan():
        st.subheader("Menu Makanan")
        menu_makanan = {
            1: ("nasi uduk", 10000, "img/NASI-UDUK.jpe"),  
            2: ("nasi pecel", 15000, "img/NASI-PECEL.jpg"),  
            3: ("nasi campur", 15000, "img/NASI-CAMPUR.jpg"),  
            4: ("roti bakar", 5000, "img/ROTI-BAKAR.jpg"),  
            5: ("kentang", 5000, "img/KENTANG.jpg")  
        }

        pilihan_makanan = st.selectbox("Pilih makanan:", options=["nasi uduk", "nasi pecel", "nasi campur", "roti bakar", "kentang"])
        porsi = st.number_input("Berapa porsi?", min_value=1, value=1)

        for key, value in menu_makanan.items():
            if value[0] == pilihan_makanan:
                st.image(value[2], caption=value[0], use_container_width=True)  
                total_makanan = porsi * value[1]
                st.write(f"{porsi} {pilihan_makanan} = Rp.{total_makanan}")
                return total_makanan, pilihan_makanan, porsi

        return 0, "", 0

total_makanan, makanan_terpilih, porsi = makanan()

