import matplotlib.pyplot as plt

file_path = "/home/atakan/Master's Degree/aileron_dt_matlab/mat files/tout_Circuit-Averaged.csv"

# CSV dosyasındaki başlık satırını atlayarak zaman verilerini oku
with open(file_path, 'r') as file1:
    # İlk satırı atlayalım
    next(file1)
    zaman1 = [float(line.strip()) for line in file1]

# Zaman serisi verilerini çizgi grafiği ile görselleştir
plt.plot(zaman1, label='Dosya 1')

# Eksen etiketleri ve başlık ekleyelim
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Time Series Visualization')

# Lejantı ekle
plt.legend()

# Grafiği göster
plt.show()
