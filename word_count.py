"""Taller evaluable"""

import glob

import pandas as pd

"""Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
def load_input(input_directory):
    filenames = glob.glob(f"{input_directory}/*.txt")


    dataframes = [pd.read_csv(filename, sep="\t", header=None, names=["text"]) for filename in filenames]
    concatened_df = pd.concat(dataframes, ignore_index=True)

    return concatened_df


"""Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
def clean_text(dataframe):
    dataframe["text"] = dataframe["text"].apply(lambda x: x.replace(",", "").replace(".", "").lower(), )
    return dataframe


"""Word count"""
def count_words(dataframe):
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].apply(lambda x: x.split())
    dataframe = dataframe.explode("text")

    return dataframe["text"].value_counts().reset_index()
    



def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep="\t", index=True, header=False)


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words(df)
    save_output(df, output_filename)
    print(df)

if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )