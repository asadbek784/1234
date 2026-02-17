import json
import os
import logging
import re
from datetime import datetime
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)
user = 'users.json'
data = 'data.json'


def Malumot() -> Dict[str, Any]:
    return {
        "matnlar": {
            "boshlash": "🍔 Fast-cooking botiga xush kelibsiz!\n\nBizning bot orqali eng mazali burgerlarni buyurtma qiling!",
            "telefon_sorash": "📱 Telefon raqamingizni yuboring:",
            "telefon_url": "📱 Telefon raqamni yuborish",
            "telefon_xato": "❌ Iltimos, telefon raqamingizni yuboring!",
            "manzil_sorash": "📍 Manzilingizni kiriting:",
            "manzil_url": "📍 Manzilni yuborish",
            "manzil_xato": "❌ Iltimos, to'liq manzil kiriting!",
            "royxat_muvaffaqiyat": "✅ Ro'yxatga muvaffaqiyatli qo'shildingiz!",
            "royxat_xato": "❌ Ro'yxatga qo'shilmadi!",
            "asosiy_menyu": "🏠 Asosiy menyu",
            "kategoriya_tanlash": "🍽 Kategoriyani tanlang:",
            "savat_bosh": "🛒 Savatingiz bo'sh",
            "sozlamalar_menyu": "⚙️ Sozlamalar bo'limi:\n\nKerakli amalni tanlang.",
            "buyurtma_qabul": "Buyurtma qabul qilindi!",
            "admin_xush": "👨‍💼 Admin panelga xush kelibsiz!",
            "aloqa_malumot": "📞 Biz bilan bog'lanish:\n\n📱 Telefon: +998 90 123 45 67\n📧 Email: info@burgerhouse.uz\n📍 Manzil: Toshkent sh., Amir Temur ko'chasi 1-uy",
            "haqida_malumot": "🏪 Burger House haqida:\n\nBiz 2020 yildan beri eng mazali burgerlarni tayyorlaymiz. Bizning maqsadimiz - har bir mijozga sifatli va mazali taom yetkazish.",
            "orqaga": "⬅️ Orqaga",
            "parol": "123456789"
        },
        "menyu": {
            "asosiy": {
                "dokon": "🍽 Do'kon",
                "savat": "🛒 Savat",
                "buyurtmalar": "📖 Mening buyurtmalarim",
                "aloqa": "📞 Biz bilan bog'lanish",
                "haqida": "ℹ️ Biz haqimizda",
                "sozlamalar": "⚙️ Sozlamalar"
            },
            "admin": {
                "buyurtmalar": "📋 Buyurtmalar",
                "foydalanuvchilar": "👥 Foydalanuvchilar",
                "statistika": "📊 Statistika",
                "mahsulotlar": "🍔 Mahsulotlar",
                "sozlamalar": "⚙️ Admin sozlamalari"
            },
            "foydalanuvchi_amallar": {
                "qayta_royxat": "♻️ Qayta ro'yxatdan o'tish",
                "buyurtma_bekor": "❌ Buyurtmani bekor qilish"
            },
            "savat": {
                "tolov": "💳 Buyurtma berish",
                "tozalash": "🗑 Savatni tozalash"
            },
            "holat": {
                "pending": "kutilmoqda",
                "accepted": "qabul qilindi",
                "processing": "tayyorlanmoqda",
                "completed": "yakunlangan",
                "cancelled": "bekor qilingan"
            }
        },
        "kategoriyalar": {
            "burgerlar": {
                "nomi": "🍔 Burgerlar",
                "rasm": "img/burgers.png",
                "mahsulotlar": {
                    "klassik_burger": {
                        "nomi": "Klassik Burger",
                        "tavsif": "Go'sht, pishloq, pomidor, salat",
                        "narx": 25000,
                        "id": 1
                    },
                    "chizburger": {
                        "nomi": "Chizburger",
                        "tavsif": "Go'sht, ikki qatlam pishloq, sous",
                        "narx": 28000,
                        "id": 2
                    },
                    "katta_burger": {
                        "nomi": "Big Burger",
                        "tavsif": "Katta burger, ikki qatlam go'sht",
                        "narx": 35000,
                        "id": 3
                    },
                    "tovuq_burger": {
                        "nomi": "Tovuq Burger",
                        "tavsif": "Tovuq filesi, salat, sous",
                        "narx": 30000,
                        "id": 4
                    }
                }
            },
    
            "ichimliklar": {
                "nomi": "🥤 Ichimliklar",
                "rasm": "img/drinks.png",
                "mahsulotlar": {
                    "kola": {
                        "nomi": "Coca Cola",
                        "tavsif": "0.5L sovuq ichimlik",
                        "narx": 8000,
                        "id": 5
                    },
                    "fanta": {
                        "nomi": "Fanta",
                        "tavsif": "0.5L apelsinli ichimlik",
                        "narx": 8000,
                        "id": 6
                    },
                    "suv": {
                        "nomi": "Suv",
                        "tavsif": "0.5L toza suv",
                        "narx": 3000,
                        "id": 7
                    },
                    "qahva": {
                        "nomi": "Qahva",
                        "tavsif": "Issiq qahva",
                        "narx": 12000,
                        "id": 8
                    }
                }
            },
            "qoshimcha": {
                "nomi": "🍟 Qo'shimcha taomlar",
                "rasm": "img/sides.png",
                "mahsulotlar": {
                    "fri": {
                        "nomi": "Kartoshka fri",
                        "tavsif": "Xirrangan kartoshka",
                        "narx": 15000,
                        "id": 9
                    },
                    "piyoz_halqa": {
                        "nomi": "Piyoz halqalari",
                        "tavsif": "Qovurilgan piyoz halqalari",
                        "narx": 18000,
                        "id": 10
                    },
                    "nagetlar": {
                        "nomi": "Nagetlar",
                        "tavsif": "Tovuq nagetlari (6 dona)",
                        "narx": 22000,
                        "id": 11
                    },
                    "qanotlar": {
                        "nomi": "Tovuq qanoti",
                        "tavsif": "Achchiq tovuq qanoti (4 dona)",
                        "narx": 25000,
                        "id": 12
                    }
                }
            },
            "shirinliklar": {
                "nomi": "🍰 Shirinliklar",
                "rasm": "img/desserts.png",
                "mahsulotlar": {
                    "muzqaymoq": {
                        "nomi": "Muzqaymoq",
                        "tavsif": "Vanilli muzqaymoq",
                        "narx": 10000,
                        "id": 13
                    },
                    "tort": {
                        "nomi": "Tort",
                        "tavsif": "Shokoladli tort bo'lagi",
                        "narx": 15000,
                        "id": 14
                    },
                    "donut": {
                        "nomi": "Donut",
                        "tavsif": "Glazurli donut",
                        "narx": 8000,
                        "id": 15
                    },
                    "molkosheyk": {
                        "nomi": "Molkosheyk",
                        "tavsif": "Vanilli molkosheyk",
                        "narx": 18000,
                        "id": 16
                    }
                }
            }
        },
        "buyurtmalar": [],
        "savatlar": {},
        "keyingi_buyurtma_id": 1
    }

def MY(fayl: str) -> Dict[str, Any]:
    if 'users' in fayl.lower():
        boshlangich = {"foydalanuvchilar": [], "adminlar": []}
    else:
        boshlangich = Malumot()

    try:
        if not os.path.exists(fayl):
            with open(fayl, 'w', encoding='utf-8') as f:
                json.dump(boshlangich, f, ensure_ascii=False, indent=2)
            logger.info(f"Yangi fayl yaratildi: {fayl}")
            return boshlangich

        with open(fayl, 'r', encoding='utf-8') as f:
            malumot = json.load(f)

        if not malumot:
            malumot = boshlangich


        if 'users' in fayl.lower():
            if 'foydalanuvchilar' not in malumot:
                logger.warning(f"{fayl} faylida 'foydalanuvchilar' kaliti yo'q, qo'shilmoqda")
                malumot['foydalanuvchilar'] = []
            if 'adminlar' not in malumot:
                logger.warning(f"{fayl} faylida 'adminlar' kaliti yo'q, qo'shilmoqda")
                malumot['adminlar'] = []

        if 'data' in fayl.lower():
            standart = Malumot()
            for kalit in ['kategoriyalar', 'matnlar', 'menyu', 'buyurtmalar', 'savatlar', 'keyingi_buyurtma_id']:
                if kalit not in malumot:
                    logger.warning(f"{fayl} faylida '{kalit}' kaliti yo'q, qo'shilmoqda")
                    if kalit == 'buyurtmalar':
                        malumot[kalit] = []
                    elif kalit == 'keyingi_buyurtma_id':
                        malumot[kalit] = 1
                    else:
                        malumot[kalit] = standart.get(kalit, {})

        return malumot

    except json.JSONDecodeError as e:
        logger.error(f"JSON xatosi {fayl} faylini o'qishda: {e}")
        return boshlangich
    except Exception as e:
        logger.error(f"Ma'lumotlar bazasini yuklashda xatolik: {e}")
        return boshlangich


def MS(malumot: Dict[str, Any], fayl: str) -> bool:
    try:
        with open(fayl, 'w', encoding='utf-8') as f:
            json.dump(malumot, f, ensure_ascii=False, indent=2)
        logger.info(f"Ma'lumotlar saqlandi: {fayl}")
        return True
    except Exception as e:
        logger.error(f"Ma'lumotlar bazasini saqlashda xatolik: {e}")
        return False
