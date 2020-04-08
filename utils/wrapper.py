from utils.computation import *
from utils.diagnostics import *
class non_convex_optimisation:
    def __init__(self, func, dfunc, optimal, optimum, trail = None):
        self.func = func
        self.dfunc = dfunc
        self.optimal = optimal
        self.optimum = optimum
        self.distance_arg = None
        self.distance_val = None
        self.trail = trail
    def do_experiments(self, mean0, D, alpha, beta, adjust):
            self.val, self.arg, self.stats = cma_es_general(mean0, D, alpha, beta, adjust,\
                                            self.func, self.dfunc, self.optimal, self.optimum)
    def get_recorded_data(self):
        return self.val, self.arg, self.stats
    def get_results_points(self):
        return self.res, self.points
    @staticmethod
    def plot_scatter(self, func, lim, N):
        plot_scatter(func, lim, N)
    @staticmethod
    def plot_surface(self, func, lim, N):
        plot_surface(func, lim, N)   

non_convex_optimisation.plot_distance = plot_distance
non_convex_optimisation.get_distance = get_distance
non_convex_optimisation.print_mean_variance = print_mean_variance
non_convex_optimisation.print_evaluations_per_iteration = print_evaluations_per_iteration
non_convex_optimisation.print_arguments_before_and_after_move = non_convex_optimisation
non_convex_optimisation.generate_point_cloud = generate_point_cloud
non_convex_optimisation.plot_prob_vs_radius = plot_prob_vs_radius
non_convex_optimisation.plot_cloud_point = plot_cloud_point
non_convex_optimisation.get_distance = get_distance
non_convex_optimisation.plot_distance_common = plot_distance_common
non_convex_optimisation.cma_es_general = cma_es_general