
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
 
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
 
litres = 10
fat = 4.2
snf = 8.7
 
fat_steps = round((fat - STANDARD_FAT) / 0.1)
snf_steps = round((snf - STANDARD_SNF) / 0.1)
 
rate = (
BASE_RATE
+ (fat_steps * FAT_STEP_VALUE)
+ (snf_steps * SNF_STEP_VALUE)
)
 
payment = litres * rate
 
print("Fat Steps =", fat_steps)
print("SNF Steps =", snf_steps)
print("Rate =", rate)
print("Payment =", payment)
