balance = 1000
print(f'You have {balance} SEK.')
amount = int(input('How much you want to withdraw (only 100 SEK bills available)? '))
if amount % 100 == 0 and amount <= balance:   
     balance -= amount    
     print(f'Your new balance is {balance}')
else:    
    print('Not accepted. ')  

print('  -> Only 100 SEK bills available')   
print('  -> You can only withdraw less than your current balance')