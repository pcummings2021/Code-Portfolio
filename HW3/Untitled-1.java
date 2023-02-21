// initial values, sets the maximum to the first item in the list
int count = 1;
int max = 1;
String currentElement = list.get(0);
String maxElement = list.get(0);
// loops through all remaining elements of list, compares to current max
for(int i = 1; i < list.size(); i++) {
    if(currentElement.equals(list.get(i))) { // tallies up the count for each element
        count++;
        if(max < count) { // sets the new max and maxElement to the current max and elements
            max = count;
            maxElement = currentElement;
        }
    }
    else {
        if(max < count) { // if the count is greater than the current max count, that element is the new max
            max = count;
            maxElement = currentElement;
        }
        currentElement = list.get(i); // begins the next iteration
        count = 1;
    }
}
// combines the name and number for the data into a format String, returns the String
String str = String.format("%s %s", String.valueOf(max), maxElement);
return str;