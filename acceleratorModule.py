class accelerator_module():
    def __init__(self, num_of_turns , current , cross_sectional_area , gap , delta_x):
        self.num_of_turns = num_of_turns
        self.current = current
        self.cross_sectional_area = cross_sectional_area
        self.gap = gap
        self.delta_x = delta_x
        self.force = pow((num_of_turns * current) , 2) * (12.566 * pow(10 , -7)) * (cross_sectional_area / (2 * pow(gap , 2)))

    def calc_projectile_stats(self, mass , initial_velocity):
        acceleration = self.force / mass
        final_velocity = pow((initial_velocity + (2 * acceleration * self.delta_x)) , 0.5)
        time = (final_velocity - initial_velocity) / acceleration
        print(final_velocity)
        print(time)

#impulse = force * time
#delta_velocity = impulse / mass
#delta_kinetic_energy = 0.5 * mass * pow(delta_velocity , 2)