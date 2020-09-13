#!/usr/bin/env python

from ptg import PTG
from helpers import Vehicle, show_trajectory

def main():
	#trajectory
	#(si, si_dot, si_ddot, d, d_dot, d_ddot,)
	vehicle = Vehicle([5,10,0,0,0,0])
	#(t)
	predictions = {0: vehicle}


	target = 0
	#vehicle_number

	delta = [0, 0, 0, 0, 0 ,0]
	#perturb parameter --> #(si, si_dot, si_ddot, d, d_dot, d_ddot,)

	start_s = [0, 0, 0]
	start_d = [4, 0, 0]

	T = 20

	best = PTG(start_s, start_d, target, delta, T, predictions)
	show_trajectory(best[0], best[1], best[2], vehicle)

if __name__ == "__main__":
	main()