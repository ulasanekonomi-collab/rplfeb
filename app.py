import streamlit as st

# Config
st.set_page_config(page_title="RPL UNISBA", layout="wide")

# Header
st.title("📘 Sistem Rekognisi Pembelajaran Lampau (RPL)")
st.subheader("Program Studi Ekonomi Pembangunan - FEB UNISBA")

st.markdown("---")

# Menu sederhana
menu = st.sidebar.selectbox("Menu", [
    "Home",
    "Pendaftaran",
    "Form Evaluasi Diri (FED)",
    "Penilaian Asesor",
    "Hasil"
])

# HOME
if menu == "Home":
    st.success("Sistem RPL siap digunakan 🚀")
    st.write("""
    Sistem ini digunakan untuk:
    - Pendaftaran peserta RPL
    - Pengisian Evaluasi Diri (FED)
    - Penilaian oleh asesor
    - Penetapan hasil RPL
    """)

# PENDAFTARAN
elif menu == "Pendaftaran":
    st.header("Form Pendaftaran")
    nama = st.text_input("Nama")
    email = st.text_input("Email")

    if st.button("Daftar"):
        st.success(f"{nama} berhasil terdaftar!")

# FED
elif menu == "Form Evaluasi Diri (FED)":
    st.header("Form Evaluasi Diri")

    cpl = st.selectbox("Pilih CPL", ["CP1", "CP3", "CP5", "CP7", "CP10"])
    pengalaman = st.text_area("Jelaskan pengalaman Anda")

    if st.button("Simpan FED"):
        st.success("FED berhasil disimpan")

# ASESOR
elif menu == "Penilaian Asesor":
    st.header("Penilaian Asesor")

    n1 = st.slider("Knowledge", 1, 4)
    n2 = st.slider("Application", 1, 4)
    n3 = st.slider("Impact", 1, 4)

    if st.button("Hitung Hasil"):
        rata = (n1 + n2 + n3) / 3

        if rata >= 3:
            hasil = "Diakui Penuh"
        elif rata >= 2:
            hasil = "Diakui Sebagian"
        else:
            hasil = "Tidak Diakui"

        st.success(f"Hasil: {hasil}")

# HASIL
elif menu == "Hasil":
    st.header("Dashboard Hasil")

    st.metric("Total Peserta", 20)
    st.metric("Diakui Penuh", 12)
    st.metric("Diakui Sebagian", 5)
    st.metric("Tidak Diakui", 3)
