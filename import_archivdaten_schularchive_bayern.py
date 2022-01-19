import csv
import mwclient
from mwclient import Site
from requests.auth import HTTPDigestAuth
import time

#This wikibot was used to upload data to the school archives wiki (https://schularchive.bbf.dipf.de/index.php/Hauptseite). You can use it as a basis for your own bots :)

def creatematerial(begindate, enddate, note, school, archive,site,link):
    text = "{{Archivgut\n"
    text += "|Archivgut=Findbuch"
    text += "|Startdatum=" + begindate + "\n"
    text += "||Enddatum=" + enddate + "\n"
    text += "|ArchivgutKommentar=" + note + "\n"
    text += "||ArchivgutHerkunft=" + school + "\n"
    text += "||Link/Findbuch=" + link + "\n"
    text += "||ArchivgutLagerort=" + archive + "\n}}"
    pagename = "Findbuch " + school + " " + begindate + "-" + enddate
    try:
        page = site.pages[pagename]  # open page
        if page.text() == "":
            page.save(text)  # save page with text
        else:
            print(pagename+ " exists") # do nothing since page exists
    except:
        print("Error ###################################################### " + pagename)

def createschool(school, wikidata,state,site,ort):
    text = "{{SchuleVorlage"
    text += "|Schulort=" + ort + "\n"
    text += "|Wikidata ID=" + wikidata + "\n}}\n"
    text += "{{SchuladresseVorlage\n"
    text += "|Land=" + state + "\n" + "}}"
    try:
        page = site.pages[school]  # open page
        page.save(text)  # save page with text
    except:
        print("Error ###################################################### " + school)

def main():
    site = mwclient.Site('test.com', path='/') #define url to page
    with open('Schularchive_StABa.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        state = "Bayern" #define state
        archive = "Staatsarchiv Bamberg" #define name of the archive
        for row in reader:
            school= row["Schule"]
            begindate = row["Startdatum"]
            enddate = row["Enddatum"]
            note = row["Enthaelt"]
            ort = row["Ort"]
            link = row["Link"]
            wikidata = ""
            site.login('', '') #username and password for your account
            creatematerial(begindate, enddate, note, school, archive,site,link)
            schoolpage = site.pages[school]
            if schoolpage.text() == "":
                createschool(school, wikidata, state, site,ort)
            else:
                print(school + " exists") # do nothing since school exists
        print("fertig")

if __name__ == "__main__":
    main()