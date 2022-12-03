#将一定数量的钱，分类成几个更小的货币单元，让用户输入总金额，程序来进行分配，并生成结果报告Page75

#提示用户输入一个十进制的带小数点的数组，例如：11，56
amount = eval(input("请输入钱数（如：11.56）:"))
#将钱数（11，56）转换成分数（1156）
renainingAmount = int(amount *100)
#将分数除以100得到美元个数，使用分数%100得到余数即是剩余的分数
numberOfOneDollars = renainingAmount // 100
renainingAmount = renainingAmount % 100
#将剩余的分数除以25得到两角五分硬币的个数，使用分数%25得到余数即是剩余的分数
numberOfQuarters = renainingAmount // 25
renainingAmount = renainingAmount % 25
#将剩余的分数除以10的到一角硬币的个数，使用分数%10得到的余数即是剩余的分数
numberOfDimes = renainingAmount // 10
renainingAmount = renainingAmount % 10
#将剩余的分数除以5得到五分硬币的个数，使用分数%5得到的余数即是剩余的分数
numberOfNickels = renainingAmount // 5
renainingAmount = renainingAmount % 5
#剩余的分数就是一美分的硬币数
numberOfPennies = renainingAmount

#显示结果
print("你输入的总金额为：",amount,"拆分后为：\n",
      "\t",numberOfOneDollars,"个美元\n",
      "\t",numberOfQuarters,"个两角五分硬币\n"
      "\t",numberOfDimes,"个一角硬币\n"
      "\t",numberOfNickels,"个五分硬币\n"
      "\t",numberOfPennies,"个一分硬币"
      )
