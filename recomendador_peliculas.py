import streamlit as st
import pandas as pd

def cargar_datos():
    try:
        df = pd.read_csv("peliculas.csv")
        return df
    except FileNotFoundError:
        st.error("El archivo 'peliculas.csv' no se encontró.")
        return None
    except pd.errors.EmptyDataError:
        st.error("El archivo 'peliculas.csv' está vacío.")
        return None
    except pd.errors.ParserError:
        st.error("Error al parsear el archivo 'peliculas.csv'. Asegúrate de que el formato es correcto.")
        return None

def main():
    st.title('Sistema de Recomendación de Películas')
    df = cargar_datos()

    if df is not None:
        st.header('Ingrese sus preferencias')
        if 'genre' in df.columns and 'crew' in df.columns:
            generos_unicos = df['genre'].unique()
            genero = st.selectbox('Seleccione un género', generos_unicos)
            actor = st.text_input('Ingrese su actor/actriz favorito')

            if st.button('Obtener Recomendaciones'):
                recomendaciones = df[(df['genre'] == genero) & (df['crew'].str.contains(actor, case=False))]

                st.header('Recomendaciones')
                if recomendaciones.empty:
                    st.write('Lo siento, no se encontraron recomendaciones para sus preferencias.')
                else:
                    for idx, row in recomendaciones.iterrows():
                        st.subheader(row['title'])
                        st.write(f"Año: {row['year']}")
                        st.write(f"Sinopsis: {row['synopsis']}")
                        st.write(f"Calificación crítica: {row['critic_score']}")
                        st.write(f"Calificación del público: {row['people_score']}")
                        st.write(f"Género: {row['genre']}")
                        st.write(f"Director: {row['director']}")
                        st.write(f"Productor: {row['producer']}")
                        st.write(f"Duración: {row['runtime']} minutos")
        else:
            st.error("El archivo CSV no contiene las columnas necesarias: 'genre' y 'crew'.")

if __name__ == '__main__':
    main()