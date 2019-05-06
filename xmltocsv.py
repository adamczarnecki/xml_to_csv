# _*_ coding: utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xml.etree.ElementTree as ET
import csv
print "wczytuję plik XML"
tree = ET.parse('PL_long_xml_9-04.xml')
print "Wczytano"
root1 = tree.getroot()
root = root1[0]
print "otwieram plik csv"
productData = open("feed_csv_PL_9-04.csv", "wb")

csvwriter = csv.writer(productData)
productHead = ['ID', 'Tytuł', 'Kategoria', 'Grupa', 'Marka', 'GTIN',
               'Link do zdęcia', 'Link do produktu', 'Google Product Category']
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
    Category = member.find('g:product_type', namespaces).text
    product.append(Category)
    Group = member.find('g:item_group_id', namespaces).text
    product.append(Group)
    Brand = member.find('g:brand', namespaces).text
    product.append(Brand)
    GTIN = member.find('gtin').text
    product.append(GTIN)
    imageLink = member.find('g:image_link', namespaces).text
    product.append(imageLink)
    Link = member.find('link').text
    product.append(Link)
    # google_product_category = member.find('g:google_product_category', namespaces).text
    # product.append(google_product_category)
    csvwriter.writerow(product)
    prodCout = prodCout + 1
    if prodCout == 1000:
        prodCout1 = prodCout1 + 1
        print "Przepisano", prodCout1, "tysięcy produktów"
        prodCout = 0
print "zamykam plik csv"
productData.close()
