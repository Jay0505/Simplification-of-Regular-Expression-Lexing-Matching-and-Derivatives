import sys
from node import Node

class ConstructTree(object):
	"""docstring for ConstructTree"""
	def __init__(self, inputRegexString):
		self.operatorStack = [] 		# contents are of only string type
		self.operandStack = [] 			# contents are of only string type
		self.bracketsStack = []			# contents are of only string type [ '(' and ')']
		self.nodeStack = []				# contents are of only node type
		self.temporaryStack = []		# contents are of only node type
		self.temporaryStackUsedWhileConcatenating = [] # contents are of only node type
		self.inputRegexString = inputRegexString
		self.stackNumber = 0
		self.listOfOperators = ['+', '*', ')', '(']


	def construct_Tree(self):
		lengthOfTheInputRegexString = len(self.inputRegexString)
		noOfCharactersToBeScanned = lengthOfTheInputRegexString

		while noOfCharactersToBeScanned > 0:
			noOfCharactersToBeScanned -= 1

			if self.inputRegexString[noOfCharactersToBeScanned] not in self.listOfOperators:
				self.operandStack.append(self.inputRegexString[noOfCharactersToBeScanned])

				if noOfCharactersToBeScanned == 0:



	def check_The_Count_Of_All_The_Stacks(self):
		if len(self.operandStack) != 0 and len(self.operandStack) == 0 and len(self.nodeStack) == 0 and len(self.bracketsStack) == 0:


# 	def constructTreeFromTheInputString(self):

# 		noOfCharactersToBeScanned = len(self.inputRegexString)

# 		for character in self.inputRegexString:
# 			noOfCharactersToBeScanned -= 1

# 			if self.inputRegexString[noOfCharactersToBeScanned] == ")":

# 				if noOfCharactersToBeScanned == len(self.inputRegexString) - 1:

# 					if len(self.operatorStack) == 0 and len(self.operandStack) != 0:
# 						concatenate_Operand_And_Node_Stack_Element_When_Zero_Operators()
# 						while  len(self.nodeStack) != 0: 
# 							self.temporaryStack.append(self.nodeStack.pop())





# 	def auxillaryConstructTree(self):
# 		if len(self.bracketsStack) < 2:

# 			if len(self.operatorStack) ==0:

# 				if len(self.operandStack) != 0 and len(self.nodeStack) == 0:
# 					concatenate_Contents_Of_The_Operand_Stack_And_Push_Onto_Node_Stack()

# 				if len(self.operandStack) != 0 and len(self.nodeStack) != 0:
# 					concatenate_Operand_And_Node_Stack_Element_When_Zero_Operators()

# 				if len(self.operandStack) == 0 and len(self.nodeStack) != 0:

# 					if len(self.nodeStack) >= 2:
# 						concatenate_Node_Stack_elements_When_Zero_Operand_And_Operator_Elements()


# 			else:
# 				when_Star_Or_Other_Operators_Encountered_And_It_Is_Last()



# ######################################

# 	def concatenate_Contents_Of_The_Operand_Stack_And_Push_Onto_Node_Stack(self):
# 		if len(self.operandStack) == 1:
# 			nodeWithOperandStContentsConcatenated = concatenate_Contents_Of_A_Stack_With_Each_Other(self.operandStack)
# 			self.nodeStack.append(nodeWithOperandStContentsConcatenated)

# 		if len(self.operandStack) >= 2:
# 			concatenationOperatorNode = Node("~")
# 			nodeWithOperandStContentsConcatenated = concatenate_Contents_Of_A_Stack_With_Each_Other(self.operandStack)
# 			concatenationOperatorNode.firstChild = nodeWithOperandStContentsConcatenated
# 			self.nodeStack.append(nodeWithOperandStContentsConcatenated)



# 	def concatenate_Operands_With_Each_Other(self, stackWhoseContentsToBeConcatenated):
# 		firstOperand = stackWhoseContentsToBeConcatenated.pop()
# 		firstOperandNode = Node(firstOperand)

# 		tempNode = firstOperandNode
# 		while len(stackWhoseContentsToBeConcatenated) != 0:
# 			tempOperand = stackWhoseContentsToBeConcatenated.pop()
# 			tempOperandNode = Node(tempOperand)
# 			tempNode.nextChild = tempOperandNode
# 			tempNode = tempOperandNode

# 		return firstOperandNode

# ############################################################################

# 	def concatenate_Contents_Of_A_Stack_With_Each_Other(self, stackWhoseContentsToBeConcatenated):
# 		if len(stackWhoseContentsToBeConcatenated) == 1:
# 			onlyItemInTheStack = stackWhoseContentsToBeConcatenated.pop()
# 			onlyItemInTheStackNode = Node(onlyItemInTheStack)
# 			return onlyItemInTheStackNode

# 		elif len(stackWhoseContentsToBeConcatenated) >= 2:
# 			nodeWithAllTheNodesConcatenated = concatenate_Operands_With_Each_Other(stackWhoseContentsToBeConcatenated)
# 			return nodeWithAllTheNodesConcatenated




# 	def concatenate_Operand_And_Node_Stack_Element_When_Zero_Operators(self):
# 		concatenationNode = Node("~")

# 		if len(self.operandStack) != 0:
# 			NodeWithOperandStContentsConcatenated = concatenate_Contents_Of_A_Stack_With_Each_Other(self.operandStack)

# 		if len(self.nodeStack) != 0:
# 			NodeWithNodeStContentsConcatenated = concatenate_Contents_Of_A_Stack_With_Each_Other(self.nodeStack)

# 		concatenationNode.firstChild = NodeWithOperandStContentsConcatenated
# 		concatenationNode.firstChild.nextChild = NodeWithNodeStContentsConcatenated

# 		self.nodeStack.append(concatenationNode)




# 	def concatenate_Contents_Of_The_Operand_Stack(self):
# 		pass



# 	def concatenate_Node_Stack_elements_When_Zero_Operand_And_Operator_Elements(self):
# 		pass


# 	def when_Star_Or_Other_Operators_Encountered_And_It_Is_Last_In_The_Operator_Stack(self):
		


# 	def concatenate_Node_Stack_Elements_When_Zero_Operand_And_Operator_Stack_Elemets(self):
# 		pass


# 	def when_Star_Operator_Encountered(self):
# 		starNode = Node('*')

# 		if len(self.nodeStack) == 1:

# 			create_A_Node_Element_When_Star_Operator_Encountered()

# 		else:
# 			concatenate_Node_Stack_Elements_When_Zero_Operand_And_Operator_Stack_Elemets()
# 			create_A_Node_Element_When_Star_Operator_Encountered()


# 	def create_A_Node_Element_When_Star_Operator_Encountered(self):
# 		starNode = Node('*')

# 		onlyNodeInNodeStack = self.nodeStack.pop()
# 		starNode.firstChild = onlyNodeInNodeStack
# 		onlyNodeInNodeStack.parentNode = starNode
# 		self.nodeStack.append(starNode)


