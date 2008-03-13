# ******************************** #
# Double pole balancing experiment #
# ******************************** #
from neat import config, population, chromosome, genome2, visualize
import math, random
import cPickle as pickle
from cart_pole import CartPole

def evaluate_population(population):
       
    simulation = CartPole(population, markov = False)
    simulation.run()
   

if __name__ == "__main__":
    
    #config.load('dpole_config') 
    config.load('dpole_config_ctrnn')
    
    # change the number of inputs accordingly to the type
    # of experiment: markov (6) or non-markov (3)
    # you can also set the configs in dpole_config as long
    # as you have two config files for each type of experiment
    config.Config.input_nodes = 3

    # Temporary workaround
    #chromosome.node_gene_type = genome2.NodeGene
    chromosome.node_gene_type = genome2.CTNodeGene
    
    population.Population.evaluate = evaluate_population
    pop = population.Population()
    pop.epoch(200, report=1, save_best=0)
    
    winner = pop.stats[0][-1]
    
    # visualize the best topology
    visualize.draw_net(winner) # best chromosome
    # Plots the evolution of the best/average fitness
    #visualize.plot_stats(pop.stats)
    # Visualizes speciation
    #visualize.plot_species(pop.species_log)
    
    print 'Number of evaluations: %d' %winner.id
    from time import strftime
    # saves the winner
    date = strftime("%Y_%m_%d_%Hh%Mm%Ss")
    # saves the winner
    file = open('winner_'+date, 'w')
    pickle.dump(winner, file)
    file.close()
    
    #print winner
