people, chicken = map(int, input().split())

if chicken > people:
  leftovers = chicken - people
  if leftovers == 1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
  else:
    print("Dr. Chaz will have", leftovers, "pieces of chicken left over!")

else:
  needed = people - chicken 
  if needed == 1:
    print("Dr. Chaz needs 1 more piece of chicken!")
  else:
    print("Dr. Chaz needs", needed, "more pieces of chicken!")