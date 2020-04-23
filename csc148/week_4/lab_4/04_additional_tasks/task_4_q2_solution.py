from mystack import Stack

current_string = ''
undo_stack = Stack()
redo_stack = Stack()

print('Please type one of the following commands:')
print('REDO - redo undoed action')
print('UNDO - show previously registered string')
print('ADD - Add new string')
print('EXIT - exit program')

# 1. Prompt string
while True:
    print('Current string: {}'.format(current_string))
    print(undo_stack._items)
    response = input('>>> ')

    # 2. If user types 'EXIT', then exit program
    if response == 'EXIT':
        break
    # 3. If user types 'UNDO',
    elif response == 'UNDO':
        #   3.1 If stack for undo is empty, return nothing
        if undo_stack.is_empty():
            continue

        #   3.2 If stack for undo not empty, then pop an item, push a copy to
        #   redo and display value to user
        redo_stack.push(current_string)
        undo_popped_val = undo_stack.pop()
        current_string = undo_popped_val

    # 4. If user types 'REDO'
    elif response == 'REDO':
        #   4.1 If stack for redo is empty, return nothing
        if redo_stack.is_empty():
            continue

        #   4.2 If stack for redo not empty, then pop an item, push a copy to
        #   undo and display value to user
        undo_stack.push(current_string)
        redo_popped_val = redo_stack.pop()
        current_string = redo_popped_val

    else:
        undo_stack.push(current_string)
        current_string = response
        redo_stack = Stack()

