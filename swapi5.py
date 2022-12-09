import  requests


from  swapi2.swapi4 import produce_characters

start = 1
stop = 15

obj = produce_characters()
characters = []

for i in range(start,stop+1):
    characters.append(next(obj))

if __name__ == "__main__":

    print("Current module getting executed")

    home_url = "https://swapi.dev"
    relative = "/api/people/{0}"

    for num_ in characters:
        absolute_url = home_url + relative.format(num_)
        print(f"fatching details using - {absolute_url} =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        print(response)
        print("****" * 20 )