
EKLEMEK İSTEDİĞİNİZ ŞEYLERİ BURAYA YAZIN. Kodda yaptığınız değişiklikleri comment'te ve burada document edin.

Google'ın hali hazırda pretrained word2vec vocabulary'sini buldum bunu kullanabiliriz.
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

Olmadı KOÇ'un da var bi tane wall street journal'den üretmişler. -> https://github.com/ai-ku/wvec

Google word2vec modeli hakkında güzel bi yazı -> http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/

Aşamalar:

1.)Google word2vec vocabulary ile bir matrix oluştur.
2.)Matrix'i K-Means Clustering'e sok.


Sıkıntılar:

1.) Google'ın verdiği vector 3.5 GB ve benim RAM'ım almayacak sanırım.

2.) KESİNLİKLE 64 BIT PYTHON KULLANMALISINIZ.




KODDA YAPTIKLARIMIZ :
A) Dataset manupulation :
1 : word2vec ile, catogorileri clusterlamaya çaliştik , ancak, datasette restorant dışında diğer kuruluşların varlığı , mutfak isimlerinin millet isimleri ile 
aynu olması nedeniyle ve word2vec'in kelimeleri cümledeki kullanım yerlerine bakarak sınıflandirmasi nedeni ile, düzgün bir catogorileştirme yapamadi. 

diğer kuruluşları elemek için restorant kategorisine sahip olamayan kuruluşları datasetten çikardik, ancak word2vecin mutfak ismi sorununa manuel clustrlaştirma
dişinda bir çözüm düşünemedik.

örneğin:


2: Önce mutfak isimlerine göre manuel clusterlaştirdik.:
[asdasd,asdasdas , other]

daha sonra bu manuel clusterlarida kendi içlerinde henüz bakmadiğimiz kategorilere bakarak word2vec ile clusterlaştirdik.

--ŞEKIL--




