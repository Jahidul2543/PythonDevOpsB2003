import logging
from self import self
import json


logging.basicConfig(filename='log/log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

# logging.info("Running Urban Planning")

self.logger = logging.getLogger('urbanGUI')


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "age": 4,
        "hobby": ("Cricket", "Football", "Cycling")

    }
}


def logging_demo():
    logging.info("Let's log in a file")


"""
Write JSON to file
Serialization
JSON Module Demo

Python	            JSON

dict	            object
list, tuple	        array
str	                string
int, long, float	number
True	            true
False	            false
None	            null

"""
def write_to_file():
    print("Data type of data object: {}".format(type(data)))
    with open("data/data_file.json", "w") as write_file:
        json.dump(data, write_file)
    print(json.dumps(data, indent=5))

"""
Deserializing JSON
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""


def read_from_file():
    logging.info("Read a JSON a file")
    with open("data/data_file.json", "r") as read_file:
        file_data = json.load(read_file)
        print('data type: {}'.format(type(file_data)))

    json_as_string = """
    {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian", "age": 4, "hobby": ["Cricket", "Football", "Cycling"]}}
    """
    print(type(json_as_string))
    print(json.loads(json_as_string))


if __name__ == '__main__':
    read_from_file()