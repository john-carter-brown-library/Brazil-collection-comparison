#creates a list of cleanly formatted primary titles from records exported from the NYPL web catalog
nypl_brazil = open("NYPL_Brazil_18c.txt","r",encoding="utf-8")

active_title = ""
title_building = False
titles = []

for line in nypl_brazil:
    if title_building:
        if (line[0] == " "):
            spaces = True
            for character in line:
                if (character == " ") and (spaces == True):
                    continue
                elif (character != " ") and (spaces == True):
                    spaces = False
                    clean_title = character
                else:
                    clean_title += character
            if ((clean_title[len(clean_title) - 1] == '\n') or (clean_title[len(clean_title) - 1] == '\r')) and (clean_title[len(clean_title) - 2] != " "):
                active_title = active_title + clean_title[:len(clean_title) - 1] + " "
            elif ((clean_title[len(clean_title) - 1] == '\n') or (clean_title[len(clean_title) - 1] == '\r')) and (clean_title[len(clean_title) - 2] == " "):
                active_title = active_title + clean_title[:len(clean_title) - 1]
            elif (clean_title[len(clean_title) - 1] == ' '):
                active_title = active_title + clean_title[13:len(clean_title)]
            else:
                active_title = active_title + clean_title[13:len(clean_title)] + " "
        else:
            titles.append(active_title)
            active_title = ""
            title_building = False
    else:
        if ("TITLE" in line) and ("ADD TITLE" not in line):
            if ((line[len(line) - 1] == '\n') or (line[len(line) - 1] == '\r')) and (line[len(line) - 2] != " "):
                active_title = line[13:len(line) - 1] + " "
            elif ((line[len(line) - 1] == '\n') or (line[len(line) - 1] == '\r')) and (line[len(line) - 2] == " "):
                active_title = line[13:len(line) - 1]
            elif (line[len(line) - 1] == ' '):
                active_title = line[13:len(line)]
            else:
                active_title = line[13:len(line)] + " "
            title_building = True

nypl_brazil.close()
print(len(titles))
