import requests
from bs4 import BeautifulSoup
from datetime import datetime

day=datetime.now().day
month=datetime.now().month
year=datetime.now().year

url=f"https://www.yallakora.com/match-center/مركز-المباريات?date={day}/{month}/{year}#matchesclipNext"

page = requests.get(url)

def save_to_file(matches_details, filename="matches_details.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for match in matches_details:
            file.write(f"Tournament type: {match['Tournament type']}\n")
            file.write(f"Team A: {match['Team A']}\n")
            file.write(f"Team B: {match['Team B']}\n")
            file.write(f"Match Time: {match['Match Time']}\n")
            file.write(f"Match result: {match['Match result']}\n")
            file.write("-" * 40 + "\n")


def main(page):
    src=page.content
    soup = BeautifulSoup(src, "lxml")
    chompionShips_details=soup.find_all("div",{'class':'matchCard'})
    matches_details=[]

    def get_match_details(chompionShips_details):
        chompionShip_title=chompionShips_details.contents[1].find('h2').text.strip()
        chompionShip_teams=chompionShips_details.contents[3].find_all("div",{'class':'liItem'})

        for i in range(len(chompionShip_teams)):
            teamA=chompionShip_teams[i].find("div",{'class':'teamA'}).find('p').text.strip()
            teamB=chompionShip_teams[i].find("div",{'class':'teamB'}).find('p').text.strip()
            Match_Resultat=chompionShip_teams[i].find('div',{'class':'MResult'}).find_all('span')
            goalsA = "0" if Match_Resultat[0].text.strip() == "-" else Match_Resultat[0].text.strip()
            goalsB = "0" if Match_Resultat[2].text.strip() == "-" else Match_Resultat[2].text.strip()
            goals = f"{goalsA} - {goalsB}"
            match_time=Match_Resultat[3].text.strip()
            matches_details.append({
                                'Tournament type':chompionShip_title,
                                'Team A':teamA,
                                'Team B':teamB,
                                'Match Time':match_time,
                                'Match result':goals,
                                  })
        
    for i in range (len(chompionShips_details)):
        get_match_details(chompionShips_details[i])

    # for match in matches_details :
    #     print(match)

    save_to_file(matches_details)
    print("Match details saved to matches_details.txt")


main(page)  