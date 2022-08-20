from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes")

endereco = input("Digite um endereco com numero e cidade. "
                 "Exemplo: avenida paulista, 100 Sao Paulo: ")

resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0] != 'None':
    print("Endereco completo.: ", resultado)
    print("Bairro............: ", resultado[1])
    print("Cidade............: ", resultado[2])
    print("Regiao............: ", resultado[3])
