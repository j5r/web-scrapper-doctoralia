# DoctorSiteManager.py
We implemented a web scrapper for getting data from the website "doctoralia.com.br" and saving it into an Excel sheet.

 - getSpecialtyUrls(): this method gets all the urls from the [Set of specialties](https://www.doctoralia.com.br/medicos) for all specialties. It returns a list containing these urls.

 - getCityUrls(specialty_url): this method gets all the urls from the page when we click on "mais>>" in the [Set of specialties](https://www.doctoralia.com.br/medicos) link. When we click on it, we get one page like [Set of cities](https://www.doctoralia.com.br/especializacoes-medicas/em-detalhe/alergista). This method returns a list of all urls of cities. It needs some url from the getSpecialtyUrls() method as a mandatory positional argument.

 - getDoctorUrls(city_url): this method gets all the urls of doctor pages like in [Set of Doctors](https://www.doctoralia.com.br/alergista/alem-paraiba). This method returns a list of urls. It needs some url from the getCityUrls() method as a mandatory positional argument.

 - getDoctor(doctor_url): this method gets all the specific data from a page like [Doctor Page](https://www.doctoralia.com.br/thais-de-oliveira-ferreira/alergista/alem-paraiba#address-id=[214158]). It returns an object of type Doctor, implemented on Doctor.py.


# Doctor.py
In this file we implemented a simple class for storing data. Simple getters and setters are implemented, all of it are strings. We implemented a simple representation method, for using print() method.

 - Name
 - Specialty
 - Skills (list)
 - State (provincy)
 - City
 - Phone


# scrapper.py
In this file we implemented the main function, composed by nested loops, passing through the four functions already described in DoctorSiteManager.py. It will create an Excel file containing the required data as specified in Doctor.py. When some error occurs, we save the "doctor url" in the file "doctor_url_error.txt".











