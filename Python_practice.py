#counties=["Arapahoe","Denver","Jefferson"]
#for county in counties:
 #   print(county)






#if "El Paso" in counties:
 #   print("El Paso is in the list of counties")
#else:
#    print("El Paso is not in the list of counties")





#if counties[1]=='Denver':
 
 #   print(counties[1])


counties_dict={"Arapahoe":422829, "Denver":463353,"Jefferson":432438}
for key, value in counties_dict.items():
    #print(key," county has ", value, " registered voters")
    print(f"{key} county has {value:,} registered voters.")


