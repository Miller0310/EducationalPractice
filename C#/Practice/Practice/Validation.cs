using System;
using System.IO;
using System.Text.RegularExpressions;

namespace Practice
{
    class Validation
    {
        public string File(string value)
        {

            string pattern = @"\w+(.txt)+";
            Match match = Regex.Match(value, pattern);
            if (!match.Success)
            {
                throw new ArgumentOutOfRangeException("Wrong format of file name");
            }
            try
            {
                StreamReader stream = new StreamReader(value);
                stream.Close();
            }
            catch
            {
                throw new Exception("File don't exist");
            }
            return value;
        }
        public int Integer(string value)
        {
            int result = Convert.ToInt32(value);
            if (result < 0)
            {
                throw new Exception("Value is not integer type or less than 0");
            }
            return result;
        }
        public string Bank(string value)
        {
            string pattern = "([A-Z]*[a-z]*)";
            Match match = Regex.Match(value, pattern);
            if (!match.Success)
            {
                throw new Exception("Incorrect bank name");
            }
            return value;
        }
        public string CardNumber(string value)
        {
            string pattern = "([0-9]{4}[ ][0-9]{4}[ ][0-9]{4}[ ][0-9]{4})";
            MatchCollection matches = Regex.Matches(value, pattern);

            if (value.Equals(Convert.ToString(matches[0])))
            {
                return value;
            }
            throw new Exception("Wrong card number");
        }
            public string Date(string value)
        {
            if (!DateTime.TryParse(value, out _))
            {
                throw new Exception("Wrong date");
            }
            return value;
        }
        public int CVC(string value)
        {
            int result = Convert.ToInt32(value);
            if (result <0 || result>=1000)
            {
                throw new Exception("CVC must be from 0 to 999");
            }
            return result;
        }
        public string OwnerName(string value)
        {
            string pattern = "([A-Z][a-z]* [A-Z][a-z]*)";
            Match match = Regex.Match(value, pattern);
            if (!match.Success)
            {
                throw new Exception("Incorrect owner name");
            }
            return value;
        }
    }
}
