import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def serialize_animal(animal):
    """Convert an animal object into an HTML list item."""
    output = ""
    name = animal.get("name")

    if not name:
        return

    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])
    output += '<li class="cards__item">\n'

    output += f'<div class ="card__title" >{name}</div>\n'
    output += '<p class="card__text">\n'
    if "diet" in characteristics:
        output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"

    if locations:
        output += f"<strong>Location:</strong> {locations[0]}<br/>\n"

    if "type" in characteristics:
        output += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"

    output += '</li>'
    output += "\n"

    return output



def get_animals_info(animals_data):
    """Return combined HTML string for all animals."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output

def load_html_template(file_path):
    with open(file_path, "r", encoding="utf-8") as fileobj:
        return fileobj.read()

def write_html_template(data, file_path):
    with open(file_path, "w", encoding="utf-8") as fileobj:
        fileobj.write(data)


def main():
    animals_data = load_data('animals_data.json')
    animals_info = get_animals_info(animals_data)
    html_template = load_html_template('animals_template.html')
    html_new_template = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    write_html_template(html_new_template, "animals.html")


if __name__ == "__main__":
    main()
