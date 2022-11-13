import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../OriginalData/0_DOLNOSLASKIE.csv")

def bins_labels(bins,**kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins)+bin_w/2+0.001, bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

days_after_purchase = df[["Dni od zakupu"]]
days_after_purchase.to_csv("../AnalysisData/dni_od_zakupu.csv")

bins = np.arange(0,20,1)
ax = days_after_purchase.plot(kind="hist",bins = bins, figsize = (15,8), legend = False, fontsize = 12, ec = "black")
ax.set_ylabel("Liczba kupionych produktów", fontsize = 15)
ax.set_xlabel("Liczba dni, po których wystawiono ocenę",fontsize=15)
ax.set_title("Liczba dni od wystawienia oceny produktu",fontsize=20)
bins_labels(bins)
fig = ax.get_figure()
fig.savefig("../Documents/dni_od_zakupu.jpg")

brand_purchases = df[["Marka","Wiek kupującego"]]
brand_purchases = brand_purchases.groupby("Marka").count()
brand_purchases.to_csv("../AnalysisData/marka.csv")

ax = brand_purchases.plot(kind= "bar", figsize = (15,8),fontsize = 12, rot = 0, legend = False, ec= 'black')
ax.set_ylabel("Ilość sprzedanych produktów",fontsize = 15)
ax.set_xlabel("Marka odkurzacza",fontsize = 15)
for bar in ax.patches:
    ax.annotate(format(bar.get_height(), 'd'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')
ax.set_title("Sprzedaż każdej z marek odkurzaczy", fontsize = 20)
fig = ax.get_figure()
fig.savefig("../Documents/marka.jpg")

customer_age = df[["Wiek kupującego"]]
customer_age.to_csv("../AnalysisData/wiek.csv")

bins = np.arange(15,80,5)
ax = customer_age.plot(kind= "hist", figsize = (15,8),fontsize = 12, rot = 0, legend = False,
                        bins = bins, ec='black')
ax.set_title("Wiek kupującego",fontsize = 20)
ax.set_xlabel("Przedział wiekowy",fontsize = 15)
ax.set_ylabel("Ilość konsumentów",fontsize = 15)
bins_labels(bins)
fig = ax.get_figure()
fig.savefig("../Documents/wiek.jpg")

gender_count = df[["Płeć kupującego","Unnamed: 0"]]
gender_count = gender_count.groupby("Płeć kupującego").count()
gender_count.to_csv("../AnalysisData/płeć.csv")

ax = gender_count.plot(kind= "bar", figsize = (15,8),fontsize = 12, rot = 0, legend = False,ec="black")
ax.set_ylabel("Ilość zakupionych odkurzaczy",fontsize = 15)
ax.set_xlabel("Płeć konsumenta",fontsize = 15)
for bar in ax.patches:
    ax.annotate(format(bar.get_height(), 'd'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')
ax.set_title("Ilość zakupionych produktów ze względu na płeć", fontsize = 20)
fig = ax.get_figure()
fig.savefig("../Documents/płeć.jpg")

rates = df[["Ocena"]]
rates.to_csv("../AnalysisData/ocena.csv")

bins = np.arange(0,6,0.5)
ax = rates.plot(kind= "hist", figsize = (15,8),fontsize = 12, rot = 0, legend = False,
                        bins = bins, ec='black')
ax.set_title("Ocena produktów",fontsize = 20)
ax.set_xlabel("Ocena",fontsize = 15)
ax.set_ylabel("Ilość wystawionych ocen",fontsize = 15)
bins_labels(bins)
fig = ax.get_figure()
fig.savefig("../Documents/ocena.jpg")