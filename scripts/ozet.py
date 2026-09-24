#!/usr/bin/env python3
"""Yerel CSV'lerden kaynak özetini yeniden üretir; internete bağlanmaz."""

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(name):
    with (ROOT / "data" / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    saf = read_csv("ab-saf-2025.csv")
    assert len(saf) == 2, "SAF karşılaştırması tam iki gösterge içermeli"
    assert {row["Yıl"] for row in saf} == {"2025"}, "Yıllar aynı olmalı"
    assert len({row["Bölge"] for row in saf}) == 1, "Coğrafi kapsam aynı olmalı"
    shares = {row["Gösterge"]: Decimal(row["Pay (%)"]) for row in saf}
    target = shares["Zorunlu asgari SAF payı"]
    actual = shares["Bildirilen SAF tedarik payı"]
    print(f"AB 2025 SAF tedariki: asgari %{target}; bildirilen %{actual}")
    print(f"Fark: {actual - target} yüzde puanı (emisyon azaltımı değil)")

    sources = read_csv("isparta-kaynaklari.csv")
    print("\nIsparta kaynak dizini (trafik istatistiği değildir):")
    for row in sources:
        assert row["URL"].startswith("https://"), "Kaynak bağlantısı gerekli"
        print(f"- {row['Başlık']} | {row['Kaynak türü']} | {row['Tarih notu']}")


if __name__ == "__main__":
    main()
