from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  totalProduk = 10
  stokMenipis = 2
  transaksiHariIni = 7
  pendapatan = 1000000
  y_hasilPenjualan = [10, 5, 25, 15, 35]
  return render_template('index.html', data_penjualan=y_hasilPenjualan, card_product=totalProduk, card_stock=stokMenipis, card_transaction=transaksiHariIni, card_income=pendapatan)
  
if __name__=='__main__':
  app.run(debug=True)