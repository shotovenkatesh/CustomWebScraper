from bs4 import BeautifulSoup
import requests




# headers = {"User-agent":
#            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
response = requests.get(url= "https://animeschedule.net/?year=2022&week=33",)
anime_data = response.text
weeks = ["Sunday","Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday"]

soup = BeautifulSoup(anime_data,"html.parser")

#sunday data

for week in weeks:
    titles_data = soup.select(selector= f".{week} .show-link .show-title-bar")
    titles = [title.getText() for title in titles_data]
    print(titles)
    # print(len(titles))

    #episode nos
    episode_no_data = soup.select(selector= f".{week} .show-episode")
    episode_no = [epi.getText() for epi in episode_no_data]
    episode_no = [s.replace("Ep\n","") for s in episode_no]
    episode_no = [s.replace("\n","") for s in episode_no]
    print(episode_no)
    # print(len(episode_no))

    #AIR Time
    time_data = soup.select(selector=f".{week} .show-air-time")
    show_time = [t.getText() for t in time_data]
    show_time = [s.replace("\n","") for s in show_time]
    show_time = [s.replace("\n","") for s in show_time]
    print(show_time)
    # print(len(show_time))

    #Watch links
    site_link = "https://animeschedule.net/"
    link_data = soup.select(selector=f".{week} .show-link")
    links = [site_link+a['href'] for a in link_data]
    print(links)
    # print(len(links))







