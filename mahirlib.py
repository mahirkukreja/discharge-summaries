def convert(fname, pages=None):
    from cStringIO import StringIO
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
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


def download_file(download_url):
            import urllib2
            response = urllib2.urlopen(download_url)
            if download_url.endswith('.pdf'):
                file = open("document.pdf", 'wb')
                file.write(response.read())
                file.close()
            else: 
                file = open("document.txt", 'wb')
                file.write(response.read())
                file.close()