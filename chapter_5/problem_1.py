
from random import randint 

'''
Խնդիր։ Գրել ծրագիր, որը գեներացնում է [1,10] միջակայքից որևէ պատահական ամբողջ թիվ, 
իսկ ծրագրորդը փորձում է կռահել այդ թիվը: 
Ծրագիրը պետք է տա հաղորդագրություն այն մասին, թե ծրագրորդն արդյոք կռահե՞լ է թիվը, 
թե՞ ոչ, և արտածի գեներացված պատահական թիվը:
'''

number=randint(1,10) # գեներացվում է պատահական ամբողջ թիվ
num=eval(input('Enter your number: ')) #ծրագրորդի մուտքագրած թիվը

if num==number:
    print('You won. The random number=', number)
else:
    print('You didn\'t guess. The random number =', number)
