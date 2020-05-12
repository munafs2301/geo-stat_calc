'''
USER INTERFACE
This script contains codes for the user interface
'''
import statistics
from geometry import *
from sys import exit

def exists():
	'''exists function'''
	print(f"\nGoodbye {name}!")
	exit()

def headings(*title):
	'''formats the header of each section'''
	print("=" * 52)
	for string in title:
		print(string.center(52))
	print("=" *52)
	
def errormessage(numlist, func):
	'''formats the error messages'''
	print(f"\nWrong input! Please enter a number {numlist}.")
	print( "=" * 52)
	func()

def stat_calc(func, concept):
	'''Solves calculation in statistics'''
	try:
		data = input("\nProvide data as comma seperated values --> a,b,c,d\nEnter the numbers: ").strip().split(",")
		datalist = [float(num) for num in data ]
		print(f"\nThe {concept} value is {round(func(datalist), 4)}")
		print("="*52)
	#	options()
	except:
		print("\nWrong input format! Enter your data as comma seperated values. \nExample: 2,3,4,5,6")
		stat_calc(func, concept)
		
def range(data):
	'''Calculates the range of numbers'''
	range = max(data) - min(data)
	return range
	
'''Variable Declaration '''
name = input("Hello scholar! What is your name: ")

geoconcepts = {"Definition" : "\nWhat is Geometry? \n\nThe word Geometry was formed full the Greek words 'Geo' meaning 'earth' and 'metry' meaning 'measurement'. Geometry is branch of mathematics that studies the sizes, shapes, portions, angles and commending of things'.\n",
						"Branches" : "\n Branches in Geometry: \n\n1. Euclidean Geometry 2. Non Euclidean Geometry\n",
						"Applications" : "\nApplication of Geometry\n\nGeometry is applied to solve real life problems in the following fields:\n1. Astronomy: geometry calculations between coordinates help to chart a trajectory for spaceships's journey into space.\n2. Geographic Information Systems: geometry uses coordinates to calculate locations on the earth's surface\n3. Architecture: geometry helps to design buildings shape through software such as CAD. \n4. And many more\n"}
					
staconcepts = {"Definition" : "\nWhat is Statistics? \n\n Statistics is a branch of mathematics that deals with data collection, organization, analysis, interpretation, and presentation.The two main branches of statistics are Descriptive statistics' and other Differential Statistics'. \n",
						"Branches" : "\nBranches in Statistics: \n\n1. Descriptive Statistics: are used to synopsize data from a sample exercising the mean or standard deviation. \n2. Inferential Statistics:are used when data is viewed as a subclass of a specific population. \n",
						"Applications" : "\nApplication of Statistics\n\n Statistics is applied in the following fields:\n1. Biostatistics: biological phenomenon is studied by statistical analysis.\n2. Reliability Engineering: the reliability of a system by means of statistics. \n3. Machine Learning: this is a subfield of computer science that formulates algorithms in order to make prediction from data. \n4. And many more\n"}
 
#Program name and general function
headings("GEOSTAT CALCULATOR\n", "An Advanced Calculator for Geometry and Statistics")

print(f"\nWelcome {name}!!!")#welcome message
 
def select_topic():
    '''Selects topic available in the program'''
   
    print(" \nSelect a topic of interest:")
    print("\tStatistics {1}\n\tGeometry {2}\n\tExit Program {3}\n\n ")
   
    try:
        choice = int(input("Enter a choice: "))
   
        #Selects Statistics
        if choice == 1:
            statistics_interface()
   
        #Selects Geometry
        elif choice == 2:
            geometry_interface()
           
        #Exits the program
        elif choice == 3:
        	exists()
            
        else:
            errormessage([1, 2, 3], select_topic)
           
    except ValueError:
    	errormessage([1, 2, 3], select_topic)
        
       
def statistics_interface():
    ''' Selects an option from the statistics interface'''
    
    headings("STATISTICS") 
    print(f"\nWhat would you like to do {name}?: ", end = "")
    print("\n\tLearn the basic concepts of Statistics {1}\n\tMake calculations {2} \n\tPrevious menu {3} \n\tExit Program {4} \n\n ", sep = "")
    
    def options():
        try:
            choice = int(input("Enter a choice: "))

            #Selects statistics concept
            if choice == 1:
                statistics_concepts()

            #Selects calcutions
            elif choice == 2:
                statistics_calculator()
            
            #Takes user back to previous function
            elif choice == 3:
                print( "=" * 52)
                select_topic()

            #Exits the program
            elif choice == 4:
                exists()
                
            else:
                errormessage([1, 2, 3, 4], options)
            
        except ValueError:
            errormessage([1, 2, 3, 4], options)

    return options()
       
def geometry_interface():
    ''' Selects an option from the geometry interface'''

    headings("GEOMETRY")
    print(f"\nWhat would you like to do {name}?: ", end = "")
    print("\n\tLearn the basic concepts of Geometry {1}\n\tMake calculations {2} \n\tPrevious menu {3} \n\tExit Program {4} \n\n ", sep = "")
       
    def options():
        try:
            choice = int(input("Enter a choice: "))

            #Selects geometry concepts
            if choice == 1:
                geometry_concepts()
        
            #Selects calcutions
            elif choice == 2:
                geometry_calculator()
                
            #Takes user back to previous function
            elif choice == 3:
                print( "=" * 52)
                select_topic()
            
            #Exits the program
            elif choice == 4:
                exists()
            
            else:
                errormessage([1, 2, 3, 4], options)
            
        except ValueError:
                errormessage([1, 2, 3, 4], options)

    return options()
    
def geometry_concepts():
    '''This gives an overview of basic concepts in Geometry'''
    
    headings("GEOMETRY: overview  of basic concepts")
    print ()
    
    #This prints out the concepts in geometry 
    for info in geoconcepts.values():
    	print(info)
	
    def options():
        try:
            choice = int(input("Previous menu (1)\nExit program (2) \n")) 
            
            #Takes user back to previous function
            if choice == 1:
              #  print( "=" * 52)
                geometry_interface()

            #Exits the program
            elif choice == 2:
                exists()
            
            else:
                errormessage([1, 2], options)
            
        except ValueError:
            errormessage([1, 2], options)

    return options()
    
def statistics_concepts():
    '''This gives an overview of basic concepts I. Statistics'''
    headings("STATISTICS: overview  of basic concepts")
    print ()
    
    for info in staconcepts.values():
    	print(info)
	
    def options():
        try:
            choice = int(input("Previous menu (1)\nExit program (2) \n")) 
            
            #Takes user back to previous function
            if choice == 1:
               # print( "=" * 52)
                statistics_interface()

            #Exits the program
            elif choice == 2:
                exists()
            
            else:
            	errormessage([1, 2], options)
            
        except ValueError:
            errormessage([1, 2], options)

    return options()


def statistics_calculator():
    '''Solves calculation in statistics'''
    
    headings("STAT-CALC")
    print("\nCalculations in statistics:")

    def options():
        try:
            print("\nMean {1}\nHarmonic Mean {2} \nMedian {3} \nHigh Median {4} \nLow Median {5} \nMode {6} \nStandard Deviation {7} \nVariance {8} \nRange{9}\n\nPrevious menu {10} \nExit Program {11} \n", sep = "")
            choice = int(input("Enter a choice from the option to make calculations: "))

            if choice == 1:
                stat_calc(statistics.mean, "mean")
                options()

            elif choice == 2:
                stat_calc(statistics.harmonic_mean, "harmonic mean")
                options()

            elif choice == 3:
                stat_calc(statistics.median, "median")
                options()

            elif choice == 4:
                stat_calc(statistics.median_high, "median high")
                options()

            elif choice == 5:
                stat_calc(statistics.median_low, "median low")
                options()

            elif choice == 6:
                stat_calc(statistics.mode, "mode")
                options()

            elif choice == 7:
            	stat_calc(statistics.stdev, "standard deviation")
            	options()

            elif choice == 8:
            	stat_calc(statistics.variance, "variance")
            	options()
            	
            elif choice == 9:
            	stat_calc(range, "range")
            	options()
                
            #Takes user back to previous function
            elif choice == 10:
                print( "=" * 52)
                statistics_interface()
            
            #Exits the program
            elif choice == 11:
                exists()
            
            else:
                print("Wrong input. Enter a valid set of numbers")
                options()
            
        except ValueError:
                errormessage(["1 - 10"], options)
    return options()
    
    
def geometry_calculator():
    '''Solves calculation in geometry'''
    headings("GEO-CALC")
    print("\nCalculations in geometry:")   
     
    def options():
        try:
            print("\n{1} Circle-->Area\n{2} Circle-->Circumference\n{3} Circle-->Arc Length \n{4} Circle-->Area of sector\n{5} Circle-->Area of segment \n{6} Circle-->Perimeter of segment\n{7} Circle-->Length of chord \n{8} Triangle-->Area\n{9} Triangle-->Perimeter\n{10} Equilateral Triangle-->Area \n{11} Equilatetal Triangle-->Perimeter \n{12} Rectangle-->Area  \n{13} Rectangle-->Perimeter \n{14} Rectangle-->Length of diagonal \n{15} Square-->Area\n{16} Square-->Perimeter\n{17} Trapezium-->Area \n{18} Paralleogram-->Area\n{19} Parallelogram-->Perimeter \n\nPrevious menu {20} \nExit Program {21} \n", sep = "")
            choice = int(input("Enter a choice from the option to make calculations on any of these shapes: "))

            if choice == 1:
            	radius = float(input("\nEnter radius: "))
            	print(f"Area of the circle is {Circle(radius).area()}")
            	geometry_interface()
            	
            elif choice == 2:
            	radius = float(input("\nEnter radius: "))
            	print(f"Circumference of the circle is {Circle(radius).circumference()}")
            	geometry_interface()

            elif choice == 3:
                radius = float(input("\nEnter radius: "))
                angle = int(input("Enter angle: "))
                print(f"Length of arc of the circle is {Circle(radius,angle).arc_length()}")
                geometry_interface()

            elif choice == 4:
                radius = float(input("\nEnter radius: "))
                angle = float(input("Enter angle: "))
                print(f"Area of sector of the circle is {Circle(radius,angle).sector_area()}")
                geometry_interface()
                
            elif choice == 5:
                radius = float(input("\nEnter radius: "))
                angle = float(input("Enter angle: "))
                print(f"Area of segment of the circle is {Circle(radius,angle).segment_area()}")
                geometry_interface()

            elif choice == 6:
                radius = float(input("\nEnter radius: "))
                angle = float(input("Enter angle: "))
                print(f"Perimeter of segment of the circle is {Circle(radius,angle).segment_perimeter()}")
                geometry_interface()

            elif choice == 7:
            	radius = float(input("\nEnter radius: "))
            	angle = float(input("Enter angle: "))
            	height = float(input("Enter height: "))
            	print(f"Length of chord of the circle is {Circle(radius,angle,height).chord_length()}")
            	geometry_interface()

            elif choice == 8:
            	base = float(input("\nEnter the base: "))
            	tri_height = float(input("Enter the height: "))
            	print(f"Area of the triangle is {Triangle(base, height = tri_height, type =  'height').area()}")
            	geometry_interface()
            	
            elif choice == 9:
            	base = float(input("\nEnter the base: "))
            	side1 = float(input("Enter the first side: "))
            	side2 = float(input("Enter the second side:"))
            	print(f"Perimeter of the triangle is {Triangle(base, side1, side2).perimeter()}")
            	geometry_interface()
            	
            elif choice == 10:
            	base = float(input("\nEnter the base: "))
            	print(f"Area of the equilateral triangle is {Equilateral(base).area()}")
            	geometry_interface()
            	
            elif choice == 11:
            	base = float(input("\nEnter the base: "))
            	print(f"Perimeter of the equilateral triangle is {Equilateral(base).perimeter()}")
            	geometry_interface()
            	
            elif choice == 12:
            	base = float(input("\nEnter the base: "))
            	rect_height = float(input("Enter the height: "))
            	print(f"Area of the rectangle is {Rectangle(base, height = rect_height).area()}")
            	geometry_interface()
            	
            elif choice == 13:
            	base = float(input("\nEnter the base: "))
            	rect_height = float(input("Enter the height: "))
            	print(f"Perimeter of the rectangle is {Rectangle(base, height = rect_height).perimeter()}")
            	geometry_interface()
            	
            elif choice == 14:
            	base = float(input("\nEnter the base: "))
            	rect_height = float(input("Enter the height: "))
            	print(f"Diagonal length of the rectangle is {Rectangle(base, height = rect_height).diagonal_len()}")
            	geometry_interface()
            	
            elif choice == 15:
            	base = float(input("\nEnter the base: "))
            	print(f"Area of the square is {Square(base).area()}")
            	geometry_interface()
            	
            elif choice == 16:
            	base = float(input("\nEnter the base: "))
            	print(f"Perimeter of the square is {Square(base).perimeter()}")
            	geometry_interface()
            
            elif choice == 17:
            	base = float(input("\nEnter the base: "))
            	base2 = float(input("Enter opposite side: "))
            	trap_height= float(input("Enter height: "))
            	print(f"Area of the trapezium is {Trapezium(base, base2, height = trap_height).area()}")
            	geometry_interface()
            	
            elif choice == 18:
            	base = float(input("\nEnter the base: "))
            	para_height = floatt(input("Enter the height: "))
            	print(f"Area of the parallelogram is {Parallelogram(base, height = para_height).area()}")
            	geometry_interface()
            	
            elif choice == 19:
            	base = float(input("\nEnter the base: "))
            	para_diag= float(input("Enter the side: "))
            	print(f"Perimeter of the parallelogram is {Parallelogram(base, diagonal = para_diag).perimeter()}")
            	geometry_interface()
                
            #Takes user back to previous function
            elif choice == 20:
                print( "=" * 52)
                geometry_interface()
            
            #Exits the program
            elif choice == 21:
                exists()
            
            else:
                print("\nWrong input. Enter a valid number")
                print("-" * 52)
                options()
            
        except ValueError:
                errormessage("1 - 22", options)
    options()           
select_topic()