from bs4 import BeautifulSoup as BS
from Doctor import *
import urllib.request as request
root_url = "https://www.doctoralia.com.br"
main_page_url = root_url + "/medicos"




def getSpecialtyUrls():
    """
    This function returns a list of urls of the main page, that is,
    urls for each Specialty of doctor. See the page
        https://www.doctoralia.com.br/especializacoes-medicas
    It returns the url for each "mais>>" link.
    """
    page = request.urlopen(main_page_url).read()
    soup = BS(page,"html.parser")

    list_of_specialties_on_main_page = soup.find_all("a",class_="text-muted")
    url_list_of_specialty_pages = []

    for item in list_of_specialties_on_main_page:
        #getting the url of the "mais>>" link
        if item.string.find("mais") >=0 :
            url_list_of_specialty_pages.append(item["href"])
    #returning the url list of the "mais>>" links
    #these urls point to a list of page of cities with its own specialty
    return url_list_of_specialty_pages



def getCityUrls(specialty_url):
    """
    This function returns a list of urls of Speciality from a specific
    city. See the page
    https://www.doctoralia.com.br/especializacoes-medicas/em-detalhe/alergista
    It returns the url for each city link.
    """
    page = request.urlopen(specialty_url).read()
    soup = BS(page,"html.parser")
    list_of_cities_div = soup.find_all("li",class_="col-sm-6")

    city_list_urls = []
    for div in list_of_cities_div:
        city_list_urls.append(root_url + div.a["href"])

    return city_list_urls










def getDoctorUrls(city_url):
    """This function returns a list of urls of Doctor pages"""
    page = request.urlopen(city_url).read()
    soup = BS(page,"html.parser")
    city_name_h1 = soup.find("h1",class_="col-md-9")
    city_name = " ".join(city_name_h1.string.split()[2:])

    list_doctor_a = soup.find_all("a",class_="rank-element-name__link")
    list_doctor_url = []

    for doctor_a in list_doctor_a:
        doctor_url = doctor_a["href"]
        list_doctor_url.append(doctor_url)

    return list_doctor_url









def getDoctor(url):
    page = request.urlopen(url).read()
    soup = BS(page,"html.parser")

    # FULL NAME : doctor_name
    doctor_name = soup.find_all("li", class_="dropdown")[-1].span.string #OK

    # SKILLS LIST : doctor_skills_list
    doctor_skills_h2 = soup.find_all("h2", class_="h4")[0]
    doctor_skills_a = doctor_skills_h2.find_all('a')
    doctor_skills_list = []
    for a in doctor_skills_a:
        doctor_skills_list.append(a.string)


    #SPECIALTY
    doctor_specialty = soup.find_all("li", \
        class_="dropdown")[1].find_all("a",\
        itemprop="item")[0].span.string

    # CITY
    doctor_city = soup.find_all("li", \
        class_="dropdown")[2].find_all("a", \
        itemprop="item")[0].span.string

    # STATE
    doctor_state = soup.find_all("span", \
        class_="province region")[0]["content"]

    # PHONE
    doctor_phone = soup.find_all("a", class_="visible-xs")[1].string
    D = Doctor()
    D.setName(doctor_name)
    D.setSpecialty(doctor_specialty)
    D.setSkills(", ".join(doctor_skills_list))
    D.setState(doctor_state)
    D.setCity(doctor_city)
    D.setPhone(doctor_phone)

    return D




