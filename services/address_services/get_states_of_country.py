from project.models.address_model import State

def getStateOfCountry(country_id):
    all_states = State.query.filter_by(Country_id=country_id).all()
    return all_states
    