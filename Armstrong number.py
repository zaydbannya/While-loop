num=int(input("enter a number whose sum you want to find"))
sum=0
temp=num
while temp>0:
 digit=temp%10
 sum+=digit**3
 temp//=10
if num==sum:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")