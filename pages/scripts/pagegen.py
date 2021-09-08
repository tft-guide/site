# Script used to generate index.html, character pages, and item pages

import os
import math

# ------------------ Variables ------------------
# General Stuff
tftSet = 5
indent = "    "
championList = list()
# Directories
rootDir = "../../"
htmlDir = "pages/"
templateDir = htmlDir + "templates/"
championDir = htmlDir + "champions/"
imgDir = "img/"
traitDir = imgDir + "traits/"
portraitDir = imgDir + "champions/portraits/"
iconDir = imgDir + "champions/icons/"
summonDir = iconDir + "summons/"
# Page-specific Stuff
blankImage = "CHAMP_BLANK.png"
header = open(rootDir + templateDir + "header.html", "r") # default page header for all pages


# ------------------ Generating index.html ------------------
with open(rootDir + "indexTest.html", "w") as indexPage:
    # start with the header
    indexPage.write(header.read()) 
    # body start
    indexPage.write("\n\n" + indent + "<body>\n") 
    # add in the menu bar
    indexPage.write(open(rootDir + templateDir + "menu_bar.html", "r").read() + "\n\n")
    # start the champion icon grid
    indexPage.write(2*indent + "<div class=\"row\">\n")
    indexPage.write(3*indent + "<div class=\"col-8\">\n")
    indexPage.write(4*indent + "<div class=\"champ_grid\">\n")

    # iterate over the list of champion icons
    for file in os.listdir(rootDir + iconDir):
        filename = os.fsdecode(file)
        champion = ""
        if filename.startswith("TFT" + str(tftSet)) and filename.endswith(".png"):
            # pull out the champion name
            sansExtension = filename.split('.')[0]
            champion = sansExtension.split('_')[1]
            # write out the html for the icon
            indexPage.write(5*indent)
            indexPage.write("<img src=\"" + iconDir + filename + "\" ")
            indexPage.write("id=\"champ_icon\" alt=\"" + champion + " ")
            indexPage.write("Icon\" title=\"" + champion + "\">\n")
            # add to the champion list
            championList.append(champion)
    
    # count how many summons there are
    summonCount = len([name for name in os.listdir(rootDir + summonDir)])

    # figure out how many rows, columns, and blanks there should be
    totalCount = summonCount + len(championList)
    rows = math.ceil(math.sqrt(totalCount))
    blanks = rows ** 2 - totalCount

    # write out the blanks
    for x in range(blanks):
        indexPage.write(5*indent)
        indexPage.write("<img src=\"" + iconDir + blankImage + "\" ")
        indexPage.write("id=\"blank_icon\">\n")

    # write out the summons
    for file in os.listdir(rootDir + summonDir):
        filename = os.fsdecode(file)
        sansExtension = filename.split('.')[0]
        champion = sansExtension.split('_')[2]
        indexPage.write(5*indent)
        indexPage.write("<img src=\"" + summonDir + filename + "\" ")
        indexPage.write("id=\"champ_icon\" alt=\"" + champion + " ")
        indexPage.write("Icon\" title=\"" + champion + "\">\n")

    # close out the champion grid
    indexPage.write(4*indent + "</div>\n")
    indexPage.write(3*indent + "</div>\n")
    indexPage.write(2*indent + "</div>\n")

    # page end
    indexPage.write(indent + "</body>\n</html>") 

# ------------------ Generating Champion Pages ------------------
for champion in championList:
    with open(rootDir + "indexTest.html", "w") as indexPage:

# ------------------ Generating Item Pages ------------------
