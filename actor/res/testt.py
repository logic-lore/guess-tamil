_x = """ Vijay
 Rajinikanth
 Ajith
 Kamal Haasan
 Surya
 Dhanush
 Vikram
 Karthi
 Prakash Raj
 Ashwin Kumar Lakshmi Kanthan
 Siva Karthikeyan
 Jayam Ravi
 Dhruv Vikram
 Arjun Das
 Vijay Sethupathi
 R. Sarathkumar
 Madhavan
 Arvind Swami
 Sathyaraj
 Jiiva
 Arun Vijay
 Vishal
 Arya
 Jai Sampa th
 Atharvaa Murali
 Bobby Simha
 Vijay Antony
 Vishnu Vishal
 Simbu
 Siddharth
 Vimal
 Arjun Sarja
 Vikranth
 Harish Kalyan
 Bharath
 Sibi Sathyaraj
 Gautam Karthik
 Sundeep Kishan
 Ganesh Venkatraman
 Ashok Selvan 
 Santhanam
 Udhayanidhi Stalin
 RJ Balaji 
 Shiva
 Mahat Raghavendra
 Teejay Arunasalam
 S J Surya
 Hiphop Tamizha 
 G V Prakash
 Krishna
 Srikanth
 Kavin
 Pradeep Ranganathan
 Yogi Babu
 Vadivelu
 Soori
 Goundamani
 Manobala
 Senthil
 Vikram Prabhu
 Prasanna
 Vivek
 Abbas
 Prashanth
 Nassar
 Raju Sundaram
 Manivannan
 Ramesh Khanna
 Thalaivivasal Vijay
 Sunder Rajan
 Charle
 Singamuthu
 Pandu
 Delhi Ganesh
 Kishen Das
 Aajeedh Khlique
 VTV Ganesh
 John Vijay
 Sathish
 Sriman
 Shaam
 Karunas
 Sampath Raj
 Vivek Prasanna
 Kaali Venkat
 Adithya Bhaskar
 Rajkiran
 R Parthiban
 Samuthirakani
 Vijayakanth
 R K Suresh
 Amitash Pradhan
 Vidharth
 Aarar
 Bharani
 Shakthi
 Vaiyapuri
 Ganja Karuppu
 Sudeep
 Thambi Ramaiah 
 Vijaykumar
 Aadukalam Naren
 Prabhu Deva
 Robo Shankar
 Sathyan
 S P Balasubrahmanyam
 Ramji
 Daniel Balaji
 Atlee Kumar
 Jackie Shroff
 Kathir
 Bharathiraja
 Munishkanth
 Hrishikesh
 Cell Murugan
 M Sasikumar
 Sananth 
 Natarajan Subramaniam
 Vela Ramamoorthy
 Pakoda Pandi
 Ajmal Ameer
 Saran Shakthi
 Raghava Lawrence
 Mayilsamy
 Rajendran
 Jagan
 Pugazh
 Sha Ra
 Gautham Vasedev Menon
 K Bhagyaraj
 Aravind Akash
 Subbaraju
 Bala Saravanan
 Dheena
 Radha Ravi
 Singapuli
 S J Surya
 Vinay Rai
 Redin Kingsley
 Vaibhav Reddy
 Kishore
 Ashwin Kakunmanu
 Ashish Vidyarthi
 Varun   
 Jaya Prakash
 Suman 
 Imman Annachi
 Crane Manohar
 Joe Malloori
 Thakur Anoop Singh 
 Chaams
 Narain
 Karunakaran
 Krishnakumar Balasubramanian
 Powerstar Srinivasan"""

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
    output_+=f"""a++;
window["ans"+a] = "{i.strip()}"; //Ans{cout}
window["noans1"+a] = "{produce(i)}";
window["noans2"+a] = "{produce(i)}";
window["noans3"+a] = "{produce(i)}";
window["noans4"+a] = "{produce(i)}";

"""
    cout+=1

f = open('actorOutput.txt', 'a')
f.write(output_)
f.close()