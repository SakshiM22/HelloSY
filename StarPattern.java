public class StarPattern {
    public static void main(String[] args) {
        int rows = 5; // Adjust the number of rows as needed

        for (int i = 0; i < rows; i++) {
            for (int j = rows - i; j > 1; j--) {
                System.out.print(" "); // Print spaces before the stars
            }
            for (int j = 0; j <= i; j++) {
                System.out.print("* "); // Print stars
            }
            System.out.println(); // Move to the next line
        }
    }
}
