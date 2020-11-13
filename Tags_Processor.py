import pprint
from collections import Counter
import xlwt

__author__ = 'Abduljaleel Al Rubaye'


# The main function
if __name__ == "__main__":

    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet('Tags')

    repo_urls = open("JupyterNotebook.txt", 'r')
    repo_urls_read = repo_urls.read()
    rr = repo_urls_read.replace('\n', ',')
    rr2 = rr.replace('\r','')
    ru = rr2.split(',')
    repo_urls.close()
    tags = [i for i in ru if i]
    # print (tags)
    # print len(tags)

    c = Counter(tags).items()
    # print c[0][0]
    row = 0
    for t in range(0, len(c)-1):
        sheet1.write(row, 0, str(c[t][0]))
        sheet1.write(row, 1, str(c[t][1]))
        row += 1

    results.save("tags_jupyter.xls")



