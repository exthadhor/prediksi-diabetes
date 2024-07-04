import pickle
import streamlit as st

# Load model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Ubah tema Streamlit
st.set_page_config(
    page_title='Prediksi Diabetes Menggunakan SVM',
    layout='wide',
    initial_sidebar_state='expanded',
)

# Judul, gambar, dan deskripsi
st.title('𝐏𝐫𝐞𝐝𝐢𝐤𝐬𝐢 𝐃𝐢𝐚𝐛𝐞𝐭𝐞𝐬 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 SVM')
st.image('https://pnghq.com/wp-content/uploads/diabetes-free-png-images-95134.png', width=200)
st.write('Masukkan nilai-nilai berikut untuk memprediksi apakah seseorang mungkin menderita diabetes.')
st.write('')

# Informasi kelompok dengan tampilan yang lebih rapi
st.sidebar.title('𝐊𝐞𝐥𝐨𝐦𝐩𝐨𝐤 𝟓')
st.sidebar.subheader('𝐀𝐧𝐠𝐠𝐨𝐭𝐚 :')

# Membuat tabel anggota kelompok menggunakan Markdown
members_markdown = """
|  DOSEN PENGAMPU     |HAFIZH AL KAUTSAR AIDILOF, ST.,M.Kom          |
|---------------------|-------------|
| Nama                | NIM         |
|---------------------|-------------|
| 𝐌𝐮𝐡𝐚𝐦𝐦𝐚𝐝 𝐍𝐚𝐮𝐟𝐚𝐥 | 𝟐𝟏𝟎𝟏𝟕𝟎𝟏𝟗𝟏 |
| 𝐌𝐮𝐡𝐚𝐦𝐦𝐚𝐝 𝐍𝐨𝐯𝐚𝐥  | 𝟐𝟏𝟎𝟏𝟕𝟎𝟏𝟖𝟗 |
| 𝐌𝐮𝐧𝐢𝐫𝐰𝐚𝐧         | 𝟐𝟏𝟎𝟏𝟕𝟎𝟐𝟖𝟕 |
"""
st.sidebar.markdown(members_markdown)

# Membagi antara kolom untuk input
col1, col2 = st.columns(2)

# Input fields
with col1:
    Kehamilan = st.text_input('Kehamilan')
    TekananDarah = st.text_input('Tekanan Darah')
    Insulin = st.text_input('Insulin')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

with col2:
    Glukosa = st.text_input('Glukosa')
    KetebalanKulit = st.text_input('Ketebalan Kulit')
    BMI = st.text_input('BMI')
    Umur = st.text_input('Umur')

# Button for prediction
if st.button('Prediksi'):
    # Check if all fields are filled
    if not all([Kehamilan, Glukosa, TekananDarah, KetebalanKulit, Insulin, BMI, DiabetesPedigreeFunction, Umur]):
        st.warning('Harap isi semua bidang input terlebih dahulu.')
    else:
        # Make prediction
        diab_prediction = diabetes_model.predict([[Kehamilan, Glukosa, TekananDarah, KetebalanKulit, Insulin, BMI, DiabetesPedigreeFunction, Umur]])

        # Show diagnosis
        if diab_prediction[0] == 1:
            st.error('Pasien terkena diabetes.')
        else:
            st.success('Pasien tidak terkena diabetes.')

    st.write('')

# Footer
st.write('')
st.write('ꜱᴜᴍʙᴇʀ: ᴍᴏᴅᴇʟ ᴘʀᴇᴅɪᴋꜱɪ ᴅɪᴀʙᴇᴛᴇꜱ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴀʟɢᴏʀɪᴛᴍᴀ SVM.')
