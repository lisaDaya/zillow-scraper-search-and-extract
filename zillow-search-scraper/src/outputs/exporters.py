thonimport json
import os

def export_to_json(data):
    output_file = 'data/output.json'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Data exported to {output_file}")