// ===== Challenge Task 1 of 3 =====

// Prompt the user with the question "Do you understand do while loops?" Store the
// result in a new String variable named response.


String response = console.readLine("Do you understand do while loops?    ");


// ===== Challenge Task 2 of 3 =====

// Now continually prompt the user in a do while loop. The loop should continue
// running as long as the response is No. Don't forget to declare response outside
// of the do while loop.


String response;

do {
response = console.readLine("Do you understand do while loops?    ");

} while (response.equalsIgnoreCase("no"));


// ===== Challenge Task 3 of 3 =====

// Finally, using console.printf print out a formatted string that says "Because you
// said <response>, you passed the test!"


String response;

do {
response = console.readLine("Do you understand do while loops?    ");

} while (response.equalsIgnoreCase("no"));

console.printf("Because you said %s, you passed the test", response);