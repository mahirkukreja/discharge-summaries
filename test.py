from flask import Flask,render_template,request,jsonify
import urllib2
import pickle
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import pandas as pd
import re
import os
import time
import sys
import re
from mahirlib import *
app = Flask(__name__)

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 
@app.route('/')
def hello_world():
    return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        res=request.json
        result1 =res['LINK']
        start = time.time()
        download_file(result1)    
        c=0
        lss=[]
        dataprep=[]
        if __name__ == '__main__':
            path = sys.argv[0]
        fnamee=[]
        dir = os.listdir('/home/rajesh/pdf parsing/parsing44k/')
        for fname in dir:
            if fname.endswith('document.pdf') :
                fnamee.append(fname)
                text=convert('/home/rajesh/pdf parsing/parsing44k/'+str(fname)) 
                text=text.lower()
                text=text.replace('\n','')
                text=text.replace('\s','')
                text=text.replace('\w','')
                text=text.replace('\t','')
                text=text.replace('\r','')
                text=text.replace('\xc2','')
                text=text.replace('\xa0','')
                os.remove(fname)
            elif fname.endswith('document.txt'):
                fnamee=str('')
                fnamee=fnamee+str(fname)
                F = open('document.txt','r') 
                text=F.read().lower()
                os.remove(fname)
            else:
                continue
            j=(text).find('blood pressure')
            k=(text).find('weight')
            l=(text).find('bmi')
            text_a=text[j:]
            text_b=text[k:]
            text_c=text[l:]
            x=re.search(r'\s(\w+\d+/\d+)',(str(text_a)))
            y=re.search(r'\d+',(str(text_b)))
            z=re.search(r"\d*\.\d+|\d+",(str(text_c)))
            if x==None:
                x='None'
            else:
                x=x.group()
            if y==None:
                y='None'
            else:
                y=y.group() 
            if z==None:
                z='None'
            else:
                z=z.group() 
            aa=dict()
            aa['BP']=x
            aa['Weight']=y
            aa['BMI']=z        
            result = request.form
            return jsonify({"FileName":fnamee,"params":aa})
if __name__ == '__main__':
    app.run(host='0.0.0.0')    
    