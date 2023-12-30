num_of_turns = 100
current = 10
cross_sectional_area = 0.0000636172512
gap = 0.001
force = pow((num_of_turns * current) , 2) * (12.566 * pow(10 , -7)) * (cross_sectional_area / (2 * pow(gap , 2)))

mass = 0.008
delta_x = 0.0127

acceleration = force / mass
initial_velocity = 0
final_velocity = pow((initial_velocity + (2 * acceleration * delta_x)) , 0.5)
time = (final_velocity - initial_velocity) / acceleration

impulse = force * time
delta_velocity = impulse / mass
delta_kinetic_energy = 0.5 * mass * pow(delta_velocity , 2)

def accelerator_module(num_of_turns , current , cross_sectional_area , gap , mass , delta_x , initial_velocity):
    force = pow((num_of_turns * current) , 2) * (12.566 * pow(10 , -7)) * (cross_sectional_area / (2 * pow(gap , 2)))
    acceleration = force / mass
    final_velocity = pow((initial_velocity + (2 * acceleration * delta_x)) , 0.5)
    time = (final_velocity - initial_velocity) / acceleration
    impulse = force * time
    delta_velocity = impulse / mass
    delta_kinetic_energy = 0.5 * mass * pow(delta_velocity , 2)