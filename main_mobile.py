from mobile import ServiceManager

accounts={}
account_id=1
print("Welcome to Service Centre")


while True:
	print("Hello! What can we help you with?\n\n\
		1.Create Profile\n\
		2.Acess services\n\
		3.Purchasing\n\
		4.Deliver mobiles\n\
		5.Exit\n")

	choice = int(input("Enter your option: "))

	if choice==1:
		account_name=input("Enter an Account Name: ")
		email_id=input("Enter an email id:")
		address=input("Enter your address: ")
		phone_no=input("Enter your phone number: ")

		accounts[account_id] = ServiceManager(account_name,email_id,account_id,address,phone_no)
		print(f"Account created successfully! Your Account id is {account_id}")
		account_id +=1


	elif choice==2:
		uid=int(input("Enter the Account id: "))

		if uid in accounts.keys():
			print(f"Welcome {accounts[uid].account_name}")


			print("Select your Operating System\n\n\
				1.Android\n\
				2.iOS\n")

			choices=int(input("Enter your option:"))

			if choices==1:
				print("Welcome to your Android services")

				accounts[uid].servicing('Android')

			else:
				print("Welcome to your Ios services")
				accounts[uid].servicing('iOS')
		else:
			print("Enter proper Account ID")

	elif choice==3:
		uid=int(input("Enter the Account id: "))

		if uid in accounts.keys():
			print(f"Welcome {accounts[uid].account_name}")


			print("Select your Operating System\n\n\
				1.Android\n\
				2.iOS\n")

			choices1=int(input("Enter your option:"))

			if choices1==1:
				print("Welcome to your Android services")

				accounts[uid].purchasing('Android')

			else:
				print("Welcome to your Ios services")
				accounts[uid].purchasing('iOS')
		else:
			print("Enter proper Account ID")

	elif choice==4:

		print("We are always happy to deliver our services to you")
		
		print("Thank you. We will be reaching you shortly :D")


	else:
		break
		# print("\n\nOops! Enter the correct option")


		# if account_id in accounts.keys():
		# 	delivery=account[account_id].delivermobile(account_id,address)
		# 	print("Delivery on the way")
