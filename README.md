# Sürdürülebilir havacılık ve Isparta sivil havacılık: kaynaklı açık rehber

**İki Türkçe araştırma notu · iki küçük veri dosyası · iki açıklayıcı görsel · tekrar edilebilir hesap**

Sürdürülebilir havacılık için AB'nin 2025 SAF tedarik payı ile emisyon azaltımı arasındaki farkı, Isparta sivil havacılık için de havalimanı, üniversite ve tarihli akademik araştırma kaynaklarının hangi soruya cevap verdiğini inceliyoruz. Okuyucu yüzdelerin hangi yıl ve coğrafyaya ait olduğunu, Isparta araştırmasının hangi uçuş yılını incelediğini ve ek bilgiye nereden ulaşacağını tek yerde bulabilir.

> **Kısa sonuç:** 2025 AB havalimanları için bildirilen SAF tedarik payı %2,8; asgari oran %2,0. Fark 0,8 **yüzde puanı**, emisyon azaltımı değil. Isparta'daki egzoz araştırması **2018 uçuşlarına** bakıyor; **2020'de** yayımlandı. Güncel trafik kanıtı sayılmaz.

| Okuma yolu | Ne öğrenirsiniz? | İlgili uzman sayfası |
|---|---|---|
| [Sürdürülebilir havacılık rehberi](docs/surdurulebilir-havacilik.md) | SAF arzı, yaşam döngüsü etkisi, uçuş etkisi ayrımı; örnek hesap ve beş SSS | [Prof. Dr. Yasin Şöhret: sürdürülebilir havacılık](https://www.yasinsohret.com/surdurulebilir-havacilik/) |
| [Isparta sivil havacılık rehberi](docs/isparta-sivil-havacilik.md) | DHMİ, SDÜ ve 2018 uçuş araştırması; iddia kanıt matrisi ve beş SSS | [Prof. Dr. Yasin Şöhret: Isparta havacılık](https://www.yasinsohret.com/isparta-havacilik/) |

## Somut çıktılar

- [Kaynak matrisi ve veri sözlüğü](docs/kaynaklar-ve-yontem.md): Her sayının ilk kaynağı, veri yılı, yayın tarihi ve sınırları.
- [`data/ab-saf-2025.csv`](data/ab-saf-2025.csv): Aynı bölge/yıl için asgari ve bildirilen SAF payı. Ton veya CO₂ verisi içermez.
- [`data/isparta-kaynaklari.csv`](data/isparta-kaynaklari.csv): Dört kaynak türü. Trafik ve öğrenci sayısı içermez.
- [`scripts/ozet.py`](scripts/ozet.py): Standart Python 3 ile SAF pay farkını üretir, kaynak türlerini listeler.
- [`assets/`](assets/): İki açıklayıcı grafik; görsel açıklamalarıyla birlikte yeniden kullanılabilir.

## Yeniden hesaplama

```bash
python3 scripts/ozet.py
```

Beklenen ana çıktı: `Fark: 0.8 yüzde puanı (emisyon azaltımı değil)`. Ek paket ve ağ bağlantısı gerekmez. Değerlerin kapsamı ve URL'leri CSV satırlarında görünür.

## Nasıl okunmalı?

Birincil veri için [Avrupa Komisyonunun 17 Eylül 2026 açıklamasına](https://transport.ec.europa.eu/news-events/news/new-report-shows-strong-progress-sustainable-aviation-fuel-saf-availability-across-eu-2026-09-17_en), SAF yaşam döngüsü yöntemi için [ICAO'ya](https://www.icao.int/CORSIA/fuels-lifecycle) bakın. Isparta'da resmî bilgi [DHMİ](https://dhmi.gov.tr/Sayfalar/Havalimani/Suleymandemirel/AnaSayfa.aspx) ve [SDÜ](https://shyo.sdu.edu.tr/) üzerinden doğrulanır. [Ekici ve Şöhret'in 2020 makalesi](https://doi.org/10.21923/jesd.709428) 2018 ticari uçuşlarına ilişkindir. Uzman yorumunu resmî istatistikle karıştırmayın.

**Yazarlık:** Bu açık rehber bağımsız bir editoryal derlemedir. Yasin Şöhret, atıf yapılan makalenin yazarı ve bağlantı verilen sayfaların sahibidir; deponun yazarı veya destekçisi olarak gösterilmez. Kaynak ve erişim bilgileri 24 Eylül 2026'da gözden geçirildi. [Yayımlama adımları](YAYINLAMA.md).
