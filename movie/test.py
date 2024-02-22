strr = """ Vikram
 Ponniyin Selvan
 Thiruchitrambalam 
 Mudhal Nee Mudivum Nee
 Gargi
 Love Today 
 Beast
 Gatta Kusthi
 Saani Kaayidham
 Panni Kutty 
 Asuran 
 Vishwaroopam 
 Thuppakki
 Nanban 
 Ghilli
 muthu
 Ethir Neechal
 Irudhi Suttru
 Pichaikkaran 
 Anniyan 
 Papanasam
 Alaipayuthey 
 Dada
 Oh My Dog
 Maaran
 Soorarai Pottru 
 Jai Bhim
 Sillunu Oru Kaadhal
 Cobra 
 Thalapathi
 Raatchasan 
 Kaakkaa Muttai
 Karnan
 Varisu
 Sardar
 Sivappu Manjal Pachai
 Oh My Kadavule
 Teddy
 Darbar
 96
 Ghajini
 Thulladha Manamum Thullum
 Friends
 Jeans
 Boys 
 Kumki
 Viswasam
 Dasavathaaram
 Kaala
 Hey Sinamika
 Kaathuvaakula Rendu Kaadhal
 Nenjuku Needhi
 O2
 My Dear Bootham
 Prince
 Coffee with Kadhal
 Kadaisi Vivasayi
 Veetla Vishesham 
 Don
 D Block
 Enna Solla Pogirai
 Naai Sekar
 3 
 Namma Veettu Pilla
 Ponmagal 
 Raangi
 Sembi
 Dia
 Velaiyilla Pattathari 
 Bigil 
 I
 Santhosh Subramaniyam 
 OK Kanmani
 Thanga Magan 
 Mahanati 
 Sarpatta Parambarai 
 Master
 Annaatthe
 Doctor
 Maara
 Bhoomi
 Eeswaran
 Pulikkuthi Pandi
 Netrikann
 Bachelor
 Vaathi
 Kanaa 
 NGK
 Anegan
 Naanum Rowdy Thaan
 Aadukalam
 7 Aum Arivu
 Engeyum Kadhal
 Vaaranam Aayiram
 Kaakha Kaakha
 Unnai Ninaithu
 Minnale
 priyamanavale
 Punnagai Desam
 kushi
 Ayan
 M.Kumaran S/O Mahalakshmi
 Vaseegara
 arul
 Kutty
 Aanandham
 Parthiban Kanavu
 Devathayai Kanden
 kannathil Muthamittal
 Raam
 Sachin
 Sandakozhi
 Enthiran
 Maattrraan
 Iru Mugan
 Singam 3
 Kanchana 3
 Kaappaan
 Lingaa
 2.0
 Vikram Vedha
 Vada Chennai
 Aandavan Kattalai
 Madras
 Mayakkam Enna
 Nerkonda Paarvai
 Deiva Thirumagal
 Psycho
 Aayirathil Oruvan
 Paruthiveeran
 Petta
 Kabali
 Avvai Shanmughi
 Kaththi
 Varuthapadatha Valibar Sangam
 Kutty stroy
 Viduthalai Part 1
 The Great Indian Kitchen
 Kaithi
 Demonte Colony
 Yennai Arindhaal
 Baahubali
 Vedhalam
 Puli
 Maari
 Aambala
 Kakki Sattai
 Romeo Juliet
 Rajini Murugan
 Komban
 Nanbenda
 Oh My Penne
 Sulthan
 Enemy 
 Kaatru Veliyidai
 Kavan
 Velaikkaran
 Vivegam
 Aramm
 Meesaya Murukku
 Bairavaa
 Bogan
 Dora
 Sarkar
 Seemaraja
 Lakshmi
 Imaikkaa Nodigal
 Kaatrin Mozhi
 Sketch
 Tik Tik Tik
 Kalakalappu 2
 Airaa
 24
 Raja Rani
 Remo
 Aadhavan
 Irumbu Thirai
 Theeran Adhigaaram Onsru
 Ko
 Anjaan
 Neram
 Saamy 2
Thalaviva
Thozha
Comali
Jayam 
Unakkum Enakkum
Kathakali
Adithya Varma
Paayum Puli
Eega
Devi 2
Veeram
Vallaikaara Durai
Marudhu
Mass
Devarattam
Mersal
Kannum Kannum Kollaiyadithaal
Ispade Rajavum Idhaya Raniyumsss"""

splitted = strr.split('\n')
for i in splitted:
    print(f"""a++;window['q'+a] = "{i.strip()}";""")
