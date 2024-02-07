from smartcard.System import readers
import smartcard
import pandas as pd

hash_col_name = "HASH"
# Ouvrir le fichier Excel et sélectionner la feuille de calcul
filename = 'FICHIER CROSS.xlsm'
try:
    df = pd.read_excel(filename, sheet_name=0)
except FileNotFoundError:
    df = pd.DataFrame(columns=[hash_col_name])
    df.to_excel(filename, index=False)

# Trouver le lecteur de puce RFID
reader_list = readers()
if len(reader_list) == 0:
    print("Aucun lecteur de puce RFID trouvé.")
    exit()
else:
    reader = reader_list[0]

# Définir la commande APDU pour récupérer la valeur de la puce
apdu = [0xFF, 0xCA, 0x00, 0x00, 0x00]

# Boucle pour scanner les dossards


def getATR(reader):
    """Return the ATR of the card inserted into the reader."""
    connection = reader.createConnection()
    atr = ""
    try:
        connection.connect()
        atr = connection.getATR()
        
        response, sw1, sw2 = connection.transmit(apdu)

        # Afficher la valeur de la puce dans la console Python
        atr= "{}".format("".join(["{:02X}".format(x) for x in response]))
        connection.disconnect()
    except smartcard.Exceptions.NoCardException:
      atr = ""

    except smartcard.Exceptions.CardConnectionException:
      atr = "Echec de lecture"
    return atr

retour1 = None
i = 0
while True: 
  try:
    retour = getATR(reader)
    if retour != "" and retour != retour1:
      if retour != "Echec de lecture":
        print("[",i,"] - ", retour)
      retour1 = retour
      i += 1

  except KeyboardInterrupt:
    print("stop")
    break
