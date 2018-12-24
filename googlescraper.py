#!/usr/bin/env python3
# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
Authortitles= ""
Professors= {}
start = 10;
import csv

def articleRemoval(raw_data):
  noArticle= re.sub('(\s+)(a|an|and|the)(\s+)', '\1\3', raw_data)
  noNumbers = re.sub('(\d)', '', noArticle)
  return(noArticle)


def updatePage(data,start):
    return "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:physics&after_author="+data+"&astart="+str(start+10)


for x in range(1,100):
    if(x == 1):
        quote_page = 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label%3Aphysics'
        page = urllib2.urlopen(quote_page)

    else:
        page = urllib2.urlopen(updatePage(data,start))
    soup = BeautifulSoup(page, 'html.parser')

    name = soup.find_all('h3', class_= 'gsc_oai_name')
    afterauthor = soup.find('button', class_= 'gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx')['onclick']
    data_raw= afterauthor.split("after_author\\")[1]
    data=data_raw.split("\\")[0][3:]
    for x in name:
        titles= ""
        innerLink = "https://scholar.google.com" + x.a['href']
        nameL = x.a.text

        Innerpage =urllib2.urlopen(innerLink)
        soup = BeautifulSoup(Innerpage, 'html.parser')

        titles_raw = soup.find_all("tr",class_="gsc_a_tr")
        if(len(titles_raw)!=0):
            print("Name of professor-------------------",nameL)
            Authortitles = ""
            for y in titles_raw:
                Authortitles = str(Authortitles+ articleRemoval(y.a.text))

                print(Authortitles)

            with open('AuthorData.csv','a') as newFile:
                newFileWriter = csv.writer(newFile)
                newFileWriter.writerow([nameL,Authortitles])
