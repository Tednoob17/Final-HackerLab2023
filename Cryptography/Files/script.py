from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode,b64encode
import sys
FLAG = 'redacted'
def handle():
    print('Welcome rookie! Here I\'m able to encrypt what you want with AES in CBC mode.\nDon\'t try to Enter in Admin room if you aint.\nLet\'s go!!!')
    welcome = """
    Choose what you want to do dude!!!
    [1] Encrypt your message
    [2] Decrypt your message
    [3] Set yout encrypted Key
    [4] Admin Panel
    [5] Exit
    """
    message = ''
    key = ''
    iv = get_random_bytes(16)
    cipher = ''
    while True:
        print(welcome)
        choice = input('$> ')
        if choice not in list('12345'):
            print('Plz redo your choice, seems not undestanble')
        else:
            choice = int(choice)
            if choice == 1:
                t_message = input('Pleazure to encrypt what ever you want. Just tell me :')
                if not len(t_message):
                    print('You enter empty message. Plz try again!!!')
                    message = ''
                else:
                    message = t_message
                    if not len(key):
                        print('You not yet set your key')
                    else:
                        cipher = AES.new(key,AES.MODE_CBC,iv)
                        enc_message = b64encode(cipher.encrypt(pad(message.encode(),AES.block_size)))
                        print('Save your message :',enc_message.decode())
            elif choice == 2:
                if not len(message):
                    print('Message field empty')
                else:
                    print('Oh you already know your message. It\'s :',message)
            elif choice == 3:
                t_key = input('Plz enter your key in base64: ')
                try:
                    t_key = b64decode(t_key)
                    if len(t_key)!=32:
                        print('Invalid Key length(32 need) :',len(t_key))
                        key = ''
                    else:
                        key = t_key
                        print('Save your key')
                except:
                    print('Your base64 key aint valid')
                    key = ''
            elif choice == 4:
                t_iv = input('Enter the iv in base64 to Enter Admin :')
                try:
                    t_t_iv = b64decode(t_iv)
                    if t_t_iv == iv:
                        print('Hi Admin, your flag :', FLAG)
                        break
                except Exception as e:
                    print('Error while decoding your iv, You aint Admin!!!')
            elif choice == 5:
                print('Byeebyebye Rookie')
                break
if __name__ == '__main__':
    handle()