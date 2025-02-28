import PyPDF2 as pd

#taking the names of the pdf files in the list 
pdfiles=[]
merger=pd.PdfFileMerger()

n=int(input('enter the number of files you wish to merge: '))
for i in range(n):
    a=input('enter the name of the file')
    pdfiles.append(a)

for file in pdfiles:
    pdfiles=open(file,'rb')
    pdfreader=pd.PdfReader(pdfiles)
    merger.append(pdfreader)
pdfiles.close()
merger.write('merged.pdf')