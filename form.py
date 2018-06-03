from model import Client
import alg
import sys

def send(text):
    (phones, info) = alg.parse(line)
    phones = set(phones)
    clients = Client.select_by_phone(list(phones))
    for client in clients:
        client.dump()
    
    insert_objs = []
    for phone in phones:
        insert_objs.append(Client(phone, info))
    success = Client.insert(insert_objs)

    if success:
        print('New info saved')

    

try:
    Client.create_table()
    print('create_table')
except Exception as e:
    print(e)

fh = open('input.txt')
for line in fh:
    send(line)


