# Import Library
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
import warnings

# Mengabaikan peringatan
warnings.filterwarnings('ignore')

# Setup
sns.set(style="whitegrid")

# Ganti dengan dua digit terakhir NIM (contoh: 01 -> 1, 00 -> 10)
np.random.seed(41)  # GANTI DENGAN DUA DIGIT TERAKHIR NIM ANDA

# Dataset Informatika
n_mhs = 150
data_informatika = {
    'Nama': [f'Mahasiswa_{i}' for i in range(n_mhs)],
    'Nilai_Algoritma': np.random.normal(80, 8, n_mhs),
    'Nilai_Pemrograman': np.random.normal(78, 10, n_mhs),
    'Jumlah_Proyek': np.random.randint(1, 10, n_mhs),
    'Semester': np.random.randint(1, 8, n_mhs),
    'IPK': np.random.uniform(2.8, 4.0, n_mhs),
    'Gender': np.random.choice(['Laki-laki', 'Perempuan'], n_mhs),
    'Umur': np.random.randint(18, 25, n_mhs),
    'Kekayaan': np.random.uniform(10, 100, n_mhs),
    'Kebahagiaan': np.random.uniform(0, 100, n_mhs),
    'Kategori': np.random.choice(['Web Dev', 'Data Science', 'AI', 'Cybersecurity'], n_mhs)
}
df_informatika = pd.DataFrame(data_informatika)

# Dataset Penyakit
n_pasien = 200
data_penyakit = {
    'ID_Pasien': [f'Pasien_{i}' for i in range(n_pasien)],
    'Usia': np.random.randint(20, 80, n_pasien),
    'Tekanan_Darah': np.random.normal(120, 15, n_pasien),
    'Kadar_Gula': np.random.normal(100, 20, n_pasien),
    'Durasi_Rawat': np.random.randint(1, 15, n_pasien),
    'Diagnosa': np.random.choice(['Diabetes', 'Hipertensi', 'Jantungan', 'Normal'], n_pasien),
    'Biaya': np.random.uniform(1000, 10000, n_pasien),
    'Gender': np.random.choice(['Laki-laki', 'Perempuan'], n_pasien),
    'IPK': np.random.uniform(2.0, 4.0, n_pasien),
    'Kekayaan': np.random.uniform(50, 500, n_pasien),
    'Kebahagiaan': np.random.uniform(0, 100, n_pasien)
}
df_penyakit = pd.DataFrame(data_penyakit)

# Visualisasi Seaborn - Scatter Plot (Informatika)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_informatika, x='IPK', y='Kebahagiaan', hue='Gender', size='Kekayaan', sizes=(20, 200))
plt.title('Hubungan IPK dan Kebahagiaan Mahasiswa Informatika')
plt.savefig('scatter_informatika_ipk_kebahagiaan.png')
plt.close()

# Visualisasi Seaborn - Box Plot (Informatika)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_informatika, x='Kategori', y='Kebahagiaan', hue='Gender', palette='Set2')
plt.title('Distribusi Kebahagiaan Mahasiswa Informatika per Kategori')
plt.savefig('box_informatika_kebahagiaan.png')
plt.close()

# Visualisasi Seaborn - Heatmap (Penyakit)
plt.figure(figsize=(10, 8))
corr_penyakit = df_penyakit[['Usia', 'Tekanan_Darah', 'Kadar_Gula', 'Durasi_Rawat', 'Biaya', 'IPK', 'Kekayaan', 'Kebahagiaan']].corr()
sns.heatmap(corr_penyakit, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korelasi Antar Variabel Pasien')
plt.savefig('heatmap_penyakit_korelasi.png')
plt.close()

# Visualisasi Seaborn - Bar Plot (Penyakit)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_penyakit, x='Diagnosa', y='Kekayaan', hue='Gender', palette='muted')
plt.title('Rata-rata Kekayaan Pasien Berdasarkan Diagnosa dan Gender')
plt.savefig('bar_penyakit_kekayaan.png')
plt.close()

# Visualisasi Bokeh - Scatter Plot (Penyakit)
output_file('bokeh_scatter_penyakit_usia_kebahagiaan.html')
source_penyakit = ColumnDataSource(df_penyakit)
p1 = figure(title="Usia vs Kebahagiaan Pasien (Interaktif)", x_axis_label='Usia', y_axis_label='Kebahagiaan', tools="pan,box_zoom,reset,save")
p1.scatter('Usia', 'Kebahagiaan', source=source_penyakit, size=8, color=Spectral6[2], legend_label='Pasien', fill_alpha=0.6)
p1.legend.click_policy = "hide"
show(p1)

# Visualisasi Bokeh - Bar Plot (Informatika)
output_file('bokeh_bar_informatika_ipk.html')
ipk_kategori_gender = df_informatika.groupby(['Kategori', 'Gender'])['IPK'].mean().reset_index()
source_informatika = ColumnDataSource(ipk_kategori_gender)
p2 = figure(x_range=ipk_kategori_gender['Kategori'].unique(), title="Rata-rata IPK per Kategori dan Gender", x_axis_label='Kategori', y_axis_label='IPK', tools="pan,reset,save")
p2.vbar(x='Kategori', top='IPK', width=0.4, source=source_informatika, color=Spectral6[3], legend_field='Gender')
p2.legend.click_policy = "hide"
show(p2)

# Visualisasi Baru: Violin Plot (Informatika)
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_informatika, x='Gender', y='Kekayaan', palette='Set3')
plt.title('Distribusi Kekayaan Mahasiswa Informatika berdasarkan Gender')
plt.savefig('violin_informatika_kekayaan.png')
plt.close()

# Dataset Penggunaan Software
n_users = 100
data_software = {
    'Nama': [f'User_{i}' for i in range(n_users)],
    'Umur': np.random.randint(18, 60, n_users),
    'Frekuensi_Penggunaan': np.random.randint(1, 10, n_users),
    'Kepuasan': np.random.uniform(0, 100, n_users),
    'Jenis_Software': np.random.choice(['Grafik', 'Pemrograman', 'Desain', ' Produktivitas'], n_users)
}
df_software = pd.DataFrame(data_software)

# Visualisasi Seaborn - Scatter Plot (Software)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_software, x='Umur', y='Kepuasan', hue='Jenis_Software', size='Frekuensi_Penggunaan', sizes=(20, 200))
plt.title('Hubungan Umur dan Kepuasan Pengguna Software')
plt.savefig('scatter_software_umur_kepuasan.png')
plt.close()

# Visualisasi Seaborn - Box Plot (Software)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_software, x='Jenis_Software', y='Kepuasan', palette='Set2')
plt.title('Distribusi Kepuasan Pengguna Software per Jenis')
plt.savefig('box_software_kepuasan.png')
plt.close()

# Visualisasi Seaborn - Heatmap (Software)
plt.figure(figsize=(10, 8))
corr_software = df_software[['Umur', 'Frekuensi_Penggunaan', 'Kepuasan']].corr()
sns.heatmap(corr_software, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korelasi Antar Variabel Pengguna Software')
plt.savefig('heatmap_software_korelasi.png')
plt.close()