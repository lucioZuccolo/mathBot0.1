#### Import previous weeks excel sheet
import pandas as pd
import math #for rounding numbers
from colorama import init #for colors in console
from colorama import Fore, Back, Style


init()

####################################################################################################################
####################################################################################################################
#########################         READING EXCEL SHEET                      #########################################
####################################################################################################################
####################################################################################################################

df = pd.read_excel('prueba6.xlsx', skiprows=1)
cols = list(df.columns.values)
print(cols)

players = df[4:len(df)-1].reset_index(drop=True)
print(players)
#players.index += 1 #i make it start in 1 as index
#players['THIS WEEK'] = players['THIS WEEK'].astype(int)

print('LOSERS')
losers = players.loc[players['THIS WEEK'] < -25]
losers = losers[[cols[0]]+[cols[2]]]
print(losers)


def runMathBot(fee, ryan, zane, austin):

    df = pd.read_excel("prueba6.xlsx", skiprows=1) #Insert here directory in your computer
    print('')
    print('')

    #Assign each column into a list 
    cols = list(df.columns.values)

    ###############################################################################################

    #Getting list of players
    players = df[4:len(df)-1].reset_index(drop=True)
    players.index += 1 #i make it start in 1 as index
    players['THIS WEEK'] = players['THIS WEEK'].astype(int) #make it round numbers

    ###############################################################################################

    #list of losers
    print('LOSERS')
    losers = players.loc[players['THIS WEEK'] < -25]
    losers = losers[[cols[0]]+[cols[2]]]
    losers = losers.sort_values('THIS WEEK', ascending=False).reset_index(drop=True)
    n_losers = losers.shape[0]
    #turn it into positive numbers
    for i in range(0,n_losers):
        losers.iloc[i,1] = -losers.iloc[i,1]
    print(losers)

    print('')

    ###############################################################################################

    #list of winners
    print('WINNERS')
    winners = players.loc[players['THIS WEEK'] > 25]
    winners = winners[[cols[0]]+[cols[2]]]
    winners = winners.sort_values('THIS WEEK', ascending = False).reset_index(drop=True)
    n_winners = winners.shape[0]

    #calculate profit
    total_win = 0
    for i in range(0,n_winners):
        wini = winners.iloc[i,1]
        total_win = total_win + wini
        
    total_lost = 0
    for i in range(0,n_losers):
        losti = losers.iloc[i,1]
        total_lost = total_lost + losti

    #adding fees and organizers into winners
    fees = fee  # float(input('Insert this week fees: '))
    fees_row = {'AGENT': 'fees', 'THIS WEEK': fees}
    winners = winners.append(fees_row, ignore_index=True)
    early_moneyR = ryan  # float(input('Amount paid early this week to Ryan: '))
    early_moneyZ = zane  # float(input('Amount paid early this week to Zane: '))
    early_moneyA = austin  # float(input('Amount paid early this week to Austin: '))

    profit_i = math.floor((total_lost - total_win - fees + early_moneyR + early_moneyZ + early_moneyA) / 3)
    organizer_1_row = {'AGENT': 'Ryan', 'THIS WEEK': profit_i - early_moneyR}
    organizer_2_row = {'AGENT': 'Zane', 'THIS WEEK': profit_i - early_moneyZ}
    organizer_3_row = {'AGENT': 'Austin', 'THIS WEEK': profit_i - early_moneyA}
    winners = winners.append(organizer_1_row,ignore_index=True)
    winners = winners.append(organizer_2_row,ignore_index=True)
    winners = winners.append(organizer_3_row,ignore_index=True)

    payment_extra = total_lost - total_win - fees - 3*profit_i  + early_moneyR + early_moneyZ + early_moneyA
    print('This is the money that was left in order to make round distribution between organizers: ' + str(payment_extra))
    print('')

    print(winners)

    print('')

    n_winners = winners.shape[0]

    ###############################################################################################

    #list of NotApplicable
    na = players.loc[(players['THIS WEEK'] > -25) & (players['THIS WEEK'] < 25)]
    na = na[[cols[0]]+[cols[2]]]
    na = na.sort_values('THIS WEEK', ascending = True).reset_index(drop=True)
    n_na = na.shape[0]
    #print(na)

    ####################################################################################################################
    ####################################################################################################################
    #########################                   PAYING ALGORITHM               #########################################
    ####################################################################################################################
    ####################################################################################################################

    count_w=0
    count_l=0

    for j in range(0,n_winners):
        if count_w == n_winners:
            break
        else:
            wini = winners.iloc[count_w,1]
        
        for i in range(0,n_losers):
            losti = losers.iloc[count_l,1]
            if losti >= wini and count_w < n_winners-1:
                tempwini = wini
                losti = losti - wini
                count_w = count_w + 1
                wini = winners.iloc[count_w,1]
                #print(Fore.WHITE + '1. ' + losers.iloc[count_l,0] + ' pays ' + str(tempwini) + ' to ' + winners.iloc[count_w-1,0] + ' and he still have ' + str(losti) + ' to pay another player')
                print(Fore.GREEN + losers.iloc[count_l,0] + ' pays ' + winners.iloc[count_w-1,0] + ' ' + str(tempwini))
                print('')
                if  losti <= wini and count_l < n_losers-1:
                    templosti = losti
                    wini = wini - losti
                    count_l = count_l + 1
                    losti = losers.iloc[count_l,1]
                    #print(Fore.WHITE + '2. ' + losers.iloc[count_l-1,0] + ' pays ' + str(templosti) + ' to ' + winners.iloc[count_w,0] + ' and the winner still needs to be paid ' + str(wini))
                    print(Fore.GREEN + losers.iloc[count_l-1,0] + ' pays ' + winners.iloc[count_w,0] + ' ' + str(templosti))
                    print('')
                else:
                    while losti > wini and count_w < n_winners-1:
                        tempwini = wini
                        losti = losti - wini
                        count_w = count_w + 1
                        wini = winners.iloc[count_w,1]
                        #print(Fore.WHITE + '3. ' + losers.iloc[count_l,0] + ' pays ' + str(tempwini) + ' to ' + winners.iloc[count_w-1,0] + ' and the loser still have to pay ' + str(losti) +' to another winner')
                        print(Fore.GREEN + losers.iloc[count_l,0] + ' pays ' + winners.iloc[count_w-1,0] + ' ' + str(tempwini))
                        print('')
                    if count_w < n_winners-1:
                        templosti = losti
                        wini = wini - losti
                        count_l = count_l + 1
                        #print(Fore.WHITE + '4. ' + losers.iloc[count_l-1,0] + ' pays ' + str(templosti) + ' to ' + winners.iloc[count_w,0] + ' and the winner still needs to be pay ' + str(wini))
                        print(Fore.GREEN + losers.iloc[count_l-1,0] + ' pays ' + winners.iloc[count_w,0] + ' ' + str(losti))
                        print('')
                    else :
                        losti = losti - wini
                        #print(Fore.WHITE + 'END '+ losers.iloc[count_l,0] + ' pays ' + str(wini) + ' to ' + winners.iloc[count_w,0] + ' and the loser still have to pay ' + str(losti))
                        print(Fore.GREEN + losers.iloc[count_l,0] + ' pays ' + winners.iloc[count_w,0] + ' ' + str(wini))
                        print('')
                        END1 = True
                        break
            else:
                if count_w == n_winners-1 and count_l == count_l and END1 == False:
                    count_w = count_w + 1
                    rest_payment = losti - wini
                    print(Fore.GREEN + losers.iloc[count_l,0] + ' pays ' + winners.iloc[count_w-1,0] + ' ' +str(wini))
                else:
                    if count_l < n_losers-1:
                        wini = wini - losti
                        count_l = count_l + 1
                        #print(Fore.WHITE + '5.' + losers.iloc[count_l-1,0] + ' pays ' + str(losti) + ' to ' + winners.iloc[count_w,0] + ' and there is ' + str(wini) + ' left to pay him')
                        print(Fore.GREEN + losers.iloc[count_l-1,0] + ' pays ' + winners.iloc[count_w,0] + ' ' + str(losti))
                        print('')
                    else:
                        break

###########################################################################