# Transforme qualquer página da Web em um e-book 
#
#pip --help # Ajuda
#pip3 list  #Lista Software instalados 
#pip3 install requests
#pip3 install BeautifulSoup4
#pip3 install epub
#pip3 install ebooklib
import requests
from bs4 import BeautifulSoup
from ebooklib import epub

def create_ebook(url, book_title):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    book = epub.EpubBook()
    book.set_title(book_title)
    
    chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml')
    chapter.content = soup.prettify()
    book.add_item(chapter)
    
    book.spine = ['nav', chapter]
    epub.write_epub(f'{book_title}.epub', book, {})

create_ebook('https://example.com/your-favorite-article', 'My eBook')