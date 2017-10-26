from simulation import Simulation


def test_simulation():
    """Should create a new simulation."""
    population_size = 1000
    vacc_percentage = 0.9
    virus_name = 'Test'
    mortality_rate = 0.7
    basic_repro_num = 0.25
    initial_infected = 5
    new_simulation = Simulation(population_size, vacc_percentage, virus_name,
                                mortality_rate, basic_repro_num, initial_infected)
    return new_simulation


def test_create_population():
    # initial_infected, vacc_percentage
    """Should create a new population with the right proportions."""
    new_simulation = test_simulation()

    infected = 0
    for person in new_simulation.population:
        if person.infected == True:
            infected += 1
    assert infected == 5
    assert len(new_simulation.infected_now) == 5
    assert new_simulation.total_infected == 5

    vaccinated = 0
    for person in new_simulation.population:
        if person.is_vaccinated == True:
            vaccinated += 1
    assert vaccinated >= 800 and vaccinated <= 1000


def test_simulation_should_continue():
    """Should return False if stop cases true"""
    new_simulation = test_simulation()
    assert new_simulation._simulation_should_continue() == True

    new_simulation.total_infected = 1000
    assert new_simulation._simulation_should_continue() == False
    new_simulation.total_infected = 5

    new_simulation.infected_now = []
    assert new_simulation._simulation_should_continue() == False


def test_run(capfd):
    """Check if message is printed after loop stops"""
    new_simulation = test_simulation()
    new_simulation.total_infected = 1000
    new_simulation.run()
    out, err = capfd.readouterr()
    assert out == ("everyone infected\n"
                   "The simulation has ended after 0 turns.\n")


def test_time_step():
    """Make sure infected interactions occur and infection attempts to kill"""
    new_simulation = test_simulation()


def test_interaction():
    # sick_person, random_person
    """Should only return True when person gets infected"""
    new_simulation = test_simulation()


def test_infect_newly_infected():
    """Should infect all peope who have their ids stored"""
    new_simulation = test_simulation()

    new_simulation.newly_infected = [42, 753, 321]
    new_simulation._infect_newly_infected()
    for person in new_simulation.population:
        if person._id == 42 or person._id == 753 or person._id == 321:
            assert person.infected == True

    assert len(new_simulation.newly_infected) == 0
    assert len(new_simulation.infected_now) == 8
