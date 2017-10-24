from logger import Logger
from person import Person


def test_logger():
    new_logger = Logger("Test_simulation_pop_1000_vp_0.9_infected_10.txt")
    return new_logger


def test_write_metadata():
    new_logger = test_logger()
    new_logger.write_metadata(1000, 0.9, 'Test', 0.7, 0.25)
    with open(new_logger.file_name, 'r') as f:
        file_data = f.readlines()
        assert file_data[0] == ("Population size: 1000\tPercent vaccinated: 0.9\t"
        "Virus name: Test\tMortality rate: 0.7\tBasic Reproduction Number: 0.25\n")


def test_log_interaction():
    new_logger = test_logger()
    sick_person = Person(0, False, True)
    random_person = Person(1, False, False)
    random_vacc_person = Person(2, True, False)
    random_sick_person = Person(3, False, True)
    new_logger.log_interaction(sick_person, random_person, True)
    new_logger.log_interaction(sick_person, random_person, False)
    new_logger.log_interaction(sick_person, random_vacc_person, False)
    new_logger.log_interaction(sick_person, random_sick_person, False)
    with open(new_logger.file_name, 'r') as f:
        file_data = f.readlines()
        assert file_data[0] == "0 infected 1\n"
        assert file_data[1] == "0 did not infect 1 because 1 got lucky\n"
        assert file_data[2] == "0 did not infect 2 because 2 is vaccinated\n"
        assert file_data[3] == "0 did not infect 3 because 3 is already infected\n"


def test_log_infection_survival():
    new_logger = test_logger()
    random_person = Person(0, False, True)
    new_logger.log_infection_survival(random_person, True)
    new_logger.log_infection_survival(random_person, False)
    with open(new_logger.file_name, 'r') as f:
        file_data = f.readlines()
        assert file_data[0] == "0 survived.\n"
        assert file_data[1] == "0 died.\n"


def test_log_time_step():
    new_logger = test_logger()
    new_logger.log_time_step(53)
    with open(new_logger.file_name, 'r') as f:
        file_data = f.readlines()
        assert file_data[0] == "Time step 53 ended, beginning 54...\n"
