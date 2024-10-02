from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker(locale="fr_FR")


# Créer une instance de Faker pour les noms français
fake = Faker('fr_FR')

def generate_kilom(num_km):
    max_mileage = []
    for _ in range(num_km):
        category = random.choice(["courte distance", "moyenne distance", "longue distance"])

        if category == "courte distance":
            max_mileage.append(random.randint(50, 100))
        elif category == "moyenne distance":
            max_mileage.append(random.randint(100, 300))
        elif category == "longue distance":
            max_mileage.append(random.randint(300, 600))
        else:
             max_mileage.append(random.randint(600, 1200))
    
    return max_mileage

generated_km = generate_kilom(700)




#Fonction pour générer des temps de réservation à l'avance en jours
def generate_random_days_reservation_before(num_days, min_days, max_days):
    return [round(random.randint(min_days, max_days), 2) for _ in range(num_days)]

# Fonction pour générer des prix de réservation aléatoires
def generate_random_prices(num_prices, min_price, max_price):
    return [round(random.uniform(min_price, max_price), 2) for _ in range(num_prices)]

days_before_reservation = generate_random_days_reservation_before(700, 1, 25)

# Générer 700 prix de réservation aléatoires entre 20€ et 200€ par jour
reservation_prices = generate_random_prices(700, 20, 200)

# Fonction pour générer des périodes de réservation aléatoires
def generate_random_periods(num_periods, start_year, end_year):
    periods = []
    for _ in range(num_periods):
        # Générer une date de début aléatoire entre le début de 2022 et la fin de 2023
        start_date = datetime(random.randint(start_year, end_year - 1), random.randint(1, 12), random.randint(1, 28))
        # Générer une durée aléatoire de réservation entre 1 et 14 jours
        duration = random.randint(1, 14)
        # Calculer la date de fin
        end_date = start_date + timedelta(days=duration)
        periods.append(f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}")
    return periods

# Générer 700 périodes de réservation aléatoires
reservation_periods = generate_random_periods(700, 2022, 2024)

# Appliquer la fonction à chaque date de début de réservation
# Fonction pour associer chaque période de réservation à une saison
def assign_season(date):
    year, month, day = map(int, date.split('-'))
    # Définir les saisons en fonction des mois
    if month in [12, 1, 2]:  # Hiver
        return "Hiver"
    elif month in [3, 4, 5]:  # Printemps
        return "Printemps"
    elif month in [6, 7, 8]:  # Été
        return "Été"
    else:  # Automne (mois 9, 10, 11)
        return "Automne"

reservation_seasons = [assign_season(date.split(' - ')[0]) for date in reservation_periods]

# Liste des types de carburants
fuel_types = ["Essence", "Diesel", "Électrique", "Hybride"]

# Fonction pour générer des types de carburant aléatoires
def generate_fuel_types(num_records):
    return [random.choice(fuel_types) for _ in range(num_records)]

# Générer 700 types de carburant aléatoires
vehicle_fuel_types = generate_fuel_types(700)

#Liste des types de véhicules
vehicules_types = ["SUV", "Berline", "Utilitaire", "Citadine", "Coupé", "Break", "Cabriolet", "Break"]

def generate_vehicules_types(num_types):
    return [random.choice(vehicules_types) for _ in range(num_types)]

vehicules_types_generated = generate_vehicules_types(700)

clients_types = ["Particulier", "Pro", "Touriste", "Agence", "Entreprise de transport"]

def generate_clients_types(num_types_clients):
    return [random.choice(clients_types) for _ in range(num_types_clients)]

clients_types_generated = generate_clients_types(700)


# Liste des événements imprévus
unforeseen_events = [
    "Confinement COVID-19", 
    "Crise économique", 
    "Grève des transports", 
    "Pénurie de carburant", 
    "Crise politique", 
    "Événement climatique extrême", 
    "Épidémie de grippe", 
    "Crise énergétique", 
    "Manifestation nationale"
]

# Fonction pour générer des événements imprévus aléatoires
def generate_unforeseen_events(num_records, probability_of_event=0.1):
    events = []
    for _ in range(num_records):
        if random.random() < probability_of_event:  # Ajouter un événement selon une probabilité (ex: 10%)
            events.append(random.choice(unforeseen_events))
        else:
            events.append("Aucun événement")  # Pas d'événement pour la majorité des cas
    return events

# Générer 700 événements imprévus avec une probabilité de 10%
generated_events = generate_unforeseen_events(700, probability_of_event=0.4)


source_reservation = ["GoogleMyBusiness", "Plateforme_tiers", "Sitewebentreprise", "Téléphone", "Réseauxsociaux"]

# Fonction pour générer des sources de réservation aléatoires
def generate_reservation_sources(num_records):
    return [random.choice(source_reservation) for _ in range(num_records)]

# Générer 700 sources de réservation aléatoires
generated_sources = generate_reservation_sources(700)

# Liste des conditions météorologiques
weather_conditions = [
    "Ensoleillé", 
    "Nuageux", 
    "Pluie légère", 
    "Pluie forte", 
    "Neige", 
    "Brouillard", 
    "Tempête", 
    "Canicule"
]

def generate_weather_conditions(num_records):
    return [random.choice(weather_conditions) for _ in range(num_records)]

# Générer 700 conditions météorologiques aléatoires
generated_weather_conditions = generate_weather_conditions(700)

# Fonction pour générer le nombre de réservations répétées par client
def generate_repeat_reservations(num_clients, regular_client_probability=0.2):
    reservations = []
    for _ in range(num_clients):
        if random.random() < regular_client_probability:  # 20% des clients sont réguliers
            reservations.append(random.randint(2, 5))  # Réservations répétées entre 2 et 5 fois
        else:
            reservations.append(1)  # Client occasionnel : 1 seule réservation
    return reservations

# Générer pour 700 clients
repeat_reservations = generate_repeat_reservations(700, regular_client_probability=0.2)

etat_vehicule = ["neuf", "d'occasion"]

def generate_etat_vehicule(num_etats):
    return [random.choice(etat_vehicule) for _ in range(num_etats)]

etat_vehicule_generated = generate_etat_vehicule(700)

# Générer 700 noms et prénoms français
names = [f"{fake.first_name()} {fake.last_name()}" for _ in range(700)]

# Générer 700 emplois
jobs = [fake.job() for _ in range(700)]

# Générer 700 âges entre 18 et 70 ans
ages = [random.randint(18, 70) for _ in range(700)]

# Liste de marques de véhicules
brands = [
    "Renault", "Peugeot", "Citroën", "Volkswagen", "BMW", 
    "Mercedes-Benz", "Audi", "Ford", "Toyota", "Nissan", 
    "Fiat", "Opel", "Honda", "Kia", "Hyundai", 
    "Mazda", "Subaru", "Volvo", "Chevrolet", "Land Rover"
]

# Liste de modèles de véhicules
models = [
    "Clio", "308", "C3", "Golf", "Z4", 
    "A4", "A3", "Fiesta", "Corolla", "Qashqai", 
    "500", "Mégane", "Civic", "Kona", "Mazda3", 
    "Outback", "V60", "Cruze", "Freelander", "Range Rover"
]

# Générer 700 modèles de véhicules aléatoires
vehicle_models = [random.choice(models) for _ in range(700)]

# Générer 700 marques de véhicules aléatoires
vehicle_brands = [random.choice(brands) for _ in range(700)]


# Liste des sexes
genders = ["Homme", "Femme"]

# Générer 700 sexes aléatoires
sexes = [random.choice(genders) for _ in range(700)]

# Afficher les 10 premiers noms pour vérifier
print(names[:10])
print(jobs[:10])
print(ages[:10])
print(vehicle_brands[:10])
print(sexes[:10])
print(vehicle_models[:10])
print(reservation_periods[:10])
print(reservation_prices[:10])
print(reservation_seasons[:10])
print(vehicle_fuel_types[:10])
print(vehicules_types_generated[:10])
print(clients_types_generated[:10])
print(generated_events[:40])
print(generated_sources[:10])
print(days_before_reservation[:10])
print((generated_weather_conditions[:10]))
print((repeat_reservations[:50]))
print(etat_vehicule_generated[:10])
print((generated_km[:15]))