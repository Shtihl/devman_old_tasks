import json
import sys


def load_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        pretty_print_json(load_json_data(filepath))
    else:
        print("Usage: python pprint_json.py path_to_json_file")
