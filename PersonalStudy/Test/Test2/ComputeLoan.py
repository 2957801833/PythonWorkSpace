#提示用户输入：年利率、贷款数、贷款年限、贷款额度
#输入的年利率是百分比的数字，例如：4.5% 程序需要将它除以100转换为小数。
annualInterestRate = eval(input("请输入年利率的百分比，例如7.25  "))
# 因为一年有12个月，所以将年利率除以12即月利率，所以为了获取月利率，需要将百分比格式的年利率除以1200
# 例如：如果年利率是4.5%，那么月利率就是4.5/1200=0.00375
monthlyInterestRate = annualInterestRate / 1200

#提示用户输入贷款年限
numberOfYears = eval(input("请输入贷款年限，数字为整数，例如：5  "))

#提示用户输入贷款金额
loanAmount =eval(input("请输入贷款金额，例如：12000.95  "))

#计算月供
monthlyPqyment = loanAmount * monthlyInterestRate /(1-1/(1+monthlyInterestRate)**(numberOfYears*12))

#通过将月供乘以12再乘以贷款年限计算出还款总额
totalPayment = monthlyPqyment * numberOfYears * 12

#显示月供和还款总额，保留小数点后两位
#月供
print("所需还款月供为：",int(monthlyPqyment * 100 )/100)

#还款总额
print("所需还款总额为：",int(totalPayment * 100)/100)
