import argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="sum of two number")
	parser.add_argument('--number1',help='first number')
	parser.add_argument('--number2',help='secondnumber')
	parser.add_argument('--o','--operation',help='operation')
	args=parser.parse_args()
	print(args.number1)
	print(args.number2)
	print(args.operation)
	n1=int(args.number1)
	n2=int(args.number2)
	result=none
	if args.operation == "add":
		result=n1+n2
	elif args.operation == "subtract":
		result=n1-n2
	elif args.operation == "multiply":
		result=n1*n2
	else:
		print("unsupported")
	print(result)

	#main()