# --- Task ---


Le test consiste à :


    Créer un script python qui va chercher le titre principal (la balise <h1>) d'une page web (l'URL sera donnée en paramètre d'URL).
    Retourner ce titre dans un format JSON (avec une clé "title").
    Ensuite, tu devras déployer ce script en tant que Google Cloud Function (via google cloud platform--> Il y a un free tier, donc c'est gratuit). 

Pour finir, tu nous envoies le lien de la fonction déployée pour qu'on puisse tester ton code en live.
Ton lien devrait ressemble à ceci: https://aaa.abc.com/?url=https://semactic.com/en/

Quelques conseils :

    Garde ton code clair et efficace.
    Pense à bien structurer ton projet, surtout pour le cloud.
    Et surtout, évite de trop t’inspirer des solutions toutes faites. Le but, c’est de voir ta manière de réfléchir et de coder.




# --- How I did it ---


- Created folder and python file
- How to get HTML data from an URL (requests)
- How to get the specific h1 tag from this data (BeautifulSoup)
- Return this as JSON
- Setup Google Cloud Platform for Google Cloud Functions
- Installed Google Cloud SDK and deployed my project from my wsl terminal
- Testing -> Error : Code wasn't compatible with Google Cloud Functions
- Fixed code  (HTTP Request)
- Redeployed



# --- How to use it ---


Go to : 

https://europe-west1-red-carver-435808-q5.cloudfunctions.net/get_title?url=WEBSITE_URL


And replace the "WEBSITE_URL" by the website url you want to get the h1 tag content from.

Example : 


https://europe-west1-red-carver-435808-q5.cloudfunctions.net/get_title?url=https://jenson.org/
