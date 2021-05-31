using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Practice
{
    class Collection<T>
    {
        private List<T> list = new List<T>();
        private readonly List<string> uniqueParams;

        public Collection(List<string> uniqueParams)
        {
            this.uniqueParams = uniqueParams;
        }

        public void Write(string fileName)
        {
            StreamWriter streamWriter = new StreamWriter(fileName);
            for (int i = 0; i < list.Count; i++)
            {
                streamWriter.WriteLine(list[i]);
            }
            streamWriter.Close();
        }

        public void Print()
        {
            for (int i = 0; i < list.Count; i++)
            {
                Console.WriteLine(list[i]);
            }
        }
        public void Add(T item)
        {
            var properties = item.GetType().GetProperties();
            foreach (var property in properties)
            {
                foreach (string param in uniqueParams)
                {
                    if (Convert.ToString(property.Name) == param)
                    {
                        for (int i = 0; i < list.Count; i++)
                        {
                            object valueCollection = list[i].GetType().GetProperty(param).GetValue(list[i]);
                            object valueItem = item.GetType().GetProperty(param).GetValue(item);
                            bool isEqual = valueCollection.Equals(valueItem);
                            if (isEqual)
                            {
                                throw new Exception(string.Format("{0} must be unique", param));
                            }

                        }
                    }
                }
            }
            list.Add(item);
        }

        public void Remove(int key)
        {
            list.Remove(this[key]);
        }

        public void Edit(int key, string parametr, string newValue)
        {
            var property = this[key].GetType().GetProperty(parametr);
            var type = property.GetValue(this[key]).GetType();
            property.SetValue(this[key], Convert.ChangeType(newValue, type));
        }

        public void Sort(string parametr)
        {
            list = list.OrderBy(collection => collection.GetType().GetProperty(parametr).GetValue(collection).ToString().ToLower()).ToList();
        }

        public void Find(string parametr)
        {
            for (int i = 0; i < list.Count; i++)
            {
                var properties = list[i].GetType().GetProperties();
                foreach (var property in properties)
                {
                    string value = Convert.ToString(property.GetValue(list[i]));
                    if (value.Contains(parametr))
                    {
                        Console.WriteLine(list[i]);
                        break;
                    }
                }
            }
        }
        public T this[int key]
        {
            get
            {
                for (int i = 0; i < list.Count; i++)
                {
                    var ID = list[i].GetType().GetProperty("Id");
                    if (ID.GetValue(list[i]).Equals(key))
                    {
                        return list[i];
                    }
                }
                throw new Exception(string.Format("Don't exist elements with id:{0}", key));
            }
            set
            {
                for (int i = 0; i < list.Count; i++)
                {
                    var ID = list[i].GetType().GetProperty("Id");
                    if (ID.GetValue(list[i]).Equals(key))
                    {
                        list[i] = value;
                    }
                }
                throw new Exception(string.Format("Don't exist elements with id:{0}", key));
            }
        }
    }
}