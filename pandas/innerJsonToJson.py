import json

# Complex JSON data
complex_json = '''
{
  "firstName": "John",
  "lastName": "Doe",
  "age": 30,
  "address": {
    "streetAddress": "123 Main St",
    "city": "New York",
    "state": "NY",
    "postalCode": "10001"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212-555-1234"
    },
    {
      "type": "fax",
      "number": "646-555-4567"
    }
  ],
  "children": [
    {
      "firstName": "Jane",
      "age": 5
    },
    {
      "firstName": "Bob",
      "age": 8
    }
  ],
  "spouse": {
    "firstName": "Jane",
    "lastName": "Doe"
  }
}
'''

parsed_json = json.loads(complex_json)

def flatten_json(nested_json, prefix=''):
    flattened_dict = {}
    for key, value in nested_json.items():
        if isinstance(value, dict):
            flattened_dict.update(flatten_json(value, prefix + key + '_')) # For Json {}
        elif isinstance(value, list):
            for i in range(len(value)):
                flattened_dict.update(flatten_json(value[i], prefix + key + '_' + str(i) + '_')) # For Lists []
        else:
            flattened_dict[prefix + key] = value
    return flattened_dict

flattened_json = flatten_json(parsed_json)

simplified_flat_json = json.dumps(flattened_json, indent=2)

print(simplified_flat_json)