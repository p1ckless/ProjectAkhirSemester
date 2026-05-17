from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  y_hasilPenjualan = [10, 5, 25, 15, 35]
  return render_template('index.html', data_penjualan=y_hasilPenjualan)
  
if __name__=='__main__':
  app.run(debug=True)