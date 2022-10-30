import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class main {
    // Swapping two elements function
    public static void swap(String[] array, int c, int j) {
        String temp = array[c];
        array[c] = array[j];
        array[j] = temp;
    }

    // Initiate last elment as pivot, insert the pivot elment in the array in a sorted manner
    public static int partition(String[] arr, int left, int right) {
        // Setting pivot
        String pivot = arr[left];

        // Initiate the index of smaller element at rightmost position of pivot
        int i = (left - 1);

        for (int j = left; j <= right - 1; j++) {

            // If current string is smaller than the pivot

            if (arr[j].compareTo(pivot) < 0) {
                // Increment index of smaller element
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, right);
        return (i + 1);
    }

    /* QuickSort Function
        arr[] --> array that stores strings
        low --> Starting index,
        high --> Ending index
    */
    public static void quickSort(String[] arr, int left, int right) {
        if (left < right) {

            // Setting pi partitioning index, arr[p]
            int pi = partition(arr, left, right);

            // Separately sort elments in two different partitions
            quickSort(arr, left, pi - 1);
            quickSort(arr, pi + 1, right);
        }
    }

    public static void main(String[] args) throws IOException {
        // Import data from text file

        // Create array list for strong strings
        List<String> wordList = new ArrayList<>();

        // Read strings from file
        BufferedReader readFile = new BufferedReader(new FileReader("sgb-words.txt"));

        // Read entire line
        String line = readFile.readLine();

        while (line != null) {
            wordList.add(line);
            line = readFile.readLine();
        }

        readFile.close();

        String[] stringList = wordList.toArray(new String[wordList.size()]);
        quickSort(stringList, 0, stringList.length-1);
        System.out.println(Arrays.toString(stringList));
    }

}