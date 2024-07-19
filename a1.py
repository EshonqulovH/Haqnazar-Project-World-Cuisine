import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CSS faylini yuklash funksiyasi
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# CSS faylini yuklash
load_css("style.css")

# Sarlavha
st.title('WORLD FAMOUS CUISINES')
st.image("https://c7.alamy.com/comp/EYX55T/collage-of-lots-of-popular-worldwide-dinner-foods-and-appetizers-EYX55T.jpg")

# Ma'lumotlarni yuklash
df = pd.read_csv("exam.csv")  # CSV fayl yo'lini to'g'irlab kiritish kerak
df1 = df.copy()

st.subheader('Clear the DataFrame')
show_table = st.button("Show table Data Fream processing")

if show_table:
    tab13,tab14,tab15 = st.tabs(["With Nan values","There are no Nan values","Detecting outlires"])
    with  tab13:
        st.header("Boxplot")
        fig,ax = plt.subplots()
        sns.boxplot(data=df1,x="Cuisine",y="Weekend Reservations",ax=ax,hue="Cuisine")
        st.pyplot(fig)

        st.header("Scatterplot")
        fig,ax = plt.subplots()
        sns.scatterplot(data=df1,x="Seating Capacity",y="Revenue",ax=ax,hue="Seating Capacity")
        st.pyplot(fig)

        st.subheader('DataFrame')
        st.write(df1)

    # NaN qiymatlarini har bir objectli ustundagi mode bilan to'ldirish
    def fill_nan_with_mode(df1):
        numeric_columns = df1.select_dtypes(include=["object"]).columns
        for column in numeric_columns:
            median_value = df1[column].mode()[0]
            df1[column].fillna(median_value,inplace=True)
        return df1
    # NaN qiymatlarini median bilan to'ldirish
    df_filled1 = fill_nan_with_mode(df1)

    # NaN qiymatlarini har bir raqamli ustundagi median bilan to'ldirish
    def fill_nan_with_median(df1):
        numeric_columns = df1.select_dtypes(include=[np.number]).columns
        for column in numeric_columns:
            median_value = df1[column].median()
            df1[column].fillna(median_value,inplace=True)
        return df1
    # NaN qiymatlarini median bilan to'ldirish
    df_filled1 = fill_nan_with_median(df1)

    with tab14:
        st.header("Boxplot")
        fig,ax = plt.subplots()
        sns.boxplot(data=df1,x="Cuisine",y="Weekend Reservations",ax=ax,hue="Cuisine")
        st.pyplot(fig)

        st.header("Scatterplot")
        fig,ax = plt.subplots()
        sns.scatterplot(data=df1,x="Seating Capacity",y="Revenue",ax=ax,hue="Seating Capacity")
        st.pyplot(fig)

        st.subheader('DataFrame')
        st.write(df1)

    # Outlierlarga ishlov berish (winsorization)
    def handle_outliers(df1):
        numeric_columns = df1.select_dtypes(include=[np.number]).columns
        for column in numeric_columns:
            Q1 = df1[column].quantile(0.5)
            Q3 = df1[column].quantile(0.95)
            IQR = Q3 - Q1
            lower_bound = Q1 - 0.25 * IQR
            upper_bound = Q3 + 0.25 * IQR
            df1[column] = np.where(df1[column] < lower_bound, lower_bound, df1[column])
            df1[column] = np.where(df1[column] > upper_bound, upper_bound, df1[column])
        return df1
    df1 = handle_outliers(df1)
    with tab15:
        st.header("Boxplot")
        fig,ax = plt.subplots()
        sns.boxplot(data=df1,x="Cuisine",y="Weekend Reservations",ax=ax,hue="Cuisine")
        st.pyplot(fig)

        st.header("Scatterplot")
        fig,ax = plt.subplots()
        sns.scatterplot(data=df1,x="Seating Capacity",y="Revenue",ax=ax,hue="Seating Capacity")
        st.pyplot(fig)

        st.subheader('DataFrame')
        st.write(df1)


# NaN qiymatlarini har bir objectli ustundagi mode bilan to'ldirish
def fill_nan_with_mode(df):
    numeric_columns = df.select_dtypes(include=["object"]).columns
    for column in numeric_columns:
        median_value = df[column].mode()[0]
        df[column].fillna(median_value,inplace=True)
    return df
# NaN qiymatlarini median bilan to'ldirish
df_filled = fill_nan_with_mode(df)

# NaN qiymatlarini har bir raqamli ustundagi median bilan to'ldirish
def fill_nan_with_median(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        median_value = df[column].median()
        df[column].fillna(median_value,inplace=True)
    return df
# NaN qiymatlarini median bilan to'ldirish
df_filled = fill_nan_with_median(df)

# Unnamedni tashlash
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

st.subheader('Location Cuisine')
#buttonlar qo'shish mamlakat bo'yicha
check = st.button("American")
check1 = st.button("French")
check2 = st.button("Italian")
check3= st.button("Indian")
check4 = st.button("Japanese")
check5 = st.button("Mexican")

if check:
    tab1, tab2 = st.tabs(["American Cuisine","Kitchen Information"])
    with tab1:
        st.header("American Cuisine")
        st.image("https://www.roadunraveled.com/wp-content/uploads/2017/04/food-map-t.png")
        st.markdown("""
            American cuisine encompasses a wide range of culinary traditions found within the United States.
            It reflects the diverse cultural influences brought by immigrants from around the world.
            Some iconic dishes include:

            - **Hamburger**: A grilled beef patty served in a bun, often with various toppings like lettuce, tomato, cheese, and condiments.

            - **Hotdog**: A sausage served in a sliced bun, typically garnished with mustard, ketchup, onions, relish, or sauerkraut.

            - **Macaroni and Cheese**: Macaroni pasta mixed with a cheese sauce, often baked until golden and crispy on top.

            - **Barbecue**: Slow-cooked meats, such as ribs, brisket, or pulled pork, often smoked and served with a variety of sauces.

            - **Pizza**: While originating from Italy, pizza has been adapted in the U.S. with various toppings like pepperoni, sausage, mushrooms, and peppers.

            - **Apple Pie**: A dessert consisting of a pastry crust filled with sliced apples, sugar, and spices, often served with ice cream or whipped cream.

            These are just a few examples, and American cuisine continues to evolve with regional specialties and international influences.
            """)
    with tab2:
        # Barplot
        st.subheader("Social Media Followers by Rating")
        fig, ax = plt.subplots()
        sns.barplot(data=df[df["Cuisine"] == "American"], x="Rating", y="Social Media Followers", ax=ax, palette="viridis")
        st.pyplot(fig)

        # Lineplot
        st.subheader("Revenue by Chef Experience Years")
        fig, ax = plt.subplots()
        sns.lineplot(data=df[df["Cuisine"] == "American"], x="Chef Experience Years", y="Revenue", ax=ax)
        st.pyplot(fig)

        # Histplot
        st.subheader('Count by Location')
        fig, ax = plt.subplots()
        sns.histplot(data=df[df["Cuisine"] == "American"], x="Location", hue="Location", ax=ax)
        st.pyplot(fig)

        # "Cuisine" ustuni "Mexican" bo'lgan ma'lumotlarni filtrlash
        mexican_data = df[df["Cuisine"] == "American"]

        # 'Location' bo'yicha o'rtacha bahoni hisoblash
        avg_rating_location = mexican_data.groupby('Location')['Service Quality Score'].mean().reset_index()

        # Pie chart yasash
        st.subheader('Service Qualtiy Score by Location for American Cuisine')
        fig, ax = plt.subplots()
        ax.pie(avg_rating_location['Service Quality Score'], labels=avg_rating_location['Location'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Doira shaklida ko'rsatish uchun

        st.pyplot(fig)

if check1:
    tab3, tab4 = st.tabs(["French Cuisine","Kitchen Information"])
    with tab3:
        st.header("French Cuisine")
        st.image("https://media.istockphoto.com/id/584597902/vector/french-cuisine-icons.jpg?s=612x612&w=0&k=20&c=-mAbhivcSqKAoTyHFZ27fH5XmlSgS-f9EUrl9Hf10IE=")
        st.markdown("""
            French cuisine is celebrated for its sophistication, diversity, and attention to culinary artistry. It is characterized by:

            - **Haute Cuisine**: High-quality dishes often prepared with elaborate techniques and presentation.

            - **Regional Diversity**: Each region of France has its own specialties, such as coq au vin from Burgundy, bouillabaisse from Provence, and cassoulet from Languedoc.

            - **Pastries and Breads**: France is famous for its pastries like croissants, eclairs, and macarons, as well as artisanal breads such as baguettes.

            - **Cheese**: France produces a wide variety of cheeses, each with its own unique flavors and textures.

            - **Wine**: French wine regions, like Bordeaux, Burgundy, and Champagne, are renowned for producing some of the world's finest wines.

            - **Influence on Global Cuisine**: French culinary techniques and dishes have had a profound influence on global cuisine.

            French cuisine emphasizes fresh, high-quality ingredients and meticulous preparation, making dining a cultural experience. It continues to evolve while maintaining its traditions and culinary excellence.
            """)
    with tab4:
        st.subheader("Social Media Followers by Rating")
        fig, ax = plt.subplots()
        sns.barplot(data=df[df["Cuisine"] == "French"], x="Rating", y="Social Media Followers", ax=ax, palette="viridis")
        st.pyplot(fig)

        st.subheader("Revenue by Chef Experience Years")
        fig, ax = plt.subplots()
        sns.lineplot(data=df[df["Cuisine"] == "French"], x="Chef Experience Years", y="Revenue", ax=ax)
        st.pyplot(fig)

        st.subheader('Count by Location')
        fig, ax = plt.subplots()
        sns.histplot(data=df[df["Cuisine"] == "French"], x="Location", ax=ax,hue="Location")
        st.pyplot(fig)

        # "Cuisine" ustuni "Mexican" bo'lgan ma'lumotlarni filtrlash
        mexican_data = df[df["Cuisine"] == "French"]

        # 'Location' bo'yicha o'rtacha bahoni hisoblash
        avg_rating_location = mexican_data.groupby('Location')['Service Quality Score'].mean().reset_index()

        # Pie chart yasash
        st.subheader('Service Qualtiy Score by Location for French Cuisine')
        fig, ax = plt.subplots()
        ax.pie(avg_rating_location['Service Quality Score'], labels=avg_rating_location['Location'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Doira shaklida ko'rsatish uchun

        st.pyplot(fig)

if check2:
    tab5, tab6 = st.tabs(["Italian Cuisine","Kitchen Information"])
    with tab5:
        st.header("Italian Cuisine")
        st.image("https://graphicriver.img.customer.envatousercontent.com/files/177236617/15_italian_food_chalk.jpg?auto=compress%2Cformat&q=80&fit=crop&crop=top&max-h=8000&max-w=590&s=bbeef2fe751beec3313b948ee2b904bd")
        st.markdown("""
            Italian cuisine is celebrated for its emphasis on fresh, high-quality ingredients and simple preparations that showcase their natural flavors. Key aspects include:

            - **Pasta**: A cornerstone of Italian cuisine, with varieties like spaghetti, penne, and ravioli, often paired with diverse sauces such as marinara, carbonara, and pesto.

            - **Pizza**: Originating from Naples, Italy, pizza features a thin crust topped with ingredients like mozzarella, tomatoes, basil, and olive oil.

            - **Antipasti**: Appetizers that include cured meats like prosciutto, cheeses like mozzarella and parmigiano-reggiano, and bruschetta topped with tomatoes and basil.

            - **Seafood**: Coastal regions feature dishes like risotto alla pescatora and seafood pasta with clams or mussels.

            - **Desserts**: Tiramisu, cannoli, and gelato are iconic Italian desserts enjoyed worldwide.

            - **Regional Specialties**: Each region boasts unique dishes; for example, risotto in the north, pasta in central Italy, and seafood along the coast.

            Italian cuisine places importance on tradition, family, and the enjoyment of food, making it a staple of global culinary culture.
            """)
    with tab6:
        st.subheader("Social Media Followers by Rating")
        fig, ax = plt.subplots()
        sns.barplot(data=df[df["Cuisine"] == "Italian"], x="Rating", y="Social Media Followers", ax=ax, palette="viridis")
        st.pyplot(fig)

        st.subheader("Revenue by Chef Experience Years")
        fig, ax = plt.subplots()
        sns.lineplot(data=df[df["Cuisine"] == "Italian"], x="Chef Experience Years", y="Revenue", ax=ax)
        st.pyplot(fig)

        st.subheader('Count by Location')
        fig, ax = plt.subplots()
        sns.histplot(data=df[df["Cuisine"] == "Italian"], x="Location",hue="Location",ax=ax)
        st.pyplot(fig)

        # "Cuisine" ustuni "Mexican" bo'lgan ma'lumotlarni filtrlash
        mexican_data = df[df["Cuisine"] == "Italian"]

        # 'Location' bo'yicha o'rtacha bahoni hisoblash
        avg_rating_location = mexican_data.groupby('Location')['Service Quality Score'].mean().reset_index()

        # Pie chart yasash
        st.subheader('Service Qualtiy Score by Location for Italian Cuisine')
        fig, ax = plt.subplots()
        ax.pie(avg_rating_location['Service Quality Score'], labels=avg_rating_location['Location'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Doira shaklida ko'rsatish uchun

        st.pyplot(fig)

if check3:
    tab7, tab8 = st.tabs(["Indian Cuisine","Kitchen Information"])
    with tab7:
        st.header("Indian Cuisine")
        st.image("https://sundayguardianlive.com/wp-content/uploads/2022/12/Indian-Cuisine-Fifth-Best-In-The-World.jpg")
        st.markdown("""
            Indian cuisine is characterized by its use of aromatic spices, herbs, and diverse cooking techniques. Key features include:

            - **Curries**: A variety of dishes with rich, flavorful sauces made from combinations of spices like turmeric, cumin, coriander, and garam masala. Popular curries include chicken tikka masala, butter chicken, and paneer tikka.

            - **Rice and Breads**: Basmati rice is often served with curries, while breads like naan, roti, and paratha accompany meals. These are baked in tandoor ovens, imparting a unique smoky flavor.

            - **Vegetarian Cuisine**: India offers a wide array of vegetarian dishes, such as dal (lentil curry), aloo gobi (potato and cauliflower), and palak paneer (spinach with cottage cheese).

            - **Street Food**: Chaat (savory snacks like samosas and pani puri), dosa (thin rice crepes filled with spicy fillings), and kebabs are popular street foods enjoyed across the country.

            - **Sweets and Desserts**: Indian sweets (mithai) like gulab jamun, rasgulla, and jalebi are famous for their sweetness and richness.

            - **Regional Diversity**: Each region of India has its own specialties; for example, biryani in Hyderabad, seafood in Kerala, and thali meals in Gujarat.

            Indian cuisine reflects the country's cultural diversity and history, offering a culinary journey through its various flavors and traditions.
            """)
    with tab8:
        st.subheader("Social Media Followers by Rating")
        fig, ax = plt.subplots()
        sns.barplot(data=df[df["Cuisine"] == "Indian"], x="Rating", y="Social Media Followers", ax=ax, palette="viridis")
        st.pyplot(fig)

        st.subheader("Revenue by Chef Experience Years")
        fig, ax = plt.subplots()
        sns.lineplot(data=df[df["Cuisine"] == "Indian"], x="Chef Experience Years", y="Revenue", ax=ax)
        st.pyplot(fig)

        st.subheader('Count by Location')
        fig, ax = plt.subplots()
        sns.histplot(data=df[df["Cuisine"] == "Indian"], x="Location",hue="Location",ax=ax)
        st.pyplot(fig)

        # "Cuisine" ustuni "Mexican" bo'lgan ma'lumotlarni filtrlash
        mexican_data = df[df["Cuisine"] == "Indian"]

        # 'Location' bo'yicha o'rtacha bahoni hisoblash
        avg_rating_location = mexican_data.groupby('Location')['Service Quality Score'].mean().reset_index()

        # Pie chart yasash
        st.subheader('Service Qualtiy Score by Location for Indian Cuisine')
        fig, ax = plt.subplots()
        ax.pie(avg_rating_location['Service Quality Score'], labels=avg_rating_location['Location'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Doira shaklida ko'rsatish uchun

        st.pyplot(fig)

if check4:
    tab9, tab10 = st.tabs(["Japanese Cuisine","Kitchen Information"])
    with tab9:
        st.header("Japanese Cuisine")
        st.image("https://www.tastingtable.com/img/gallery/20-japanese-dishes-you-need-to-try-at-least-once/l-intro-1664219638.jpg")
        st.markdown("""
            Japanese cuisine, known as washoku (å’Œé£Ÿ), is renowned for its delicate flavors, seasonal ingredients, and aesthetic presentation. Key aspects include:

            - **Sushi and Sashimi**: Raw fish served with vinegared rice (sushi) and thinly sliced raw fish (sashimi), often accompanied by soy sauce, wasabi, and pickled ginger.

            - **Tempura**: Lightly battered and deep-fried seafood and vegetables, served with tentsuyu dipping sauce.

            - **Ramen**: Noodle soup with various toppings like sliced pork, bamboo shoots, seaweed, and a seasoned broth (shoyu, shio, miso, or tonkotsu).

            - **Teppanyaki**: Grilled dishes cooked on an iron griddle, often featuring beef, seafood, and vegetables.

            - **Wagyu Beef**: High-quality Japanese beef known for its marbling and tenderness, often served as steak or in hotpot (sukiyaki).

            - **Traditional Dishes**: Such as teriyaki (grilled meat or fish with a sweet soy glaze), donburi (rice bowls topped with meat, vegetables, or seafood), and udon (thick wheat noodles in broth).

            - **Seasonal Cuisine**: Kaiseki is a multi-course meal highlighting seasonal ingredients and artistic presentation, embodying Japanese culinary artistry.

            Japanese cuisine places great importance on harmony, balance, and respecting the natural flavors of ingredients, making it a cherished part of Japanese culture and admired worldwide.
            """)
    with tab10:
        st.subheader("Social Media Followers by Rating")
        fig, ax = plt.subplots()
        sns.barplot(data=df[df["Cuisine"] == "Japanese"], x="Rating", y="Social Media Followers", ax=ax, palette="viridis")
        st.pyplot(fig)

        st.subheader("Revenue by Chef Experience Years")
        fig, ax = plt.subplots()
        sns.lineplot(data=df[df["Cuisine"] == "Japanese"], x="Chef Experience Years", y="Revenue", ax=ax)
        st.pyplot(fig)

        st.subheader('Count by Location')
        fig, ax = plt.subplots()
        sns.histplot(data=df[df["Cuisine"] == "Japanese"], x="Location", hue="Location",ax=ax)
        st.pyplot(fig)

        # "Cuisine" ustuni "Mexican" bo'lgan ma'lumotlarni filtrlash
        mexican_data = df[df["Cuisine"] == "Japanese"]

        # 'Location' bo'yicha o'rtacha bahoni hisoblash
        avg_rating_location = mexican_data.groupby('Location')['Service Quality Score'].mean().reset_index()

        # Pie chart yasash
        st.subheader('Service Qualtiy Score by Location for Japanese Cuisine')
        fig, ax = plt.subplots()
        ax.pie(avg_rating_location['Service Quality Score'], labels=avg_rating_location['Location'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Doira shaklida ko'rsatish uchun

        st.pyplot(fig)

if check5:
    tab11, tab12 = st.tabs(["Mexican Cuisine","Kitchen Information"])
    with tab11:
        st.header("Mexican Cuisine")
        st.image("https://i.pinimg.com/originals/b6/c8/3a/b6c83a45b33c60f2ea2f1731c79cfc8c.jpg")
        st.markdown("""
            Mexican cuisine is characterized by its bold flavors, rich spices, and diverse regional dishes. Key elements include:

            - **Tacos**: Corn or flour tortillas filled with a variety of ingredients such as grilled meat (like carne asada), fish (like Baja-style fish), or vegetables, topped with salsa, guacamole, and cilantro.

            - **Enchiladas**: Corn tortillas rolled around fillings such as chicken, cheese, or beans, covered with chili sauce and baked.

            - **Tamales**: Steamed pockets of masa (corn dough) filled with meats, cheese, or vegetables, often wrapped in corn husks.

            - **Guacamole**: A dip made from mashed avocados mixed with lime juice, tomatoes, onions, and cilantro.

            - **Mole**: A rich sauce made with chili peppers, chocolate, and spices, served over chicken or enchiladas.

            - **Chiles Rellenos**: Poblano peppers stuffed with cheese, meat, or beans, battered and fried.

            - **Street Food**: Tostadas (fried tortillas topped with beans, meat, and salsa), quesadillas (cheese-filled tortillas grilled or fried), and elotes (grilled corn with mayonnaise, cheese, and chili powder).

            - **Beverages**: Including horchata (sweet rice milk), agua frescas (fruit-based drinks), and tequila-based cocktails like margaritas.

            Mexican cuisine varies widely by region, showcasing indigenous ingredients and influences from Spanish and Mesoamerican cultures. It is a vibrant expression of Mexico's cultural heritage and culinary creativity.
            """)
    with tab12:
        st.subheader("Social Media Followers by Rating")
        fig, ax = plt.subplots()
        sns.barplot(data=df[df["Cuisine"] == "Mexican"], x="Rating", y="Social Media Followers", ax=ax, palette="viridis")
        st.pyplot(fig)

        st.subheader("Revenue by Chef Experience Years")
        fig, ax = plt.subplots()
        sns.lineplot(data=df[df["Cuisine"] == "Mexican"], x="Chef Experience Years", y="Revenue", ax=ax)
        st.pyplot(fig)

        st.subheader('Count by Location')
        fig, ax = plt.subplots()
        sns.histplot(data=df[df["Cuisine"] == "Mexican"], x="Location",hue="Location",ax=ax)
        st.pyplot(fig)


        # "Cuisine" ustuni "Mexican" bo'lgan ma'lumotlarni filtrlash
        mexican_data = df[df["Cuisine"] == "Mexican"]
        # 'Location' bo'yicha o'rtacha bahoni hisoblash
        avg_rating_location = mexican_data.groupby('Location')['Service Quality Score'].mean().reset_index()
        # Pie chart yasash
        st.subheader('Average Rating by Location for Mexican Cuisine')
        fig, ax = plt.subplots()
        ax.pie(avg_rating_location['Service Quality Score'], labels=avg_rating_location['Location'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Doira shaklida ko'rsatish uchun

        st.pyplot(fig)

# Tanlovlar paneli
st.sidebar.header('Select Cuisine')

# Cuisine uchun selectbox
cuisine = st.sidebar.selectbox('Cuisine', df['Cuisine'].unique())

# Location uchun selectbox
location = st.sidebar.selectbox('Location', df['Location'].unique())

# Average Meal Price uchun slider
min_price, max_price = st.sidebar.slider('Average Meal Price', float(df['Average Meal Price'].min()), float(df['Average Meal Price'].max()), (float(df['Average Meal Price'].min()), float(df['Average Meal Price'].max())))

# Radio tugmasi qo'shish
rating_radio = st.sidebar.radio('Rating Filter', ['All', 'Above 4.0', 'Above 4.5', 'Above 5.0'])

# "Show Table" tugmasi
show_table = st.sidebar.button('Show Table')

# Filtrlash va natijalarni ko'rsatish
if show_table:
    filtered_df = df.copy()

    if cuisine:
        filtered_df = filtered_df[filtered_df['Cuisine'] == cuisine]
    if location:
        filtered_df = filtered_df[filtered_df['Location'] == location]
    filtered_df = filtered_df[(filtered_df['Average Meal Price'] >= min_price) & (filtered_df['Average Meal Price'] <= max_price)]

    # Baholarni filtralash
    if rating_radio == 'Above 4.0':
        filtered_df = filtered_df[filtered_df['Rating'] > 4.0]
    elif rating_radio == 'Above 4.5':
        filtered_df = filtered_df[filtered_df['Rating'] > 4.5]
    elif rating_radio == 'Above 5.0':
        filtered_df = filtered_df[filtered_df['Rating'] == 5.0]

    # Ma'lumotlarni ko'rsatish
    st.subheader('Filtered Data')
    st.write(filtered_df)


    # 'Sig'im bo'yicha' bo'yicha o'rtacha bahoni hisoblash
    avg_rating_location = filtered_df.groupby('Parking Availability')['Seating Capacity'].mean().reset_index()

    # Pie chart yasash
    st.subheader('Parking lots Based by Average Capacity')
    fig, ax = plt.subplots()
    ax.pie(avg_rating_location['Seating Capacity'], labels=avg_rating_location['Parking Availability'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Doira shaklida ko'rsatish uchun

    st.pyplot(fig)


    st.subheader('Service Quality Score by Ambience Score')
    avg_price_cuisine = filtered_df.groupby('Ambience Score')['Service Quality Score'].mean().reset_index()
    fig, ax = plt.subplots()
    sns.regplot(y='Ambience Score', x='Service Quality Score', data=avg_price_cuisine, ax=ax)
    st.pyplot(fig)

    # Correlation
    correlation_matrix = filtered_df[['Weekend Reservations', 'Weekday Reservations']].corr()

    # Heatmap yasash
    st.subheader('Correlation between Weekend and Weekday Reservations')
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Echart
    st.subheader("Social Media Followers by Marketing Budget")
    l_chart=filtered_df.groupby("Marketing Budget")['Social Media Followers'].mean().reset_index()
    st.line_chart(data=l_chart,y='Marketing Budget',x="Social Media Followers")


    # Grafika - Baholarni taqsimlanishi
    st.subheader('Distribution of Ratings')
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['Rating'], bins=20, ax=ax)
    st.pyplot(fig)

    st.subheader("Service of Quality by Number of Reviuws")
    avg_price_cuisine = filtered_df.groupby('Number of Reviews')['Service Quality Score'].mean().reset_index()
    fig, ax = plt.subplots()
    avg_price_cuisine.plot(kind="line",ax=ax,color="r")
    ax.set_xlabel("Number of Rewiews")
    ax.set_ylabel("Service Quality Score")
    st.pyplot(fig)

else:
    st.sidebar.write("Iltimos, jadvalni ko'rish uchun 'Show Table' tugmasini bosing.")
