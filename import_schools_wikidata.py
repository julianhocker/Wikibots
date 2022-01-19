import csv
import mwclient
from mwclient import Site
from requests.auth import HTTPDigestAuth
import time
import re
from check_existing import *

##This wikibot was used to upload data to the school archives wiki (https://schularchive.bbf.dipf.de/index.php/Hauptseite). Basis for this was a data dump from Wikidata as a CSV file.

def createschool(site, school, wikidata,place, coords, adress):

    text = "{{SchuleVorlage\n"
    text += "|Schulort=" + place + "\n"
    text += "|Wikidata ID=" + wikidata + "\n}}\n"
    text += "{{SchuladresseVorlage\n"
    text += "|Koordinaten=" + coords + "\n"
    text += "|Adresse=" + adress + "\n" + "}}"
    text += "{{SchultypVorlage\n"
    text += "|Schultyp ID=1\n"
    text += "|Schultyp=Waldorfschule}}"


    try:
        page = site.pages[school]  # open page
        page.save(text)  # save page with text
    except:
        print("Error ###################################################### " + school)

def main():
    site = mwclient.Site('schularchive.bbf.dipf.de', path='/')#add path to the wiki
    with open('', newline='') as csvfile: #add path to file you want to import
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            school= row["itemLabel"]
            coords = row["long"] + " " + row["lat"]
            adress = row["adress"]
            place = row["placeLabel"]
            wikidata = row['item']
            site.login('', '')#add user credentials
            schoolpage = site.pages[school]
            schoolexist = checkwikidata(wikidata)
            if schoolexist == False:
                createschool(site,school, wikidata,place, coords, adress)
            else:
                print(school + " exists") # do nothing since school exists
        print("fertig")

if __name__ == "__main__":
    main()