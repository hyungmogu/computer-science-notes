// ===== Challenge Task 1 of 2 =====

// Add an if statement that checks to see if firstExample is equal to secondExample.
// If it is, print out "first is equal to second".

// I have imported a java.io.Console for you, it is named console.
String firstExample = "hello";
String secondExample = "hello";
String thirdExample = "HELLO";

if (firstExample.equals(secondExample)) {
  console.printf("first is equal to second");
}


// ===== Challenge Task 2 of 2 =====

// Add another if statement that checks if the firstExample is equal ignoring case
// to thirdExample. If it, is print out "first and third are the same ignoring case".


// I have imported a java.io.Console for you, it is named console.
String firstExample = "hello";
String secondExample = "hello";
String thirdExample = "HELLO";

if (firstExample.equals(secondExample)) {
  console.printf("first is equal to second");
}

if (firstExample.equalsIgnoreCase(thirdExample)) {
  console.printf("first and third are the same ignoring case");
}

