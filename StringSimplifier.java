package brooklyngrant;

/*
 * Write a program that takes as input sequences 
 * of A's, B's, C's, and E's. For example ABABAECCEC, 
 * or in general any sequence made from A, B, C, and 
 * E. The program can transform (replace subsequences) 
 * the input sequence using the following sub-sequence 
 * equalities: AC = E, AB = BC, BB = E, and Ex = x for 
 * any x. For example, ABBC can be transformed into AEC, 
 * and then AC, and then E. Your goal is to produce the 
 * sequence E. Your program should take any such 
 * sequence as input from the command line, and output 
 * the word "SUCCESS" and the set of steps that 
 * transforms the subsequence into E if it is possible
 * to do so, otherwise output "FAILURE" if it is not 
 * possible to transform the sequence to E. User your 
 * program to identify all of the sequences of length 
 * less than 10 that cannot be transformed into E. 
 * Submit these sequences as well as your source code.
 * 
 */
import java.util.*;
import java.io.FileWriter;
import java.io.IOException;


 public class StringSimplifier {

    //RULES: AC = E, AB = BC, BB = E, and Ex = x for any x.
    public static ProductionRule[] rules = {
        new ProductionRule("AC", "E"),
        new ProductionRule("AB", "BC"),
        new ProductionRule("BB", "E"),
        new ProductionRule("EA", "A"),
        new ProductionRule("EB", "B"),
        new ProductionRule("EC", "C"),
        new ProductionRule("ED", "D"),
        new ProductionRule("EE", "E"),
    };
    public static char[] letters = {'A', 'B', 'C', 'E'};

    public static class ProductionRule {
        String input;
        String output;

        public ProductionRule(String pIn, String pOut) {
            this.input = pIn;
            this.output = pOut;
        }

        public String apply(String pString, int pI) {
            if (pString.indexOf(input, pI) != pI) {
                return pString; // error, just return str
            }
            return pString.substring(0, pI) + output + pString.substring(pI+input.length());
        }
    }

    public static class MyState {
        String str;
        String changed; // tracking what changed

        public MyState(String pString, String pChanged) {
            this.str = pString;
            this.changed = pChanged;
        }

        public String toString() {
            return this.changed + "(" + this.str + ")";
        }
    }

    public static void main(String[] args) {
        if (args == null || args.length != 1) {
            System.out.println("Finding all sequences < 10 that cannot be reduced to E...");
            List<String> invalidSequences = findSequencesThatCannotReduceToE();
            
            //after finding squences, write them to file
            try (FileWriter writer = new FileWriter("invalidSequences")) {
                writer.write("Sequences of length < 10 that cannot be reduced to E:\n");
                for (String seq : invalidSequences) {
                    writer.write(seq + "\n");
                }
            } catch (IOException e) {
                System.out.println("An error occurred while writing to the file.");
                e.printStackTrace();
            }
            
            System.out.println("Open the invalidSequences file for results.");

        } else {
            String input = args[0];
    
            Stack<MyState> st = new Stack<>();
            List<MyState> history = new ArrayList<>();

            String stackResult = reduce(input, st, history); // stack is faster, going with stack
            if (stackResult.equals("E")) {
                System.out.println("SUCCESS");
                printSteps(history);
            } else {
                System.out.println("FAILURE");
                System.out.println("Reduced to: " + stackResult);
            }
        }
    }

    public static String reduce(String pString, Stack<MyState> pStorage, List<MyState> history) {
        String rVal=pString;

        pStorage.add(new MyState(pString, ""));
        history.add(new MyState(pString, "Initial"));

        while (!pStorage.isEmpty()) {
            MyState curr = pStorage.pop();
            if (rVal.length() > curr.str.length()) rVal = curr.str;
            if (curr.str.equals("E")) break; // are we at the goal?

            boolean ruleApplied = false; // Track if we apply a rule in this pass
            for (int i = 0; i < rules.length; i++) {
                int j = 0;
                while (j < curr.str.length()) {

                    j = curr.str.indexOf(rules[i].input, j);
                    if (j == -1) {
                        break;
                    }

                    String newString = rules[i].apply(curr.str, j);
                    String changed = rules[i].input + " -> " + rules[i].output; // what happened
                    if (!newString.equals(curr.str)) {
                        pStorage.add(new MyState(newString, changed));
                        history.add(new MyState(newString, changed)); // Track the steps
                        ruleApplied = true;
                    }
    
                    // Move j past this transformation
                    j += rules[i].input.length();
                }
    
                // If a rule was applied, break to process the new state before continuing
                if (ruleApplied) break;
            }
    
            // If no rules were applied and we're stuck, break out of the loop
            if (!ruleApplied) break;
        }

        return rVal;
    }

    public static List<String> findSequencesThatCannotReduceToE() {
        List<String> cannotBeESequences = new ArrayList<>();

        // gen all sequences of length < 10
        for (int len = 1; len < 10; len++) {
            generateSequences("", len, letters, cannotBeESequences);
        }

        return cannotBeESequences;
    }

    public static void generateSequences(String pFirst, int pLength, char[] pChars, List<String> pCannotBeESequences) {
        if (pFirst.length() == pLength) {
            // check if can be reduced to E
            Stack<MyState> st = new Stack<>();
            String result = reduce(pFirst, st, new ArrayList<>()); // history not important for this
            if (!result.equals("E")) {
                pCannotBeESequences.add(pFirst);
            }
            return;
        }

        for (char c : pChars) {
            generateSequences(pFirst + c, pLength, pChars, pCannotBeESequences);
        }
    }

    public static void printSteps(List<MyState> pStack) {
        for (MyState item : pStack) {
            System.out.println(item);
        }
    }

 }