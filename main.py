# Python program for creating your own lorcana collection

# Imports
from rich.console import Console
import csv
import os

# Setup 
console = Console()

collection_path = "CSV/collection.csv"
new_cards_path = "CSV/new_cards.csv"

# Functions
class CSV():
       def __init__(self, file):
              self.file = file

       def read_rows(self):
              with open(self.file, mode='r') as file:
                     csv_reader = csv.DictReader(file)

                     data_list = []

                     for row in csv_reader:
                            data_list.append(row)

                     return data_list
              
       def read_columns(self):
              with open(self.file, mode='r') as file:
                     csv_reader = csv.reader(file, delimiter=",")

                     columns = []
                     for row in csv_reader:
                            columns.append(row)
                            break
                     columns = columns[0]

                     return columns
              
       def find_row(self, row={'Set Number': None, 'Card Number': None, 'Variant': None, 'Count': None}):
              rows = self.read_rows()

              
              for finder in rows:
                     if (finder["Set Number"] == row["Set Number"] and finder["Card Number"] == row["Card Number"] and finder["Variant"] == row["Variant"]):
                            return rows.index(finder)
                            
              return -1
                     

              
       def add_row(self, content={'Set Number': None, 'Card Number': None, 'Variant': None, 'Count': None}):
              fieldnames = self.read_columns()
              rows = self.read_rows()

              new_row = None
              if (self.find_row(content) >= 0):
                     new_row = rows[self.find_row(content)]
                     rows.pop(self.find_row(content))
                     
                     new_row["Count"] = str(int(new_row["Count"]) + int(content["Count"]))
              else:
                     new_row = content

              with open(self.file, 'w') as file:
                     csv_writer = csv.DictWriter(file, fieldnames)

                     csv_writer.writeheader()
                     csv_writer.writerows(rows)

                     csv_writer.writerow(new_row)

       def del_row(self, content={'Set Number': None, 'Card Number': None, 'Variant': None, 'Count': None}):
              fieldnames = self.read_columns()

              rows = self.read_rows()

              print("Deleting")

              if (self.find_row(content) != -1):
                     new_row = rows[self.find_row(content)]
                     rows.pop(self.find_row(content))
                            
                     new_row["Count"] = str(int(new_row["Count"]) - int(content["Count"]))

                     if (int(new_row["Count"]) > 0):
                            with open(self.file, 'w') as file:
                                   csv_writer = csv.DictWriter(file, fieldnames)

                                   csv_writer.writeheader()
                                   csv_writer.writerows(rows)

                                   csv_writer.writerow(new_row)
                     else:
                            with open(self.file, 'w') as file:
                                   csv_writer = csv.DictWriter(file, fieldnames)

                                   csv_writer.writeheader()
                                   csv_writer.writerows(rows)

collection = CSV(collection_path)
new = CSV(new_cards_path)

while True:
       os.system("clear")
       console.print("")
       console.print("[bold][#CCCCFF]▒█░░░ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ ")
       console.print("[bold][#CCCCFF]▒█░░░ ▒█░░▒█ ▒█▄▄▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ")
       console.print("[bold][#CCCCFF]▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▒█░░▀█ ▒█░▒█")
       console.print("[bold][#E0B0FF] By @tomparik")
       console.print("")

       console.print("[bold][#CCCCFF]Menu: ")
       console.print("[bold][#CCCCFF]~ '[#E0B0FF]A[#CCCCFF]' = add new cards to collection and newcards ")
       console.print("[bold][#CCCCFF]~ '[#E0B0FF]D[#CCCCFF]' = delete cards from collection and newcards ")
       console.print("[bold][#CCCCFF]~ '[#E0B0FF]E[#CCCCFF]' = exit program ")
       console.print("")

       choice = console.input("[bold][#CCCCFF]What do you want to do ([#E0B0FF]A[#CCCCFF]/[#E0B0FF]D[#CCCCFF]/[#E0B0FF]E[#CCCCFF]): ")

       if (choice.upper() == "A"):
              console.print("[bold][#CCCCFF]Starting [#E0B0FF]adding cards[#CCCCFF]!")

              console.print("")
              sure = console.input("[bold][#CCCCFF]Are you [#E0B0FF]sure[#CCCCFF] you want to [#E0B0FF]add cards[#CCCCFF], the [#E0B0FF]old newcards.csv[#CCCCFF] will be [#E0B0FF]erased[#CCCCFF] ([#E0B0FF]Y[#CCCCFF]/[#E0B0FF]N[#CCCCFF]): ")

              if (sure.upper() == "Y"):
                     if (os.path.exists(new_cards_path) == True):
                            os.remove(new_cards_path)
                     with open(new_cards_path, 'a') as new_cards:
                            new_cards.write("Set Number,Card Number,Variant,Count")

                     console.print("[bold][#E0B0FF]Okay[#CCCCFF], now you can add cards!")
                     console.print("")

                     console.print("[bold][#CCCCFF]~ Put the card values in this order '[#E0B0FF]Card[#CCCCFF]-[#E0B0FF]Number Set[#CCCCFF]-[#E0B0FF]Number Variant Count'")
                     console.print("[bold][#CCCCFF]~ [#E0B0FF]Variant[#CCCCFF] = '[#E0B0FF]f[#CCCCFF]/[#E0B0FF]1[#CCCCFF]' for foil and '[#E0B0FF]n[#CCCCFF]/[#E0B0FF]0[#CCCCFF]' for normal")
                     console.print("[bold][#CCCCFF]~ If you don't type [#E0B0FF]any Count[#CCCCFF] the Count Number is [#E0B0FF]1")
                     console.print("[bold][#CCCCFF]~ You [#E0B0FF]end[#CCCCFF] the adding procces by typing '[#E0B0FF]stop[#CCCCFF]'")
                     console.print("[bold][#CCCCFF]~ You [#E0B0FF]delete[#CCCCFF] the last card added by typing '[#E0B0FF]back[#CCCCFF]'")
                     console.print("[bold][#CCCCFF]~ You [#E0B0FF]preset[#CCCCFF] the set to a specific number by typing '[#E0B0FF]set number[#CCCCFF]'")
                     console.print("[bold][#CCCCFF]~ You [#E0B0FF]unset[#CCCCFF] the set by typing '[#E0B0FF]set 0[#CCCCFF]'")
                     console.print("[bold][#CCCCFF]~ The cards are [#E0B0FF]automatically [#CCCCFF]saved")
                     console.print("")

                     splitter = console.input("[bold][#CCCCFF]Choose with which [#E0B0FF]character[#CCCCFF] you want to [#E0B0FF]split[#CCCCFF] the Number, Set, etc.: ")

                     if (splitter == ""):
                            splitter = " "

                     console.print(f"[bold][#CCCCFF]You chose '[#E0B0FF]{splitter}[#CCCCFF]' character")
                     console.print("")

                     console.print("[bold][#CCCCFF]The [#E0B0FF]adding[#CCCCFF] process: ")

                     first = True
                     values = {}
                     set_value = None

                     while True:
                            console.print("")
                            values_input = console.input("[bold][#CCCCFF]New [#E0B0FF]card[#CCCCFF]: ")

                            if (values_input.lower() == "back"):
                                   console.print("[bold][#CCCCFF]The last cards [#E0B0FF]won't be[#CCCCFF] added!")
                                   values = {}
                                   first = True
                                   continue
                            
                            elif (isinstance(values, list)):
                                   pass

                            else:
                                   if (first == True):
                                          first = False
                                   else:
                                          collection.add_row(values)
                                          new.add_row(values)

                            if (values_input.lower() == "stop"):
                                   console.print("")
                                   console.print("[bold][#E0B0FF]Saved[#CCCCFF]!")
                                   console.input("[bold][#E0B0FF]Exit [#CCCCFF]program ")
                                   break

                            if (values_input.lower().find("set") >= 0):
                                   values = values_input.split(" ")

                                   if (values[1] == "0"):
                                          set_value = None
                                          console.print(f"[bold][#CCCCFF]The set will be [#E0B0FF]unset")
                                   else:
                                          set_value = values[1]
                                          console.print(f"[bold][#CCCCFF]The set will be [#E0B0FF]{set_value}")

                                   continue


                            values = values_input.split(splitter)

                            if (set_value == None):
                                   if (len(values) == 3):
                                          values = {'Set Number': values[1], 'Card Number': values[0], 'Variant': values[2], 'Count': "1"}
                                   else:
                                          values = {'Set Number': values[1], 'Card Number': values[0], 'Variant': values[2], 'Count': values[3]}
                            else:
                                   if (len(values) == 2):
                                          values = {'Set Number': set_value, 'Card Number': values[0], 'Variant': values[1], 'Count': "1"}
                                   else:
                                          values = {'Set Number': set_value, 'Card Number': values[0], 'Variant': values[1], 'Count': values[2]}

                            if (values["Variant"] == "f" or values["Variant"] == "1"):
                                   values["Variant"] = "foil"
                            else:
                                   values['Variant'] = "normal"

                            console.print(f"[bold][#CCCCFF]Adding = Card: [#E0B0FF]{values['Card Number']} [#CCCCFF]/ Set: [#E0B0FF]{values['Set Number']} [#CCCCFF]/ Var: [#E0B0FF]{values['Variant']} [#CCCCFF]/ Count: [#E0B0FF]{values['Count']}[#CCCCFF]x")

              else:
                     continue
       
       if (choice.upper() == "D"):
              console.print("[bold][#CCCCFF]Starting [#E0B0FF]deleting cards[#CCCCFF]!")
              console.print("")
              
              open(new_cards_path, 'a')

              console.print("[bold][#CCCCFF]~ Put the card values in this order '[#E0B0FF]Card[#CCCCFF]-[#E0B0FF]Number Set[#CCCCFF]-[#E0B0FF]Number Variant Count'")
              console.print("[bold][#CCCCFF]~ [#E0B0FF]Variant[#CCCCFF] = '[#E0B0FF]f[#CCCCFF]/[#E0B0FF]1[#CCCCFF]' for foil and '[#E0B0FF]n[#CCCCFF]/[#E0B0FF]0[#CCCCFF]' for normal")
              console.print("[bold][#CCCCFF]~ If you don't type [#E0B0FF]any Count[#CCCCFF] the Count Number is [#E0B0FF]1")
              console.print("[bold][#CCCCFF]~ You [#E0B0FF]end[#CCCCFF] the deleting procces by typing '[#E0B0FF]stop[#CCCCFF]'")
              console.print("[bold][#CCCCFF]~ You [#E0B0FF]undelete[#CCCCFF] the last card deleted by typing '[#E0B0FF]back[#CCCCFF]'")
              console.print("[bold][#CCCCFF]~ You [#E0B0FF]preset[#CCCCFF] the set to a specific number by typing '[#E0B0FF]set number[#CCCCFF]'")
              console.print("[bold][#CCCCFF]~ You [#E0B0FF]unset[#CCCCFF] the set by typing '[#E0B0FF]set 0[#CCCCFF]'")
              console.print("[bold][#CCCCFF]~ The cards are [#E0B0FF]automatically [#CCCCFF]saved")
              console.print("")

              splitter = console.input("[bold][#CCCCFF]Choose with which [#E0B0FF]character[#CCCCFF] you want to [#E0B0FF]split[#CCCCFF] the Number, Set, etc.: ")

              if (splitter == ""):
                     splitter = " "

              console.print(f"[bold][#CCCCFF]You chose '[#E0B0FF]{splitter}[#CCCCFF]' character")
              console.print("")

              console.print("[bold][#CCCCFF]The [#E0B0FF]deleting[#CCCCFF] process: ")

              first = True
              values = {}
              set_value = None

              while True:
                     console.print("")
                     values_input = console.input("[bold][#CCCCFF]Delete [#E0B0FF]card[#CCCCFF]: ")

                     if (values_input.lower() == "back"):
                            console.print("[bold][#CCCCFF]The last card [#E0B0FF]won't be[#CCCCFF] deleted!")
                            values = {}
                            first = True
                            continue
                            
                     elif (isinstance(values, list)):
                            pass

                     else:
                            if (first == True):
                                   first = False
                            else:
                                   collection.del_row(values)
                                   new.del_row(values)

                     if (values_input.lower() == "stop"):
                            console.print("")
                            console.print("[bold][#E0B0FF]Saved[#CCCCFF]!")
                            console.input("[bold][#E0B0FF]Exit [#CCCCFF]program ")
                            break

                     if (values_input.lower().find("set") >= 0):
                            values = values_input.split(" ")

                            if (values[1] == "0"):
                                   set_value = None
                                   console.print(f"[bold][#CCCCFF]The set will be [#E0B0FF]unset")
                            else:
                                   set_value = values[1]
                                   console.print(f"[bold][#CCCCFF]The set will be [#E0B0FF]{set_value}")

                            continue


                     values = values_input.split(splitter)

                     if (set_value == None):
                            if (len(values) == 3):
                                   values = {'Set Number': values[1], 'Card Number': values[0], 'Variant': values[2], 'Count': "1"}
                            else:
                                   values = {'Set Number': values[1], 'Card Number': values[0], 'Variant': values[2], 'Count': values[3]}
                     else:
                            if (len(values) == 2):
                                   values = {'Set Number': set_value, 'Card Number': values[0], 'Variant': values[1], 'Count': "1"}
                            else:
                                   values = {'Set Number': set_value, 'Card Number': values[0], 'Variant': values[1], 'Count': values[2]}

                     if (values["Variant"] == "f" or values["Variant"] == "1"):
                            values["Variant"] = "foil"
                     else:
                            values['Variant'] = "normal"

                     console.print(f"[bold][#CCCCFF]Deleting = Card: [#E0B0FF]{values['Card Number']} [#CCCCFF]/ Set: [#E0B0FF]{values['Set Number']} [#CCCCFF]/ Var: [#E0B0FF]{values['Variant']} [#CCCCFF]/ Count: [#E0B0FF]{values['Count']}[#CCCCFF]x")

       if (choice.upper() == "E"):
              console.print("[bold][#E0B0FF]Bye[#CCCCFF], [#E0B0FF]bye[#CCCCFF]!")
              break