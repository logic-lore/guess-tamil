_x = """Samantha 
 Nayanthara
 Keerthy Suresh
 Trisha Krishnan
 Shruti Haasan
 Tamanna
 Jyothika
 Malavika Nair
 Kajal Agarwal
 Aishwarya Dutta
 Aparna Das
 Aishwarya Rajesh
 Nivetha Pethuraj
 Shriya Saran
 Swathi Reddy
 Priya Vadlamani
 Varalaxmi
 Laila
 Bindu Madhavi
 Aishwarya Lekshmi
 Samyuktha Menon
 Divyabharathi
 Bhavana
 B Saroja Devi
 Manorama
 Lakshmi
 Sheela
 Srividya
 Sujatha
 Ambika
 Raadhika Sarathkumar
 Suhasini Maniratnam
 Menaka
 Ramya Krishnan
 Revathi
 Urvashi
 Kalpana 
 Saranya
 Rekha
 Sukanya
 Madhoo Shah
 Roja
 Soundarya
 Rambha
 Nagma Arvind Morarji
 Maheswari
 Manisha Koirala
 Devayani
 Aishwarya Rai
 Simran
 Isha Koppikar
 Preetha Vijayakumar
 Mumtaj
 Reema Sen
 Bhumika Chawla
 Meera Jasmine
 Sadha
 Sonia Agarwal
 Genelia Deshmukh
 Pooja
 Namitha Vankawala
 Ramya
 Priyamani
 Gopika
 Asin Thottumkal
 Lakshmi Rai
 Vedhika Kumar
 Anushika Shetty
 Regina Cassandra
 Andrea Maria Jeremiah
 Anjali
 Aditi Rao Hydari
 Parvathy
 Poonam Bajwa
 Priya Anand
 Amala Paul
 Vidya Pradeep
 Srushti Dange
 Taapsee Pannu
 Hansika Motwani
 Nithya Menon
 Rakul Preet Singh
 Janani
 Radhika Apte
 Nandita Swetha
 Gayathire Shankar
 Lakshmi Menon
 Nazriya Nazim
 Sridivya
 Riythvika 
 Catherine Tresa Alexander
 Ashna Zaveri
 Miya George
 Nikki Galrani
 Varsha Bollamma 
 Nikhila Vimal
 Manjima Mohan
 Ritika Mohan Singh
 Madonna Sebastian
 Shraddha Srinath
 Sayyeshaa
 Aparna Balamurali
 Priya Bhavani Shankar
 Athulya Ravi
 Raashi Khanna
 Sai Pallavi
 Medha Akash
 Lijomol Jose
 Myna Nandhini
 Vani Bhojan
 Sivaangi Krishnakumar
 Dhanshika
 Tanya Ravichandran
 Rupa Manjari
 Rashmika Mandanna
 Nivetha Thomas
 Priyanka Arul Mohan
 Nidhhi Agerwal
 Anju Kurian
 Poorna
 Kalyani Priyadarshan
 Iswarya Menon
 Vidyullekha Raman
 Surabhi
 Anagha
 Pooja Ramachandran
 Pranitha Subhash
 Ivana
 Rich Gangopadhyay
 Raveena Ravi
 Reba Monica John
 Devadarshini
 Rohini
 Saranya
 Kovai Sarala
 Manju Warrier
 Sheela Rajkumar
 Oviya
 Yashika Aannand
 Anu Emmanuel
 Kayal Anandi
 Namiitha Pramod
 Meetha Raghunath
 Lakshmi Priya Chandramouli
 Vinodhini Vaidyanathan
 Shobana
 Amy Jackson
 Ileana D Cruz
 Anuya Y Bhagwat
 Uma Padmanabhan
 Vinaya Prasad
 Shalu Shammu
 Srianjani
 Neelima Rani
 Meera Kriahnan
 Rethika Srinivas
 Jabgiri Madhumitha
 Vanitha Krishna
 Madhumila
 Sujatha Sivakumar
 Sherin Shringar
 Suzane George
 Neha Sharma
 Athmeeya Rajan
 Vishakha Singh 
 Arthana Binu
 Gouri G Kishan
 Shalini
 Jayasudha
 Anupama Parameswaran
 Raiza Wilson
 Shivani Narayanan
 Malavika Mohanan
 Brigida
 Mallika
 Aarthi
 KUshboo
 Muktha
 Nadhiya
 Kausalya
 Sithara
 Janaki Sabesh
 Aishwarya Bhaskaran
 Abhirami
 Shamna Kasim
 Sanusha
 Akalya Venkatesan
 Kajol
 Ritu Varma
 Easwari Rao
 Karthika Nair
 Pia Bajpiee
 Dhanya Balakrishna
 Abhinaya
 Misha Ghoshal
 Kaniha
 Sunaina
 Sandhya
 Sija Rose
 Iniya"""

splited = _x.split("\n")

import random

def produce(i_value):
    _val = splited[random.randint(0, (len(splited))-1)]
    if _val == i_value:
        produce(i_value)
    else:
        return _val.strip()

cout=1
output_ = ""
for i in splited:
    output_+=f"""b++;
window["ans"+b] = "{i.strip()}"; //Ans{cout}
window["noans1"+b] = "{produce(i)}";
window["noans2"+b] = "{produce(i)}";
window["noans3"+b] = "{produce(i)}";
window["noans4"+b] = "{produce(i)}";

"""
    cout+=1

f = open('actorOutput.txt', 'a')
f.write(output_)
f.close()