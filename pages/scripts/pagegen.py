# Script used to generate index.html, character pages, and item pages

import os
import math

# ------------------ Variables ------------------
# General Stuff
tftSet = 5
indent = "    "
championList = list()
prefix = "TFT" + str(tftSet) + "_"
# Directories
htmlRootProd = "https://tft.guide/"
htmlRootDev = "file:///C:/Development/tft.guide/repo/"
htmlRoot = htmlRootProd
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
header = open(rootDir + templateDir + "header.html", "r").read()
header = header.replace("[rootDir]", htmlRoot)
menu = open(rootDir + templateDir + "menu_bar.html", "r").read()
menu = menu.replace("[rootDir]", htmlRoot)


# ------------------ Generating index.html ------------------
with open(rootDir + "index.html", "w") as indexPage:
    # start with the header
    indexPage.write(header) 
    # body start
    indexPage.write("\n\n" + indent + "<body>\n") 
    # add in the menu bar
    indexPage.write(menu + "\n\n")
    # start the champion icon grid
    indexPage.write(2*indent + "<div class=\"row\">\n")
    indexPage.write(3*indent + "<div class=\"col-8\">\n")
    indexPage.write(4*indent + "<div class=\"champ_grid\">\n")

    # iterate over the list of champion icons
    for file in os.listdir(rootDir + iconDir):
        filename = os.fsdecode(file)
        champion = ""
        if filename.startswith(prefix) and filename.endswith(".png"):
            # pull out the champion name
            sansExtension = filename.split('.')[0]
            champion = sansExtension.split('_')[1]
            # add page link
            indexPage.write(5*indent)
            indexPage.write("<a href=\"" + championDir + prefix + champion + ".html" + "\">\n")
            # write out the html for the icon
            indexPage.write(6*indent)
            indexPage.write("<img src=\"" + iconDir + filename + "\" ")
            indexPage.write("id=\"champ_icon\" alt=\"" + champion + " ")
            indexPage.write("Icon\" title=\"" + champion + "\">\n")
            indexPage.write(5*indent)
            indexPage.write("</a>\n")
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
        # TODO: Figure out a way to auto-add page links for summons

    # close out the champion grid
    indexPage.write(4*indent + "</div>\n")
    indexPage.write(3*indent + "</div>\n")
    indexPage.write(2*indent + "</div>\n")

    # page end
    indexPage.write(indent + "</body>\n</html>") 

# ------------------ Generating Champion Pages ------------------
for champion in championList:
    with open(rootDir + championDir + prefix + champion + ".html", "w") as champPage:
        # start with the header
        champPage.write(header) 
        # body start
        champPage.write("\n\n" + indent + "<body>\n") 
        # add in the menu bar
        champPage.write(menu + "\n\n")
        # champion portrait
        champPage.write(2*indent + "<div class=\"row\">\n")
        champPage.write(3*indent + "<div class=\"col-8\">\n")
        champPage.write("<img src=\"" + rootDir + portraitDir + prefix + champion + ".png\">\n")
        # Rest of the owl
        
        # close out divs
        champPage.write(3*indent + "</div>\n")
        champPage.write(2*indent + "</div>\n")
        # page end
        champPage.write(indent + "</body>\n</html>") 
# ------------------ Generating Item Pages ------------------
