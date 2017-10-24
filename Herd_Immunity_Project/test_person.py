from person import Person


def test_person():
    _id = 1
    is_vaccinated = False
    is_alive = True
    new_person = Person(_id, is_vaccinated, is_alive)
    return new_person


def test_did_survive_infection():
    new_person = test_person()
    assert new_person.did_survive_infection(1) == False
    assert new_person.did_survive_infection(0) == True
