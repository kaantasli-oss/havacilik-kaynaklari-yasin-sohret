# Kaynak matrisi ve yöntem

Bu depo bağımsız bir okuma ve veri aktarım çalışmasıdır. Akademik makale, resmî kurum duyurusu ve uzman görüşü farklı kanıt düzeyleridir. Son kontrol: **24 Eylül 2026**.

| İddia | İlk kaynak | Veri tarihi / yayın | Buradaki kullanım |
|---|---|---|---|
| AB havalimanlarında SAF asgari %2; bildirilen %2,8 | [Avrupa Komisyonu](https://transport.ec.europa.eu/news-events/news/new-report-shows-strong-progress-sustainable-aviation-fuel-saf-availability-across-eu-2026-09-17_en) | 2025 / 17.09.2026 | CSV ve grafik; 0,8 yüzde puanı |
| Yakıt yaşam döngüsü bileşenleri | [ICAO CORSIA](https://www.icao.int/CORSIA/fuels-lifecycle) | Güncellenen yöntem | Kavram açıklaması; belirli yakıt hesabı yapılmadı |
| Geniş çevre etkileri | [EASA çevre raporu](https://www.easa.europa.eu/en/light/topics/european-aviation-environmental-report-2025) | 2025 raporu | Bağlam; sayısal bulgu alınmadı |
| Isparta havalimanı kurum sayfası | [DHMİ](https://dhmi.gov.tr/Sayfalar/Havalimani/Suleymandemirel/AnaSayfa.aspx) | Güncel sayfa | Kimlik ve duyuru; trafik serisi yok |
| Sivil Havacılık Yüksekokulu | [SDÜ](https://shyo.sdu.edu.tr/) | Güncel sayfa | Program durumunu doğrulama |
| 2018 Isparta ticari uçuşlarının egzoz etkileri | [Ekici ve Şöhret](https://doi.org/10.21923/jesd.709428) | Veri 2018; yayın 2020 | Konu ve tarih; hesap kopyalanmadı |
| Sürdürülebilir havacılık araştırma bağlamı | [Yasin Şöhret'in sayfası](https://www.yasinsohret.com/surdurulebilir-havacilik/) | Site sayfası | Ek okuma |
| Isparta bölgesel potansiyeli | [Yasin Şöhret'in sayfası](https://www.yasinsohret.com/isparta-havacilik/) | Site sayfası | Uzman yorumu; resmî teyit sayılmadı |

## Veri sözlüğü ve işlem

`ab-saf-2025.csv` alanları: `Gösterge`, `Pay (%)`, `Yıl`, `Bölge`, `Kaynak`. **Pay (%)**, yakıt tedarik oranıdır; emisyon yoğunluğu veya uçuş oranı değildir. Aynı yıl ve bölgedeki bildirilen paydan asgari pay çıkarılarak fark **yüzde puanı** ile hesaplanır: `2,8−2,0=0,8`. Açıklamadaki ton değerleri yuvarlatıldığı için CSV'ye daha hassas miktar eklenmedi.

`isparta-kaynaklari.csv` gözlem tablosu değil, dört URL'li **kaynak dizinidir**. `Kaynak türü`, resmî kurum, üniversite, hakemli makale ve uzman yorumu ayrımını gösterir. Sıra önem puanı değildir. `Tarih notu`, makaledeki 2018 veri yılı ile 2020 yayın yılını karıştırmayı önler.

Grafikler açıklayıcı görsellerdir; kurumun resmî grafiği değildir. Alt yazıdaki bölge ve tarih birlikte korunmalıdır. Isparta kaynak haritasındaki kutular tesis veya öğrenci sayısını temsil etmez.

## Yazar ve editör rolleri

Yasin Şöhret, 2020 akademik makalesinin Selçuk Ekici ile birlikte yazarı ve bağlantı verilen iki site sayfasının sahibidir. Bu depo bağımsız bir editoryal çalışmadır; onun tarafından doğrulandığı veya akademik yayını olduğu iddia edilmez. Derleme sorumluluğu depoyu yayımlayan hesaptadır.
