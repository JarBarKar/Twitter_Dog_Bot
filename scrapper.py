import requests, os
from bs4 import BeautifulSoup as soup

# request data from Pixel
res = requests.get('https://www.pexels.com/search/dog/')

# Turn object into BeautifulSoup
dog_soup = soup(res.text, 'html.parser')

# Find main container
containers = dog_soup.findAll('a',{'class':'js-photo-link photo-item__link'})

# If folder is not created, create a folder to store pictures
if not os.path.exists('doggo'):
    os.makedirs('doggo')

# Change directory to the new folder
os.chdir('doggo')

index = 0

# Loop through every container and parse the source URL. Download the pictures into the new folder
for image in containers:
    try:
        url = image.img['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('doggo-'+str(index) + '.jpg' , 'wb') as output:
                output.write(source.content)
                index += 1
    except:
        pass
