import constants
from acceleratorModule import accelerator_module

module = accelerator_module(constants.num_of_turns , constants.current , constants.cross_sectional_area , constants.gap , constants.delta_x)
module.print_proj_stats(constants.mass , constants.v_0)