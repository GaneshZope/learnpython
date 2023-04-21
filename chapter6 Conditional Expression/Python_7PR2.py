sub1 = int(input("Enter the first subject marks \n:"))
sub2 = int(input("Enter the second subject marks\n :"))
sub3 = int(input("Enter the third subject marks \n:"))
sub4 = int(input("Enter the fourth subject marks\n :"))

if (sub4<33 or sub3<33 or sub2<33 or sub1<33):
    print ("Your fail because less than 33% in one the subject")

elif (sub1+sub2+sub3+sub4)/4<40:
    print ("Your fail due to total percentage are less than 40")
else :
    print ("Congratulations u are passed")