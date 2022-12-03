#导入时间包
import time

#获取当前时间
currentTime = time.time()

#获取总秒数
totalSecond = int(currentTime)

#求出现在的秒数
currentSecond = totalSecond % 60

#求出总分钟数
totalMinutes = totalSecond // 60

#求当前分钟数
currentMinute = totalMinutes % 60


#求总小时数
totalHours = totalMinutes // 60

#求当前小时数
currentHour = totalHours % 24

#计算机时间不是北京时间，时区相差8个小时，因此小时+8就转换为北京时间
print("当前时间为：",currentHour+8,"小时",currentMinute,"分钟",currentSecond,"秒")