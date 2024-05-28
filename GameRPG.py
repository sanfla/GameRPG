import streamlit as st
import time
import Greedy
import img_output
import bruteforce

st.title("Game RPG")
st.text("Selamat datang di aplikasi untuk menentukan kartu pada game RPG")

Boss = st.number_input('Masukan Power Boss:', 0, 10000)
Koin = st.number_input('Masukan Koin awal:', 0, 10000)

class Fighter:
    def __init__(self, harga, power, img_url, nama):
        self.harga = harga
        self.power = power
        self.img_url = img_url
        self.nama = nama

# Menampilkan gambar dan input di sebelahnya menggunakan kolom
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    image1 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Arthur.png', width=90, use_column_width='always', caption="Asterion")
    power1 = st.number_input("Power Fighter 1", 0, 10000, key='input1')
    Koin1 = st.number_input("Harga Fighter 1", 0, 10000, key='input2')

with col2:
    image2 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Assassin%20(1).png', width=90, use_column_width='always', caption="Shadowheart")
    power2 = st.number_input("Power Fighter 2", 0, 10000, key='input3')
    Koin2 = st.number_input("Harga Fighter 2", 0, 10000, key='input4')

with col3:
    image3 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Knight.png', width=90, use_column_width='always', caption="Karlach")
    power3 = st.number_input("Power Fighter 3", 0, 10000, key='input5')
    Koin3 = st.number_input("Harga Fighter 3", 0, 10000, key='input6')

with col4:
    image4 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wizard.png', width=90, use_column_width='always', caption="Lae'zel")
    power4 = st.number_input("Power Fighter 4", 0, 10000, key='input7')
    Koin4 = st.number_input("Harga Fighter 4", 0, 10000, key='input8')

with col5:
    image5 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wolf.png', width=90, use_column_width='always', caption="Wolf")
    power5 = st.number_input("Power Fighter 5", 0, 10000, key='input9')
    Koin5 = st.number_input("Harga Fighter 5", 0, 10000, key='input10')

# Array
img_urls = [
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Arthur.png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Assassin%20(1).png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Knight.png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wizard.png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wolf.png'
]
arrN = ["Asterion", "Shadowheart", "Karlach", "Lae'zel", "Wolf"]
arrP = [power1, power2, power3, power4, power5]
arrK = [Koin1, Koin2, Koin3, Koin4, Koin5]

# Membuat objek Fighter dan memasukkannya ke dalam list
fighters = []
# Melakukan iterasi pada indeks dari arrK
for i in range(len(arrK)):
    # Mengambil harga dari arrK
    harga = arrK[i]  
    # Mengambil power dari arrP
    power = arrP[i]  
    # Mengambil URL gambar dari img_urls
    img_url = img_urls[i]  
    # Mengambil nama dari arrN
    nama = arrN[i] 
    # Membuat objek Fighter dan menambahkannya ke dalam list fighters
    fighter = Fighter(harga, power, img_url, nama)
    fighters.append(fighter)


hasil = []
hfighter= []

#Metode = st.radio('Metode yang ingin dipakai', ['Greedy by Power', 'Greedy by Harga', 'Brute Force'])
Metode = st.selectbox('Pilih Metode yang ingin digunakan',['Greedy by Power', 'Greedy by Harga', 'Brute Force'])
if st.button('Hitung'):
    start = time.time()
    if Metode == "Greedy by Power":
        # Mengurutkan fighters berdasarkan power menggunakan insertionSort
        Greedy.insertionSortDesc(fighters, keyPower=lambda x: x.power) #lambda adalah fungsi sederhana satu baris

        # Algoritma Knapsack menggunakan Greedy
        Koin = Greedy.greedyByPower(fighters, hasil, hfighter, Koin)

        st.write("Menggunakan Algoritma Greedy by Power")
        st.write("Hasil Greedy by Power:")

        # Menampilkan output gambar
        img_output.output(hasil)

    elif Metode == "Greedy by Harga":
        # Mengurutkan fighters berdasarkan power menggunakan insertionSort
        Greedy.insertionSortAsc(fighters, keyPower=lambda x: x.harga) #lambda adalah fungsi sederhana satu baris

        # Algoritma Knapsack menggunakan Greedy
        Koin = Greedy.greedyByHarga(fighters, hasil, hfighter, Koin)

        st.write("Menggunakan Algoritma Greedy by Harga")
        st.write("Hasil Greedy by Harga:")
        
        # Menampilkan output gambar
        img_output.output(hasil)

    elif Metode == "Brute Force":
        st.write("Menggunakan Algoritma Brute Force")
        st.write("Hasil Bruteforce:")

        Koin = bruteforce.bruteForce(fighters, hasil, hfighter, Koin)

        # Menampilkan output gambar
        img_output.output(hasil)

    stop = time.time()
    duration = float(stop - start)

    st.success(f'Fighter : {hfighter}')
    st.success(f'Sisa Koin : {Koin}')
    st.success(f"Running time: {duration} seconds")