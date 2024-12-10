import pandas as pd
import sqlite3 as sql
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st



# Menambahkan CSS untuk styling
st.markdown("""
/* Desktop - 1 */

position: relative;
width: 1440px;
height: 1024px;

background: #E1AFAF;


/* Rectangle 3 */

position: absolute;
width: 1440px;
height: 1024px;
left: 0px;
top: 0px;

background: linear-gradient(243.18deg, #FFFFFF 0%, #68A7FF 100%);


/* PaperFind */

position: absolute;
width: 219px;
height: 93px;
left: 78px;
top: 43px;

font-family: 'Inknut Antiqua';
font-style: normal;
font-weight: 700;
font-size: 36px;
line-height: 93px;
/* identical to box height */

color: #000000;



/* Home */

position: absolute;
width: 55px;
height: 41px;
left: 1053px;
top: 64px;

font-family: 'Inknut Antiqua';
font-style: normal;
font-weight: 700;
font-size: 16px;
line-height: 41px;

color: #000000;



/* Login */

position: absolute;
width: 53px;
height: 41px;
left: 1179px;
top: 64px;

font-family: 'Inknut Antiqua';
font-style: normal;
font-weight: 700;
font-size: 16px;
line-height: 41px;

color: #000000;



/* Sign Up */

position: absolute;
width: 71px;
height: 41px;
left: 1303px;
top: 64px;

font-family: 'Inknut Antiqua';
font-style: normal;
font-weight: 700;
font-size: 16px;
line-height: 41px;

color: #000000;



/* Welcome to PaperFind */

position: absolute;
width: 334px;
height: 38px;
left: 119px;
top: 392px;

font-family: 'Inria Serif';
font-style: normal;
font-weight: 700;
font-size: 32px;
line-height: 38px;

color: #0026FF;



/* Where research gets real. Find what you need, stress-free and lightning fast! */

position: absolute;
width: 660px;
height: 174px;
left: 119px;
top: 452px;

font-family: 'Inria Serif';
font-style: normal;
font-weight: 700;
font-size: 48px;
line-height: 58px;

color: #000000;



/* Rectangle 1 */

position: absolute;
width: 144px;
height: 66px;
left: 119px;
top: 682px;

background: #FFFFFF;
border-radius: 30px;


/* Sign Up */

position: absolute;
width: 113px;
height: 38px;
left: 135px;
top: 696px;

font-family: 'Inria Serif';
font-style: normal;
font-weight: 700;
font-size: 32px;
line-height: 38px;

color: #000000;



/* Rectangle 2 */

position: absolute;
width: 144px;
height: 66px;
left: 309px;
top: 682px;

background: #FFFFFF;
border-radius: 30px;


/* Login */

position: absolute;
width: 82px;
height: 38px;
left: 340px;
top: 696px;

font-family: 'Inria Serif';
font-style: normal;
font-weight: 700;
font-size: 32px;
line-height: 38px;

color: #000000;


/* Rectangle 2 */

position: absolute;
width: 144px;
height: 66px;
left: 309px;
top: 682px;

background: #FFFFFF;
border-radius: 30px;""", unsafe_allow_html=True)


# Membaca file CSV dan menjadikan baris pertama sebagai header
df = pd.read_csv('D:\Download\scimagojr 2023.csv', delimiter=';', header=0)

# Menampilkan beberapa baris untuk memverifikasi
print(df.head())

# Mengecek data yang hilang dan jumlahnya
print("\nMissing values per column:")
print(df.isnull().sum())
