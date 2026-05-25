from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    totalProduk = 10
    stokMenipis = 2
    transaksiHariIni = 9
    pendapatan = 2500000

    format_pendapatan = "Rp {:,.0f}".format(pendapatan).replace(",", ".")

    hasil_penjualan = {
      "Senin": {
        "makanan" : 5,
        "minuman" : 2,
        "alat tulis" : 2
      },
      "Selasa": {
        "makanan" : 0,
        "minuman" : 5,
        "alat tulis" : 5
      },
      "Rabu": {
        "makanan" : 5,
        "minuman" : 5,
        "alat tulis" : 5
      },
      "Kamis": {
        "makanan" : 6,
        "minuman" : 7,
        "alat tulis" : 5
      },
      "Jumat": {
        "makanan" : 10,
        "minuman" : 5,
        "alat tulis" : 7
      }
    }
    y_hasilPenjualan = []
    for hari in hasil_penjualan:
      hasil = sum(hasil_penjualan[hari].values())
      y_hasilPenjualan.append(hasil)
      
    return render_template('index.html', 
    data_penjualan=y_hasilPenjualan, 
                        card_product=totalProduk, 
                        card_stock=stokMenipis, 
                        card_transaction=transaksiHariIni, 
                        card_income=format_pendapatan,
                        grafik_penjualan=hasil_penjualan)

if __name__=='__main__':
    app.run(debug=True)