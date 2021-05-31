using System;
using System.Collections.Generic;
using System.IO;

namespace Practice
{
    class Program
    {
        static void Read(Collection<CreditCard> collection, string fileName)
        {
            StreamReader streamReader = new StreamReader(fileName);
            string line = streamReader.ReadLine();
            while (line != null)
            {
                try
                {
                    CreditCard credit_card = new CreditCard(line);
                    collection.Add(credit_card);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
                line = streamReader.ReadLine();
            }
            streamReader.Close();
        }

        static void Main(string[] args)
        {
            List<string> uniqueParametrs = new List<string>
            {
                "Id","Card_number"
            };
            Collection<CreditCard> collection = new Collection<CreditCard>(uniqueParametrs);
            Validation validate = new Validation();

            char choice;
            bool run = true;

            Console.WriteLine("Enter file name");
            string fileName = Console.ReadLine();
            try
            {
                fileName = validate.File(Directory.GetCurrentDirectory() + @"\" + fileName);
            }
            catch(Exception e)
            {
                Console.WriteLine(e);
            }
            while (run)
            {
                try
                {
                    Console.WriteLine("[1] Read from file \n" +
                               "[2] Append from keyboard \n" +
                               "[3] Edit \n" +
                               "[4] Remove \n" +
                               "[5] Find \n" +
                               "[6] Sort \n" +
                               "[7] Print \n" +
                               "[8] Write \n" +
                               "[0] Quit\n" +
                               "Enter your choice: ");
                    choice = Convert.ToChar(Console.ReadLine());

                    switch (choice)
                    {
                        case '1':
                            Read(collection, fileName);
                            break;
                        case '2':
                            Console.WriteLine("Enter a new object in one line");
                            string newObject = Console.ReadLine();
                            CreditCard credit_card = new CreditCard(newObject);
                            collection.Add(credit_card);
                            break;
                        case '3':
                            Console.WriteLine("Enter ID, field, value");
                            string[] inputArray = Console.ReadLine().Split(',');
                            int ID = Convert.ToInt32(inputArray[0]);
                            string field = inputArray[1];
                            string value = inputArray[2];
                            collection.Edit(ID, field, value);
                            break;
                        case '4':
                            Console.WriteLine("Enter ID");
                            ID = Convert.ToInt32(Console.ReadLine());
                            collection.Remove(ID);
                            break;
                        case '5':
                            Console.WriteLine("Enter value");
                            value = Console.ReadLine();
                            collection.Find(value);
                            break;
                        case '6':
                            Console.WriteLine("Enter property name");
                            field = Console.ReadLine();
                            collection.Sort(field);
                            break;
                        case '7':
                            collection.Print();
                            break;
                        case '8':
                            collection.Write(fileName);
                            break;
                        default:
                            Console.WriteLine("Exit");
                            run = false;
                            break;
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }
    }
}