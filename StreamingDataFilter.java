/******************************************************************************
 *  Compilation:  javac StreamingPrinter.java
 *  Execution:    java StreamingPrinter [filepath (String)]
 *
 *  Print the contents of the file to the terminal, one line at a time.
 *
 *  % java StreamingPrinter someData.csv
 *      Prints every line in the file someData.csv -- located in the same directory
 *      as the StreamingPrinter compiled program -- to the terminal.
 *
 * @author Caitrin Eaton
 *
 ******************************************************************************/
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.*;

public class StreamingPrinter {

    /**
     * Prints the contents of a file to the terminal.
     * @param inFileName (String) path to the input file
     */
    public static void printFile( String inFileName, String windowWidth, String columnIndex){

        // This try-catch makes sure that the input file exists before trying to read it.
        Path inFile = Paths.get( inFileName );
        String[] windowArray;
        windowArray = new String[Integer.parseInt(windowWidth)];  // blank array the size of input window width

        try (BufferedReader reader = Files.newBufferedReader( inFile )){
            FileWriter writer = new FileWriter("output.csv");
            BufferedWriter bufferedWriter = new BufferedWriter(writer);
            bufferedWriter.write("raw, mean, median\n");
            String inLine = reader.readLine();
            inLine = reader.readLine();  //skips the header
            int lineNumber = 0;
            int firstrun = 1; //code only runs once
            while (inLine != null) {
                lineNumber++;
                int sum = 0;
                if (firstrun ==1){
                    for (int i = 0; i < Integer.parseInt(windowWidth) ; i++) {
                        String[] cols = inLine.split(",");
                        windowArray[i] = cols[Integer.parseInt(columnIndex)];
                        inLine = reader.readLine();
                    }
                    firstrun = 0;
                }
                for(int a = 0; a < Integer.parseInt(windowWidth); a++) {
                    //sum = 1;
                    sum = Integer.parseInt(windowArray[a]) + sum;  //makes it an int only for this line
                }
                double mean = sum / Double.parseDouble(windowWidth);
                //median,copy array, sort array, windowwidth/2
                bufferedWriter.write(windowArray[0] + "," +mean);
                bufferedWriter.newLine();
                try{
                    inLine = reader.readLine();
                    String[] cols = inLine.split(",");
                    for (int i = 0; i< Integer.parseInt(windowWidth) ; i++){
                        try {
                            windowArray[i] = windowArray[i+1];
                        }
                        catch (ArrayIndexOutOfBoundsException e) {
                            windowArray[i] = cols[Integer.parseInt(columnIndex)];
                        }
                    }
                }
                catch(NullPointerException e ){
                    bufferedWriter.close();
                    reader.close();
                }

            }

            // Close the input file stream
            reader.close();
            bufferedWriter.close();

        } catch (IOException e) {
            // Failed to read the input file. Let the user know what happened.
            e.printStackTrace();
            System.err.println("ERROR: Unable to open input file " + inFileName + " for reading.");
        }
    }

    /**
     * Parses commandline arguments, then triggers the filter.
     * @param args (String[]) commandline arguments: file path, window width, and column index
     */
    public static void main(String[] args) {
        // Parse commandline arguments: args[0] = file path, args[1] = column to read
        String filepath;
        String windowWidth;
        String columnIndex;
        String usageStatement = "USAGE: java StreamingDataFilter filepath windowWidth columnIndex";
        if( args.length > 0){ //change to 2
            filepath = args[0];
            windowWidth = args[1];
            columnIndex = args[2];
        } else {
            System.out.println( usageStatement );
            return;
        }

        // Apply filters
        printFile( filepath , windowWidth, columnIndex);
    }
}
