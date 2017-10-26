import random
import sys
from person import Person
from logger import Logger
random.seed(42)


class Simulation(object):
    '''
    Main class that will run the herd immunity simulation program. Expects
    initialization parameters passed as command line arguments when file runs.

    Simulates the spread of a virus through a given population.  The percentage
    of the population that are vaccinated, the size of the population, and the
    amount of initially infected people in a population are all variables that
    can be set when the program is run.

    _____Attributes______

    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.

    population_size: Int.  The size of the population for this simulation.

    population: [Person].  A list of person objects representing all people in
        the population.

    next_person_id: Int.  The next available id value for all created person objects.
        Each person should have a unique _id value.

    virus_name: String.  The name of the virus for the simulation.  This will be passed
    to the Virus object upon instantiation.

    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.

    basic_repro_num: Float between 0 and 1.   This will be passed
    to the Virus object upon instantiation.

    vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
        vaccinated for the given simulation.

    current_infected: Int.  The number of currently people in the population currently
        infected with the disease in the simulation.

    total_infected: Int.  The running total of people that have been infected since the
    simulation began, including any people currently infected.

    total_dead: Int.  The number of people that have died as a result of the infection
        during this simulation.  Starts at zero.


    _____Methods_____

    __init__(population_size, vacc_percentage, virus_name, mortality_rate,
     basic_repro_num, initial_infected=1):
        -- All arguments will be passed as command-line arguments when the file is run.
        -- After setting values for attributes, calls self._create_population() in order
            to create the population array that will be used for this simulation.

    _create_population(self, initial_infected):
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
    '''

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.total_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        # DONE: Create a Logger object and bind it to self.logger.  You should use this
        # logger object to log all events of any importance during the simulation.  Don't forget
        # to call these logger methods in the corresponding parts of the simulation!
        self.logger = Logger(self.file_name)
        self.logger.write_metadata(population_size, vacc_percentage,
                                   virus_name, mortality_rate, basic_repro_num)

        # This attribute will be used to keep track of all the people that catch
        # the infection during a given time step. We'll store each newly infected
        # person's .ID attribute in here.  At the end of each time step, we'll call
        # self._infect_newly_infected() and then reset .newly_infected back to an empty
        # list.
        self.newly_infected = []
        self.infected_now = []

        # DONE: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        self.population = self._create_population(initial_infected, vacc_percentage)

    def _create_population(self, initial_infected, vacc_percentage):
        # DONE: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        population = []
        infected_count = 0
        while len(population) != self.population_size:
            if infected_count != initial_infected:
                # DONE: Create all the infected people first, and then worry about the rest.
                # Don't forget to increment infected_count every time you create a
                # new infected person!
                infected_person = Person(len(population), False, True)
                population.append(infected_person)
                self.infected_now.append(infected_person)
                self.total_infected += 1
                infected_count += 1
            else:
                # Now create all the rest of the people.
                # Every time a new person will be created, generate a random number between
                # 0 and 1.  If this number is smaller than vacc_percentage, this person
                # should be created as a vaccinated person. If not, the person should be
                # created as an unvaccinated person.
                is_vacc = random.uniform(0, 1) < vacc_percentage
                regular_person = Person(len(population), is_vacc)
                population.append(regular_person)

            # DONE: After any Person object is created, whether sick or healthy,
            # you will need to increment self.next_person_id by 1. Each Person object's
            # ID has to be unique!
        return population

    def _simulation_should_continue(self):
        # DONE: Complete this method!  This method should return True if the simulation
        # should continue, or False if it should not.  The simulation should end under
        # any of the following circumstances:
        #     - The entire population is dead.
        #     - There are no infected people left in the population.
        # In all other instances, the simulation should continue.
        if self.total_infected == self.population_size:
            print('everyone infected')
            return False

        if len(self.infected_now) == 0:
            print('no one infected')
            return False

        return True

    def run(self):
        # DONE: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0

        # DONE: Remember to set this variable to an intial call of
        # self._simulation_should_continue()!
        should_continue = self._simulation_should_continue()

        while should_continue:
            # DONE: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation.  At the end of each iteration of this loop, remember
            # to rebind should_continue to another call of self._simulation_should_continue()!
            self.time_step()
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
            should_continue = self._simulation_should_continue()

        self.logger.log_final_stats(self.population_size, self.total_infected)
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        # DONE: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population:
            #        - Repeat for 100 total interactions:
            #             - Grab a random person from the population.
            #           - If the person is dead, continue and grab another new
            #                 person from the population. Since we don't interact
            #                 with dead people, this does not count as an interaction.
            #           - Else:
            #               - Call simulation.interaction(person, random_person)
            #               - Increment interaction counter by 1.
        interaction_count = 0
        for sick_person in self.infected_now:
            while interaction_count <= 100:
                alive = False
                while not alive:
                    random_person = self.population[random.randint(0, self.population_size - 1)]
                    if random_person.is_alive:
                        alive = True
                self.interaction(sick_person, random_person)
                interaction_count += 1
            interaction_count = 0

        for person in self.population:
            if person.is_alive and person.infected:
                self.logger.log_infection_survival(person,
                                                   person.did_survive_infection(self.mortality_rate))

        self.infected_now = []
        self._infect_newly_infected()

    def interaction(self, sick_person, random_person):
        # DONE: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        assert sick_person.is_alive == True
        assert random_person.is_alive == True

        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than basic_repro_num, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Remember to call self.logger.log_interaction() during this method!
        did_infect = False
        if random_person.is_vaccinated or random_person.infected:
            pass
        else:
            got_infected = random.uniform(0, 1) < self.basic_repro_num
            if got_infected:
                self.newly_infected.append(random_person._id)
                self.total_infected += 1
                did_infect = True

        self.logger.log_interaction(sick_person, random_person, did_infect)

    def _infect_newly_infected(self):
        # DONE: Finish this method! This method should be called at the end of
        # every time step.  This method should iterate through the list stored in
        # self.newly_infected, which should be filled with the IDs of every person
        # created.  Iterate though this list.
        # For every person id in self.newly_infected:
        #   - Find the Person object in self.population that has this corresponding ID.
        #   - Set this Person's .infected attribute to True.
        # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list!
        for _id in self.newly_infected:
            for person in self.population:
                if person._id == _id:
                    person.infected = True
                    self.infected_now.append(person)

        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    simulation = Simulation(pop_size, vacc_percentage, virus_name,
                            mortality_rate, basic_repro_num, initial_infected)
    simulation.run()
