def main():
    num_par=int(input('How many participants would like to respond to the questionnaire?: '))
    par_file=open('Survey_responses_TAILOR_nct40.txt','a')
    for count in range(1,num_par+1): #loop to enter data of multiple users
        print(f'\n Enter data for paticipant #{count}: ')
        ans1=input('1. Do you feel that your guiding principles and priorities for a civil society are being represented by your local government? (Yes/No):\n')
        ans2=input('\n2. Which type of government do you think is doing a good job (meets your expectations)? (Local Municipality / State / Federal):\n')
        ans3=input('\n3. On a scale of 1-5, how well do you think your local municipal government is doing to keep your community safe?: \n')
        ans4=input('\n4. How well do you know what principles your state government is seeking to advance for your state? (Scale 1-5): \n')
        ans5=input('\n5. On a scale from 1-5 how well do you know about your local government ?: \n')
        ans6=input('\n6. In one week, how often do you interact with or observe local government officials in your community?: \n')
        ans7=input('\n7. How often do you look into the decisions being made by your local government?:  \n')
        ans8=input('\n8. What is your main source for quickly getting information about what your government is doing ?: \n')
        ans9=input('\n9. What other types of sources do you use? \n Internet source \n Word of mouth i.e., Local community members \n Local community board representatives/staff flyers \n Local Television / Radio \n International Media \n Choose from above given options: \n')
        ans10=input('\n10. Why do you choose this source? \n Convenience \n I Consider it reliable \n Others told me it is reliable \n No Particular Reason \n Choose from above given options: \n')
        a=id(count)# 'a' variable will contain the generated id of each participant
        par_file.write(f'\n Responses of Participant #{count} with id={a} \n')
        par_file.write(f'{ans1}\n')
        par_file.write(f'{ans2}\n')
        par_file.write(f'{ans3}\n')
        par_file.write(f'{ans4}\n')
        par_file.write(f'{ans5}\n')
        par_file.write(f'{ans6}\n')
        par_file.write(f'{ans7}\n')
        par_file.write(f'{ans8}\n')
        par_file.write(f'{ans9}\n')
        par_file.write(f'{ans10}\n')
    par_file.close()
if __name__=='__main__':
    main()


