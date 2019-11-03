# DoctorSiteManager.py
We implemented a web scrapper for getting data from the website "doctoralia.com.br" and saving it into an Excel sheet.

 - getSpecialtyUrls( ) ==> [url_list]: this function gets all the urls from the page [Set of specialties](https://www.doctoralia.com.br/medicos) when we click on "mais>>" link, for all specialties. It returns a list containing these urls.

 - getCityUrls(specialty_url) ==> [url_list]: this function gets all the urls for all cities for some specialty, like in [Set of cities](https://www.doctoralia.com.br/especializacoes-medicas/em-detalhe/alergista). This function returns a list of all urls of cities. It needs some url from the getSpecialtyUrls() function as a mandatory positional argument.

 - getDoctorUrls(city_url) ==> [url_list]: this function gets all the urls of doctor pages like in [Set of Doctors](https://www.doctoralia.com.br/alergista/alem-paraiba). This function returns a list of urls. It needs some url from the getCityUrls() function as a mandatory positional argument.

 - getDoctor(doctor_url) ==> Doctor( ): this function gets all the specific data from a doctor page like [Doctor Page](https://www.doctoralia.com.br/thais-de-oliveira-ferreira/alergista/alem-paraiba#address-id=[214158]). It returns an object of type Doctor, implemented in Doctor.py. Each attribute of Doctor's objects was tested with try-except handler. When some of these attributes causes an error, it will be replaced by "---", except whether it is the name, when it raises an error to scrapper.py. This one for its turn sees the error raised and then save the url to "doctor_url_error.txt", indicating the name of that Doctor could not be obtained.


# Doctor.py
In this file we implemented a simple class for storing data. Simple getters and setters are implemented, all of its attributes are strings. We implemented a simple representation method, for using the print() function and the special method for comparing objects contents, like "a==b?" (this was not used in the scrapper.py).

 - Name
 - Specialty
 - Skills (list)
 - State (provincy)
 - City
 - Phone


# scrapper.py 
### (This is the main file: run it by typing "python3 scrapper.py")
In this file we implemented the main function, composed by nested loops, passing through the four functions already described in DoctorSiteManager.py. It will create an Excel file containing the required data as specified in Doctor.py. When some error occurs, we save the "doctor url" in the file "doctor_url_error.txt". If some data could not be obtained, it will be replaced by "---".
