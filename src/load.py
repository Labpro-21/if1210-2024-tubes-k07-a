# FUNGSI load : mengubah data di csv menjadi array
# Writer: Adrian Sami Pratama
# Tanggal: 30 April 2024

# fungsi panggil data csv menjadi array
def csv_to_array (filepath: str) -> list:
    lines = []
    with open(filepath, 'r') as file:
        for row in file:
            lines.append(row) # Mengubah csv menjadi array per baris 
    array = []
    for line in lines:
        row = []
        kata = ''
        for elmt in line:
            if elmt != ';' and elmt != '\n':
                kata += elmt
            elif elmt == ';':
                row.append(kata)
                kata = ''
        row.append(kata)
        array.append(row)
    return array
