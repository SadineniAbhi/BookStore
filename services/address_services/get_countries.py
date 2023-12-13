from project.models.address_model import Country

def getCountries():
    all_countries = Country.query.all()
    return all_countries