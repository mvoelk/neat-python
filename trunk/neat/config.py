# sets the configuration parameters for NEAT
       
def load(file):
    try:
        parameters = open('file','r')
    except IOError:
        print 'Error: file %s not found!' %file
    #else:
        # set class attributes
        

class Config: # read from file
    # network type
    nn_allow_recurrence = True
    
    # phenotype config
    input_nodes = 3
    output_nodes = 1
    max_weight = 50
    min_weight = -50
    
    # mutation probabilities
    prob_crossover = 0.7  # not implemented (always apply crossover)
    prob_mutation = 0.25  # dynamic mutation rate (future release)
    prob_addconn = 0.05
    prob_addnode = 0.03
    prob_mutatebias = 0.0
    prob_togglelink = 0.0
    prob_weightreplaced = 0.0 # not implemented
    prob_mutate_weight = 0.05
    weight_mutation_power = 2.5
    max_bias_pertubation = 0.1 # not implemented
    
    # genetic algorithm parameters
    pop_size = 50        # set when initializing population
    number_epochs = 1000 # not implemented
    
    # genotype compatibility 
    compatibility_threshold = 0.5
    compatibility_change = 0.1
    excess_coeficient = 1.0
    disjoint_coeficient = 1.0
    weight_coeficient = 0.4
    
    # species
    species_size = 10
    survival_threshold = 0.2
    old_threshold = 80
    youth_threshold = 10
    old_penalty = 1.2     # not implemented
    youth_boost = 0.7
    max_stagnation = 15
    
    # for a future release
    #ele_event_time = 1000
    #ele_events = False            
                