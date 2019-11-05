from bs4 import BeautifulSoup as BS
from Doctor import *
import urllib.request as request

file_name_if_couldnt_get_doctor_name = "doctor_url_error.txt"
root_url = "https://www.doctoralia.com.br"
main_page_url = root_url + "/medicos"


def getSpecialtyUrls():
    """
    This function returns a list of urls of the main page, that is,
    urls for each Specialty of doctor. See the page
        https://www.doctoralia.com.br/especializacoes-medicas
    It returns the url for each "mais>>" link.
    """
    #requesting the MAIN page and reading it
    page = request.urlopen(main_page_url).read()

    #taking the BS manager
    soup = BS(page,"html.parser")

    #listing all the anchors '<a class="text-muted"></a>'
    list_of_specialties_on_main_page = soup.find_all("a",class_="text-muted")

    #list for returning
    url_list_of_specialty_pages = []
    for item in list_of_specialties_on_main_page:
        #getting the url of the "mais>>" link
        if item.string.find("mais") >= 0:
            #if there is "mais" in the string, append the url into a list
            url_list_of_specialty_pages.append(item["href"])

    #returning the url list of the "mais>>" links
    return url_list_of_specialty_pages



def getCityUrls(specialty_url):
    """
    This function returns a list of urls of Speciality from a specific
    city. See the page
    https://www.doctoralia.com.br/especializacoes-medicas/em-detalhe/alergista
    It needs a url from the getSpecialtyUrls() function.
    It returns the url for each city link.
    """
    #requesting the page and reading it
    page = request.urlopen(specialty_url).read()

    #taking the BS manager
    soup = BS(page,"html.parser")

    #listing all the list items '<li class="col-sm-6"></li>'
    list_of_cities_div = soup.find_all("li",class_="col-sm-6")

    #list for returning
    city_list_urls = []
    for div in list_of_cities_div:
        #concatenating the ROOT_URL to the url and appending it into a list
        city_list_urls.append(root_url + div.a["href"])

    return city_list_urls










def getDoctorUrls(city_url):
    """This function returns a list of urls of Doctor pages"""

    #requesting the page and reading it
    page = request.urlopen(city_url).read()

    #taking the BS manager
    soup = BS(page,"html.parser")

    #taking the h1 title '<h1 class="col-md-9"></h1>' as string
    city_name_h1 = soup.find("h1",class_="col-md-9")
    city_name = " ".join(city_name_h1.string.split()[2:])

    #listing all the anchors '<a class="rank-element-name__link"></a>'
    list_doctor_a = soup.find_all("a",class_="rank-element-name__link")

    #list for returning
    list_doctor_url = []
    for doctor_a in list_doctor_a:
        #taking a url from an anchor and appending it into a list
        doctor_url = doctor_a["href"]
        list_doctor_url.append(doctor_url)

    return list_doctor_url









def getDoctor(url):
    """
    This function takes an url from a Doctor page and grabs all the
    needed data from there.
    """
    #requesting the page and reading it
    try:
        page = request.urlopen(url).read()
    except Exception as e:
        #if some error occurs, it returns a void Doctor object
        #(all attributes are setted as "---")
        print(e)
        return Doctor()

    #taking the BS manager
    soup = BS(page,"html.parser")


    #FULL NAME : doctor_name: IS MANDATORY! If it is not possible
    #to obtain the name, it raises an error to be treated in the main
    #function
    try:
        #taking, from all list item '<li class="dropdown"></li>',
        #the string of the last one
        doctor_name = soup.find_all("li", class_="dropdown")[-1].span.string #OK
    except:
        print("Couldn't get name.")
        f = open(file_name_if_couldnt_get_doctor_name,"a")
        f.write(url+"\n")
        f.close()
        raise Exception("\033[91;mCould not get a name. A void entry is returned as '---'.\033[m")


    # SKILLS LIST : doctor_skills_list
    try:
        #taking, from all h2 title '<h2 class="h4"></h2>', the first entry
        doctor_skills_h2 = soup.find_all("h2", class_="h4")[0]
        #taking all the anchors <a> inside the <h2>
        doctor_skills_a = doctor_skills_h2.find_all('a')

        #list for appending
        doctor_skills_list = []
        for a in doctor_skills_a:
            doctor_skills_list.append(a.string)
    except:
        #if it fails, take it as ["---"]
        doctor_skills_list = ["---"]
        print("Couldn't get doctor_skills_list.")


    #SPECIALTY
    try:
        #taking, from all list item '<li class="dropdown"></li>', the second entry
        #taking, from all anchors '<a itemprop="item"></a>', the first entry
        #inside the <li> as string
        doctor_specialty = soup.find_all("li", \
            class_="dropdown")[1].find_all("a",\
            itemprop="item")[0].span.string
    except:
        #if it fails, take it as "---"
        doctor_specialty = "---"
        print("Couldn't get specialty.")


    # CITY
    try:
        #taking, from all list item '<li class="dropdown"></li>', the third entry
        #taking, from all anchors '<a itemprop="item"></a>', the first entry
        #inside the <li> as string
        doctor_city = soup.find_all("li", \
            class_="dropdown")[2].find_all("a", \
            itemprop="item")[0].span.string
    except:
        #if it fails, take it as "---"
        doctor_city = "---"
        print("Couldn't get city.")


    # STATE
    try:
        #taking,from all span, the content of the first entry
        #'<span class="province region"></span>'
        doctor_state = soup.find_all("span", \
            class_="province region")[0]["content"]
    except:
        #if it fails, take it as "---"
        doctor_state = "---"
        print("Couldn't get state.")

    # PHONE
    try:
        #taking, from all anchors '<a class="visible-xs"></a>', the second entry
        #as string
        doctor_phone = soup.find_all("a", class_="visible-xs")[1].string
    except:
        #if it fails, take it as "---"
        doctor_phone = "---"
        print("Couldn't get phone number.")

    #building a Doctor object for returning
    D = Doctor()
    D.setName(doctor_name)
    D.setSpecialty(doctor_specialty)
    D.setSkills(", ".join(doctor_skills_list))
    D.setState(doctor_state)
    D.setCity(doctor_city)
    D.setPhone(doctor_phone)

    return D




