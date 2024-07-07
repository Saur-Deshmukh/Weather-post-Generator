import requests
import json
from PIL import Image, ImageFont, ImageDraw
import datetime

my_image = Image.open("post.png")
font = ImageFont.truetype('Inter-Medium.ttf', 50)
content = "Latest Weather Forcast"
draw = ImageDraw.Draw(my_image)
color = 'rgb(255,255,255)'
draw.text((258, 50), content, color, font=font)


font = ImageFont.truetype('Inter-Medium.ttf', 25)
content = "Date:   "+datetime.date.today().strftime("%A, %d %B, %Y")
color = 'rgb(255,255,255)'
draw.text((50, 150), content, color, font=font)


font = ImageFont.truetype('Inter-Medium.ttf', 25)
content = "Time:   "+datetime.datetime.now().strftime("%I:%M %p")
color = 'rgb(255,255,255)'
draw.text((820, 150), content, color, font=font)
my_image.save("weather_post.png")


api_key = "your_openweathermap_api_key" #Enter your api key here.
india = ["Mumbai", "Delhi", "Jaipur", "Nagpur", "Hyderabad"]
uk = ["London", "Manchester", "Glasgow", "Belfast", "Birmingham"]
japan = ["Tokyo", "Kyoto", "Nagasaki", "Hiroshima", "Osaka"]
countries = [india, uk, japan]
country_name = ["India", "UK", "Japan"]
index = 0
base = Image.open("weather_post.png")
for country in countries:
    cities = country
    cities_height = {cities[0]: 300, cities[1]: 428, cities[2]: 556, cities[3]: 690, cities[4]: 824}
    copy_ = base.copy()
    draw = ImageDraw.Draw(copy_)
    content = "Country:   " + country_name[index]
    font = ImageFont.truetype('Inter-Medium.ttf', 25)
    draw.text((490, 150), content, color, font=font)
    for city in cities:
        geocoder = requests.get("http://api.openweathermap.org/geo/1.0/direct?q="+city+"&limit=5&appid="+api_key)
        geocode = json.loads(geocoder.content)
        api_req = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(geocode[0]["lat"])+"&lon="+str(geocode[0]["lon"])+"&appid=18bb461ee1bd4f7533824dd2d1b46662&units=metric")
        api = json.loads(api_req.content)

        name = city
        temp = str(api["main"]["temp"])+"\u00b0"
        humidity = str(api["main"]["humidity"])+"%"
        font = ImageFont.truetype('Inter-Medium.ttf', 50)
        color = 'rgb(0,0,0)'
        draw.text((135, cities_height[city]), name, color, font=font)
        color = 'rgb(255,255,255)'
        draw.text((600, cities_height[city]), temp, color, font=font)
        draw.text((805, cities_height[city]), humidity, color, font=font)

    copy_.save(country_name[index]+"_"+str(datetime.date.today())+"_post.png")
    copy_pdf = copy_.convert('RGB')
    copy_pdf.save(country_name[index] + "_" + str(datetime.date.today()) + "_post.pdf")
    index += 1
