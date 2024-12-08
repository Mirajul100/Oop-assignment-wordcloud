from wordcloud import WordCloud , STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = """
HOSSAIN ISLAM SULTANA KHAN HASAN ANIK REZAUL TABASSUM SABIKUN NAHAR
MOTIUR ALAM MAHMUD SUMAIYA ARIFUL SHARIFA NAJM TAHMID AKIB RAHMAN WASIF
SARMIN ANIK SRABON ALVI MASUM SUMON ARIFUL DIPTO RAHUL CHANDRA SAHIL
ALOM ALIN SALIN ANIK ALO KALU ASA JOY MIM KIM SIM JAK PAK DAK SIR SUN 
PUN MOOM SANI NAFA SAFA RABBI SHAOW TASIN MAHAFUZ TUHIN TAMIM JAHID 
TOMA ISRAT IMO LIKE RAKIB ROKI RAZIB RAJUL SAJU SOJOL NUPUR NUR RANI
OPU PIAL SAMI ALOM ASIF TOMAL KAMAL KORIM SOFIK LIALA LIA LIMA LISA MITHU 
tasin arif ifti mridul mahe mahim sani ismail samanta suba siam 
"""
python_mask = np.array(PIL.Image.open("Anik.png"))

wc = WordCloud(stopwords=STOPWORDS,
                mask=python_mask,
                background_color="black").generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()
