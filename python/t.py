import pandas
from datetime import datetime, time, timedelta
from collections import defaultdict


def getRunners():
  return pandas.read_excel("fichier cross 2023.xlsm", sheet_name="inscription")


def renderDossardsHTML():
  dataInscription = getRunners()
  classes = dataInscription.set_index(dataInscription.CLASSE)

  html = "<html><head><link rel='stylesheet' href='style.css' ><style>@page { size: A4 }</style></head><body class='A4'>"
  for classe in classes.index.drop_duplicates():
    cl = classes.loc[classe]
    html = html + "<div class='sheet padding-10mm'><div class='logo'></div><div class='title'>Cross PrépaWallon<br/>Récap course<br/>Mardi 28 mars 2023</div><div class='class_name'>" + \
        str(classe) + "</div><div class='table'>"
    html = html + "<div class='row row_first'><div class='title_col col_1'>Nom</div><div class='title_col col_2'>Prénom</div><div class='title_col col_3'>Participation</div><div class='title_col col_4'>Dossards</div></div>"
    for _, s in cl.iterrows():
      html = html + "<div class='row'><div class='cell col_1'>" + str(s.NOM) + "</div><div class='cell col_2'>" + str(
          s.PRENOM) + "</div><div class='cell col_3'>" + str(s.PARTICIPATION) + "</div><div class='cell col_4'>" + str(int(s.DOSSARDS)) + "</div></div>"""
      #
    html = html + "</div><div class='footer'>Merci de bien respecter les dossards distribués.</br>Des épingles vous seront fournies au niveau du départ</div></div>"
  html = html + "</div></div></body></html>"
  file = open("recap_inscription.html", "w")
  file.write(html)
  file.close()
  print("[DOSSARDS] - done")


def convert_datetime_to_time(val):
    if isinstance(val, datetime):
        return val.time()
    else:
        return val


def getAllTime():
  hourTab = [time(16, 39, 00), time(16, 33, 59), time(16, 30, 00)]
  distTab = [3.33, 5.62, 8.72]

  dataTimeEnd = pandas.read_excel("fichier cross 2023.xlsm", sheet_name="arrivée")
  print("[STEP 1] - Acquisition données - ✅")
  # Tri des participants en fonction des courses via les dossards d'arrivée
  data3km = dataTimeEnd[(dataTimeEnd['DOSSARDS'] >= 3000)
                        & (dataTimeEnd['DOSSARDS'] <= 4000)]
  data5km = dataTimeEnd[(dataTimeEnd['DOSSARDS'] >= 5000)
                        & (dataTimeEnd['DOSSARDS'] <= 6000)]
  data8km = dataTimeEnd[(dataTimeEnd['DOSSARDS'] >= 8000)
                        & (dataTimeEnd['DOSSARDS'] <= 9000)]

  # Récupération des données des coureurs inscrits
  dataRun = getRunners()

  lastDos = dataTimeEnd["DOSSARDS"].values[-1]
  # Stockage des données des coureurs en fonction des distances parcourues
  allDataKm = {
      "3": {
          "dos": data3km['DOSSARDS'].apply(lambda x: int(x)),
          "hour": data3km['HEURE'].apply(lambda x: convert_datetime_to_time(x)),
          "name": data3km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'NOM'].iloc[0]]),
          "surname": data3km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'PRENOM'].iloc[0]]),
          "class": data3km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'CLASSE'].iloc[0]]),
          "squad": data3km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'EQUIPE'].iloc[0]]),
          "sex": data3km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'SEXE'].iloc[0]]),
          "durationRun": data3km['HEURE'].apply(lambda x: convert_datetime_to_time(x)).apply(lambda x: datetime.combine(datetime.min, x) - datetime.combine(datetime.min, hourTab[0])),
          "dep": hourTab[0],
          "realDist": distTab[0],
      },
      "5": {
          "dos": data5km['DOSSARDS'].apply(lambda x: int(x)),
          "hour": data5km['HEURE'].apply(lambda x: convert_datetime_to_time(x)),
          "name": data5km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'NOM'].iloc[0]]),
          "surname": data5km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'PRENOM'].iloc[0]]),
          "class": data5km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'CLASSE'].iloc[0]]),
          "squad": data5km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'EQUIPE'].iloc[0]]),
          "sex": data5km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'SEXE'].iloc[0]]),
          "durationRun": data5km['HEURE'].apply(lambda x: convert_datetime_to_time(x)).apply(lambda x: datetime.combine(datetime.min, x) - datetime.combine(datetime.min, hourTab[1])),
          "dep": hourTab[1],
          "realDist": distTab[1],
      },
      "8": {
          "dos": data8km['DOSSARDS'].apply(lambda x: int(x)),
          "hour": data8km['HEURE'].apply(lambda x: convert_datetime_to_time(x)),
          "name": data8km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'NOM'].iloc[0]]),
          "surname": data8km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'PRENOM'].iloc[0]]),
          "class": data8km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'CLASSE'].iloc[0]]),
          "squad": data8km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'EQUIPE'].iloc[0]]),
          "sex": data8km['DOSSARDS'].apply(lambda d: [dataRun.loc[dataRun['DOSSARDS'] == d, 'SEXE'].iloc[0]]),
          "durationRun": data8km['HEURE'].apply(lambda x: convert_datetime_to_time(x)).apply(lambda x: datetime.combine(datetime.min, x) - datetime.combine(datetime.min, hourTab[2])),
          "dep": hourTab[2],
          "realDist": distTab[2],
      }
  }
  print("[STEP 2] - Répartition /distance parcourue - ✅")

  # Données en fonction du sexe des participants
  sexData = {
      "women": {
          "duration": [],
          "speed": [],
          "dos": [],
          "length": [],
          "netDuration": [],
          "netSpeed": []
      },
      "men": {
          "duration": [],
          "speed": [],
          "dos": [],
          "length": [],
          "netDuration": [],
          "netSpeed": []
      }
  }
  print("[STEP 2] - Répartiion /sexe des coureurs - ✅")

  # Attribution des données en fonction du sexe des participants
  for _, s in allDataKm.items():
    for sex, duration, dos in zip(s.get("sex"), s.get("durationRun"), s.get("dos")):
      dataR = sexData["women" if sex[0] == "F" else "men"]
      dataR["duration"].append(duration)
      dataR["dos"].append(dos)
      dataR["length"].append(s.get("realDist"))

  # Calcul de la somme des distances & des durées
  womenDistSum = 0
  womenDurSum = timedelta()
  for i in range(len(sexData["women"]["length"])):
    womenDistSum += sexData["women"]["length"][i]
    womenDurSum += sexData["women"]["duration"][i]

  menDistSum = 0
  menDurSum = timedelta()
  for i in range(len(sexData["men"]["length"])):
    menDistSum += sexData["men"]["length"][i]
    menDurSum += sexData["men"]["duration"][i]

  totDist = menDistSum + womenDistSum
  totDur = menDurSum + womenDurSum

  # Calcul vitesse brute
  for _, s in sexData.items():
    for duration, length in zip(s.get("duration"), s.get("length")):
      sexData[_]["speed"].append(length / duration.total_seconds() * 3600)

  # Calcul vitesses Gén et /sex
  speedGen = totDist / totDur.total_seconds() * 3600
  speedMen = menDistSum / menDurSum.total_seconds() * 3600
  speedWomen = womenDistSum / womenDurSum.total_seconds() * 3600

  # Calcul des temps & vitesses nets de course de chaque participants
  for _, s in sexData.items():
    for duration, speed in zip(s.get("duration"), s.get("speed")):
      netDuration = (speedWomen if _ == "women" else speedMen) / speedGen * duration.total_seconds()

      sexData[_]["netDuration"].append(timedelta(seconds=netDuration))
      sexData[_]["netSpeed"].append(speedGen / (speedWomen if _ == "women" else speedMen) * speed)

  print("[STEP 4] - Calculs des vitesses & durées nettes - ✅")
  classData = dict()

  def getNetSpeed(dos):
    for _, s in sexData.items():
      for doss, netSpeed, netDuration in zip(s.get("dos"), s.get("netSpeed"), s.get("netDuration")):
        if doss == dos:
          return (netSpeed, netDuration)

  # Gestion des partipants en fonction de leur classe
  for _, s in allDataKm.items():
    for dos, clas, squad in zip(s.get("dos"), s.get("class"), s.get("squad")):
      try:
        classData[clas[0]]["dos"].append(dos)
        classData[clas[0]]["squad"].append(squad[0])
        classData[clas[0]]["netSpeed"].append(getNetSpeed(dos)[0])
        classData[clas[0]]["netDuration"].append(getNetSpeed(dos)[1])
      except:
        classData[clas[0]] = dict(
            {"dos": [dos], "squad": [squad[0]], "netSpeed": [getNetSpeed(dos)[0]], "netDuration": [getNetSpeed(dos)[1]]})

  # Calcul des distances totales à parcourir / classes
  effectDic = {
      "MPSI-2I": 47,
      "MPSI1": 44,
      "MP(I)E": 41,
      "MP(I)": 41,
      "DCG3": 35,
      "DCG1": 40,
      "PC": 40,
      "PCE": 37,
      "PCSI1": 46,
      "PCSI2": 43,
      "PSI": 41
  }

  for _, s in classData.items():
    s["distToRun"] = effectDic[_] * 2.5
    tierOfdist = s["distToRun"] / 3
    dos8km, dos8kmSum = [], 0
    dos5km, dos5kmSum = [], 0
    dosRest, dosRestSum = [], 0
    dosComplete = []
    speedComplete = []
    durationComplete = []
    for dos in s.get("dos"):
      if dos8kmSum < tierOfdist and dos > 7999:
        dos8km.append(dos)
        dos8kmSum += distTab[2]
      if dos5kmSum < tierOfdist and dos > 4999:
        dos5km.append(dos)
        dos5kmSum += distTab[1]
    for dos in s.get("dos"):
      if dos8kmSum + dos5kmSum + dosRestSum < s.get("distToRun") and not dos8km.count(dos) and not dos5km.count(dos):
        dosRest.append(dos)
        dosRestSum += distTab[2] if dos > 7999 else distTab[1] if dos > 4999 else distTab[0]
    while dos8kmSum + dos5kmSum + dosRestSum < s.get("distToRun"): 
        print(dos8kmSum + dos5kmSum + dosRestSum)
        dosRest.append(lastDos)
        dosRestSum += distTab[2] if lastDos > 7999 else distTab[1] if lastDos > 4999 else distTab[0]
    for i in dos8km:
      dosComplete.append(i)
    for i in dos5km:
      dosComplete.append(i)
    for i in dosRest:
      dosComplete.append(i)
    s["dosComplete"] = dosComplete
    for dossards in dosComplete:
      speedComplete.append(getNetSpeed(dossards)[0])
      durationComplete.append(getNetSpeed(dossards)[1])
    s["speedComplete"] = speedComplete
    s["durationComplete"] = durationComplete

  # Début des calculs incompréhensibles
    sumDistComplete = 0
    sumDurComplete = timedelta(0)

  # A REPRENDRE AVEC LA FORMULE FOURNIE
    for dos, duration in zip(s.get("dosComplete"), s.get("durationComplete")):
      sumDistComplete += distTab[2] if dos > 7999 else distTab[1] if dos > 4999 else distTab[0]
      sumDurComplete += duration
    s["speedTot"] = sumDistComplete / sumDurComplete.seconds * 3600

  print("[STEP 5] - Calcul des vitesses /classes - ✅")
  resListClass = []
  for _, s in classData.items():
    resListClass.append((_, round(s.get("speedTot"), 3)))
  resListClass.sort(key=lambda x: x[1], reverse=True)

  resList8Men = []
  resList8Women = []
  resList5Men = []
  resList5Women = []
  resList3Men = []
  resList3Women = []

  for _, s in sexData.items():
    for dos, netSpeed, netDuration, speed, duration in zip(s.get("dos"), s.get("netSpeed"), s.get("netDuration"), s.get("speed"), s.get("duration")):
      if dos > 7999:
        if _ == "women":
          resList8Women.append((dataRun.loc[dataRun['DOSSARDS'] == dos, 'PRENOM'].iloc[0]+" " + dataRun.loc[dataRun['DOSSARDS'] == dos, 'NOM'].iloc[0].upper(), round(
              netSpeed, 3), netDuration, dataRun.loc[dataRun['DOSSARDS'] == dos, 'CLASSE'].iloc[0], round(speed, 3), timedelta(seconds=duration.total_seconds())))
        else:
          resList8Men.append((dataRun.loc[dataRun['DOSSARDS'] == dos, 'PRENOM'].iloc[0]+" " + dataRun.loc[dataRun['DOSSARDS'] == dos, 'NOM'].iloc[0].upper(), round(
              netSpeed, 3), netDuration, dataRun.loc[dataRun['DOSSARDS'] == dos, 'CLASSE'].iloc[0], round(speed, 3), timedelta(seconds=duration.total_seconds())))
      elif dos > 4999:
        if _ == "women":
          resList5Women.append((dataRun.loc[dataRun['DOSSARDS'] == dos, 'PRENOM'].iloc[0]+" " + dataRun.loc[dataRun['DOSSARDS'] == dos, 'NOM'].iloc[0].upper(), round(
              netSpeed, 3), netDuration, dataRun.loc[dataRun['DOSSARDS'] == dos, 'CLASSE'].iloc[0], round(speed, 3), timedelta(seconds=duration.total_seconds())))
        else:
          resList5Men.append((dataRun.loc[dataRun['DOSSARDS'] == dos, 'PRENOM'].iloc[0]+" " + dataRun.loc[dataRun['DOSSARDS'] == dos, 'NOM'].iloc[0].upper(), round(
              netSpeed, 3), netDuration, dataRun.loc[dataRun['DOSSARDS'] == dos, 'CLASSE'].iloc[0], round(speed, 3), timedelta(seconds=duration.total_seconds())))
      elif dos > 2999:
        if _ == "women":
          resList3Women.append((dataRun.loc[dataRun['DOSSARDS'] == dos, 'PRENOM'].iloc[0]+" " + dataRun.loc[dataRun['DOSSARDS'] == dos, 'NOM'].iloc[0].upper(), round(
              netSpeed, 3), netDuration, dataRun.loc[dataRun['DOSSARDS'] == dos, 'CLASSE'].iloc[0], round(speed, 3), timedelta(seconds=duration.total_seconds())))
        else:
          resList3Men.append((dataRun.loc[dataRun['DOSSARDS'] == dos, 'PRENOM'].iloc[0]+" " + dataRun.loc[dataRun['DOSSARDS'] == dos, 'NOM'].iloc[0].upper(), round(netSpeed, 3), netDuration, dataRun.loc[dataRun['DOSSARDS'] == dos, 'CLASSE'].iloc[0], round(speed,3), timedelta(seconds = duration.total_seconds())))
  
  resList8Men.sort(key=lambda x: x[1], reverse=True)
  resList8Women.sort(key=lambda x: x[1], reverse=True)
  resList5Men.sort(key=lambda x: x[1], reverse=True)
  resList5Women.sort(key=lambda x: x[1], reverse=True)
  resList3Men.sort(key=lambda x: x[1], reverse=True)
  resList3Women.sort(key=lambda x: x[1], reverse=True)
  print("[FINAL STEP 1] - Génération des classements - ✅")
  print(resList3Men)
  # print(resListClass)

  # for _,s in classData["MPSI-2I"].items():
  #   print(_," - ",s ,"\n\n")
  # for _,s in classData.items():
  #   print(_," - ",s ,"\n\n")

  # Générer le code HTML
  html = """
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="UTF-8">
      <title>Résultats de la course</title>
      <link rel="stylesheet" type="text/css" href="style2.css">
    </head>
    <body>
      <div id="header">
        <img src="https://cdn.discordapp.com/attachments/1013487666966311007/1089990641691406376/logo_wallon.png" alt="Logo">
      </div>
      <div id="html">
        <h1>CROSS DE WALLON 2023 - RÉSULTATS</h1>
        <h1>Classement général</h1>
        <table>
          <tr>
            <th>Équipe</th>
            <th>Vitesse nette (km/h)</th>
          </tr>
  """

  for team, speed in resListClass:
      html += f"""
          <tr>
            <td>{team}</td>
            <td>{speed}</td>
          </tr>
  """

  html += """
        </table>
<div style="page-break-after: always;" class="breakafter"></div>
  """
  # Ajouter le classement des hommes et des femmes pour les différentes distances
  html += "<h2>Classement des coureurs individuels</h2>"

  # 8 km Hommes
  html += "<h3>8 km Hommes</h3>"
  html += "<table><tr><th>Nom et prénom</th><th>Classe</th><th>Vitesse brute (km/h)</th><th>Durée brute</th></tr>"
  for runner in resList8Men:
      html += f"<tr><td>{runner[0]}</td><td>{runner[3]}</td><td>{runner[4]}</td><td>{runner[5]}</td></tr>"
  html += "</table>"

  # 8 km Femmes
  html += "<h3>8 km Femmes</h3>"
  html += "<table><tr><th>Nom et prénom</th><th>Classe</th><th>Vitesse brute (km/h)</th><th>Durée brute</th></tr>"
  for runner in resList8Women:
      html += f"<tr><td>{runner[0]}</td><td>{runner[3]}</td><td>{runner[4]}</td><td>{runner[5]}</td></tr>"
  html += "</table>"

  # 5 km Hommes
  html += "<h3>5 km Hommes</h3>"
  html += "<table><tr><th>Nom et prénom</th><th>Classe</th><th>Vitesse brute (km/h)</th><th>Durée brute</th></tr>"
  for runner in resList5Men:
      html += f"<tr><td>{runner[0]}</td><td>{runner[3]}</td><td>{runner[4]}</td><td>{runner[5]}</td></tr>"
  html += "</table>"

  # 5 km Femmes
  html += "<h3>5 km Femmes</h3>"
  html += "<table><tr><th>Nom et prénom</th><th>Classe</th><th>Vitesse brute (km/h)</th><th>Durée brute</th></tr>"
  for runner in resList5Women:
      html += f"<tr><td>{runner[0]}</td><td>{runner[3]}</td><td>{runner[4]}</td><td>{runner[5]}</td></tr>"
  html += "</table>"

  # 3 km Hommes
  html += "<h3>3 km Hommes</h3>"
  html += "<table><tr><th>Nom et prénom</th><th>Classe</th><th>Vitesse brute (km/h)</th><th>Durée brute</th></tr>"
  for runner in resList3Men:
      html += f"<tr><td>{runner[0]}</td><td>{runner[3]}</td><td>{runner[4]}</td><td>{runner[5]}</td></tr>"
  html += "</table>"

  # 3 km Femmes
  html += "<h3>3 km Femmes</h3>"
  html += "<table><tr><th>Nom et prénom</th><th>Classe</th><th>Vitesse brute (km/h)</th><th>Durée brute</th></tr>"
  for runner in resList3Women:
      html += f"<tr><td>{runner[0]}</td><td>{runner[3]}</td><td>{runner[4]}</td><td>{runner[5]}</td></tr>"
  html += "</table>"

  file = open("result.html", "wb")
  file.write(html.encode())
  file.close()
  print("[FINAL STEP 2] - Génération des fichiers d'affichages - ✅")


#renderDossardsHTML()
getAllTime()
