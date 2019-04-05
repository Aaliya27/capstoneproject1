#parent class
class ServiceManager:

		def __init__(self,account_name,email_id,account_id,address,phone_no):
			self.account_name=account_name
			self.email_id=email_id
			self.account_id=account_id
			self.address=address
			self.phone_no=phone_no

		def servicing(self, type_of_phone):
			print("How can we help you?\n\n\
				1.Body replacement\n\
				2.General servicing\n\
				3.Screen replacement\n")

			android = {"Body Replacement":10000, "General Servicing":1000, "Screen replacement":5000}
			ios = {"Body Replacement":30000, "General Servicing":5000, "Screen replacement":15000}

			select=int(input("Enter your option:"))

			if type_of_phone == 'Android':
				if select==1:
					print(f"You have opted for body replacement of your phone. \n\
						The bill amount will be {android['Body Replacement']}")


				elif select==2:
					print(f"You have opted for general servicing. \n\
						The bill amount will be {android['General Servicing']}")

				elif select==3:
					printf(f"You have opted for screen replacement of your phone. \n\
						The bill amount will be {android['Screen replacement']}")
				
				else:
					print("Enter the correct option")

			else:
				if select==1:
					print(f"You have opted for body replacement of your phone. \
						The bill amount will be {ios['Body Replacement']}")


				elif select==2:
					print(f"You have opted for general servicing. \
						The bill amount will be {ios['General Servicing']}")

				elif select==3:
					printf(f"Ypu have opted for screen replacement of your phone. \n\
						The bill amount will be {ios['screen replacement']}")
				
				else:
					print("Enter the correct option")


		def purchasing(self,type_of_phone):
			print("What would you like to buy?\n\n\
				1.android\n\
				2.ios\n")

			android = {"estimated minimum cost":6000}
			ios = {"estimated minimum cost":20000}

			select1=int(input("Enter your option: "))

			if select1==1:
				print(f"You have opted for purchasing an android phone. \n\
					The estimated amount will be {android['estimated minimum cost']}")

			elif select1==2:
				print(f"You have opted for purchasing an ios phone. \n\
					The estimated amount will be {ios['estimated minimum cost']}")
			else:
				print("Enter the correct option")

		# def screenreplacement(self,type_of_phone):
		# 	print("Welcome, let's replace your screen.Select your option:\n\n\
		# 		1.Android\n\
		# 		2.ios\n")

		# 	android = {"screen replacement":5000}
		# 	ios = {"screen replacement":15000}

		# 	select2=int(input("Enter your option:"))

		# 	if select2==1:
		# 		print(f"You have opted for screen replacement of your phone. \n\
		# 			The bill amount will be {android['screen Replacement']}")


		# 	elif select2==2:
		# 		print(f"You have opted for screen replacement. \n\
		# 			The bill amount will be {ios['screen replacement']}")
				
				
				
		# 	else:
		# 		print("Enter the correct option")



#child class 1
# class Android(ServiceManager):
# 	def __init__(self,account_name,email_id):
# 		self.account_name=account_name
# 		self.email_id=email_id



# # child class 2
# class Ios(ServiceManager):
# 	def __init__(self,account_name,email_id):
# 		self.account_name=account_name
# 		self.email_id=email_id


