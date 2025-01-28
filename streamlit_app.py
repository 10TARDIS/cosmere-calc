import streamlit as st

st.set_page_config(
    page_title="Cosmere Completion Calculator",
    page_icon="🌌"
    )

books = {
    "The Eleventh Metal": 6713,
    "The Final Empire": 215981,
    "The Well of Ascension": 250034,
    "The Hero of Ages": 242659,
    "Secret History": 44981,

    "Alloy of Law": 96979,
    "Allomancer Jak and the Pits of Eltania": 7047,
    "Shadows of Self": 115209,
    "Bands of Mourning": 131325,
    "The Lost Metal": 165352,


    "The Way of Kings": 386022,
    "Words of Radiance": 402168,
    "Edgedancer": 40660,
    "Oathbringer": 456283,
    "Dawnshard": 56248,
    "Rhythm of War": 467876,
    "Wind and Truth": 487746,
    
    "Elantris": 202835,
    "The Hope of Elantris": 6030,
    "The Emperor's Soul": 31925,
    "Warbreaker": 245471,
    "White Sand": 208838,
    "Shadows for Silence in the Forests of Hell": 17647,
    "Sixth of the Dusk": 17794,
    "Tress of the Emerald Sea": 111658,
    "Yumi and the Nightmare Painter": 118787,
    "The Sunlit Man": 107408,
    }

cosmere_word_count = sum(books.values())


def main():
    books_read = []
    
    st.title("Cosmere Completion Percent Calculator")
    st.write("Mark which books you have read to calculate what percent of the Cosmere you have read.")
    st.divider()

    st.write("Mistborn Era 1:")
    eleventh_metal = st.checkbox("The Eleventh Metal")
    final_empire = st.checkbox("The Final Empire")
    well_of_ascension = st.checkbox("The Well of Ascension")
    hero_of_ages = st.checkbox("The Hero of Ages")
    secret_history = st.checkbox("Secret History")
    
    st.write("Mistborn Era 2:")
    alloy_of_law = st.checkbox("Alloy of Law")
    allowmancer_jak = st.checkbox("Allomancer Jak and the Pits of Eltania")
    shadows_of_self = st.checkbox("Shadows of Self")
    bands_of_mourning = st.checkbox("Bands of Mourning")
    lost_metal = st.checkbox("The Lost Metal")

    st.write("The Stormlight Archive:")
    way_of_kings = st.checkbox("The Way of Kings")
    words_of_radiance = st.checkbox("Words of Radiance")
    edgedancer = st.checkbox("Edgedancer")
    oathbringer = st.checkbox("Oathbringer")
    dawnshard = st.checkbox("Dawnshard")
    rhythm_of_war = st.checkbox("Rhythm of War")
    wind_and_truth = st.checkbox("Wind and Truth")
    
    st.write("Stand-Alone Novels:")
    elantris = st.checkbox("Elantris")
    hope_of_elantris = st.checkbox("The Hope of Elantris")
    emperors_soul = st.checkbox ("The Emperor's Soul")
    warbreaker = st.checkbox("Warbreaker")
    white_sand = st.checkbox("White Sand (all three volumes)")
    shadows_for_silence = st.checkbox("Shadows for Silence in the Forests of Hell")
    sixth_of_the_dust = st.checkbox("Sixth of the Dusk")
    tress = st.checkbox("Tress of the Emerald Sea")
    yumi = st.checkbox("Yumi and the Nightmare Painter")
    sunlit_man = st.checkbox("The Sunlit Man")


    if eleventh_metal:
        books_read.append(books.get("The Eleventh Metal"))  
    if final_empire:
        books_read.append(books.get("The Final Empire"))
    if well_of_ascension:
        books_read.append(books.get("The Well of Ascension"))
    if hero_of_ages:
        books_read.append(books.get("The Hero of Ages"))
    if secret_history:
        books_read.append(books.get("Secret History"))

    if alloy_of_law:
        books_read.append(books.get("Alloy of Law"))
    if allowmancer_jak:
        books_read.append(books.get("Allomancer Jak and the Pits of Eltania"))
    if shadows_of_self:
        books_read.append(books.get("Shadows of Self"))
    if bands_of_mourning:
        books_read.append(books.get("Bands of Mourning"))
    if lost_metal:
        books_read.append(books.get("The Lost Metal"))

    if way_of_kings:
        books_read.append(books.get("The Way of Kings"))
    if words_of_radiance:
        books_read.append(books.get("Words of Radiance"))
    if edgedancer:
        books_read.append(books.get("Edgedancer"))
    if oathbringer:
        books_read.append(books.get("Oathbringer"))
    if dawnshard:
        books_read.append(books.get("Dawnshard"))
    if rhythm_of_war:
        books_read.append(books.get("Rhythm of War"))
    if wind_and_truth:
        books_read.append(books.get("Wind and Truth"))

    if elantris:
        books_read.append(books.get("Elantris"))
    if hope_of_elantris:
        books_read.append(books.get("The Hope of Elantris"))
    if emperors_soul:
        books_read.append(books.get("The Emperor's Soul"))
    if warbreaker:
        books_read.append(books.get("Warbreaker"))
    if white_sand:
        books_read.append(books.get("White Sand"))
    if shadows_for_silence:
        books_read.append(books.get("Shadows for Silence in the Forests of Hell"))
    if sixth_of_the_dust:
        books_read.append(books.get("Sixth of the Dusk"))
    if tress:
        books_read.append(books.get("Tress of the Emerald Sea"))
    if yumi:
        books_read.append(books.get("Yumi and the Nightmare Painter"))
    if sunlit_man:
        books_read.append(books.get("The Sunlit Man"))

    st.divider()
    
    read_word_count = sum(books_read)
    read_percent = round(((read_word_count / cosmere_word_count) * 100), 2)
    if st.button("Calculate Percentage"):
        st.write(f"You have read about {read_percent}% of the Cosmere")


main()
