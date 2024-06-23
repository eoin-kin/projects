'''

This programme is one to be uploaded onto the arduino and will interface with the nfc tag and the file system locally in the unit.
It will write the info of the users into the sd card on a file system using a hashed version of the bank card number.
I chose this approach to add scalability to firebase later on when we move to a network model.

It will take an input of the card number and return an output of the loyalty level as seen be LEDs on the arduino.
The first time the card number is used it will call a registration function to create a new file for the user and return a loyalty level of 1

'''


if __name__ == "__main__":
    #importing necessary modules
    from Crypto.Hash import SHA384
    import os

    def LEDS(num_leds:int) -> None:
        """This will tell the arduino how many LEDs to activate.

        Args:
            num_leds (int): The loyalty level associated with a customer
        """       

        '''
        pin = d6
        library = fast leds
        
        ''' 
        
        print(num_leds)
    
    def NFC() -> int:
        """This function takes the data from the NFC card and interprets the bank card number

        Returns:
            int: Bank card number to be hashed.
        """        
        '''
        werner pn 532 reading bank card
        '''
    

    #a temporary input system
    number = str(90111353) #input("Enter card number:")

    #creating a hash of the input and converting it to a string
    '''
    COMPANY HAS ACCESS TO DE-HASH UNDER CURRENT RETENTION IMPLIMENTATION
    LOCK THE SENSITIVE DATA
    '''
    crypt = SHA384.new(bytes(number,'utf-8')).hexdigest()
    
    #opening our database of customers
    with open('./files/customer_records/customers.txt','r') as fp:
        customer_list = fp.read().split()

    #checking if they're a new customer
    if crypt not in customer_list: #if they're a new customer
        #add them to the database
        with open('./files/customer_records/customers.txt','a') as fp:
            fp.write('\n'+crypt)
        #create the file for the customer
        init = str(crypt)+'.txt'
        with open(os.path.join('./files./customer_records', init), 'w') as fp:
            #first digit is loyalty level, second is full cards.
            fp.write("1\n0")
        
        #reading the loyalty level and displaying the number of leds
        with open(os.path.join('./files./customer_records', init), 'r') as fp:
            loyalty = fp.read().split()[0]
            LEDS(loyalty)

    
    #handling returning customers
    else:
        #accessing the customer records
        init = str(crypt)+'.txt'
        with open(os.path.join('./files./customer_records', init), 'r') as fp:
            #initialising variables
            file = fp.read().split()
            loyalty = int(file[0])
            full_cards  = int(file[1])
            loyalty += 1

            #handling a full card
            if loyalty == 10:
                LEDS(loyalty)
                loyalty = 0
                full_cards += 1

            #handling non full card transaction
            else:
                LEDS(loyalty)
                new_file = str(loyalty) + '\n'+ str(full_cards)
                with open(os.path.join('./files./customer_records', init), 'w') as fp:

                    #updating the customer records
                    fp.write(new_file)


            