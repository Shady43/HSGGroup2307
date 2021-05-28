import datetime # integrate the basic library that is already provided by python


def read_csv():
    # read_csv function opens csv file and returns the integrated tuple of data
    # open csv file and encode it with the 8-bit Unicode (below utf8)
    with open("Covid Data Complet Python.csv", "r", encoding="utf8") as f:
        # get and read all lines from the file. With the code below we started to clean the data and make the
        # data points more comprehensive for us, to be able to further work with them in the follow-up code
        content = f.readlines()
        new = []
        # first line are the titles, therefore we store them separatly
        # remove \n at the end of each line and
        titles = content[0].replace("\n", "")
	# separate titles from data for further calculations
        content.pop(0)
        # loop for each line in file
        for line in content:
            # remove present \n at the end of each line
            line = line.replace("\n", "")
            # split line by comma to get separated data
            newline = line.split(',')
            # Convert date string in fourth column to datetime object and define back to a string
            # with format mm/dd/yyyy to fix any inconsistency in date (for example 2/2/2020 instead of 02/02/2020)
            # so the user can insert both options, and does not have to consider/input one exact date, but the
            # date format of his choice (with the dates below)
            date = newline[3]
            date = datetime.datetime.strptime(date, "%m/%d/%Y")
            date = date.strftime("%m/%d/%Y")
            newline[3] = date
            # column five to last are numeric data which can be empty, therefore we replace it with 0
            for i in range(4, len(newline)):
                if newline[i] == "":
                    newline[i] = 0
            new.append(newline)
        # return the tuple with titles as first element and data as second element
        return (titles, new)
    # return empty data
    return ([], [])

    # Here we print/show the user the available countries he can choose from. We chose this approach to limit
    # the data, but also to provide the user the options. Else, the user would have no idea, from which countries
    # he can choose the data from.
def print_avaibale_countries(countries):

    print("Available Countries:")
    # loop through all countries list to print name of along with index like "1.1. Albania"
    for i in range(0, len(countries)):
        print("1."+str(i+1)+".  "+countries[i])
        # above, we also added the code/function that creates the index, we will use below, when the user choses
        # the specific country for the data


def print_options(options):
    # print available options for the user, that he can choose/that are available
    print("Available Options: ")
    # loop from zero to length of options list to print option name along with index like "3.1. Death Rate"
    for i in range(0, len(options)):
        print("3."+str(i+1)+".  "+options[i][0])
        # here we used the same logic as above, to show the user, what options we can provide, indexed dynamically

    # here we provide the user the chosen data
def showOutput(title, output):
    # receives output data to show as argument and print data in the form of table
    print(f"{title[0]:>35}|{title[1]:>20}")
    print("-------------------------------------------------------") # this is for design reasons
    for row in output:
        print(f"{row[0]:>35}|{row[1]:>20}")

    # this code below runs in the background. As we created a file, where we want to store all requests made from
    # the user (i.e. if he wants to work with them later, because in python we just & only show the data, but
    # if the user wants to use them, he can do so with our created CSV. file with the requested data
def saveOutput(title, output):
    # receives data and write it in file
    # open out.csv in append mode (append mode because we want to save the requests and not overwrite!
    f = open("out.csv", 'a')
    # Write the recieved data in the csv.file
    f.write("\n")
    f.write(f"{title[0]},{title[1]}\n")
    for row in output:
        f.write(f"{row[0]},{row[1]}\n")


def showOutput_switz(title, output, switz):
    # receives output data along with data of switzerland and prints data in the form of a table
    print(
        f"{title[1]:>35}|{title[0]:>25}|{'Switzerland':>25}|{'Percentage':>20}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(0, len(output)):
        out = output[i]
        sw = switz[i]
        # handle case where data is zero to avoid division by zero. Luckily we found that case while testing
        if float(sw[1]) == 0:
            per = 0
        else:
            per = (float(out[1])-float(sw[1]))/float(sw[1])
        per *= 100
        # round percentage up to two decimals
        per = round(per, 2)
        # print data
        print(f"{out[0]:>35}|{out[1]:>25}|{sw[1]:>25}|", end="")
        p_out = ""
        # check if positive/negative percentage value to give answer if switzerland has an increasing or decreasing value
        if per >= 0:
            p_out = "Switzerland has "+str(per)+f"% less {out[0]}"
        else:
            per = -1*per
            p_out = "Switzerland has "+str(per)+f"% more {out[0]}"
        print(f"{p_out:>20}")


def Output_switz(country, menu_options, date, titles, data):
    # generates chosen output (country & option) and switzerland list with selected options, country and required date
    # for the comparison
    title = [country, date]
    output = []
    switz = []
    # loop through data of Switzerland to get complementing data
    for row in data:
        # check date
        if row[3] == date:
            # check country
            if row[2] == country:
                # save data of required options
                for option in menu_options:
                    op_name = option[0]
                    op_value = row[option[1]]
                    output.append([op_name, op_value])
            elif row[2] == "Switzerland":
                # save data of required options for switzerland
                for option in menu_options:
                    op_name = option[0]
                    op_value = row[option[1]]
                    switz.append([op_name, op_value])
    # check if no data was found for switzerland to compare
    if switz == []:
        print("Switzerland does not have any data for the chosen date!")
    else:
        # call showoutput_switz to print the desired data
        showOutput_switz(title, output, switz)


def Output(country, menu_options, date, titles, data):
    # creates output list from data for required country and specific date
    title = [country, date]
    output = []
    for row in data:
        # compare date and country
        if row[3] == date and row[2] == country:
            # save required options data
            for option in menu_options:
                op_name = option[0]
                op_value = row[option[1]]
                output.append([op_name, op_value])
    showOutput(title, output)
    saveOutput(title, output)


# titles and data returned from read_csv
titles, data = read_csv()
# countries list which we have defined upfront, to limit the list
# this is limited, because we wanted to show the user, what countries he could choose from, and as the list should
# not be too long, else the user would not be able/it would not be practical to scroll through a long list
countries = ['Africa', 'Albania', 'Andorra', 'Austria', 'Belgium',
             'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czechia', 'Denmark',
             'Estonia', 'Greece', 'Greenland', 'Hungary', 'Iceland',
             'Ireland', 'Israel', 'Italy', 'Kazakhstan', 'Liechtenstein',
             'Luxembourg', 'Netherlands', 'Poland', 'Portugal', 'Romania',
             'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom',
             ]
# options list containing name and its index predefined in the Covid-data file
options = [("Total cases", 4), ("New Cases (day)", 5), ("Total deaths", 7), ("New deaths (day)", 8),
           ("Total Cases per Million", 10), ("Reproduction Rate",
                                             16), ("Hospitalization Patients", 18),
           ("Positive Rate", 31), ("People vaccinated",
                                   35), ("People fully vaccinated", 36),
           ("New vaccinations", 37), ("People fully vaccinated per hundred", 41),
           ("Population", 44), ("GDP per capita", 49), ("Life expectancy", 57), ("Human development index", 58)]
# split titles string to get all titles
titles = titles.split(",")
print("Welcome to our COVID Simulator! Stay healthy!")
# print available countries
print_avaibale_countries(countries)


# this is the main user-process to choose from the available options/countries/dates
while True:
    # input country number
    num = input("Enter a Country Number (between 1 and " +
                str(len(countries))+"): ")
    # handle invalid input
    try:
        num = int(num)
    except:
        print("Invalid Input")
        continue
    # if input is within range then input the possible options
    if num in range(1, len(countries)+1, 1):
        print_options(options)
        menu_options = []
        date = None
        while True:
            # input option
            menu_options = []
            inp_options = input(
                "Enter option numbers(between 1 and "+str(len(options))+") separated by comma: ")
            # split input by comma
            inp_options = inp_options.split(',')
            invalid = False
            # validate all options the user has inserted
            for option in inp_options:
                try:
                    option = int(option)
                except:
                    invalid = True # if there is an invalid input/chosen option, the user gets the message and can try again
                    print("Invalid Input ", option, " !!")
                    break
                if option not in range(1, len(options)+1, 1):
                    invalid = True
                    print("Option", option, "is not in available options")
                    break
                else:
                    menu_options.append(options[option-1])

            if invalid == False:
                break
        # if the chosen options are valid then we will continue here with the date
        while True:
            # input date
            date = input("Enter your desired date (mm/dd/yyyy):")
            # validate date
            try:
                date = datetime.datetime.strptime(date, "%m/%d/%Y")
            except:
                print("Invalid date. Please try again!")
                continue
            # check if the chosen date exists for the chosen country
            date = date.strftime("%m/%d/%Y")
            if date not in [row[3] for row in data if row[2] == countries[num-1]]:
                print("Date", date, "is not present in available dates")
                continue
            break
        # call output function to calculate, print and save output for required country, options and date
        Output(countries[num-1], menu_options, date, titles, data)
        # ask if user wants to compare his chosen country & data with switzerland
        compare = input("Do you want to compare your data with Switzerland (y/n)?: ")
        if compare == "Y" or compare == "y":
            # if yes then call outputswitz to calculate and print data in comparison with switzerland
            Output_switz(countries[num-1], menu_options, date, titles, data)
        cont = input("Do you want to continue(y/n): ") # with this function, we want to enable the user to start over again
        if cont == "Y" or cont == "y":
            continue
        else:
            break
    else:
        print("Invalid Input! Please try again.")
