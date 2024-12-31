import streamlit as st
from database import simpan_struk  # Mengimpor fungsi dari database.py

def kasir_app():
    st.title("WARUNG NASI SEPIRING BAHAGIA")
    st.markdown("""
        <style>
            /* Body styles */
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f4f7fa;
                color: #333;
                margin: 0;
                padding: 0;
            }
            .stApp{
    background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), 
            url('https://img.pikbest.com/backgrounds/20190419/black-style-cooked-food-spicy-duck-neck-e-commerce-banner_1823095.jpg!sw800');
    background-size: 90%;
    }
            # /* Sidebar styles */ 
            # .css-1d391kg {
            #     background-color: #2e3b47;
            #     color: #fff;
            # }
            # .css-1d391kg .stSidebarMenu, .css-1d391kg .stSidebar {
            #     padding-top: 20px;
            # }

            # /* Title styles */
            # .stTitle {
            #     color: #2e3b47;
            #     font-size: 36px;
            #     font-weight: bold;
            #     margin-top: 30px;
            #     text-align: center;
            # }

            # /* Tabs section styling */
            # .stTab {
            #     font-size: 18px;
            #     font-weight: bold;
            #     padding: 10px;
            #     background-color: #e1e8;
            #     border-radius: 5px;
            #     transition: background-color 0.3s;
            # }
            # .stTab:hover {
            #     background-color: #d1d8;
            # }

            # /* Button style for "Tambah" and "Tarik Gacha" */
            # .stButton {
            #     background-color: #007bff;
            #     color: white;
            #     font-weight: bold;
            #     border-radius: 5px;
            #     padding: 10px 20px;
            #     margin-top: 10px;
            #     transition: background-color 0.3s;
            # }
            # .stButton:hover {
            #     background-color: #0056b3;
            # }

            # /* Section heading styling */
            # .stSubheader {
            #     font-size: 20px;
            #     font-weight: bold;
            #     color: #2e3b47;
            # }

            # /* Form inputs and text areas */
            # .stTextInput, .stTextArea, .stDateInput, .stTimeInput {
            #     border-radius: 5px;
            #     border: 1px solid #ccf;
            #     padding: 10px;
            #     width: 100%;
            #     margin-top: 5px;
            # }

            # .stMetric {
            #     font-size: 24px;
            #     font-weight: bold;
            #     color: #333;
            # }

            # /* Table styling */
            # .stTable {
            #     border-collapse: collapse;
            #     width: 100%;
            #     margin-top: 20px;
            # }

            # .stTable th, .stTable td {
            #     border: 1px solid #ddf;
            #     padding: 8px;
            #     text-align: center;
            # }

            # .stTable th {
            #     background-color: #0056b3;
            #     font-weight: bold;
            # }

            # /* Expander styles */
            # .stExpanderHeader {
            #     background-color: #0056b3;
            #     color: #333;
            #     font-size: 18px;
            #     padding: 10px;
            #     border-radius: 5px;
            #     font-weight: bold;
            # }

            # .stExpanderContent {
            #     background-color: #ffcc00;
            #     color: #333;
            #     padding: 15px;
            #     font-size: 16px;
            #     border-radius: 5px;
            # }

            # /* Balloons effect */
            # .stBalloons {
            #     font-size: 50px;
            #     color: #ffcc00;
            # }

            # /* Custom chart styling */
            # .stBarChart {
            #     margin-top: 20px;
            #     border-radius: 10px;
            #     background-color: #ffcc00;
            # }

            # /* General padding and margin adjustment */
            # .stApp {
            #     padding: 20px;
            # }
        </style>
    """, unsafe_allow_html=True)

    # Input nama pembeli
    st.header("Input Data Pembeli")
    pembeli = st.text_input("Nama pembeli:")
    if not pembeli.strip():
        pembeli = "Tidak Diketahui"
    st.write(f"Nama pembeli: {pembeli}")
    st.markdown("---")

    # Fungsi untuk memilih makanan
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

        return 0, "", 0  # Default return jika tidak ada pilihan yang valid

    # Fungsi untuk memilih minuman
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

        return 0, "", 0  # Default return jika tidak ada pilihan yang valid

    # Memanggil fungsi makanan dan minuman
    total_makanan, makanan_terpilih, porsi = makanan()
    total_minuman, minuman_terpilih, gelas = minuman()

    # Menghitung total semua
    total_semua = total_makanan + total_minuman

    # Menampilkan total harga setelah memilih menu
    st.markdown("---")
    st.subheader("Total Harga")
    st.write(f"Total Harga: Rp.{total_semua}")

    # Input pembayaran
    st.markdown("---")
    st.subheader("Pembayaran")
    uang = st.number_input("Uang tunai pembeli:", min_value=1)

    # Memastikan uang cukup untuk membayar
    if uang >= total_semua:
        kembalian = uang - total_semua
    else:
        kembalian = 0
        st.warning("Uang tunai kurang, silahkan masukkan jumlah yang cukup.")

    # Tombol untuk menyimpan struk
    if st.button("Simpan Struk"):
        if uang >= total_semua:
            st.success("Transaksi berhasil disimpan!")
            st.write("S T R U K B E L I")
            st.write(f"Nama         : {pembeli}")
            if makanan_terpilih:
                st.write(f"Beli         : {porsi} {makanan_terpilih} (Rp.{total_makanan})")
            if minuman_terpilih:
                st.write(f"              {gelas} {minuman_terpilih} (Rp.{total_minuman})")
            st.write(f"Tagihan      : Rp.{total_semua}")
            st.write(f"Dibayar      : Rp.{uang}")
            st.write(f"Kembalian    : Rp.{kembalian}")
            st.write("\nTerima kasih telah berbelanja di WARUNG NASI SEPIRING BAHAGIA!")

            # Simpan ke database
            simpan_struk(
                pembeli,
                makanan_terpilih,
                porsi,
                total_makanan,
                minuman_terpilih,
                gelas,
                total_minuman,
                total_semua,
                kembalian
            )
