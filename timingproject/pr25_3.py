#from pprint import pprint
import requests

from timingproject.pr25_2 import swap_2

#from pprint import pprint

from timingproject.tim_ import timeit


@timeit
def get_all_vehicle_names(result: dict)  "List":
    char_urls = result.get("characters")
    char_data = pr25_2(char_urls) if char_urls else []  # ternary operator
    char_names = [char.get("name") for char in char_data if char_data]
    return char_names


@timeit
def get_all_vehicle_names(result: Dict) -> List:
    """
    pick all vehicle names
    :param result: data from first film
    :return: names of vehicles
    """

    v_urls = result.get("vehicles")
    v_data = swap_2(v_urls) if v_urls else []
    v_names = [vehicle.get("name") for vehicle in v_data if v_data]
    return v_names


if __name__ == "__main__":
    url = "https://swapi.dev/api/films/1/"
    response = requests.request("GET", url)
    # response = requests.get(url)
    result = response.json()

    char_names = get_all_character_names(result)
    v_names = get_all_vehicle_names(result)

    print(char_names)
    print("**"*20)
    #pprint(v_names)