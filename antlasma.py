#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""900 Devirde Barış Antlaşması — çalışan, resmi, gereksiz protokol."""

import time
import random
import sys

MADDELER = [
    "Madde 1: Hiçbir çorap, eşi olmadan sınır dışı edilemez.",
    "Madde 2: Durulama hakkı; sıcak su, soğuk su ve ılık su için eşittir.",
    "Madde 3: 900 devir istisnai sıkmadır. Amacı barış, sonucu hafif buruşuktur.",
    "Madde 4: Kumaş yumuşatıcı tarafsız bölgedir. Kimse oraya seçim afişi asamaz.",
    "Madde 5: Kayıp çorap komisyonu kurulur. Rapor yazılmaz, çünkü çorap zaten yok.",
    "Madde 6: Tambur döner. Gündem de dönebilir. Bu teknik bir tespittir.",
    "Madde 7: Program bitişinde herkes temiz çıkar. Kir iddiası kabul edilmez.",
]

ASAMALAR = [
    ("Ön yıkama", 1.0),
    ("Ana yıkama", 1.2),
    ("Durulama", 1.4),
    ("Sıkma 900 d/dk", 1.6),
    ("Antlaşma mühürleme", 0.8),
]


def damga():
    return (
        "\n---\n"
        "Damga: Kayyum Grok · Tentivory · 30 Eylül 2026\n"
        "İmza: ıslak, sonra kuru, sonra yine ıslak (durulama şart)\n"
        "Ciddiyet seviyesi: yüksek / içerik seviyesi: düşük\n"
    )


def main():
    print("=" * 56)
    print("  900 DEVİRDE BARIŞ ANTLAŞMASI — OTURUM AÇILDI")
    print("=" * 56)
    print("Katılımcılar hazır. Çorap sağ henüz gelmedi. Olsun.\n")

    for i, (ad, bekle) in enumerate(ASAMALAR, start=1):
        print(f"[{i}/{len(ASAMALAR)}] Aşama: {ad}")
        time.sleep(min(bekle, 0.4))  # gerçek hayatta daha uzun sürer, burada nezaket
        madde = MADDELER[(i - 1) % len(MADDELER)]
        print(f"    » {madde}")
        if random.random() < 0.35:
            print("    (tamburdan ufak bir itiraz yükseldi, yok sayıldı)")
        print()

    print("OYLAMA: Tambur evet dedi. Çünkü tambur hep döner.")
    print("SONUÇ: Antlaşma yürürlüktedir. Çamaşırları asınız.\n")
    print(damga())
    return 0


if __name__ == "__main__":
    sys.exit(main())
