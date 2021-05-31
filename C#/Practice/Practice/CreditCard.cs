using System;

namespace Practice
{
    class CreditCard
    {
        private Validation validation = new Validation();
        private int ID;
        private string bank;
        private string card_number;
        private string date_of_issue;
        private string date_of_expire;
        private int cvc;
        private string owner_name;
        public CreditCard(string arguments)
        {
            _ = Parse(arguments);
        }

        public override string ToString()
        {
            string result = "";
            Type type = GetType();
            var properties = type.GetProperties();
            foreach (var property in properties)
            {
                result += property.GetValue(this) + ",";
            }
            result = result.Remove(result.Length - 1);
            return result;
        }

        public int Id
        {
            get => ID;
            set => ID = validation.Integer(Convert.ToString(value));
        }

        public string Bank
        {
            get => bank;
            set => bank = validation.Bank(value);
        }

        public string Card_number
        {
            get => card_number;
            set => card_number = validation.CardNumber(value);
        }

        public string Date_of_issue
        {
            get => date_of_issue;
            set
            {
                if ((Convert.ToDateTime(Date_of_expire) > Convert.ToDateTime(value)) ||(Date_of_expire == null))
                {
                    date_of_issue = validation.Date(value);
                }
                else
                {
                    throw new Exception("Issue date is earlier than expire");
                }
            }
        }

        public string Date_of_expire
        {
            get => date_of_expire;
            set
            {
                if ((Convert.ToDateTime(value) > Convert.ToDateTime(Date_of_issue)) || (Date_of_issue == null))
                {
                    date_of_expire = validation.Date(value);
                }
                else
                {
                    throw new Exception("Issue date is earlier than expire");
                }
            }
        }

        public int Cvc
        {
            get => cvc;
            set => cvc = validation.CVC(Convert.ToString(value));
        }
        public string Owner_name
        {
            get => owner_name;
            set => owner_name = validation.OwnerName(Convert.ToString(value));
        }
        public CreditCard Parse(string line)
        {
            try
            {
                string[] arguments = line.Split(',');
                Id = Convert.ToInt32(arguments[0]);
                Bank = arguments[1];
                Card_number = arguments[2];
                Date_of_issue = arguments[3];
                Date_of_expire = arguments[4];
                Cvc = Convert.ToInt16(arguments[5]);
                Owner_name = arguments[6];
            }
            catch (Exception e)
            {
                throw new Exception(e.Message);
            }
            return this;
        }
    }

}