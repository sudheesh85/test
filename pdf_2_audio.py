import pyttsx3
import PyPDF2
book = open('/Users/sudheeshmadathil/Documents/SWAMI-VIVEKANANDA-COMPLETE-WORKS-Vol-9.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(20, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()