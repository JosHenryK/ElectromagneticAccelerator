import math

class accelerator_module():
    def __init__(self, num_of_turns , current , cross_sectional_area , gap , delta_x):
        self.num_of_turns = num_of_turns
        self.current = current
        self.cross_sectional_area = cross_sectional_area
        self.gap = gap
        self.delta_x = delta_x
        self.force = pow((num_of_turns * current) , 2) * (12.566 * pow(10 , -7)) * (cross_sectional_area / (2 * pow(gap , 2)))

    def calc_proj_final_velocity(self , mass , initial_velocity):
        acceleration = self.force / mass
        final_velocity = math.sqrt(initial_velocity + (2 * acceleration * self.delta_x))
        return final_velocity

    def print_proj_stats(self , mass , initial_velocity):
        final_velocity = self.calc_proj_final_velocity(mass , initial_velocity)
        delta_velocity = final_velocity - initial_velocity
        initial_kinetic_energy = 0.5 * mass * pow(initial_velocity , 2)
        final_kinetic_energy = 0.5 * mass * pow(final_velocity , 2)
        delta_kinetic_energy = (0.5 * mass * pow(final_velocity , 2)) - (0.5 * mass * pow(initial_velocity , 2))
        acceleration = self.force / mass
        time = (final_velocity - initial_velocity) / acceleration
        impulse = self.force * time
        
        print()

        print("Initial Velocity: " + str(initial_velocity) + " m/s")
        print("final velocity: " + str(final_velocity) + " m/s")
        print("delta velocity: " + str(delta_velocity) + " m/s")
        print()

        print("initial kinetic energy: " + str(initial_kinetic_energy) + " J")
        print("final kinetic energy: " + str(final_kinetic_energy) + " J")
        print("delta kinetic energy: " + str(delta_kinetic_energy) + " J")
        print()

        print("Time: " + str(time) + " s")
        print("Acceleration: " + str(acceleration) + " m/s^2")
        print("Impulse: " + str(impulse) + " Ns")
        print()