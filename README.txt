
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




--- düzen ---
vectorized_business

[[bussinessid _ , mutfak, bu restoronta verilen ortalama star, review_count, City]
[]
]

review 
[[userid, bussiness id , star]
[]
]


user
[[userid, review_count ,avragestar,  Catagorilere verilen avrage starlar arrayi ]
[]]


bu makalenin küçük bir özeti -> https://pdfs.semanticscholar.org/a7d2/5c03ec2a7dfe54c7b2e39729e906283e8e07.pdf

Burada öncelikle restaurant reviewlarını good ve bad ayırmak yerine direk ratingi tahmin etme çabasına girilmiş.
İlk denediği baseline approach çok basit Baseline 4.1 sectionında görebilirsiniz. Oradaki formül ile direk bir kullanıcının
tüm restoranlara verdiği average rating ve tüm restoranlara verilen average rating ve kullanıcının oy verdiği restoranın average
rating'ini birleştirip direk bunu geri beslemiş ve buradan hatasını hesaplamış. Bu approach ı bir deneyebiliriz.

2. approach ilginç bir yöntem. Bir üyenin bir restorana verdiği puanı tahmin etmek için önce tahmin edilmeye çalışan restorana
puan veren tüm üyelere bakılıyor ve KNN ile en yakın üye bulunuyor ve bu yöntemle tahmin edilmeye çalışıyor. Bu da pek iyi
bir yöntem sayılmaz. Bunun sonucu kötü çıkıyor hatta ilkinden de kötü çünkü matris çok sparse.



3. approach 2. olaydaki KNN'deki sparselık sorununu yiyecekleri kategorize ederek çözüyor. Bizim yaptığımız gibi manuel
kategorizasyon. Bu sefer bu şimdiye kadar ki en iyi sonucu veriyor.

4. approach da kategoriler altında yine kategori yapıyor ama değişik bir yöntem var garip. alt kategorilerde sadece casual romantic
ve trendy var. (Data'daki neye göre yapıyor bilmiyorum.)

En son SVD denilen bir yaklaşım kullanıyor ama sonucu çok kötü denemeye değmez.

Asıl önemli nokta -> Bir üyenin bir restorana verdiği rating i tahmin etmeye çalışırken KNN 'i bu üye ve bu restorana oy veren diğer üyelerden yapıyor.
Bizim gibi direk bütün üye listesinden KNN ile en yakını bulmuyor. Biz de böyle yaparak sonuçlarımızı test edebiliriz.



bu makalenin küçük bir özeti -> http://snap.stanford.edu/class/cs224w-2013/projects2013/cs224w-038-final.pdf