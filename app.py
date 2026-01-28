from flask import Flask, render_template, request

app = Flask(__name__)

# Şimdilik sabit fiyatlar (mantığı oturtuyoruz)
URUNLER = {
    "nutella": {
        "Migros": 199,
        "A101": 189,
        "Şok": 195
    },
    "çay": {
        "Migros": 120,
        "A101": 110,
        "Şok": 115
    },
    "şeker": {
        "Migros": 95,
        "A101": 90,
        "Şok": 92
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = None
    en_ucuz = None
    urun_adi = ""

    if request.method == "POST":
        urun_adi = request.form.get("urun").lower()
        if urun_adi in URUNLER:
            sonuc = URUNLER[urun_adi]
            en_ucuz = min(sonuc, key=sonuc.get)

    return render_template(
        "index.html",
        sonuc=sonuc,
        en_ucuz=en_ucuz,
        urun_adi=urun_adi
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

