# algorithms-and-data-structures-class
Programms written as answers to the Algorigthms and Data Structures class, exercises

Binary_Search_Tree.py: A solution to the Runway Reservation System problem, where a plane makes a request for landing at a specific time and the airport replies affirmatively if there is no other landing scheduled at this time +-3 mins (specific to this programm). 

AVL_Tree.py: A solution to the same problem as the above, demonstrating the different properties of an AVL tree.

Hashing_Client_Cards.py: A solution to the following problem: We assume there exist 5000 different clients in an establishment each having a "Client's Card" distinguished by 16 alpharithmetic characters. The first 13 are always the same, and the last 3 change from client to client. This is done because 36 different alpharithmetic characters (0-9, A-Z) are enough to produce 7,140 different card numbers. We suppose 500,000 visits are made to the establishment and a random client is selected as the visitor. If it is the client's first visit we add him using hashing in a table of 10007 entries. If it's not we search for the client on the aforementioned table and add the spendings of his visit, to his total spendings. Our goal is to find the client with the most spendings, demonstrating the linear search time of the hashing algorithm as well as it's linear insertion time compared to a sorted array.

