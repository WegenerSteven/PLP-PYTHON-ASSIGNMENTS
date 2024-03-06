/*void main(){
  print("Hello World!");
}*/
/* VARIABLES IN DART
void main() {
  //declaring variables
  String name = "John"; //must be in quotes
  String address = "Kenya";//must be in quotes
  num age = 20;//whole numbers
  num height = 5.9;//Decimal numbers
  bool isMarried = false;

//printing variables values
  print("Name is $name");
  print("Address is in $address");
  print("Age is $age years old");
  print("Height is $height meters tall");
  print("Married status is $isMarried");

/*You can also use string interpolation to combine the variable with other strings, like this: */
print("$name is from $address and he is $age years old.");
}*/
//DATA TYPES IN DART
/*Numbers
void main() {
//Declaring variables
  int num1 = 100; //without decimal point
  double num2 = 130.2; //with decimal points
  num num3 = 50;
  num num4 = 50.4;
  //for sum
  num sum = num1 + num2 + num3 + num4;

//printing info
  print("Num 1 is $num1");
  print("Num 2 is $num2");
  print("Num 3 is $num3");
  print("Num 4 is $num4");
  print("Sum is $sum");
}*/
/*STRINGS
void main(){
  String schoolName = "Powerlearn Project Academy";
  String address="AFRICA";

  //printing values
  print("My School name is $schoolName and the address is $address");
}*/
/*BOOLEAN
void main(){
  bool isMarried=true;
  print("Married status: $isMarried");
}*/
/*Lists
  List is similar to an array, which is the ordered collection of the objects. is 
  you want to store multiple values without creating multiple variables, you can use a list
void main() {
  List<String> names = ["John", "James", "peter"];
  print("Value of names is $names");
  print("Value of names[0] is ${names[0]}"); // index 0
  print("Value of names[1] is ${names[1]}"); // index 1
  print("Value of names[2] is ${names[2]}"); // index 2
  print(names);
}*/
/*MAPS
//A map is a dynamic  data structure that stores key-value pairs.
//It is used when we need to store related information together ARE LIKE DICTIONARIES IN PY ARE USED TO STORE KEY
void main() {
//creating a Map with string keys and int values
  Map<String, int> ages = {
    'Alice': 30,
    'Bob': 25,
    'Charlie': 35,
  };
  print("Ages of students: $ages");
}*/

/*Runes
//A rune can be defined as an integer used to represent any Unicode code point.
/*As a Dart string is a simple sequence of UTF-16 code units, 32-bit Unicode values
in a string are represented using a special syntax.*/
void main(){
  //Define a string with runes
  String runesString="Runes in Dart: \u{1F600} \u{1F64B} \u{1F680}";
  
  //print the string
  print(runesString);
}*/

/*ARITHMETIC OPERATIONS using Numbers
void main() {
  //declaring two numbers
  int num1 = 10;
  int num2 = 3;
  //performing arithmetc calculation
  int sum = num1 + num2; // addition
  int diff = num1 - num2; // subtraction
  int subtract = num2 - num1; // unary minus
  int mul = num1 * num2; // multiplication
  double div = num1 / num2; // division
  int div2 = num1 ~/ num2; // integer division
  int mod = num1 % num2; // show remainder

//Printing info
  print("The addition is $sum.");
  print("The subtraction is $diff.");
  print("The unary minus is $subtract");
  print("The multiplication is $mul.");
  print("The division is $div.");
  print("The integer division is $div2.");
  print("The modulus is $mod.");
}*/

//FUNCTIONS
//writing function outside main function.
void printName() {
  print("My name is John James");
}
//this is out main function
