from DoctorSiteManager import *
from openpyxl import Workbook as WB

wb = WB()
excel = wb.active
excel["A1"] = "Nome do Médico"
excel["B1"] = "Especialidade"
excel["C1"] = "Competências"
excel["D1"] = "Estado"
excel["E1"] = "Cidade"
excel["F1"] = "Telefone"


"""
STRATEGY (you can see it in README.md)
We will pass through a list of urls that point out to another list of
urls, that, again, point to another list of urls.

We call the first one as "specialities_urls", that is in the main page.
These urls points to other pages, which is one for each city.
For each city, there is a group of doctors, which in turn have their
own pages. We will navegate through this tree until reaching the doctors
pages, where we will get the data.
"""


specialities_urls = getSpecialtyUrls()
try:
    for s in specialities_urls:
        cities_urls = getCityUrls(s)
        try:
            for c in cities_urls:
                doctors_urls = getDoctorUrls(c)
                ########################## GENERATING EXCEL SHEET
                print("saving data")
                try:
                    while len(doctors_urls):
                        url_doctor = doctors_urls.pop()
                        try:
                            D = getDoctor(url_doctor)
                            row = (
                                D.getName(),
                                D.getSpecialty(),
                                D.getSkills(),
                                D.getState(),
                                D.getCity(),
                                D.getPhone()
                                )
                            try:
                                excel.append(row)
                            except KeyboardInterrupt:
                                wb.save("database.xlsx")
                                quit()
                        except:
                            print("Error in: \033[1;31m",url_doctor,"\033[m")
                            with open("doctor_url_error.txt","a") as f:
                                f.write(url_doctor + "\n")
                                f.close()
                except KeyboardInterrupt:
                    wb.save("database.xlsx")
                    quit()

        except KeyboardInterrupt:
            wb.save("database.xlsx")
            quit()
except KeyboardInterrupt:
    wb.save("database.xlsx")
    quit()




