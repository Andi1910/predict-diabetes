import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(page_title="Prediksi Diabetes", layout="wide")
# Create menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Prediksi"],
    icons=["house", "calculator"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

row0_spacer1, row0_1, row0_spacer2= st.columns(
    (0.1, 3.2, 0.1)
)
row1_spacer1, row1_1, row1_spacer2, row1_2 = st.columns((0.1, 1.5, 0.1, 1.5))
#row1_spacer1, row1_1, row1_spacer2 = st.columns((0.1, 3.2, 0.1))
row0_spacer3, row3_0, row0_spacer3= st.columns((0.1, 3.2, 0.1))
# Load dataset
df = pd.read_csv('Data/diabetes.csv')
# Kelompok usia
age_grup = []
for i in df['Age']:
    if i >= 17 and i <= 25:
        age_grup.append('Remaja Akhir')
    elif i >= 26 and i <= 35:
        age_grup.append('Dewasa Awal')
    elif i >= 36 and i <= 45:
        age_grup.append('Dewasa Akhir')
    elif i >= 46 and i <= 55:
        age_grup.append('Lansia Awal')
    elif i >= 56 and i <= 65:
        age_grup.append('Lansia Akhir')
    else:
        age_grup.append('Manula')
df['AgeGrup'] = age_grup
# Kelompok BMI
BMI_grup = []
for i in df['BMI']:
    if i >= 0 and i <= 18.5:
        BMI_grup.append('Kurus')
    elif i >= 18.6 and i <= 22.9:
        BMI_grup.append('Normal')
    elif i >= 23 and i <= 24.9:
        BMI_grup.append('Gemuk')
    elif i >= 25 and i <= 29.9:
        BMI_grup.append('Obesitas')
    else:
        BMI_grup.append('Obesitas II')            
df['BMIGrup'] = BMI_grup
# Model
model = pd.read_pickle('model_svm.pkl')
# Handle selected option
if selected == "Home":
    row0_1.title("App Prediksi Diabetes")
    with row0_1:
        st.markdown(
            "App Prediksi Diabtes adalah sebuah aplikasi yang berguna untuk memPrediksi kemungkinan seseorang menderita diabetes berdasarkan beberapa fitur yang dimasukkan. Aplikasi ini menggunakan dataset diabetes dari Kaggle untuk melakukan Prediksi. Dengan memasukkan fitur yang relevan, seperti kadar gula darah, tekanan darah, dan sebagainya, aplikasi ini dapat memberikan Prediksi yang cukup akurat mengenai kemungkinan seseorang menderita diabetes. Aplikasi ini sangat bermanfaat bagi orang-orang yang ingin mengetahui apakah mereka berisiko terkena diabetes atau tidak, sehingga dapat memperbaiki pola makan dan gaya hidup mereka untuk mencegah terjadinya penyakit diabetes. by Andi Irfan Daeng Mappa (1519620004), Braina Mulya Tritama (1519620006), Rafiif Ikbaar Taufiqulhakiim (1519620032)"
        )
        st.markdown('Dataset : https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset')
        st.write(df.head())

elif selected == "Prediksi":
    with row0_1:
        st.subheader('Masukkan Data')
    with row1_1:
        pregnancies = st.number_input('Riwayat Kehamilan', min_value=0, max_value=20, value=0)
        glucose = st.number_input('Kadar Glukosa', min_value=0, max_value=200, value=0)
        blood_pressure = st.number_input('Tekanan darah tubuh (mm Hg)', min_value=0, max_value=200, value=0)
        skin_thickness = st.number_input('Ketebalan kulit (mm)', min_value=0, max_value=100, value=0)
    with row1_2:
        insulin = st.number_input('Hormon insulin (mu U/ml)', min_value=0, max_value=1000, value=0)
        bmi = st.number_input('Berat badan (kg)', min_value=0, max_value=100, value=0)
        diabetes_pedigree_function = st.number_input('Indikator riwayat diabetes keluarga', min_value=0, max_value=5, value=0)
        age = st.number_input('Usia', min_value=0, max_value=100, value=0)
    with row3_0:
        button = st.button('Test Prediksi')
        if button:
            data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
            pred = model.predict(data)
            if pred == 1:
                st.write('Pasien terkena diabetes')
            else:
                st.write('Pasien tidak terkena diabetes')
