# WORLD FAMOUS CUISINES Streamlit Dasturi

## Tavsif

Ushbu Streamlit dasturi dunyo bo'ylab taomlar haqidagi ma'lumotlarni interaktiv tarzda o'rganish va vizualizatsiya qilish imkonini beradi. Foydalanuvchilar turli taomlar, masalan, Amerika, Frantsiya, Italiya, Hindiston, Yaponiya va Meksika taomlari bo'yicha ma'lumotlarni ko'rishlari va tahlil qilishlari mumkin. Dastur ma'lumotlarni vizualizatsiya qilish va har bir taomning batafsil tavsiflarini taqdim etadi, shuningdek, ma'lumotlarni qayta ishlash va tozalash funksiyalarini ham o'z ichiga oladi.

## Xususiyatlar

- **Ma'lumotlarni Vizualizatsiya qilish**:
  - Turli grafiklar: boxplot, scatterplot, barplot, lineplot va pie chart.
  - Ma'lumotlar tozalanganidan keyingi va oldingi vizualizatsiyalarni ko'rish uchun interaktiv tablar.

- **Ma'lumotlarni Qayta ishlash**:
  - Yo'qolgan qiymatlarni median yoki mod bilan to'ldirish.
  - Anomaliyalarni aniqlash va ularni winsorization orqali boshqarish.

- **Taomlar Haqida Ma'lumotlar**:
  - Turli dunyo taomlarining batafsil tavsiflari va rasmlari.
  - Tanlangan taom bo'yicha statistikalar va tahlillar.

- **Sidebar Filtrlari**:
  - Taom, joylashuv, o'rtacha ovqat narxi va reyting bo'yicha filtrlash.
  - Filtrlangan ma'lumotlarni va tegishli vizualizatsiyalarni ko'rsatish uchun interaktiv vidjetlar.

## O'rnatish

1. Repositoriyani klonlash:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Loyihaga o'tish:
    ```bash
    cd your-repository
    ```

3. Kerakli paketlarni o'rnatish:
    ```bash
    pip install -r requirements.txt
    ```

## Ishlatish

1. Streamlit dasturini ishga tushirish:
    ```bash
    streamlit run app.py
    ```

2. Dastur o'z veb brauzeringizda ochiladi (odatda `http://localhost:8501` manzilida).

## Ma'lumot

Dastur `exam.csv` nomli CSV faylidan foydalanadi, u turli taomlar haqidagi ma'lumotlarni o'z ichiga oladi. Fayl `app.py` bilan bir xil papkada joylashgan bo'lishi kerak yoki fayl yo'lini tegishli tarzda yangilashingiz mumkin.

## Fayl Tuzilishi

- `app.py`: Asosiy Streamlit dasturi skripti.
- `style.css`: Dastur uchun maxsus CSS fayli.
- `exam.csv`: Taomlar haqidagi ma'lumotlarni o'z ichiga olgan CSV fayl.
- `requirements.txt`: Dastur uchun kerakli Python paketlari ro'yxati.

## Talablar

- Python 3.x
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Litsenziya

Ushbu loyiha MIT Litsenziyasi ostida litsenziyalanadi - batafsil ma'lumot uchun [LICENSE](LICENSE) faylini ko'rib chiqing.

## Tashakkurlar

- Dasturda foydalanilgan rasmlar turli veb-saytlardan olingan bo'lib, ta'lim va illyustrativ maqsadlarda foydalaniladi.

Har qanday muammolar yoki hissalar uchun GitHub repository'sida issue oching yoki pull request yuboring.

