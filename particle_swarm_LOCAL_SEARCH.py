import random
import numpy as np

class Particle:
    def __init__(self, num_students, num_groups):
        self.position = self.generate_random_position(num_students, num_groups)
        self.velocity = self.generate_random_velocity(num_students, num_groups)
        self.personal_best = self.position.copy()
        self.fitness = float('inf')  # Initially set to infinity

    def generate_random_position(self, num_students, num_groups):
        # Randomly assign students to groups
        return [random.randint(1, num_groups) for _ in range(num_students)]

    def generate_random_velocity(self, num_students, num_groups):
        # Initialize velocity randomly
        return [random.randint(-1, 1) for _ in range(num_students)]

class PSO:
    def __init__(self, num_students, num_groups, num_particles, max_iterations):
        self.num_students = num_students
        self.num_groups = num_groups
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.particles = [Particle(num_students, num_groups) for _ in range(num_particles)]
        self.global_best = None

    def update_fitness(self):
        group_marks = [[] for _ in range(self.num_groups)]  # Initialize group_marks
        for particle in self.particles:
            for student, group in enumerate(particle.position):
                # Ensure group index is within valid range
                if 1 <= group <= self.num_groups:
                    # Append student to the corresponding group
                    group_marks[group - 1].append(student + 1)  # Student index starts from 1
        # Calculate fitness (diversity in groups) based on group_marks
        group_variances = [np.var(marks) for marks in group_marks]
        for particle, variance in zip(self.particles, group_variances):
            particle.fitness = variance

    def update_global_best(self):
        best_particle = min(self.particles, key=lambda x: x.fitness)
        if self.global_best is None or best_particle.fitness < self.global_best.fitness:
            self.global_best = best_particle

    def update_velocity_and_position(self, inertia_weight=0.5, personal_influence=1, social_influence=1):
        for particle in self.particles:
            for i in range(self.num_students):
                r1, r2 = random.random(), random.random()
                personal_delta = personal_influence * r1 * (particle.personal_best[i] - particle.position[i])
                social_delta = social_influence * r2 * (self.global_best.position[i] - particle.position[i])
                velocity_update = inertia_weight * particle.velocity[i] + personal_delta + social_delta
                particle.velocity[i] = velocity_update
                particle.position[i] = int(round(particle.position[i] + velocity_update))

    def optimize(self):
        for _ in range(self.max_iterations):
            self.update_fitness()
            self.update_global_best()
            self.update_velocity_and_position()
        return self.global_best.position


N = 6  
k = 2  
set_of_marks = [50, 20, 10, 5, 15, 45]
num_particles = 20
max_iterations = 100

pso = PSO(N, k, num_particles, max_iterations)
best_solution = pso.optimize()
print("Best solution (Grouping of Students):", best_solution)
