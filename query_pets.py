import sqlite3 as lite
import sys

con = lite.connect('pets.db')

with con:

	cur = con.cursor()

	while True:
		user_id = raw_input("Owner ID:")

		if user_id.isdigit()==False:
			if (user_id == '-1'):
				sys.exit()

			print "Numeral ID only."
			continue

		cur.execute("SELECT * FROM Person WHERE id=%s"  % (user_id) )
		person = cur.fetchone()

		if person == None:
			print 'No Owner by that ID'
			continue

		person_name = person[1] + ' ' + person[2]
		person_age = person[3]

		print  "%s, %s years old. " % (person_name, person_age)

		pets = cur.execute("SELECT * FROM Person_pet WHERE person_id=%s"  % (user_id))
		person_pets = cur.fetchall()
		pets_counter = len(person_pets)

		while pets_counter > 0:
			pets_counter-=1
			person_pet = person_pets[pets_counter]

			pet_id = person_pet[1]
			cur.execute("SELECT * FROM Pet WHERE id=%s"  % (pet_id))
			pet = cur.fetchone()

			pet_name = pet[1]
			pet_breed = pet[2]
			pet_age = pet[3]
			pet_alive = pet[4]

			if pet_alive:
				print  "%s owns %s %s, that is %s years old." % (person_name, pet_name, pet_breed, pet_age)
			else:
				print  "%s owned %s %s, that was %s years old." % (person_name, pet_name, pet_breed, pet_age)


