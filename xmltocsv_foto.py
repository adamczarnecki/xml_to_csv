# _*_ coding: utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xml.etree.ElementTree as ET
import csv
print "wczytuję plik XML"
# tree = ET.parse('PL_long_xml-foto.xml')
tree = ET.parse('test.xml')
print "Wczytano"
root1 = tree.getroot()
root = root1[0]
print "otwieram plik csv"
productData = open("feed_csv_PL_9-04.csv", "wb")

csvwriter = csv.writer(productData)
productHead = ['ID', 'Tytuł', 'Link do głównego zdjęcia', 'Reszta zdjęć']
csvwriter.writerow(productHead)

namespaces = {'g': 'http://base.google.com/ns/1.0'}

count = 0
prodCout = 0
prodCout1 = 0
for member in root.findall('item', namespaces):
    product = []

    ID = member.find('g:id', namespaces).text
    product.append(ID)
    Title = member.find('title').text
    product.append(Title)

    imageLink = member.find('g:image_link', namespaces).text
    product.append(imageLink)
    for foto in member.findall('g:additional_image_link', namespaces):
        extraImageLink = foto.text
        product.append(extraImageLink)

    csvwriter.writerow(product)
    prodCout = prodCout + 1
    if prodCout == 1000:
        prodCout1 = prodCout1 + 1
        print "Przepisano", prodCout1, "tysięcy produktów"
        prodCout = 0
print "zamykam plik csv"
productData.close()
