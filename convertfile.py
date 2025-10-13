import pandas as pd
import csv
import json
import yaml
import xml.etree.ElementTree as ET
import os

def csv_xls(csv_file, xls_file):
    df = pd.read_csv(csv_file)
    df.to_excel(xls_file, index=False)

def csv_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records', indent=2, force_ascii=False)

def csv_xml(csv_file, xml_file):
    df = pd.read_csv(csv_file)
    df.to_xml(xml_file, index=False)
    
def csv_yaml(csv_file, yaml_file):
    df = pd.read_csv(csv_file)
    df.to_yaml(yaml_file, index=False, allow_unicode=True)

def json_csv(json_file, csv_file):
    df = pd.read_json(json_file)
    df.to_csv(csv_file, index=False)
    
def json_xls(json_file, xls_file):
    df = pd.read_json(json_file)
    df.to_excel(xls_file, index=False)

def json_xml(json_file, xml_file):
    df = pd.read_json(json_file)
    df.to_xml(xml_file, index=False)

def json_yaml(json_file, yaml_file):
    df = pd.read_json(json_file)
    df.to_yaml(yaml_file, index=False, allow_unicode=True)

def xml_json(xml_file, json_file):
    df = pd.read_xml(xml_file)
    df.to_json(json_file, orient='records', indent=2, force_ascii=False)
    
def xls_csv(xls_file, csv_file):
    df = pd.read_excel(xls_file)
    df.to_csv(csv_file, index=False)


print('Bonjour')
while (True):
    print("1. Convertir un fichier CSV a un fichier XLSX")
    print("2. Convertir un fichier CSV a un fichier JSON")
    print("3. Convertir un fichier CSV a un fichier XML")
    print("4. Convertir un fichier CSV a un fichier YAML")
    print("5. Convertir un fichier Json a un fichier CSV")
    print("6. Convertir un fichier Json a un fichier XLSX")
    print("7. Convertir un fichier Json a un fichier XML")
    print("8. Convertir un fichier Json a un fichier YAML")
    print("9. Convertir un fichier XML a un fichier JSON")
    print("10. Convertir un fichier XLSX a un fichier CSV")
    choice = input("Choisissez une option (1-10) : ")
    
    if choice == '1':
        csv_file = input("Entrez le nom du fichier CSV source : ")
        if  os.path.exists(csv_file):
            xls_file = input("Entrez le nom du fichier XLSX de destination : ")
            csv_xls(csv_file, xls_file)
            print(f"Conversion de {csv_file} en {xls_file} terminée.")
        else:
            print(f"Le fichier {csv_file} n'existe pas.")
    elif choice == '2':
        csv_file = input("Entrez le nom du fichier CSV source : ")
        if  os.path.exists(csv_file):
            json_file = input("Entrez le nom du fichier JSON de destination : ")
            csv_json(csv_file, json_file)
            print(f"Conversion de {csv_file} en {json_file} terminée.")
        else:
            print(f"Le fichier {csv_file} n'existe pas.")
    elif choice == '3':
        csv_file = input("Entrez le nom du fichier CSV source : ")
        if  os.path.exists(csv_file):
            xml_file = input("Entrez le nom du fichier XML de destination : ")
            csv_xml(csv_file, xml_file)
            print(f"Conversion de {csv_file} en {xml_file} terminée.")
        else:
            print(f"Le fichier {csv_file} n'existe pas.")
    elif choice == '4':
        csv_file = input("Entrez le nom du fichier CSV source : ")
        if  os.path.exists(csv_file):
            yaml_file = input("Entrez le nom du fichier YAML de destination : ")
            csv_yaml(csv_file, yaml_file)
            print(f"Conversion de {csv_file} en {yaml_file} terminée.")
        else:
            print(f"Le fichier {csv_file} n'existe pas.")
    elif choice == '5':
        json_file = input("Entrez le nom du fichier JSON source : ")
        if  os.path.exists(json_file):
            csv_file = input("Entrez le nom du fichier CSV de destination : ")
            json_csv(json_file, csv_file)
            print(f"Conversion de {json_file} en {csv_file} terminée.")
        else:
            print(f"Le fichier {json_file} n'existe pas.")
    elif choice == '6':
        json_file = input("Entrez le nom du fichier JSON source : ")
        if  os.path.exists(json_file):
            xls_file = input("Entrez le nom du fichier XLSX de destination : ")
            json_xls(json_file, xls_file)
            print(f"Conversion de {json_file} en {xls_file} terminée.")
        else:
            print(f"Le fichier {json_file} n'existe pas.")
    elif choice == '7':
        json_file = input("Entrez le nom du fichier JSON source : ")
        if  os.path.exists(json_file):
            xml_file = input("Entrez le nom du fichier XML de destination : ")
            json_xml(json_file, xml_file)
        else:
            print(f"Le fichier {json_file} n'existe pas.")
    elif choice == '8':
        json_file = input("Entrez le nom du fichier JSON source : ")
        if  os.path.exists(json_file):
            yaml_file = input("Entrez le nom du fichier YAML de destination : ")
            json_yaml(json_file, yaml_file)
        else:
            print(f"Le fichier {json_file} n'existe pas.")
    elif choice == '9':
        xml_file = input("Entrez le nom du fichier XML source : ")
        if  os.path.exists(xml_file):
            json_file = input("Entrez le nom du fichier JSON de destination : ")
            xml_json(xml_file, json_file)
        else:
            print(f"Le fichier {xml_file} n'existe pas.")
    elif choice == '10':
        xls_file = input("Entrez le nom du fichier XLSX source : ")
        if  os.path.exists(xls_file):
            csv_file = input("Entrez le nom du fichier CSV de destination : ")
            xls_csv(xls_file, csv_file)
        else:
            print(f"Le fichier {xls_file} n'existe pas.")
    else:
        print("Option invalide. Veuillez choisir une option entre 1 et 10.")

    if input("Voulez-vous effectuer une autre conversion ? (o/n) : ") != 'o':
        break
    
#input("Voulez-vous continuer ? (o/n) : ") == 'o'