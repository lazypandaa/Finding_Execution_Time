import time

initial = time.time()
k = 0
while(k<45):
    k = k+1
    print("This is Eswar")
print("While loop ran i n", time.time()- initial,"Seconds")


initial2 = time.time()
for i in range(45):
    print("This is Eswar")

print("While loop ran i n", time.time()- initial2,"Seconds")
loacltime =  time.asctime(time.localtime(time.time()))
print(loacltime)
