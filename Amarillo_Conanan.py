
import os
import string
	

def list_objects(limit): 							# This accepts number of inputs for objects
	lis_objects = [] 								# Initialize array
	invalid_objects = set(string.punctuation) 		# This is used for special character input

	for i in range(limit): 							# This will loop until user input reach the object limit
		objects = (raw_input("Enter object : "))

		if any(char in invalid_objects for char in objects):							# Checks if input has special chars 
			print("\t Invalid input! Input should not contain numbers and symbols")		# Prompt message for invalid input
			objects = (raw_input("\nEnter again : "))									# Asks for another input
			lis_objects.append(objects)													# Append to string
		elif any(char.isdigit() for char in objects):									# Checks if input has digit
			print("\t Invalid input! Input should not contain numbers and symbols")		# Prompt message for invalid 
			objects = (raw_input("\nEnter again : "))			
			lis_objects.append(objects)
		else:
			lis_objects.append(objects)

	return lis_objects																	# This will return the list of objects (lis_objects) ex. ["1", "2"]



def extend_list(lst, old_limit):														# The parameter accepts the list and the old_limit
																						# old_limit because this will extend the limit of the list of objects
	
	new_limit = int(input("\nEnter extended number of objects : "))						# Accepts input for new_limit
	
	while new_limit <= old_limit:
		print("\tInvalid input! Input should not be less than the original limit! \n\t(Must be greater than %d)" %old_limit)		# Prompt message for invalid input
		new_limit = int(input("\nEnter again : "))										# Asks for another input					
	
	extend = new_limit - old_limit														# extend is the variable for new occurence
	print lst 																			# Prints old_list
	print "  :plus(+)", extend

	lst1 = list_objects(extend)															# calls list_objects for new input
 	output = lst + lst1																	# Concatenate 2 lists (the old list plus the extended list)

 	return output 																		# returns new list
 


def compute_freq(lst):
	num = len(lst)																		# used for divisor later for percentage
	lst1 = [] 																			# initialized array for lower case
	lst2 = [] 																			# for no repeatition array

	lst1 = [item.lower() for item in lst]												# convert old list to lower()

	for char in lst1:																	# filter same objects
		if char not in lst2:															# object without the same in the list will append to lst2 (no reps array)
			lst2.append(char)

	for i in range(0, len(lst2)):														# computes the frequency of the object 
		freq = float(lst1.count(lst2[i])) / num 										# return fre as float, count of object divide the len(lst) for frequency

		print "\t", lst2[i],":\t", int(freq*100),"%" 									# prints the [ object : percentage] ex. Narra : 20%

	compare_objects(lst, lst1, lst2)													# calls compare_object to compare objects
			
	

def compare_objects(lst, lst1, lst2):													# Compares objects
	choice1 = 0
	while choice1 != "Yes":

		choice1 = raw_input("\nWould you like to compare two objects? [y]es, or [n]o: ").lower()
		if choice1 == "y":
			print "\nChoices : "
			for i in range(0, len(lst2)):
				print "\t", lst2[i]


			obj = raw_input("\nObject: ").lower()
			comp = raw_input("Compare against: ").lower()

			result = lst1.index(obj)													# Finds obj location in list2 (no reps array)
			result1 = lst1.index(comp)													# Finds comp location in list2

			res = float(lst1.count(lst1[result]))										# Count of object's occurence in the list1 (lower case)
			res1 = float(lst1.count(lst1[result1]))


			if res > res1:
				fResult = res / res1
				print ("%s compared against %s : It appears that %s has occured %.3f times greater than %s." % (obj, comp, obj, fResult, comp))
			elif res < res1:
				fResult = res / res1
				print ("%s compared against %s : It appears that %s has occured %.3f times less than %s." % (obj, comp, obj, fResult, comp))
			elif res == res1:
				fResult = res / res1
				print ("%s compared against %s : It appears that %s has occured %.3f times equal wwith %s." % (obj, comp, obj, fResult, comp))

			change_freq(lst, lst1, lst2, obj,comp, res, res1)							# parameter       lst = orig ; lst1 = lower case ; lst2 = bawas na

		elif choice1 == "n":
			end_prog()



def change_freq(lst, lst1, lst2, obj, against, res, res1): #lst = orig ; lst1 = lower case ; lst2 = bawas na
	choicee = 0
	while choicee != "Yes":
		choicee = raw_input("\nWould you like to increase the frequency? [y]es, or [n]o: ").lower()
		if choicee == "y":

			print "\nOriginal List: "
			for char in lst:
				print "\t", char

			print ("\nObject you want to change frequency: %s" %obj)
			num_freq = int(input("Frequency against %s: " %against))

			fResult = res/res1

			while fResult >= num_freq:
				print("\tInvalid input! Input should not be less than the occurence! \n\t(Must be greater than %d)" %fResult)		# Prompt message for invalid input
				num_freq = int(input("\nEnter again : "))								# Asks for another input

			need = num_freq*res1 														# To find the needed occurence
			new_occ = int(need - res)													# New occurence 

			new_lst = []
			for i in range(new_occ):													# Appends object to create new occurence
				new_lst.append(obj)

 			fin_lst = lst + new_lst													# concatenate old list and the new list

 			print "\nNew list:"															# Prints list
 			for char in fin_lst:
 				print "\t", char

 			choicee = 0
			while choicee != "Yes":
				choicee = raw_input("\nWould you want to view the frequency of all objects? [y]es, or [n]o: ").lower()
				if choicee == "y":
					compute_freq(fin_lst)
				elif choicee == "n":
					end_prog()

		elif choicee == "n":
			end_prog()



def end_prog():																			# restarts or terminate program
	choicee = 0
	while choicee != "Yes":
		choicee = raw_input("\nWould you want to start all over again? [y]es, or [n]o (terminate program): ").lower()
		if choicee == "y":
			lst = []
			lst2 = []
			choice = 0
			flow()
		elif choicee == "n":
			print "Bye!"
			exit()



def clear():																			# clear cmd
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')



def flow():
	clear()
	choice = 0

	set_name = (raw_input("Enter name of set : "))										# input set name
	orig_limit = int(input("Enter number of objects : "))								# input number of objects
	lst = list_objects(orig_limit)														# calls for list_objects that asks for inputs


	while choice != "Yes":
		choice = raw_input("\nWould you like to extend the list? [y]es, or [n]o: ").lower()		# Question for limit extension
		if choice == "y":																		# if yes, this will call the extend list that return concatenated list
			lst = extend_list(lst, orig_limit)
		elif choice == "n":
			choice1 = 0

			print "\nSet:", set_name
			print "Objects: "
			for char in lst:
				print "\t", char

			print "Output :"

			compute_freq(lst)


			
if __name__ == "__main__":
   flow()






# flow()

# list_objects() ret list +
# extend_list() --
# --list_objects() ret list +
	
# 	++compute_freq(list)
# 		compare_objects(lst, lst1, lst2)
# 			change_freq(lst, lst1, lst2, obj,comp, res, res1)
# 				compute_freq(fin_list)


