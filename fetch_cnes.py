!pip install pysus
!pip install datasus-fetcher

#DOWNLOAD ESTABELECIMENTOS CNES USANDO PYSUS:
from pysus import CNES

cnes = CNES()

# Get files for 'ST' group, year 2023, and state SP
cnes_files_filtered = cnes.get_files(group='ST', year=2023, uf='SP')

if cnes_files_filtered:
    print(f"Found {len(cnes_files_filtered)} CNES files for group 'ST', year 2023, and state SP:")
    for file in cnes_files_filtered:
        print(file)

    # Download these files
    downloaded_cnes_files = cnes.download(cnes_files_filtered)
    print("\nDownloaded CNES files:")
    for file in downloaded_cnes_files:
        print(file)
else:
    print(f"No CNES files found for group 'ST', year 2023, and state SP.")



#DOWNLOAD ESTABELECIMENTOS USANDO datasus-fectcher
!datasus-fetcher list-datasets cnes-st
!datasus-fetcher data cnes-st --data-dir datasus_cnes

file_path = '<YOUR_FILE_PATH>'

try:
    # Read the .dbc file
    dbc = Dbc(file_path)
    df_cnes_st = dbc.read()

    # Display the first few rows of the DataFrame
    display(df_cnes_st.head())

except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred while reading the DBC file: {e}")


