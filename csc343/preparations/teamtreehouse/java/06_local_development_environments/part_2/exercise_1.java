"""
===== Challenge Task 1 of 1 =====

Please copy and paste the results from running Systemizer locally here

package com.company;
import java.util.Set;
import java.util.TreeSet;

public class Main {

    public static void main(String[] args) {
        System.out.printf("This is the classpath:  %s %n",
                System.getProperty("java.class.path"));
        Set<String> propNames = new TreeSet<String>(System.getProperties().stringPropertyNames());
        for (String propertyName : propNames) {
            System.out.printf("%s is %s %n",
                    propertyName,
                    System.getProperty(propertyName));
        }
    }
}
"""

// Solution omitted due to sensitivity of data
