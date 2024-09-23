import base64

# WARNING: This is a secret key. Do not expose it.
srt_key = 'secretkey'  # TODO: change the placeholder

def encode_input(usr_input):
    if len(usr_input) <= 1:
        raise ValueError("PT must be greater than 1")
    if len(usr_input) % 2 != 0:
        raise ValueError("PT can only be an even number")
    if not usr_input.isalnum():
        raise ValueError("Only alphabets and numbers supported")

    rsv_input = usr_input[::-1]
    output_arr = []
    for i in range(int(len(usr_input) / 2)):
        c1 = ord(usr_input[i])
        c2 = ord(rsv_input[i])
        enc_p1 = chr(c1 ^ ord(srt_key[i % len(srt_key)]))
        enc_p2 = chr(c2 ^ ord(srt_key[i % len(srt_key)]))
        output_arr.append(enc_p1)
        output_arr.append(enc_p2)

    encoded_val = ''.join(output_arr)
    b64_enc_val = base64.b64encode(encoded_val.encode())
    return b64_enc_val.decode()

def decode_input(encoded_val):
    decoded_bytes = base64.b64decode(encoded_val)
    decoded_str = decoded_bytes.decode()
    output_arr = []
    
    for i in range(0, len(decoded_str), 2):
        enc_p1 = decoded_str[i]
        enc_p2 = decoded_str[i + 1]
        dec_c1 = chr(ord(enc_p1) ^ ord(srt_key[i // 2 % len(srt_key)]))
        dec_c2 = chr(ord(enc_p2) ^ ord(srt_key[i // 2 % len(srt_key)]))
        output_arr.append(dec_c1)
        output_arr.append(dec_c2)

    original_reversed = ''.join(output_arr)
    return original_reversed[::-1]

# Example usage
action = input("Choose action (encode/decode): ").strip().lower()
if action == "encode":
    usr_input = input("Enter the string to encode: ")
    result = encode_input(usr_input)
    print("Encoded Cipher Text:", result)
elif action == "decode":
    encoded_val = input("Enter the encoded cipher text: ")
    try:
        result = decode_input(encoded_val)
        print("Decoded Original Input:", result)
    except Exception as e:
        print("Error during decoding:", e)
else:
    print("Invalid action. Please choose 'encode' or 'decode'.")
