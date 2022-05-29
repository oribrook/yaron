# Puzzle

Requirements:
	numpy

	
Usage:
	
    File puzzle.py contains a function called "solve_puzzle"
        
    Usage example by python-CLI:
	
		from puzzle import solve_puzzle	
		res = solve_puzzle([image_1, image_2, image_3, image_4])
		
		""" 
			image_i args should be a numpy array
			returned res is a list with indexes 0-3 in the order of the args images
			
                    e.g if image_1 at the usage example is index 2 (third part of the pazzle, bottom left), 
			res will contains as first element: 2 
		"""
		
	You can use create_images(n, size) from testing_puzzle.py to create data-example as test:

		from testing_puzzle import create_images
		from puzzle import solve_puzzle
		files = create_images(1000, 8)

		solve_puzzle(files, 1000)  # output: [0, 1, 2, 3]
		
		files = [files[2], files[1], files[0], files[3]]
		solve_puzzle(files, 1000)  # output: [2, 1, 0, 3] 

Testing:
	
        File testing_puzzle.py contains create_subimages function.
        and run it for {num_tests} times
        
            By default it runs with arguments:
                n = rand in range(10, 1000),
                s (size) = rand in range(2, sqrt(n)
            
            if placed at the same folder with puzzle.py, just run it from CMD: 
                python testing_puzzle.py
                
            You can adjust args n and s (& num_test) as you like at lines 34-37


